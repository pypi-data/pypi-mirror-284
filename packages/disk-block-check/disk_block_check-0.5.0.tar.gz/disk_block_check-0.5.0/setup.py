# coding: utf-8

from setuptools import setup, find_packages
import os
import sys

# https://setuptools.pypa.io/en/latest/userguide/quickstart.html

# https://setuptools.pypa.io/en/latest/userguide/quickstart.html
# pip install --upgrade pip
# pip install --upgrade build
# pip install --upgrade setuptools
# python3 -m pip install --upgrade twine
# python3 -m build
# python3 -m twine upload --repository testpypi dist/*
# pip3 install --no-deps --index-url https://test.pypi.org/simple {package_name}

base_dir = os.path.dirname(__file__)
req_txt_path = os.path.join(base_dir, "requirements.txt")
ver_path = os.path.join(base_dir, "disk_block_check")
ver_path = os.path.join(ver_path, "__version__.py")

main_ns = {}
with open(ver_path, "r", encoding="utf-8") as ver_file_fd:
    exec(ver_file_fd.read(), main_ns)

setup(
    name="disk_block_check",
    version=main_ns["__version__"],
    install_requires=["argparse", "tqdm"],
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['disk_block_check'],  # ['*'] by default
    ),
    entry_points={
        "console_scripts": [
                "disk_block_check = disk_block_check.__main__:main",
            ]
    },
    # include_package_data=True,  # setuptools is so stupid...
    # package_data={
    #     "static": ["static/file.json"]
    # }
)
