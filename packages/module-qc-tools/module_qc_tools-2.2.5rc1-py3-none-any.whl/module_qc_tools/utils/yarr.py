#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import json
import logging
import re
import sys
import time
from pathlib import Path

from module_qc_tools.utils.hardware_control_base import hardware_control_base

# if sys.version_info >= (3, 9):
#    from importlib import resources
# else:
#    import importlib_resources as resources

logger = logging.getLogger("measurement")


class yarr(hardware_control_base):
    def __init__(self, config, *args, name="yarr", **kwargs):
        self.run_dir = ""
        self.controller = ""
        self.connectivity = ""
        self.scanConsole_exe = ""
        self.write_register_exe = ""
        self.read_register_exe = ""
        self.read_adc_exe = ""
        self.switchLPM_exe = ""
        self.lpm_digitalscan = ""
        self.read_ringosc_exe = ""
        self.eyeDiagram_exe = ""
        self.success_code = 0
        self.emulator = False
        self.usingTempConfig = False
        self.max_attempts = (
            2  # max retries in case of communication failure with module
        )
        self.sleep_attempts = 2  # time (seconds) to sleep after each failed attempt
        super().__init__(config, *args, name=name, **kwargs)
        if "emulator" in self.scanConsole_exe:
            self.emulator = True
            logger.info(f"[{name}] running scanConsole emulator!!")
        if "emulator" in self.write_register_exe:
            self.emulator = True
            logger.info(f"[{name}] running write_register emulator!!")
        if "emulator" in self.switchLPM_exe:
            self.emulator = True
            logger.info(f"[{name}] running switchLPM emulator!!")
        if "emulator" in self.eyeDiagram_exe:
            self.emulator = True
            logger.info(f"[{name}] running eyeDiagram emulator!!")
        connect_spec = self.get_connectivity()
        self._number_of_chips = len(connect_spec["chips"])
        self._enabled_chip_positions = set()
        self._chip_rx = {}
        for chip in range(self._number_of_chips):
            if connect_spec["chips"][chip]["enable"]:
                self._enabled_chip_positions.add(chip)
            self._chip_rx[chip] = connect_spec["chips"][chip]["rx"]
        self._register = [{} for chip in range(self._number_of_chips)]

    def running_emulator(self):
        return self.emulator

    def configure(self, skip_reset=False):
        cmd = f'{self.scanConsole_exe} -r {self.controller} -c {self.connectivity} {"--skip-reset" if skip_reset else ""}'

        self._register = [{} for chip in range(self._number_of_chips)]

        currLevel = logger.getEffectiveLevel()
        logger.setLevel(logging.DEBUG)
        # Below is the only case where success_code=1 is the default.
        # This is because the exit code of scanConsole for configuring the chip is 1 for success.
        # This will have to be removed once the YARR MR is merged (https://gitlab.cern.ch/YARR/YARR/-/issues/192).
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Sending command (attempt {n_try}): ")
                logger.debug(cmd)
                self.send_command(cmd, purpose="configure module", success_code=1)
                logger.setLevel(currLevel)
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning(
                        "Failed to configure. Running eye diagram scan and retrying."
                    )
                    time.sleep(self.sleep_attempts)
                    self.eyeDiagram()
                    continue
                logger.error(
                    f"Unable to configure module after {self.max_attempts} attempts. Continuing measurement."
                )

        # Check for LP-mode
        for handler in logger.handlers:
            if isinstance(handler, logging.FileHandler):
                filename = handler.baseFilename
                with Path(filename).open(encoding="utf-8") as f:
                    for line in f:
                        if "LPM Status" in line:
                            match = int(re.search(r":\s*(\d+)$", line).group(1))
                            if match != 0:
                                logger.warning(
                                    "[bright_yellow]Attention! Module is in low-power mode. If this is not intended, you can turn it off by running `./bin/switchLPM off` in YARR directory.[/]"
                                )

        return 0

    # Reads controller file, returns spec number
    def get_spec(self):
        controller_path = self.run_dir / self.controller
        with controller_path.open(encoding="utf-8") as file:
            controller_params = json.load(file)
        try:
            return controller_params.get("ctrlCfg").get("cfg").get("specNum")
        except Exception:
            logger.warning(
                "Unable to read specNum from controller file. Assuming spec #0"
            )
            return 0

    def run_scan(self, scan, output=None, skip_reset=False):
        if output:
            cmd = f'{self.scanConsole_exe} -r {self.controller} -c {self.connectivity} -s {scan} -o {output} {"--skip-reset" if skip_reset else ""}'
        else:
            cmd = f'{self.scanConsole_exe} -r {self.controller} -c {self.connectivity} -s {scan} {"--skip-reset" if skip_reset else ""}'

        self._register = [{} for chip in range(self._number_of_chips)]

        logger.info(f"Running YARR scan: {scan} ...")
        # Always save scan output in log file
        currLevel = logger.getEffectiveLevel()
        logger.setLevel("DEBUG")
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Sending command (attempt {n_try}): ")
                logger.debug(cmd)
                self.send_command(cmd, purpose="configure module", success_code=0)
                logger.setLevel(currLevel)
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning(
                        "Failed to run scan. Running eye diagram scan and retrying."
                    )
                    time.sleep(self.sleep_attempts)
                    self.eyeDiagram()
                    continue
                logger.error(
                    f"Unable to run scan after {self.max_attempts} attempts. Continuing measurement."
                )

        return 0

    def write_register(self, name, value, chip_position=None):
        if (
            chip_position is not None
            and chip_position not in self._enabled_chip_positions
        ):
            return 0
        if (
            chip_position is not None
            and self._register[chip_position].get(name) == value
        ):
            return 0
        cmd = f'{self.write_register_exe} -r {self.controller} -c {self.connectivity} {"-i "+str(chip_position) if chip_position is not None else ""} {name} {value}'
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Writing register {name} to {value} (attempt {n_try}): ")
                logger.debug(cmd)
                self.send_command(
                    cmd,
                    purpose=f"write register {name}: {value}",
                    success_code=self.success_code,
                )
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning(
                        "Failed to write register. Running eye diagram scan and retrying."
                    )
                    time.sleep(self.sleep_attempts)
                    self.eyeDiagram()
                    continue
                logger.error(
                    f"Unable to write register after {self.max_attempts} attempts. Continuing measurement."
                )

        if chip_position is not None:
            self._register[chip_position][name] = value
        else:
            for chip in range(self._number_of_chips):
                self._register[chip][name] = value

        return 0

    def read_register(self, name, chip_position=None):
        if (
            chip_position is not None
            and chip_position not in self._enabled_chip_positions
        ):
            return 0
        cmd = f'{self.read_register_exe} -r {self.controller} -c {self.connectivity} {"-i "+str(chip_position) if chip_position is not None else ""} {name}'
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Sending command (attempt {n_try}): ")
                logger.debug(cmd)
                result, status = self.send_command_and_read(
                    cmd, purpose="read register", success_code=self.success_code
                )
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning(
                        "Failed to read register. Running eye diagram scan and retrying."
                    )
                    time.sleep(self.sleep_attempts)
                    self.eyeDiagram()
                    continue
                logger.error(
                    f"Unable to read register after {self.max_attempts} attempts. Continuing measurement."
                )

        try:
            result = result.split()
        except Exception:
            logger.debug(
                f"read_register returned a single value ({result}), this happens if only single chip is enabled."
            )
            result = [result]
        return result, status

    def eyeDiagram(self, dryrun=False, skipconfig=False, testsize=None):
        _dryrun = ""
        _skipconfig = ""
        _testsize = ""
        if dryrun:
            _dryrun = "-n"
        if skipconfig:
            _skipconfig = "-s"
        else:
            self._register = [{} for chip in range(self._number_of_chips)]
        if testsize is not None:
            _testsize = f"-t {testsize!s}"

        cmd = f"{self.eyeDiagram_exe} -r {self.controller} -c {self.connectivity} {_dryrun} {_skipconfig} {_testsize}"
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Sending command (attempt {n_try}): ")
                logger.debug(cmd)
                result = self.send_command_and_read(
                    cmd,
                    dtype=str,
                    purpose="eye diagram",
                    success_code=self.success_code,
                )
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning("Failed to run eye diagram. Retrying.")
                    time.sleep(self.sleep_attempts)
                    continue
                logger.error(
                    f"Unable to run eye diagram after {self.max_attempts} attempts. Continuing measurement."
                )
        return result

    def read_adc(
        self,
        vmux,
        chip_position=None,
        readCurrent=False,
        rawCounts=False,
        share_vmux=True,
    ):
        if (
            chip_position is not None
            and chip_position not in self._enabled_chip_positions
        ):
            return 0
        cmd = f'{self.read_adc_exe} -r {self.controller} -c {self.connectivity} {"-i "+str(chip_position) if chip_position is not None else ""} {"-I " if readCurrent else ""} {"-R " if rawCounts else ""} {"-s 63" if share_vmux else ""} {vmux}'
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Sending command (attempt {n_try}): ")
                logger.debug(cmd)
                result = self.send_command_and_read(
                    cmd, dtype=str, purpose="read adc", success_code=self.success_code
                )
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning(
                        "Failed to read ADC. Running eye diagram scan and retrying."
                    )
                    time.sleep(self.sleep_attempts)
                    self.eyeDiagram()
                    continue
                logger.error(
                    f"Unable to read ADC after {self.max_attempts} attempts. Continuing measurement."
                )
        return result

    def read_ringosc(self, chip_position=None):
        if (
            chip_position is not None
            and chip_position not in self._enabled_chip_positions
        ):
            return 0
        cmd = f'{self.read_ringosc_exe} -r {self.controller} -c {self.connectivity} {"-i "+str(chip_position) if chip_position is not None else ""}'
        n_try = 0
        while n_try < self.max_attempts:
            try:
                logger.debug(f"Sending command (attempt {n_try}): ")
                logger.debug(cmd)
                mea, status = self.send_command_and_read(
                    cmd, dtype=str, purpose="read ringsoc"
                )
                break
            except Exception:
                n_try += 1
                if n_try < self.max_attempts:
                    logger.warning(
                        "Failed to read ring oscillator. Running eye diagram scan and retrying."
                    )
                    time.sleep(self.sleep_attempts)
                    self.eyeDiagram()
                    continue
                logger.error(
                    f"Unable to read ring oscillator after {self.max_attempts} attempts. Continuing measurement."
                )
        mea = mea.splitlines()
        return mea, status

    def set_mux(self, chip_position=None, v_mux=-1, i_mux=-1, reset_other_chips=True):
        for chip in range(self._number_of_chips):
            if reset_other_chips:
                self.write_register(name="MonitorV", value=63, chip_position=chip)
                self.write_register(name="MonitorI", value=63, chip_position=chip)
        for chip in range(self._number_of_chips):
            if chip == chip_position:
                # Set Vmux=1 to measure the I_mux pad voltage when a non-negative I_mux value is passed.
                if i_mux >= 0:
                    v_mux = 1
                # TODO: Consider this in read-adc script too
                # Set Imux=63 when measuring NTC pad voltage through Vmux2.
                if v_mux == 2:
                    self.write_register(name="MonitorI", value=63, chip_position=chip)
                    self.write_register(
                        name="MonitorV", value=v_mux, chip_position=chip
                    )
                self.write_register(name="MonitorV", value=v_mux, chip_position=chip)
                if i_mux >= 0:
                    self.write_register(
                        name="MonitorI", value=i_mux, chip_position=chip
                    )
        return 0

    def reset_tempsens_enable(self, chip_position=None):
        self.write_register(
            name="MonSensSldoAnaEn", value=0, chip_position=chip_position
        )
        self.write_register(
            name="MonSensSldoDigEn", value=0, chip_position=chip_position
        )
        self.write_register(name="MonSensAcbEn", value=0, chip_position=chip_position)

        return 0

    def reset_tempsens_bias(self, chip_position=None):
        self.write_register(
            name="MonSensSldoAnaSelBias", value=0, chip_position=chip_position
        )

        self.write_register(
            name="MonSensSldoDigSelBias", value=0, chip_position=chip_position
        )

        self.write_register(
            name="MonSensAcbSelBias", value=0, chip_position=chip_position
        )

        return 0

    def reset_tempsens_dem(self, chip_position=None):
        self.write_register(
            name="MonSensSldoAnaDem", value=0, chip_position=chip_position
        )

        self.write_register(
            name="MonSensSldoDigDem", value=0, chip_position=chip_position
        )

        self.write_register(name="MonSensAcbDem", value=0, chip_position=chip_position)

        return 0

    def reset_tempsens(self, chip_position=None):
        self.reset_tempsens_enable(chip_position=chip_position)
        self.reset_tempsens_bias(chip_position=chip_position)
        self.reset_tempsens_dem(chip_position=chip_position)

        return 0

    def enable_tempsens(self, chip_position=None, v_mux=-1, reset_other_chips=True):
        # First reset all MOS sensors.
        self.reset_tempsens_enable(chip_position=chip_position)

        if v_mux == 14:
            self.write_register(
                name="MonSensSldoAnaEn", value=1, chip_position=chip_position
            )
        elif v_mux == 16:
            self.write_register(
                name="MonSensSldoDigEn", value=1, chip_position=chip_position
            )
        elif v_mux == 18:
            self.write_register(
                name="MonSensAcbEn", value=1, chip_position=chip_position
            )
        else:
            msg = "Incorrect VMUX value for measuring temperature!"
            raise RuntimeError(msg)

        if reset_other_chips and chip_position is not None:
            for chip in range(self._number_of_chips):
                if chip == chip_position:
                    continue
                self.reset_tempsens_enable(chip_position=chip)

        return 0

    def set_tempsens_bias(
        self, chip_position=None, v_mux=-1, bias=0, reset_other_chips=True
    ):
        if v_mux == 14:
            self.write_register(
                name="MonSensSldoAnaSelBias", value=bias, chip_position=chip_position
            )
        elif v_mux == 16:
            self.write_register(
                name="MonSensSldoDigSelBias", value=bias, chip_position=chip_position
            )
        elif v_mux == 18:
            self.write_register(
                name="MonSensAcbSelBias", value=bias, chip_position=chip_position
            )
        else:
            msg = "Incorrect VMUX value for measuring temperature!"
            raise RuntimeError(msg)

        if reset_other_chips and chip_position is not None:
            for chip in range(self._number_of_chips):
                if chip == chip_position:
                    continue
                self.reset_tempsens(chip_position=chip)

        return 0

    # TODO Does it even make sense to have reset option here? That only matters when setting MonitorV
    def set_tempsens_dem(
        self, chip_position=None, v_mux=-1, dem=0, reset_other_chips=True
    ):
        if v_mux == 14:
            self.write_register(
                name="MonSensSldoAnaDem", value=dem, chip_position=chip_position
            )
        elif v_mux == 16:
            self.write_register(
                name="MonSensSldoDigDem", value=dem, chip_position=chip_position
            )
        elif v_mux == 18:
            self.write_register(
                name="MonSensAcbDem", value=dem, chip_position=chip_position
            )
        else:
            msg = "Incorrect VMUX value for measuring temperature!"
            raise RuntimeError(msg)
        if reset_other_chips and chip_position is not None:
            for chip in range(self._number_of_chips):
                if chip == chip_position:
                    continue
                self.reset_tempsens(chip_position=chip)

        return 0

    def set_trim(self, chip_position=None, v_mux=-1, trim=0):
        if v_mux == 34:
            self.write_register(
                name="SldoTrimA", value=trim, chip_position=chip_position
            )
        elif v_mux == 38:
            self.write_register(
                name="SldoTrimD", value=trim, chip_position=chip_position
            )
        else:
            msg = "Incorrect VMUX value for setting trim!"
            raise RuntimeError(msg)

        return 0

    def switchLPM(self, position):
        cmd = f"{self.switchLPM_exe} {position} -s {self.get_spec()}"
        return self.send_command(cmd, purpose="switch LP mode on/off")

    def get_connectivity(self):
        with Path(self.connectivity).open(encoding="utf-8") as file:
            return json.load(file)

    def get_config(self, chip_position):
        connect_spec = self.get_connectivity()
        config_path = connect_spec["chips"][chip_position]["config"]
        path = Path(self.connectivity).parent / config_path

        with Path(path).open(encoding="utf-8") as file:
            spec = json.load(file)

        with contextlib.suppress(KeyError):
            chipname = ""
            try:
                chipname = next(iter(spec))
            except IndexError:
                logger.warning("Empty Chip Config")
            spec[chipname].pop("PixelConfig")

        return spec

    def omit_pixel_config(self, tmp_dir_name="tmp"):
        tmp_dir = str(Path(self.connectivity).parent) + "/" + tmp_dir_name
        logger.info(
            f"Creating temporary connectivity file and chip configs without pixel config in {tmp_dir}"
        )

        # Create new directory for new temporary files, will not overwrite if it already exists
        try:
            Path(tmp_dir).mkdir(parents=True, exist_ok=False)
        except Exception:
            logger.error(
                f"[bright_red]Unable to make temporary directory: {tmp_dir} , please delete this directory or choose a different directory name[/]"
            )
            sys.exit(1)

        # Create new connectivity file pointing to new chip config files
        new_conn = (
            str(Path(self.connectivity).with_suffix("").stem) + "_noPixConfig.json"
        )
        with Path(self.connectivity).open(encoding="utf-8") as file:
            orig_config = json.load(file)
        new_config = orig_config
        for i, c in enumerate(orig_config["chips"]):
            new_path = str(Path(c["config"]).with_suffix("").stem) + "_noPixConfig.json"
            new_config["chips"][i]["config"] = new_path

            # Save temporary chip config (without Pixel Config)
            new_chip_config = Path(tmp_dir + "/" + new_path)
            new_chip_config.touch(exist_ok=False)
            with new_chip_config.open(mode="w", encoding="utf-8") as file:
                json.dump(self.get_config(i), file, indent=4)

        new_conn_file = Path(tmp_dir + "/" + new_conn)
        new_conn_file.touch(exist_ok=False)
        with new_conn_file.open(mode="w", encoding="utf-8") as fp:
            json.dump(new_config, fp, indent=4)

        # Use temporary connectivity file
        self.connectivity = tmp_dir + "/" + new_conn
        self.usingTempConfig = True
        return 0

    def remove_tmp_connectivity(self):
        logger.info(f"Deleting temporary files: {Path(self.connectivity).parent}")
        if not self.usingTempConfig:
            logger.warning(
                "[bright_yellow]Requesting to delete temporary config files - but temporary config files are not being used! Will not delete any files.[/]"
            )
            return 0

        if Path(self.connectivity).parent.exists():
            for child in Path(self.connectivity).parent.iterdir():
                child.unlink()
            Path(self.connectivity).parent.rmdir()
        else:
            logger.warning(
                f"[bright_yellow]Temporary files ({Path(self.connectivity).parent}) do not exist - something may have gone wrong[/]"
            )
        return 0
