#!/bin/env python3
#python check_crab_status.py --match "SingleMuon" --clean

import os
import sys
import re
from PhysicsTools.NanoAODTools.postprocessing.analysis.scripts.aux import colors
from argparse import ArgumentParser

parser = ArgumentParser()

# https://martin-thoma.com/how-to-parse-command-line-arguments-in-python/
# Add more options if you like
parser.add_argument("--match", dest="match", default="",
                    help="When reading CRAB tasks, take only tasks whose names contain this string")
parser.add_argument("-clean", "--clean", action="store_true", dest="clean", default=False,
                    help="use this flag to clean crab.log inside every input directory")
opts = parser.parse_args()


def getFinalCRABDir(opts, crabdir):
   taskNames  = crabdir
   
   if opts.match != "":
      if opts.match.lower() in crabdir.lower():
         return crabdir
      #else:
      #   raise Exception("Did NOT find proper match, try to remove some string") #FIXME
   else:
      return taskNames   
   
filesfolders = os.listdir(".")
folders = []
for filen in filesfolders:
    if os.path.isdir(os.path.join(os.path.abspath("."), filen)):
        if filen.startswith("crab_"):
           
           finalDir = getFinalCRABDir(opts, filen)
           if finalDir != None:
              print colors.colordict["GREEN"] + "Checking status for crab directory: " + colors.colordict['CEND'], colors.colordict['BLUE'] + finalDir + colors.colordict['CEND']
           
              print(os.popen("crab status -d "+filen).read())
              print 50*"="
              # delete crab.log file
              if (opts.clean):
                 delcmd = "rm "+filen+"/crab.log"
                 print colors.colordict['ORANGE'] + delcmd + colors.colordict['CEND']
                 os.system(delcmd)
           
            
