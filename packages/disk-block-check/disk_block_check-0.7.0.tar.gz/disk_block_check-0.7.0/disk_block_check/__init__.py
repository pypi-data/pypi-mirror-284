# coding: utf-8


class GL:
    SECTOR_SIZE = 512  # bytes
    block_device_path = None
    version = None
    bd = None  # opened block device
    args = None
    start = None
    end = None
    sectors_num = None
    pbar_postfix = None


from disk_block_check.__version__ import __version__
from disk_block_check.main import entry_point


GL.version = __version__


__all__ = [__version__, GL]


def main():
    entry_point()
