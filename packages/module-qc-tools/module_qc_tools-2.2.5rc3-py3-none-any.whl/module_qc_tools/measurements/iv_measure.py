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

TEST_TYPE = "IV_MEASURE"


@inject_metadata(test_type=TEST_TYPE, uses_yarr=False)
def run(config, ps, hv, layer):
    """
    Measure the sensor leakage current against reverse bias voltage.

    Args:
        config (dict): Full config dictionary
        ps (Class power_supply): An instance of Class power_supply for power on and power off.
        hv (Class power_supply): An instance of Class power_supply for high-voltage power on and power off.
        layer (str): Layer information for the module

    Returns:
        data (list): data[chip_id][vmux/imux_type].
    """
    measurement_config = copy.deepcopy(config["tasks"]["GENERAL"])
    measurement_config.update(config["tasks"][TEST_TYPE])

    nt = ntc(config["ntc"])

    data = qcDataFrame(
        columns=[
            "time",
            "voltage",
            "current",
            "sigma current",
            "temperature",
            "humidity",
        ],
        units=["s", "V", "A", "A", "C", "%"],
    )
    data.set_x("voltage", True)

    # get current status
    lv_set = {"voltage": ps.getV(), "current": ps.getI()}
    hv_set = {"voltage": hv.getV(), "current": hv.getI()}

    lv_status = {"voltage": ps.measV(), "current": ps.measI()}
    logger.debug("lv_status " + str(lv_status))
    hv_status = {"voltage": hv.measV(), "current": hv.measI()}
    logger.debug("hv_status " + str(hv_status))

    # turn off LV and HV, set HV for measurement
    if (
        hv_status["voltage"][0] and hv_status["current"][0]
    ):  # if both HV voltage and current are != 0 then HV is on
        logger.debug(
            "HV voltage: "
            + str(hv_status["voltage"][0])
            + " HV current: "
            + str(hv_status["current"][0])
        )
        logger.info("Ramping HV to 0V before starting measurement...")
        hv.rampV(v=0, i=measurement_config["i_max"][layer])
        hv.off()

    if (
        lv_status["voltage"][0] and lv_status["current"][0]
    ):  # if both LV voltage and current are != 0 then LV is on
        logger.debug(
            "LV voltage: "
            + str(lv_status["voltage"][0])
            + " LV current: "
            + str(lv_status["current"][0])
        )
        logger.info("Switching off LV before starting measurement...")
        ps.off()

    hv.set(
        v=measurement_config["v_min"][layer],
        i=measurement_config["i_max"][layer],
        check=False,
    )
    if "emulator" not in hv.on_cmd:
        hv.on()
    hv.checkTarget(
        v=measurement_config["v_min"][layer], i=measurement_config["i_max"][layer]
    )

    voltages = np.linspace(
        measurement_config["v_min"][layer],
        measurement_config["v_max"][layer],
        measurement_config["n_points"][layer],
    )
    starttime = time.time()
    logger.info(
        "--------------------------------------------------------------------------"
    )
    for value in voltages:
        mea = {}
        currents = []

        # set and measure current for power supply
        try:
            hv.set(
                v=value, i=measurement_config["i_max"][layer]
            )  # will return only when target is reached
        except RuntimeError as err:
            logger.exception(
                f"{err}: Voltage target ({value} V) cannot be set and reached, possible HV interlock triggered. Ramping down!"
            )
            break

        if "emulator" not in hv.measV_cmd:
            time.sleep(measurement_config["settling_time"][layer])

        duration = time.time() - starttime
        # read voltage
        voltage, v_status = hv.measV()
        if v_status:
            logger.error(
                'Cannot read voltage from the HV supply. Try increase "n_try" in the measurement configuration.'
            )
            break

        # read current
        i_status = 0
        for _j in range(3):  ## takes 0.5s for 3 readings
            current, i_status = hv.measI()
            if i_status:
                logger.error(
                    'Cannot read current from the HV supply. Try increase "n_try" in the measurement configuration.'
                )
                break  ## out of the current loop
            currents.append(current)
        if i_status:
            break  ## out of the voltage loop

        # read temperature
        temp, _temp_status = nt.read()
        # TODO: humidity: interface with influxDB?

        # fill in data
        mea["time"] = [duration]
        mea["voltage"] = [voltage]
        mea["current"] = [np.mean(currents)]
        mea["sigma current"] = [np.std(currents)]
        mea["temperature"] = [temp]
        data.add_data(mea)
        logger.info("\n" + tabulate(mea, headers="keys"))
        # logger.debug(time.time()-starttime) ## ~ 2 seconds for all the readings

        if abs(mea["current"][0]) >= measurement_config["i_max"][layer]:
            logger.warning(
                f'Measured leakage current {abs(mea["current"][0])}A exceeds the current compliance {measurement_config["i_max"][layer]}A! Ramping down!'
            )
            break

    time.sleep(1)
    # Return to initial state
    logger.info(f'Ramping HV back to initial state at {hv_set["voltage"][0]}V...')
    hv.rampV(v=hv_set["voltage"][0], i=hv_set["current"][0])
    ps.set(v=lv_set["voltage"][0], i=lv_set["current"][0], check=False)
    ## if not emulator and LV was on previously
    if (
        "emulator" not in ps.on_cmd
        and lv_status["voltage"][0]
        and lv_status["current"][0]
    ):
        ps.on()
        ps.checkTarget(v=lv_set["voltage"][0], i=lv_set["current"][0])

    data.add_meta_data("AverageTemperature", np.average(data["temperature"]))
    data.add_meta_data("SettlingTime", measurement_config["settling_time"][layer])
    return data
