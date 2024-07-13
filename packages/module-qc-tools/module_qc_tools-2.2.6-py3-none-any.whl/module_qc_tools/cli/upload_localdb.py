#!/usr/bin/env python3
from __future__ import annotations

import json
import logging
import time
from pathlib import Path

import requests
import typer

from module_qc_tools.cli.globals import (
    CONTEXT_SETTINGS,
    OPTIONS,
    LogLevel,
)

logger = logging.getLogger("upload")
app = typer.Typer(context_settings=CONTEXT_SETTINGS)


@app.command()
def main(
    measurement_path: Path = OPTIONS["measurement_path"],
    host: str = OPTIONS["host"],
    port: int = OPTIONS["port"],
    dry_run: bool = OPTIONS["dry_run"],
    output_path: Path = OPTIONS["output_path"],
    _verbosity: LogLevel = OPTIONS["verbosity"],
):
    """
    Walk through the specified directory (recursively) and attempt to submit all json files to LocalDB as the QC measurement

    Given a path to a directory with the output files, the script will recursively
    search the directory and upload all files with the `.json` extension. Supply the
    option `--dry-run` to see which files the script finds without uploading to
    localDB.

    Args:
        path (str or pathlib.Path): root directory to walk through
        host (str): localDB server host
        port (int): localDB server port
        out  (str): analysis output result json file path to save in the local host

    Returns:
        None: The files are uploaded to localDB.
    """

    logger.info("Searching candidate RAW json files...")

    # Allow user to submit single file or directory
    if measurement_path.is_dir():
        flist = list(measurement_path.glob("*.json"))
    elif measurement_path.is_file():
        if measurement_path.suffix == ".json":
            flist = [measurement_path]
        else:
            logger.error(
                f"[bright_red]The file you are trying to upload ({measurement_path}) is not a json file! Please upload the measurement json output file, or a path to the directory containing the measurement output json files.[/]"
            )
            return
    else:
        logger.error(
            f"[bright_red]Input measurement path ({measurement_path}) is not recognized as a json file or path to directory containing json file - please check![/]"
        )
        return

    pack = []
    for path in flist:
        logger.info(f"  - {path}")
        with path.open(encoding="utf-8") as fpointer:
            meas_data = json.load(fpointer)

            # Perform some basic checks on data before uploading

            if len(meas_data) == 0:
                logger.warning(f"[bright_yellow]{path} is empty - please check![/]")
                continue

            if not isinstance(meas_data[0], list):
                logger.error(
                    f"[bright_red]Measurements read from {path} are ill-formatted - please check that you are uploading measurement results and not analysis results![/]"
                )
                continue
            pack.extend(meas_data)

    logger.info(f"Extracted {len(pack)} tests from {len(flist)} input files.")
    logger.info("==> Submitting RAW results pack...")

    protocol = "http" if port != 443 else "https"

    if not dry_run:
        try:
            response = requests.post(
                f"{protocol}://{host}:{port}/localdb/qc_uploader_post",
                json=pack,
                timeout=120,
            )
            response.raise_for_status()

            data = response.json()

            logger.info(data)

        except Exception as err:
            logger.error("failure in uploading!")
            logger.error(err)
            logger.error(response.json())
            raise typer.Exit(1) from err

        logger.info(
            f"\nDone! LocalDB has accepted the following {len(data)} TestRun results"
        )
        for testRun in data:
            if testRun is None:
                logger.info("A test run is already uploaded and will be skipped.")
                continue

            logger.info(
                f'SerialNumber: {testRun["serialNumber"]}, Stage: {testRun["stage"]}, TestType: {testRun["testType"]}, QC-passed: {testRun["passed"]}'
            )

        try:
            with output_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                logger.info(f"Saved the output TestRun to {output_path}")

        except Exception:
            logger.warning(
                f"[bright_yellow]Failed to saved the output TestRun to {output_path}[/]"
            )
            altFilePath = f"/var/tmp/module-qc-tools-record-{int(time.time())}.json"

            try:
                with Path(altFilePath).open("w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
                logger.info(f"Saved the output TestRun to {altFilePath}")

            except Exception:
                logger.warning(
                    f"[bright_yellow]Failed to saved the output TestRun to {altFilePath}[/]"
                )


if __name__ == "__main__":
    typer.run(main)
