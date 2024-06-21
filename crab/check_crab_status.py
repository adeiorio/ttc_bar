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
parser.add_argument("--match", dest="match", default="", help="When reading CRAB tasks, take only tasks whose names contain this string")
parser.add_argument("-clean", "--clean", action="store_true", dest="clean", default=False, help="use this flag to clean crab.log inside every input directory")
parser.add_argument("-resubmit", "--resubmit", action="store_true", dest="resubmit", default=False, help="use this flag to resubmit the crab jobs")
parser.add_argument("-getout", "--getout", action="store_true", dest="getout", default=False, help="use this flag to get the output from the crab jobs")
opts = parser.parse_args()

def getfile(sample):
    f = open(str(sample)+".txt", "w")
    url = os.popen('crab getoutput --xrootd --jobids=1 -d crab_' + str(sample) + '/').readlines()[2]
    print(url)
    s1=url.split(str(os.environ.get('USER')))
    print(s1[1])
    s2=s1[1].split('0000')
    print(s2)
    path_xrd = 'root://cms-xrd-global.cern.ch//store/user/' + str(os.environ.get('USER')) + s2[0]
    newurl = 'srm://stormfe1.pi.infn.it:8444/cms/store/user/' + str(os.environ.get('USER')) + s2[0] #:8444/srm/managerv2?SFN=

    print(newurl)
    
    i=0
    print('\nChecking files in the folder '+newurl.strip('\n')+'\n')
    while True:
        print('gfal-ls '+ newurl.strip('\n')+'000'+str(i))
        folder = os.popen('eval `scram unsetenv -sh`; gfal-ls '+ newurl.strip('\n')+'000'+str(i)).readlines()
        newpath_xrd = path_xrd.strip('\n')+'000'+str(i)
        if(len(folder)==0):
            print("The folder does not exist: "+ str(folder))
            break
        print('sottocartella: '+'000'+str(i))
        for file in range(len(folder)):
            if(folder[file].strip('\n') == 'log'):
                continue
            f.write(newpath_xrd+'/'+folder[file]) 
        i+=1

    f.close()
    print(" ")
    print("The file " + str(sample) + ".txt has been created.")
    
    print('Goodbye')

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
              print (colors.colordict["GREEN"] + "Checking status for crab directory: " + colors.colordict['CEND']), 
              print (colors.colordict['BLUE'] + finalDir + colors.colordict['CEND'])
           
              print(os.popen("crab status -d "+filen).read())
              print (50*"=")
              # resubmit the crab task
              if (opts.resubmit):
                 print (colors.colordict['ORANGE'] + "Resubmit:  " + colors.colordict['CEND']),
                 print (colors.colordict['BLUE'] + finalDir + colors.colordict['CEND'])
                 print(os.popen("crab resubmit -d "+filen).read())

              # delete crab.log file
              if (opts.clean):
                 delcmd = "rm "+filen+"/crab.log"
                 print (colors.colordict['ORANGE'] + delcmd + colors.colordict['CEND'])
                 os.system(delcmd)
              # get the output   
              if (opts.getout):
                 os.system("crab getoutput -d " + filen + " --xrootd > " + filen.replace("crab_", "") + ".txt")
                 print("crab getoutput -d " + filen + " --xrootd > " + filen.replace("crab_", "") + ".txt")
                 infile = open(filen.replace("crab_", "") + ".txt")
                 line = infile.readlines()[2]
                 if not line.startswith("root://"):
                    getfile(filen.replace("crab_", ""))
