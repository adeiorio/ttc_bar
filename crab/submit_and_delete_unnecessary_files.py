#==============
# Last used:
# python submit_and_delete_unnecessary_files.py -i "bhplus_config_crab_2017"
#==============

#!/bin/env python3

import os
import sys
import re
import argparse
from PhysicsTools.NanoAODTools.postprocessing.analysis.scripts.aux import colors

usage = 'usage: %prog [options]'
parser = argparse.ArgumentParser(description=usage)
parser.add_argument('-i', '--indir', dest='indir')
parser.add_argument("--submit", action="store_true")
args = parser.parse_args()

if args.indir is None:
    print (colors.colordict['ORANGE']+"Provide one directory (-i dir_name) with input crab config files"+colors.colordict['CEND'])
    sys.exit(1)
if not args.submit:
    print (colors.colordict["ORANGE"]+"It was just a test, "+colors.colordict['CEND']+colors.colordict["GREEN"]+ "do ( --submit) for actual submission"+colors.colordict['CEND'])
    sys.exit(1)

path = args.indir
files = os.listdir(path)
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        if ".pyc" not in file and "init" not in file  and "list_input_sample" not in file and file.endswith("py"):
            print (colors.colordict["GREEN"]+"crab submit -c "+path+"/"+file+colors.colordict['CEND'])
            os.popen("crab submit -c "+path+"/"+file).read()
            # latest directory
            fld = os.popen('ls -td -- */ | head -n 1').read().rstrip()
            print fld
            fld = "rm "+fld+"/inputs/*.tgz"
            os.popen(fld).read().rstrip()
