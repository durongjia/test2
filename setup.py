#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright 2021 BayLibre, SAS.

import setuptools

setuptools.setup(
    name="aiot-bootrom",
    version="1.1.1",
    author="Fabien Parent",
    author_email="fparent@baylibre.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "": ["bin/bootrom-tool", "bin/bootrom-tool.exe"],
    },
    entry_points={
        'console_scripts': [
            'aiot-bootrom=aiot_bootrom.bootrom:main',
        ]},
);
