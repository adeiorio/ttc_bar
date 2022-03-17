#!/bin/env python3

import os
import sys
import re


# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class colors:
   colordict = {
                'RED'        : '\033[91m',
                'GREEN'      : '\033[92m',
                'BLUE'       : '\033[34m',
                'GRAY'       : '\033[90m',
                'WHITE'      : '\033[00m',
                'ORANGE'     : '\033[33m',
                'CYAN'       : '\033[36m',
                'PURPLE'     : '\033[35m',
                'LIGHTRED'   : '\033[91m',
                'PINK'       : '\033[95m',
                'YELLOW'     : '\033[93m',
                'BLINK'      : '\033[5m' ,
                'NORMAL'     : '\033[28m' ,
                "WARNING"    : '\033[33m',
                "CEND"       : '\033[0m',
                }

filesfolders = os.listdir(".")
folders = []
for filen in filesfolders:
    if os.path.isdir(os.path.join(os.path.abspath("."), filen)):
        if filen.startswith("crab_"):
            print colors.colordict["GREEN"] + "Checking status for crab directory: " + colors.colordict['CEND'], colors.colordict['BLUE'] + filen + colors.colordict['CEND']
            
            print(os.popen("crab status -d "+filen).read())
            print 50*"="
            
            
