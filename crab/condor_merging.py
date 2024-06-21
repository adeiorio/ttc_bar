import os
import optparse
import sys
import json

usage = 'python submit_condor.py -d dataset_name -f destination_folder'
parser = optparse.OptionParser(usage)
parser.add_option('-e', '--era', dest='era', type=str, default = '2017', help='Please enter an era')
parser.add_option('-f', '--folder', dest='folder', type=str, default = 'v5', help='Please enter a destination folder')
#parser.add_option('-u', '--user', dest='us', type='string', default = 'ade', help="")
(opt, args) = parser.parse_args()
#Insert here your uid... you can see it typing echo $uid
uid = 0
username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])

def sub_writer(sample, n, folder):
    f = open("condor.sub", "w")
    f.write("Proxy_filename          = x509up_u103214\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    f.write("transfer_input_files    = $(Proxy_path)\n")
    #f.write("transfer_output_remaps  = \""+ sample + "_part" + str(n) + ".root=/eos/user/"+inituser + "/" + username+"/Wprime/nosynch/" + folder + "/" + sample +"/"+ sample + "_part" + str(n) + ".root\"\n")
    f.write("+JobFlavour             = \"workday\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write("executable              = runner_"+sample+"_"+str(n)+".sh \n")
    f.write("output                  = condor/output/"+ sample + "_part" + str(n) + ".out\n")
    f.write("error                   = condor/error/"+ sample + "_part" + str(n) + ".err\n")
    f.write("log                     = condor/log/"+ sample + "_part" + str(n) + ".log\n")
    f.write("MY.SingularityImage     = \"/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/batch-team/containers/plusbatch/el7-full:latest\"\n")
    f.write("queue\n")

def runner_writer(sample, n, files, folder, era):
    f = open("runner_"+sample+"_"+str(n)+".sh", "w")
    f.write("#!/bin/bash \n")
    f.write("cd " + str(os.getcwd()) + "\n")
    #f.write("cmssw-el7 \n")    
    #f.write("eval `scramv1 runtime -sh` \n")
    f.write("pwd \n")
    #f.write("cmsenv \n")
    if n==0:
        f.write("python ../scripts/haddnano.py /eos/cms/store/group/phys_b2g/ExYukawa/bHplus/" + str(era) + "/" + str(folder) + "/" + sample + ".root " + str(files) + "\n")
    else:
        f.write("python ../scripts/haddnano.py /eos/cms/store/group/phys_b2g/ExYukawa/bHplus/" + str(era) + "/" + str(folder) + "/" + sample+"_"+str(n)+ ".root " + str(files) + "\n")
    f.write("rm runner_"+sample+"_"+str(n)+".sh")

if not os.path.exists("condor/output"):
    os.makedirs("condor/output")
if not os.path.exists("condor/error"):
    os.makedirs("condor/error")
if not os.path.exists("condor/log"):
    os.makedirs("condor/log")

folder = opt.folder
split = 30
era = opt.era
#Writing the configuration file
samplesjson = {
    '2016apv': 'bhplus_samples2016apv.json',
    '2016': 'bhplus_samples2016.json',
    '2017': 'bhplus_samples2017.json',
    '2018': 'bhplus_samples2018.json',
}

with open(samplesjson[era], 'r') as fin:
  data = fin.read()
  lines = json.loads(data)
  keys = lines.keys()
  for key, value in lines.items() :
    # for Data
    print(key, value)
    if len(value)==3:
      print("Data sample: ", key)
    if not os.path.exists("/eos/cms/store/group/phys_b2g/ExYukawa/bHplus/" + str(era) + "/" + str(folder)):
        os.makedirs("/eos/cms/store/group/phys_b2g/ExYukawa/bHplus/" + str(era) + "/" + str(folder))
    f = open(value[0] + ".txt", "r")
    files_list = f.read().splitlines()
    print(str(len(files_list)))
    if not value[0].startswith("TTTo"):
        i = 0
        runner_writer(value[0], i, " ".join(f for f in files_list if f.startswith("root:")), folder, era)
        sub_writer(value[0], i, folder)
        os.system('condor_submit condor.sub')
        print('condor_submit condor.sub')
        #os.popen("python tree_skimmer.py " " + value[0] + " " + str(i) + " " + str(files))
    else:
        for i in range(int(len(files_list)/split)+1):
            runner_writer(value[0], i, " ".join( e for e in files_list[split*i:split*(i+1)]), folder, era)
            sub_writer(value[0], i, folder)
            print('condor_submit condor.sub')
            os.system('condor_submit condor.sub')
            #os.popen("python tree_skimmer.py " + value[0] + " " + str(i) + " " + ",".join( e for e in files_list[split*i:split*(i+1)]))
