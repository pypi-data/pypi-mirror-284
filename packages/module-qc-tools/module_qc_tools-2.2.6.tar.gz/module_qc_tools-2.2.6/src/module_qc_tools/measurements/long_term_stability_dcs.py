import copy
import logging
import time

import numpy as np
import typer
from module_qc_data_tools import (
    qcDataFrame,
)
from tabulate import tabulate

from module_qc_tools.cli.globals import (
    CONTEXT_SETTINGS,
)
from module_qc_tools.utils.misc import inject_metadata
from module_qc_tools.utils.ntc import ntc

logger = logging.getLogger("measurement")

app = typer.Typer(context_settings=CONTEXT_SETTINGS)

TEST_TYPE = "LONG_TERM_STABILITY_DCS"


@inject_metadata(test_type=TEST_TYPE, uses_yarr=False)
def run(config, ps, hv):
    """
    Measure the sensor leakage current, low-power voltage, and temperature.

    Args:
        config (dict): Full config dictionary
        ps (Class power_supply): An instance of Class power_supply for power on and power off.
        hv (Class power_supply): An instance of Class power_supply for high-voltage power on and power off.

    Returns:
        data (list): data[chip_id][vmux/imux_type].
    """
    measurement_config = copy.deepcopy(config["tasks"]["GENERAL"])
    measurement_config.update(config["tasks"][TEST_TYPE])

    nt = ntc(config["ntc"])

    data = qcDataFrame(
        columns=[
            "time",
            "BIAS_VOLT",
            "LEAKAGE_CURR",
            "LV_VOLT",
            "LV_CURR",
            "MOD_TEMP",
            "MOD_HUM",
        ],
        units=["s", "V", "A", "V", "A", "C", "%"],
    )
    data.set_x("time", True)

    lv_status = {"voltage": ps.measV(), "current": ps.measI()}
    logger.debug("lv_status " + str(lv_status))
    hv_status = {"voltage": hv.measV(), "current": hv.measI()}
    logger.debug("hv_status " + str(hv_status))

    if not (hv_status["voltage"][0] and hv_status["current"][0]):
        logger.error("HV must be on (the sensor must be biased for stability testing)")
        msg = f"Module is not properly powered. HV voltage ({hv_status['voltage'][0]}) and current ({hv_status['current'][0]})."
        raise RuntimeError(msg)

    if not (lv_status["voltage"][0] and lv_status["current"][0]):
        logger.error("LV must be on (module must be powered for stability testing)")
        msg = f"Module is not properly powered. LV voltage ({lv_status['voltage'][0]}) and current ({lv_status['current'][0]})."
        raise RuntimeError(msg)

    logger.info(
        "--------------------------------------------------------------------------"
    )

    starttime = time.time()
    duration = 0.0
    while duration < measurement_config["duration"]:
        # read voltage
        bias_volt, hv_status = hv.measV()
        if hv_status:
            logger.error(
                'Cannot read voltage from the HV supply. Try increase "n_try" in the measurement configuration.'
            )
            break

        lv_volt, lv_status = ps.measV()
        if lv_status:
            logger.error(
                'Cannot read voltage from the LV supply. Try increase "n_try" in the measurement configuration.'
            )
            break

        # read current
        leakage_curr, hi_status = hv.measI()
        if hi_status:
            logger.error(
                'cannot read current from the HV supply. try increase "n_try" in the measurement configuration.'
            )

        lv_curr, li_status = ps.measI()
        if li_status:
            logger.error(
                'cannot read current from the LV supply. try increase "n_try" in the measurement configuration.'
            )

        # read temperature
        mod_temp, _temp_status = nt.read()
        # TODO: humidity: interface with influxDB?

        # fill in data
        mea = {
            "time": [duration],
            "BIAS_VOLT": [bias_volt],
            "LEAKAGE_CURR": [leakage_curr],
            "LV_VOLT": [lv_volt],
            "LV_CURR": [lv_curr],
            "MOD_TEMP": [mod_temp],
        }
        data.add_data(mea)
        logger.info("\n" + tabulate(mea, headers="keys"))

        time.sleep(measurement_config["period"])
        duration = time.time() - starttime

    data.add_meta_data("AverageTemperature", np.average(data["MOD_TEMP"]))
    return data
