#!/bin/bash -e 
echo "TEST FIRST" 

PWD=`pwd`
HOME=$PWD

echo $HOME 
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh

# this is the actual work dir (replaced from python)
WorkDir=/afs/cern.ch/user/g/gkole/work/BHplus/2017_Ntuple_temp_lxplus7/CMSSW_10_6_30/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test/

cd $WorkDir
ls -lrth
eval `scramv1 runtime -sh`

# run the command to skim
python private_production_test.py --batch 1 --indir /eos/cms/store/group/phys_b2g/ExYukawa/ntu_prod/TBarZQB_2017UL/ --outdir /eos/cms/store/group/phys_b2g/ExYukawa/bHplus/2017/TBarZQB_test --fpjob 1000
