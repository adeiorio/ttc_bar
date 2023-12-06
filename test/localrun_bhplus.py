#==============
# Last used:
# python localrun_bhplus.py -m -i /eos/cms/store/group/phys_top/ExtraYukawa/input_for_tests/TTTo2L2Nu_2017.root --year 2017 -o $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test -n 1000
# python localrun_bhplus.py -m -i /eos/cms/store/group/phys_top/ExtraYukawa/input_for_tests/BGToTHpm_MH-200_TuneCP5_13TeV_G2HDM-rhott06_rhotc04_rhotu00.root --year 2017 -o $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test -n 1000
#==============

import os
import sys
import optparse
import ROOT
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.muonScaleResProducer import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.muSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.eleSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.BHProducer import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.topleptonmva import*
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.leptonvariables import *
### main python file to run ###

def main():

  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('--year', dest='year', help='which year sample', default='2018', type='string')
  parser.add_option('-m', dest='ismc', help='to apply sf correction or not', default=True, action='store_true')
  parser.add_option('-n','--nEve', dest='nEvent', help='number of event', type='int', action='store')
  parser.add_option('-i', '--in', dest='inputs', help='input directory with files', default=None, type='string')
  parser.add_option('-d', dest='ismc', help='to apply sf correction or not', action='store_false')
  parser.add_option('-o', '--out', dest='output', help='output directory with files', default=None, type='string')
  (opt, args) = parser.parse_args()

  print ('ismc:',opt.ismc)

  if opt.ismc:
    if opt.year == "2016a":
      p = PostProcessor(opt.output, [opt.inputs], modules=[countHistogramsModule(),puAutoWeight_2016_preAPV(),PrefCorr2016(), TopMVA2016apvProducer(), mu_idisosf_2016APV(),muonScaleRes2016a(),ele_recoidsf_2016APV(), jmeCorrections_UL2016APVMC(), btagSF2016ULapv(), BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(), outputbranchsel="keep_and_drop.txt",maxEntries=opt.nEvent)
    if opt.year == "2016b":
      p = PostProcessor(opt.output, [opt.inputs], modules=[countHistogramsModule(),puAutoWeight_2016_postAPV(), PrefCorr2016(), TopMVA2016postapvProducer(), mu_idisosf_2016(),muonScaleRes2016b(),ele_recoidsf_2016(), jmeCorrections_UL2016MC(), btagSF2016UL(), BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(), outputbranchsel="keep_and_drop.txt",maxEntries=opt.nEvent)
    if opt.year == "2017":
      p = PostProcessor(opt.output, [opt.inputs], modules=[countHistogramsModule(),puWeight_2017(),PrefCorr(),LeptonVariablesModule(), TopMVA2017Producer(), mu_idisosf_2017(),muonScaleRes2017(),ele_recoidsf_2017(), jmeCorrections_UL2017MC(),btagSF2017UL(), BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt",maxEntries=opt.nEvent)
    if opt.year == "2018":
      p = PostProcessor(opt.output, [opt.inputs], modules=[countHistogramsModule(),puAutoWeight_2018(), TopMVA2018Producer(), mu_idisosf_2018(),muonScaleRes2018(),ele_recoidsf_2018(), jmeCorrections_UL2018MC(), btagSF2018UL(), BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(), outputbranchsel="keep_and_drop.txt",maxEntries=opt.nEvent)


# Sequence for data
  if not (opt.ismc):
    if opt.year == "2016b" or opt.year == "2016c" or opt.year == "2016d":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
    if opt.year == "2016e" or opt.year == "2016f":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
    if opt.year == "2016g" or opt.year == "2016h":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016b(),BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
    if opt.year == "2017":
      #p = PostProcessor(opt.output, [opt.inputs], modules=[muonScaleRes2017(),BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),maxEntries=10000)
      p = PostProcessor(opt.output, [opt.inputs], modules=[muonScaleRes2017(), BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),maxEntries=10000)
    if opt.year == "2018a":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
    if opt.year == "2018b":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
    if opt.year == "2018c":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
    if opt.year == "2018d":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis())
  p.run()

if __name__ == "__main__":
    sys.exit(main())
