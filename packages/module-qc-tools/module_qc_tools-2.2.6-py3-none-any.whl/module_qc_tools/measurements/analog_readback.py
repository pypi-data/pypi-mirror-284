import logging
from datetime import datetime

from module_qc_data_tools import (
    qcDataFrame,
)
from tabulate import tabulate

from module_qc_tools.utils.misc import (
    check_adc_ground,
    initialize_chip_metadata,
    inject_metadata,
    read_vmux,
)
from module_qc_tools.utils.multimeter import multimeter
from module_qc_tools.utils.ntc import ntc

logger = logging.getLogger("measurement")

TEST_TYPE = "ADC_CALIBRATION"


@inject_metadata(test_type=TEST_TYPE)
def run_vmeas(config, ps, yr, layer, use_calib_adc):
    """
    This function measures given internal voltages by going through all VMUX and IMUX settings provided in the config.

    Args:
        config (dict): Full config dictionary
        ps (Class power_supply): An instance of Class power_supply for power on and power off.
        yr (Class yarr): An instance of Class yarr for chip conifugration and change register.
        layer (str): Layer information for the module
        use_calib_adc (bool): use calibrated ADC instead of multimeter

    Returns:
        data (list): data[chip_id][vmux/imux_type].
    """
    logger.info("Start V scan!")
    logger.info(f"TimeStart: {datetime.now().strftime('%Y-%m-%d_%H%M%S')}")

    measurement_config = config["tasks"]["GENERAL"]
    measurement_config.update(config["tasks"]["ANALOG_READBACK"])

    meter = multimeter(config["multimeter"])

    data = [
        qcDataFrame(
            columns=[
                f"Vmux{v_mux}"
                for v_mux in measurement_config["v_mux"]
                + [measurement_config["v_mux_gnd"]]
            ]
            + [
                f"Imux{i_mux}"
                for i_mux in measurement_config["i_mux"]
                + [measurement_config["i_mux_gnd"]]
            ],
            units=[
                "V"
                for v_mux in measurement_config["v_mux"]
                + [measurement_config["v_mux_gnd"]]
            ]
            + [
                "V"
                for i_mux in measurement_config["i_mux"]
                + [measurement_config["i_mux_gnd"]]
            ],
        )
        for _ in range(yr._number_of_chips)
    ]
    initialize_chip_metadata(yr, data)

    if yr.running_emulator():
        ps.on(
            measurement_config["v_max"],
            measurement_config["i_config"][layer],
        )  # Only for emulator do the emulation of power on/off.
        # For real measurements avoid turn on/off the chip by commands. Just leave the chip running.

    # Check ADC ground
    if use_calib_adc:
        vmux_adc_gnd, imux_adc_gnd = check_adc_ground(yr, measurement_config)
        for i, chip in enumerate(yr._enabled_chip_positions):
            data[chip].add_meta_data("VMUX30_ADC", vmux_adc_gnd[i])
            data[chip].add_meta_data("IMUX63_ADC", imux_adc_gnd[i])

    # Set and measure current for power supply
    i_mea = [{} for _ in range(yr._number_of_chips)]

    # Measure ground once.
    vmux_value_gnd = measurement_config["v_mux_gnd"]
    vmux_gnd = read_vmux(
        meter,
        yr,
        measurement_config,
        v_mux=vmux_value_gnd,
        use_adc=use_calib_adc,
    )
    imux_value_gnd = measurement_config["i_mux_gnd"]
    imux_gnd = read_vmux(
        meter,
        yr,
        measurement_config,
        i_mux=imux_value_gnd,
        use_adc=use_calib_adc,
    )
    for i, chip in enumerate(yr._enabled_chip_positions):
        i_mea[chip][f"Vmux{vmux_value_gnd}"] = [vmux_gnd[i]]
        i_mea[chip][f"Imux{imux_value_gnd}"] = [imux_gnd[i]]

    # measure v_mux
    for v_mux in measurement_config["v_mux"]:
        mea_chips = read_vmux(
            meter,
            yr,
            measurement_config,
            v_mux=v_mux,
            use_adc=use_calib_adc,
        )
        for i, chip in enumerate(yr._enabled_chip_positions):
            i_mea[chip][f"Vmux{v_mux}"] = [mea_chips[i]]

    # measure i_mux
    for i_mux in measurement_config["i_mux"]:
        mea_chips = read_vmux(
            meter,
            yr,
            measurement_config,
            i_mux=i_mux,
            use_adc=use_calib_adc,
        )
        for i, chip in enumerate(yr._enabled_chip_positions):
            i_mea[chip][f"Imux{i_mux}"] = [mea_chips[i]]

    for chip in yr._enabled_chip_positions:
        data[chip].add_data(i_mea[chip])

        logger.info(
            "--------------------------------------------------------------------------"
        )
        logger.info(f"Chip-{chip+1}")
        logger.info("\n" + tabulate(i_mea[chip], headers="keys", floatfmt=".3f"))

    logger.info("V scan done!")
    logger.info(f"TimeEnd: {datetime.now().strftime('%Y-%m-%d_%H%M%S')}")

    return data


@inject_metadata(test_type=TEST_TYPE)
def run_tmeas(config, ps, yr, layer, use_calib_adc):
    """
    This function measures temperature of the NTC nad MOS sensor though VMUX and IMUX settings provided in the config.

    Args:
        config (dict): An subdict dumped from json including the task information.
        ps (Class power_supply): An instance of Class power_supply for power on and power off.
        yr (Class yarr): An instance of Class yarr for chip conifugration and change register.

    Returns:
        data (list): data[chip_id][vmux/imux_type or bias/dem].
    """
    logger.info("Start T measurement!")
    logger.info(f"TimeStart: {datetime.now().strftime('%Y-%m-%d_%H%M%S')}")

    measurement_config = config["tasks"]["GENERAL"]
    measurement_config.update(config["tasks"]["ANALOG_READBACK"])

    meter = multimeter(config["multimeter"])
    nt = ntc(config["ntc"])

    data = [
        qcDataFrame(
            columns=[
                f"Vmux{v_mux}"
                for v_mux in [
                    measurement_config["v_mux_ntc"],
                    measurement_config["v_mux_gnd"],
                ]
            ]
            + [
                f"Imux{i_mux}"
                for i_mux in [
                    measurement_config["i_mux_ntc"],
                    measurement_config["i_mux_gnd"],
                ]
            ]
            + [f"Vmux{v_mux}" for v_mux in measurement_config["v_mux_tempsens"]]
            + ["MonSensSldoAnaSelBias"]
            + ["MonSensSldoDigSelBias"]
            + ["MonSensAcbSelBias"]
            + ["MonSensSldoAnaDem"]
            + ["MonSensSldoDigDem"]
            + ["MonSensAcbDem"]
            + ["TExtExtNTC"],
            units=[
                "V"
                for v_mux in [
                    measurement_config["v_mux_ntc"],
                    measurement_config["v_mux_gnd"],
                ]
            ]
            + [
                "V"
                for i_mux in [
                    measurement_config["i_mux_ntc"],
                    measurement_config["i_mux_gnd"],
                ]
            ]
            + ["V" for v_mux in measurement_config["v_mux_tempsens"]]
            + ["-"]
            + ["-"]
            + ["-"]
            + ["-"]
            + ["-"]
            + ["-"]
            + ["C"],
        )
        for _ in range(yr._number_of_chips)
    ]
    initialize_chip_metadata(yr, data)

    if yr.running_emulator():
        ps.on(
            measurement_config["v_max"],
            measurement_config["i_config"][layer],
        )  # Only for emulator do the emulation of power on/off.
        # For real measurements avoid turn on/off the chip by commands. Just leave the chip running.

    # Check ADC ground
    if use_calib_adc:
        vmux_adc_gnd, imux_adc_gnd = check_adc_ground(yr, measurement_config)
        for i, chip in enumerate(yr._enabled_chip_positions):
            data[chip].add_meta_data("VMUX30_ADC", vmux_adc_gnd[i])
            data[chip].add_meta_data("IMUX63_ADC", imux_adc_gnd[i])

    # Chip config mapping
    bias_maps = {
        14: "MonSensSldoAnaSelBias",
        16: "MonSensSldoDigSelBias",
        18: "MonSensAcbSelBias",
    }
    dem_maps = {
        14: "MonSensSldoAnaDem",
        16: "MonSensSldoDigDem",
        18: "MonSensAcbDem",
    }

    # Measure ground once.
    vmux_value_gnd = measurement_config["v_mux_gnd"]
    vmux_gnd = read_vmux(
        meter,
        yr,
        measurement_config,
        v_mux=vmux_value_gnd,
        use_adc=use_calib_adc,
    )
    imux_value_gnd = measurement_config["i_mux_gnd"]
    imux_gnd = read_vmux(
        meter,
        yr,
        measurement_config,
        i_mux=imux_value_gnd,
        use_adc=use_calib_adc,
    )

    i_mea = [{} for _ in range(yr._number_of_chips)]
    # Measure v_mux_tempmeas
    for v_mux in measurement_config["v_mux_tempsens"]:
        yr.enable_tempsens(v_mux=v_mux)
        for bias in measurement_config[bias_maps[v_mux]]:
            yr.set_tempsens_bias(v_mux=v_mux, bias=bias)
            for dem in measurement_config[dem_maps[v_mux]]:
                yr.set_tempsens_dem(
                    v_mux=v_mux,
                    dem=dem,
                )
                mea_chips = read_vmux(
                    meter,
                    yr,
                    measurement_config,
                    v_mux=v_mux,
                    use_adc=use_calib_adc,
                )

                for i, chip in enumerate(yr._enabled_chip_positions):
                    # Reset i_mea[chip]
                    i_mea[chip] = {}
                    # Record vmux, bias, and dem.
                    i_mea[chip][f"Vmux{v_mux}"] = [mea_chips[i]]
                    i_mea[chip][bias_maps[v_mux]] = [bias]
                    i_mea[chip][dem_maps[v_mux]] = [dem]

                    data[chip].add_data(i_mea[chip])
    yr.reset_tempsens()

    # Measure NTCs
    # Measure external external (flex) NTC
    mea_ntc, _status = nt.read()
    # Measure external (chip) NTCs
    v_mux_value_ntc = measurement_config["v_mux_ntc"]
    v_mux_ntc = read_vmux(
        meter,
        yr,
        measurement_config,
        v_mux=v_mux_value_ntc,
        use_adc=use_calib_adc,
    )
    i_mux_value_ntc = measurement_config["i_mux_ntc"]
    i_mux_ntc = read_vmux(
        meter,
        yr,
        measurement_config,
        i_mux=i_mux_value_ntc,
        use_adc=use_calib_adc,
    )

    max_n_measure = max(len(d["Vmux14"]) if d else 0 for d in data)
    n_measure = 0
    while n_measure < max_n_measure:
        # Clear dictionary to hold data
        i_mea = [{} for _ in range(yr._number_of_chips)]
        for i, chip in enumerate(yr._enabled_chip_positions):
            i_mea[chip][f"Vmux{v_mux_value_ntc}"] = [v_mux_ntc[i]]
            i_mea[chip][f"Vmux{vmux_value_gnd}"] = [vmux_gnd[i]]
            i_mea[chip][f"Imux{i_mux_value_ntc}"] = [i_mux_ntc[i]]
            i_mea[chip][f"Imux{imux_value_gnd}"] = [imux_gnd[i]]
            i_mea[chip]["TExtExtNTC"] = [mea_ntc]
            data[chip].add_data(i_mea[chip])
        n_measure += 1

    for chip in yr._enabled_chip_positions:
        logger.info(
            "--------------------------------------------------------------------------"
        )
        logger.info(f"Chip-{chip+1}")
        logger.info("\n" + tabulate(i_mea[chip], headers="keys", floatfmt=".3f"))

    logger.info("T measurement done!")
    logger.info(f"TimeEnd: {datetime.now().strftime('%Y-%m-%d_%H%M%S')}")

    return data


@inject_metadata(test_type=TEST_TYPE)
def run_vdda_vddd_vs_trim(config, ps, yr, layer, debug_gnd, use_calib_adc):
    """
    This function measures how VDDA and VDDD changes with Trim.

    Args:
        config (dict): An subdict dumped from json including the task information.
        ps (Class power_supply): An instance of Class power_supply for power on and power off.
        yr (Class yarr): An instance of Class yarr for chip conifugration and change register.

    Returns:
        data (list): data[chip_id][vmux/imux_type or bias/dem].
    """
    logger.info("Start VDD vs Trim measurement!")
    logger.info(f"TimeStart: {datetime.now().strftime('%Y-%m-%d_%H%M%S')}")

    measurement_config = config["tasks"]["GENERAL"]
    measurement_config.update(config["tasks"]["ANALOG_READBACK"])

    meter = multimeter(config["multimeter"])

    data = [
        qcDataFrame(
            columns=["Vmux34"]
            + ["Vmux38"]
            + [f"Vmux{measurement_config['v_mux_gnd']}"]
            + ["SldoTrimA"]
            + ["SldoTrimD"]
            + [f"ROSC{i}" for i in range(42)],
            units=["V"] + ["V"] + ["V"] + ["-"] + ["-"] + ["MHz" for i in range(42)],
        )
        for _ in range(yr._number_of_chips)
    ]
    initialize_chip_metadata(yr, data)

    if yr.running_emulator():
        ps.on(
            measurement_config["v_max"],
            measurement_config["i_config"][layer],
        )  # Only for emulator do the emulation of power on/off.
        # For real measurements avoid turn on/off the chip by commands. Just leave the chip running.

    # Check ADC ground
    if use_calib_adc:
        vmux_adc_gnd, imux_adc_gnd = check_adc_ground(yr, measurement_config)
        for i, chip in enumerate(yr._enabled_chip_positions):
            data[chip].add_meta_data("VMUX30_ADC", vmux_adc_gnd[i])
            data[chip].add_meta_data("IMUX63_ADC", imux_adc_gnd[i])

    # Trim to Vmux mapping
    vmux_to_trim = {
        34: "SldoTrimA",
        38: "SldoTrimD",
    }

    # Measure ground once.
    vmux_value_gnd = measurement_config["v_mux_gnd"]
    vmux_gnd = -999.0
    if not debug_gnd:
        vmux_gnd = read_vmux(
            meter,
            yr,
            measurement_config,
            v_mux=vmux_value_gnd,
            use_adc=use_calib_adc,
        )

    # Measure VDDA/VDDD and ROSC vs SldoTrimA/SldoTrimD
    for n, (v_mux, trim_name) in enumerate(vmux_to_trim.items()):
        # Reset i_mea
        i_mea = [{} for _ in range(yr._number_of_chips)]

        # Read initial Trim in chip config
        config_trim, _status = yr.read_register(name=trim_name)

        for trim in measurement_config[trim_name]:
            # Set trim of all chips
            yr.write_register(name=trim_name, value=trim)

            # Run eye-diagram and update the delay in the controller config according to new trim values
            logger.info(f"Running eye diagram for VMUX{v_mux}={trim}")
            _eye, _status = yr.eyeDiagram(skipconfig=True, testsize=100000)

            # if debug GND set, measure the GND for the first VMUX
            if debug_gnd and n == 0:
                vmux_gnd = read_vmux(
                    meter,
                    yr,
                    measurement_config,
                    v_mux=vmux_value_gnd,
                    use_adc=use_calib_adc,
                )

            mea_chips = read_vmux(
                meter,
                yr,
                measurement_config,
                v_mux=v_mux,
                use_adc=use_calib_adc,
            )

            for i, chip in enumerate(yr._enabled_chip_positions):
                # Record vmux and trim.
                i_mea[chip][f"Vmux{v_mux}"] = [mea_chips[i]]
                i_mea[chip][trim_name] = [trim]
                if n == 0:
                    # if debug_gnd=False these values will be the same for all trims
                    i_mea[chip][f"Vmux{vmux_value_gnd}"] = [vmux_gnd[i]]

            # Read ROSC vs trim
            if v_mux == 38:
                mea, _status = yr.read_ringosc()
                for i, chip in enumerate(yr._enabled_chip_positions):
                    rosc_mea = [float(num) for num in mea[i].split()]
                    for j, item in enumerate(rosc_mea):
                        i_mea[chip][f"ROSC{j}"] = [item]

            for chip in yr._enabled_chip_positions:
                data[chip].add_data(i_mea[chip])

        i_mea = [{} for _ in range(yr._number_of_chips)]
        for i, chip in enumerate(yr._enabled_chip_positions):
            # Reset Trim to value in config and restore delay settings via eye diagram
            logger.info(
                f"Set VMUX{v_mux} back to default and re-running :eye: diagram."
            )
            yr.write_register(name=trim_name, value=config_trim[i], chip_position=chip)
            _eye, _status = yr.eyeDiagram(skipconfig=True)

    logger.info("VDDA/VDDD measurement done!")
    logger.info(f"TimeEnd: {datetime.now().strftime('%Y-%m-%d_%H%M%S')}")

    return data
