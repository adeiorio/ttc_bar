#==============
# Last used:
# python submit_and_delete_unnecessary_files.py --i "config_crab_2016_signal_11"
#==============

#!/bin/env python3

import os
import sys
import re
import argparse

usage = 'usage: %prog [options]'
parser = argparse.ArgumentParser(description=usage)
parser.add_argument('-i', '--indir', dest='indir')
parser.add_argument("--submit", action="store_true")
args = parser.parse_args()

if args.indir is None:
    print ("Provide one directory (-i dir_name) with input crab config files")
    sys.exit(1)
if not args.submit:
    print ("It was just a test, do ( --submit) for actual submission")
    sys.exit(1)

path = args.indir
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        if ".pyc" not in file and "init" not in file  and "list_input_sample" not in file and file.endswith("py"):
            print "crab submit -c "+path+"/"+file
            os.popen("crab submit -c "+path+"/"+file).read()
            # latest directory
            fld = os.popen('ls -td -- */ | head -n 1').read().rstrip()
            print fld
            fld = "rm "+fld+"/inputs/*.tgz"
            os.popen(fld).read().rstrip()
