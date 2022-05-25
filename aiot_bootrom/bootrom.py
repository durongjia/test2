# SPDX-License-Identifier: MIT
# Copyright 2021 (c) BayLibre, SAS
# Author: Fabien Parent <fparent@baylibre.com>

import pkg_resources
import platform
import subprocess
import sys
import time

def main():
    bin_name = 'bin/bootrom-tool'
    if platform.system() == "Windows":
        bin_name += ".exe"

    binary = pkg_resources.resource_filename('aiot_bootrom', bin_name)
    sys.argv[0] = binary

    for _ in range(5):
        try:
            subprocess.run(sys.argv, check=True)
        except KeyboardInterrupt:
            pass
        except Exception as expt:
            print("aiot_bootrom failure: ", expt)
            time.sleep(0.2)
