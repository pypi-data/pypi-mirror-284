# coding: utf-8


import argparse
from . import __version__


def parse_args(args: list):
    parser = argparse.ArgumentParser(
        prog="disk_block_check",
        description="Disk Block Check\n"
                    "Use one of these items: \n"
                    "1) {read} - only read. Sector by sector. "
                    "In most cases, this is enough to identify the problem on the device. "
                    "2) {write}, then {verify} - Write hashes to device at the first, then verify (read) them. "
                    "3) {danger_verify} - read data to store, write hashes, verify them and restore the initial data. "
                    "And so on for each device sector. Sector by sector one by one. "
                    "If an error occurs or power outage happened, data may be lost. "
                    "So this can be used where there is no time to transfer data from the device. Use at your own risk",
                                     )

    parser.add_argument('--version', action='version', version=f"V{__version__}")

    parser.add_argument("action", choices=["read", "write", "verify", "danger_verify"],
                        help="Action to perform on the device")

    parser.add_argument("device_path", type=str,
                        help="Path to the device")

    parser.add_argument("--start", "--from", type=int, required=False,
                        help="Starting value for the operation (including)")

    parser.add_argument("--end", "--to", type=int, required=False,
                        help="Ending value for the operation (including)")

    parser.add_argument("--mode", type=int, choices=[1, 2, 3], required=False,
                        help="Mode for the operation")

    parser.add_argument("--yes", required=False, action="store_true",
                        help="Automatically answer positive on any questions. ")

    args = parser.parse_args(args)

    return args
