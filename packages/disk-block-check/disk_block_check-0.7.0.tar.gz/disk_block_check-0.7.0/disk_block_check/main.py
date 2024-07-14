# coding: utf-8

import os
import sys
import time


# base_dir = os.path.dirname(__file__)
# sys.path.insert(0, base_dir)
# sys.path.append(os.path.dirname(base_dir))


from . import GL, __version__
from .low import *
from .args import parse_args
from . import __version__
from .logic import read_sectors, write_sectors, verify_sectors, danger_check_sectors, read_write_bytes
from .error_handler import process_errors


def entry_point():

    args = parse_args(sys.argv[1:])
    GL.block_device_path = args.device_path
    GL.args = args
    GL.version = __version__

    if os.geteuid() != 0:
        print("\n\tRun it as root. \n")
        exit()
    elif args.action == "read":
        errors = read_sectors()
        process_errors(errors)
    elif args.action == "write":
        errors = write_sectors()
        process_errors(errors)
    elif args.action == "verify":
        errors = verify_sectors()
        process_errors(errors)
    elif args.action == "danger_check":
        errors = danger_check_sectors()
        process_errors(errors)
    elif args.action == "read_bytes":
        errors = read_write_bytes(False)
        process_errors(errors)
    elif args.action == "write_bytes":
        errors = read_write_bytes(True)
        process_errors(errors)
    else:
        print("Failed successfully: entry_point. Exiting...")
        exit(-1)
