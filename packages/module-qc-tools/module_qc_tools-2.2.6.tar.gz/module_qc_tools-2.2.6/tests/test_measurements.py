from __future__ import annotations

from types import SimpleNamespace

import pytest

import module_qc_tools as mqt
from module_qc_tools.measurements.adc_calibration import run
from module_qc_tools.utils.misc import (
    load_config,
)
from module_qc_tools.utils.power_supply import power_supply
from module_qc_tools.utils.yarr import yarr


@pytest.fixture()
def config_emulator():
    return load_config(mqt.data / "configs" / "emulator_merged_vmux.json")


@pytest.fixture()
def hardware(config_emulator):
    return SimpleNamespace(
        ps=power_supply(config_emulator["power_supply"]),
        yr=yarr(config_emulator["yarr"]),
    )


def test_issue114(config_emulator, hardware):
    TEST_TYPE = "ADC_CALIBRATION"
    layer = "L1"
    measurement_config = config_emulator["tasks"]["GENERAL"]
    measurement_config.update(config_emulator["tasks"][TEST_TYPE])

    hardware.ps.set(
        v=measurement_config["v_max"], i=measurement_config["i_config"][layer]
    )

    data = run(config_emulator, hardware.ps, hardware.yr, layer, False)
    metadata = data[0].get_meta_data()

    assert "ChipConfigs" in metadata
    assert "RD53B" in metadata["ChipConfigs"]
    assert "GlobalConfig" in metadata["ChipConfigs"]["RD53B"]
    assert "InjVcalRange" in metadata["ChipConfigs"]["RD53B"]["GlobalConfig"]
