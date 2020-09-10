#! /usr/bin/env python3

import os
import subprocess
import sys

filepath = '/root/Desktop/Screenshots'

screenshooterPath = ’/usr/bin/xfce4-screenshooter’
options = '-r -s filepath'
subprocess.Popen([screenshooterPath, options])



