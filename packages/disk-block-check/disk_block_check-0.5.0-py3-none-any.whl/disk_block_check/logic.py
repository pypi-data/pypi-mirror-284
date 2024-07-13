# coding: utf-8

import os
from tqdm import tqdm

from .low import *
from . import GL


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
    for i in pbar:
        try:
            bs = read_sector(block_device, i)
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

        if not i % 1024:
            pbar.set_postfix({"MB": f'{(i*512)/(1024*1024):.2f}'})

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
    for i in pbar:
        try:
            data_to_write = get_hash_from_sector_number(i+578)
            write_sector(block_device, i, data_to_write)
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

        if not i % 1024:
            pbar.set_postfix({"MB": f'{(i*512)/(1024*1024):.2f}'})

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
    for i in pbar:
        try:
            sector_hash = get_hash_from_sector_number(i+578)
            readed_hash = read_sector(block_device, i)
            if readed_hash != sector_hash:
                print(f"Hashes do not match at sector: {i}")
                errors.append({0: f"Hashes do not match at sector: {i}"})
                input()
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

        if not i % 1024:
            pbar.set_postfix({"MB": f'{(i*512)/(1024*1024):.2f}'})

    return errors


def danger_verify_sectors() -> list:
    """
    start and end included
    return errors
    """
    errors = []

    define_start_and_end()

    start_sector, end_sector = GL.start, GL.end

    open_device("rb+")

    block_device = GL.bd
    pbar = tqdm(range(start_sector, end_sector+1))
    for i in pbar:
        try:
            data_before = read_sector(block_device, i)
            sector_hash = get_hash_from_sector_number(i)

            write_sector(block_device, i, sector_hash)
            readed_hash = read_sector(block_device, i)

            write_sector(block_device, i, data_before)
            if data_before != read_sector(block_device, i):
                print(f"Data cannot be restored at sector: {i}")
                errors.append({0: f"Data cannot be restored at sector: {i}"})
            if readed_hash != sector_hash:
                print(f"Hashes do not match at sector: {i}")
                errors.append({0: f"Hashes do not match at sector: {i}"})
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

        if not i % 1024:
            pbar.set_postfix({"MB": f'{(i*512)/(1024*1024):.2f}'})

    return errors
