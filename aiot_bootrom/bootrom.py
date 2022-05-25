# SPDX-License-Identifier: MIT
# Copyright 2021 (c) BayLibre, SAS
# Author: Fabien Parent <fparent@baylibre.com>

import pkg_resources
import platform
import subprocess
import sys

if platform.system() == 'Linux':
    import pyudev

def udev_wait():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem="usb")

    for action, device in monitor:
        if 'ID_VENDOR_ID' in device and 'ID_MODEL_ID' in device:
            if device['ID_VENDOR_ID'] == '0e8d':
                if action == 'bind':
                    break

def main():
    bin_name = 'bin/bootrom-tool'
    if platform.system() == "Windows":
        bin_name += ".exe"

    binary = pkg_resources.resource_filename('aiot_bootrom', bin_name)
    sys.argv[0] = binary

    try:
        if platform.system() == 'Linux':
            udev_wait()
        subprocess.run(sys.argv, check=True)
    except KeyboardInterrupt:
        pass
