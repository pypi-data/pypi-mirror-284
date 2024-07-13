#  Copyright 2022-present, the Waterdip Labs Pvt. Ltd.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import Union

import click

from dcs_cli.__version__ import __version__
from dcs_cli.dcs.cli import data_diff_cli


@click.version_option(version=__version__, package_name="dcs_cli", prog_name="DCS CLI")
@click.group(help=f"DCS CLI version {__version__}")
def main():
    pass


@main.command(
    short_help="Starts DCS CLI",
)
@click.option(
    "-C",
    "--config-path",
    required=True,
    default=None,
    help="Specify the file path for configuration",
)
@click.option(
    "--save-json",
    "-j",
    is_flag=True,
    help="Save data into JSON file",
)
@click.option(
    "--json-path",
    "-jp",
    required=False,
    default="dcs_report.json",
    help="Specify the file path for JSON file",
)
@click.option(
    "--compare",
    required=True,
    help="Run only specific comparison using comparison name",
)
@click.option(
    "--stats",
    is_flag=True,
    help="Print stats about data diff",
)
@click.option(
    "--send-data",
    is_flag=True,
    help="Send Data to server",
)
@click.option(
    "--html-report",
    is_flag=True,
    help="Save table as HTML",
)
@click.option(
    "--report-path",
    required=False,
    default="dcs_report.html",
    help="Specify the file path for HTML report",
)
def run(
    config_path: Union[str, None],
    save_json: bool = False,
    json_path: str = "dcs_report.json",
    compare: str = None,
    stats: bool = False,
    send_data: bool = False,
    html_report: bool = False,
    report_path: str = "dcs_report.html",
):
    data_diff_cli(
        config_path=config_path,
        save_json=save_json,
        json_path=json_path,
        compare=compare,
        is_cli=True,
        show_stats=stats,
        send_data=send_data,
        html_report=html_report,
        report_path=report_path,
    )


if __name__ == "__main__":
    main()
