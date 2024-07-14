# coding: utf-8

import os
import stat
import hashlib
import re
import subprocess

import argparse


from . import GL


def sha512sum(bs: bytes) -> bytes:
    return hashlib.sha512(bs).digest()


def get_hash_from_sector_number(sector_number) -> bytes:
    """
    return 512 BYTES hash of sector_number
    """
    res = sha512sum(sector_number.to_bytes(64, byteorder='big'))
    for i in range(7):  # 512 BYTES = 8 times * 64 bytes (512 bit)
        res += sha512sum(res)
    return res


def int_to_byte512(a: int) -> bytes:
    return a.to_bytes(512, byteorder='big')


def byte512_to_int(bs: bytes) -> int:
    return int.from_bytes(bs)


def get_sectors_num(device_path: str) -> int or None:
    if os.path.exists(device_path):
        if os.path.isfile(device_path) or stat.S_ISBLK(os.stat(device_path).st_mode):
            if os.path.isfile(device_path):
                print(f"\"{device_path}\" is not block device. It is a file. Continues anyway...")
            try:
                result = subprocess.run(['fdisk', '-l', device_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True)

                if result.returncode == 0:
                    match = re.search(r'\sbytes,\s(\d+) sectors', result.stdout)
                    sector_nums = int(match.group(1))

                    return sector_nums
                else:
                    print(f"Error while run fdisk: {result.stderr}")
                    return None
            except Exception as e:
                print(f"Error: {e}")
                return None
        else:
            if os.path.isdir(device_path):
                print(f"This \"{device_path}\" is directory. File needed. Exiting.")
                exit()
    else:
        print(f"No such file: \"{device_path}\". Exiting.")
        exit(-1)


def write_sector(block_device: "TextIO", sector_num: int, bs: bytes):
    """
    sudo dd if=/dev/sdx bs=512 count=1 skip=sector_num
    """
    SECTOR_SIZE = GL.SECTOR_SIZE
    assert len(bs) == SECTOR_SIZE
    block_device.seek(sector_num * SECTOR_SIZE)
    block_device.write(bs)
    block_device.flush()


def read_sector(block_device: "TextIO", sector_num: int) -> bytes:
    """
    sudo dd of=/dev/sdx bs=512 count=1 skip=sector_num < -
    """
    SECTOR_SIZE = GL.SECTOR_SIZE
    block_device.seek(sector_num * SECTOR_SIZE)
    res = block_device.read(SECTOR_SIZE)
    assert len(res) == SECTOR_SIZE
    return res


def bytes_to_str(bs: bytes) -> str:
    a = list(bs)  # list of ints
    res = ", ".join(map(str, a))
    return f"[{res}]"


def str_to_bytes(s: str) -> bytes:
    a = list(map(int, s[1:len(s)-1].split(", ")))
    return bytes(a)
