# coding: utf-8

import os
from tqdm import tqdm

from .low import *
from . import GL
import time


def define_start_and_end():
    GL.sectors_num = get_sectors_num(GL.block_device_path)
    if GL.args.start is not None:
        GL.start = GL.args.start
    else:
        GL.start = 0
    if GL.args.end is not None:
        GL.end = GL.args.end
    else:
        GL.end = GL.sectors_num-1

    if GL.start < 0:
        print(f"\n--start ({GL.start}) cannot be negative")
        exit()
    if GL.start > GL.end:
        print(f"\n--start ({GL.start}) cannot be greater then --end ({GL.end})")
        exit()

    if GL.end >= GL.sectors_num:
        print(f"--end must be less than sectors on device {GL.block_device_path}")
        print(f"end={GL.end} >= sectors={GL.sectors_num}")
        exit()

    if GL.start >= GL.sectors_num:
        print(f"--end must be less than sectors on device {GL.block_device_path}")
        print(f"end={GL.end} >= sectors={GL.sectors_num}")
        exit()


def open_device(mode: str = "rb+"):
    GL.bd = open(GL.block_device_path, mode)


def close_device():
    GL.bd.close()


def interrupt_if_need():
    if GL.args.interrupt:
        input(f"Error occurred. Use CTRL+C to exit or Enter to continue...")


def process_pbar_postfix_init():
    GL.pbar_postfix = {}
    GL.pbar_postfix["prev_MB"] = 0
    GL.pbar_postfix["prev_time"] = time.time()


def process_pbar_postfix(pbar, i: int):
    ONE_MB = 1024*1024
    if not i % 1024:
        current_MB = (i*512)/ONE_MB
        current_time = time.time()
        mb_per_sec = 0
        try:
            mb_per_sec = (current_MB-GL.pbar_postfix["prev_MB"])/(current_time-GL.pbar_postfix["prev_time"])
        except ZeroDivisionError:
            pass

        GL.pbar_postfix["prev_MB"] = current_MB
        GL.pbar_postfix["prev_time"] = current_time

        pbar.set_postfix({"MB": f"{current_MB:.2f}", "MB/s": f"{mb_per_sec:.2f}"})


def read_sectors() -> list:
    """
    start and end included
    return errors
    """
    errors = []

    define_start_and_end()

    start_sector, end_sector = GL.start, GL.end

    open_device("rb")

    block_device = GL.bd
    pbar = tqdm(range(start_sector, end_sector+1))
    process_pbar_postfix_init()
    for i in pbar:
        try:
            bs = read_sector(block_device, i)
        except OSError as e:
            if e.errno == 5:
                print(f"Input/output error in sector: {i}")
                errors.append({5: f"Input/output error in sector: {i}"})
                interrupt_if_need()
            else:
                print(f"Another error {e.errno}: {e}")
                errors.append({e.errno: f"Another error {e.errno}: {e}"})
                interrupt_if_need()
        except Exception as e_e:
            print(f"Another error: {e_e}")
            errors.append({-1: f"Another error: {e_e}"})
            interrupt_if_need()

        process_pbar_postfix(pbar, i)

    return errors


def write_sectors() -> list:
    """
    start and end included
    return errors
    """
    errors = []

    define_start_and_end()

    start_sector, end_sector = GL.start, GL.end

    if not GL.args.yes:
        input(f"All data on device \"{GL.block_device_path}\" will be erased. Use CTRL+C to exit or Enter to continue...")

    open_device("wb")

    block_device = GL.bd
    pbar = tqdm(range(start_sector, end_sector+1))
    process_pbar_postfix_init()
    for i in pbar:
        try:
            data_to_write = get_hash_from_sector_number(i+578)
            write_sector(block_device, i, data_to_write)
        except OSError as e:
            if e.errno == 5:
                print(f"Input/output error in sector: {i}")
                errors.append({5: f"Input/output error in sector: {i}"})
                interrupt_if_need()
            else:
                print(f"Another error {e.errno}: {e}")
                errors.append({e.errno: f"Another error {e.errno}: {e}"})
                interrupt_if_need()
        except Exception as e_e:
            print(f"Another error: {e_e}")
            errors.append({-1: f"Another error: {e_e}"})
            interrupt_if_need()

        process_pbar_postfix(pbar, i)

    return errors


def verify_sectors() -> list:
    """
    start and end included
    return errors
    """
    errors = []

    define_start_and_end()

    start_sector, end_sector = GL.start, GL.end

    open_device("rb")

    block_device = GL.bd
    pbar = tqdm(range(start_sector, end_sector+1))
    process_pbar_postfix_init()
    for i in pbar:
        try:
            sector_hash = get_hash_from_sector_number(i+578)
            readed_hash = read_sector(block_device, i)
            if readed_hash != sector_hash:
                print(f"Hashes do not match at sector: {i}")
                errors.append({0: f"Hashes do not match at sector: {i}"})
                interrupt_if_need()
        except OSError as e:
            if e.errno == 5:
                print(f"Input/output error in sector: {i}")
                errors.append({5: f"Input/output error in sector: {i}"})
                interrupt_if_need()
            else:
                print(f"Another error {e.errno}: {e}")
                errors.append({e.errno: f"Another error {e.errno}: {e}"})
                interrupt_if_need()
        except Exception as e_e:
            print(f"Another error: {e_e}")
            errors.append({-1: f"Another error: {e_e}"})
            interrupt_if_need()

        process_pbar_postfix(pbar, i)

    return errors


def danger_check_sectors() -> list:
    """
    start and end included
    return errors
    """
    errors = []

    define_start_and_end()

    start_sector, end_sector = GL.start, GL.end

    if not GL.args.yes:
        input(f"Data may be lost during execution if there is a power outage or other unexpected error. "
              f"Use at your own risk. \n"
              f"If the data cannot be restored after sector \"danger checking\", it will be output to the terminal, "
              "and you can restore it using action {write_bytes}. \n"
              f"Use CTRL+C to exit or Enter to continue...")

    open_device("rb+")

    block_device = GL.bd
    pbar = tqdm(range(start_sector, end_sector+1))
    process_pbar_postfix_init()
    for i in pbar:
        try:
            data_before = read_sector(block_device, i)
            sector_hash = get_hash_from_sector_number(i)

            write_sector(block_device, i, sector_hash)
            readed_hash = read_sector(block_device, i)

            write_sector(block_device, i, data_before)
            if data_before != read_sector(block_device, i):
                print(f"Data cannot be restored at sector: {i}")
                print(bytes_to_str(data_before))
                errors.append({0: f"Data cannot be restored at sector: {i}"})
                interrupt_if_need()
            if readed_hash != sector_hash:
                print(f"Hashes do not match at sector: {i}")
                errors.append({0: f"Hashes do not match at sector: {i}"})
                interrupt_if_need()
        except OSError as e:
            if e.errno == 5:
                print(f"Input/output error in sector: {i}")
                errors.append({5: f"Input/output error in sector: {i}"})
                interrupt_if_need()
            else:
                print(f"Another error {e.errno}: {e}")
                errors.append({e.errno: f"Another error {e.errno}: {e}"})
                interrupt_if_need()
        except Exception as e_e:
            print(f"Another error: {e_e}")
            errors.append({-1: f"Another error: {e_e}"})
            interrupt_if_need()

        process_pbar_postfix(pbar, i)

    return errors


def read_write_bytes(read_write: bool):
    errors = []
    i = int(input("Input sector number: "))
    bs = None
    if read_write:
        bs_as_str = input("Enter bytes: \n")
        bs = str_to_bytes(bs_as_str)
        assert len(bs) == GL.SECTOR_SIZE

    if read_write and not GL.args.yes:
        input(f"Sector of the device \"{GL.block_device_path}\" will be rewrited with inputted bytes. "
              f"Use CTRL+C to exit or Enter to continue...")

    if read_write == False:
        open_device("rb")
    else:
        open_device("wb")
    block_device = GL.bd

    try:
        if read_write == False:
            bs = read_sector(block_device, i)
            print(f"Readed bytes from sector {i} of device \"{GL.block_device_path}\": \n{bytes_to_str(bs)}")
        else:
            write_sector(block_device, i, bs)
    except OSError as e:
        if e.errno == 5:
            print(f"Input/output error in sector: {i}")
            errors.append({5: f"Input/output error in sector: {i}"})
        else:
            print(f"Another error {e.errno}: {e}")
            errors.append({e.errno: f"Another error {e.errno}: {e}"})
    except Exception as e_e:
        print(f"Another error: {e_e}")
        errors.append({-1: f"Another error: {e_e}"})

    print("\nDone! ")

    return errors
