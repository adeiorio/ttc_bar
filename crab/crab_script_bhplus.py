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
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles, runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.leptonvariables import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.modules.topleptonmva import*
### main python file to run ###

def main():

  usage = 'usage: %prog [options]'
  parser = optparse.OptionParser(usage)
  parser.add_option('--year', dest='year', help='which year sample', default='2018', type='string')
  parser.add_option('-m', dest='ismc', help='to apply sf correction or not', default=True, action='store_true')
  parser.add_option('-d', dest='ismc', help='to apply sf correction or not', action='store_false')
  (opt, args) = parser.parse_args()

  if opt.ismc:
    if opt.year == "2016a":
      p = PostProcessor(".", inputFiles(), modules=[countHistogramsModule(),puWeight_2016_preAPV(),PrefCorr2016(),LeptonVariablesModule(), TopMVA2016apvProducer(), mu_idisosf_2016APV(),muonScaleRes2016a(),ele_recoidsf_2016APV(),jmeCorrections_UL2016APVMC(),btagSF2016ULapv(), BH2016apv()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016b":
      p = PostProcessor(".", inputFiles(), modules=[countHistogramsModule(),puWeight_2016_postAPV(),PrefCorr2016(),LeptonVariablesModule(), TopMVA2016postapvProducer(), mu_idisosf_2016(),muonScaleRes2016b(),ele_recoidsf_2016(),jmeCorrections_UL2016MC(),btagSF2016UL(), BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2017":
      p = PostProcessor(".", inputFiles(), modules=[countHistogramsModule(),puWeight_2017(),PrefCorr2017(), LeptonVariablesModule(), TopMVA2017Producer(), mu_idisosf_2017(),muonScaleRes2017(),ele_recoidsf_2017(), jmeCorrections_UL2017MC(),btagSF2017UL(), BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2018":
      p = PostProcessor(".", inputFiles(), modules=[countHistogramsModule(),puWeight_2018(), LeptonVariablesModule(), TopMVA2018Producer(), mu_idisosf_2018(),muonScaleRes2018(),ele_recoidsf_2018(),jmeCorrections_UL2018MC(), btagSF2018UL(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")


# Sequence for data
  if not (opt.ismc):
    if opt.year == "2016b":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),LeptonVariablesModule(), TopMVA2016apvProducer(), jmeCorrections_UL2016B(),BH2016apv()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016c":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),LeptonVariablesModule(), TopMVA2016apvProducer(), jmeCorrections_UL2016C(),BH2016apv()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016d":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),LeptonVariablesModule(), TopMVA2016apvProducer(), jmeCorrections_UL2016D(),BH2016apv()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016e":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),LeptonVariablesModule(), TopMVA2016apvProducer(), jmeCorrections_UL2016E(),BH2016apv()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016f_apv":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016a(),LeptonVariablesModule(), TopMVA2016apvProducer(), jmeCorrections_UL2016APVF(),BH2016apv()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016f":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016b(),LeptonVariablesModule(), TopMVA2016postapvProducer(), jmeCorrections_UL2016F(),BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016g":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016b(),LeptonVariablesModule(), TopMVA2016postapvProducer(), jmeCorrections_UL2016G(),BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2016h":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2016b(),LeptonVariablesModule(), TopMVA2016postapvProducer(), jmeCorrections_UL2016H(),BH2016()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2017b":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2017(),LeptonVariablesModule(), TopMVA2017Producer(), jmeCorrections_UL2017B(),BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2017c":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2017(),LeptonVariablesModule(), TopMVA2017Producer(), jmeCorrections_UL2017C(),BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2017d":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2017(),LeptonVariablesModule(), TopMVA2017Producer(), jmeCorrections_UL2017D(),BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2017e":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2017(),LeptonVariablesModule(), TopMVA2017Producer(), jmeCorrections_UL2017E(),BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2017f":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2017(),LeptonVariablesModule(), TopMVA2017Producer(), jmeCorrections_UL2017F(),BH2017()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2018a":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(), LeptonVariablesModule(), TopMVA2018Producer(), jmeCorrections_UL2018A(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2018b":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(), LeptonVariablesModule(), TopMVA2018Producer(), jmeCorrections_UL2018B(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2018c":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(), LeptonVariablesModule(), TopMVA2018Producer(), jmeCorrections_UL2018C(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
    if opt.year == "2018d":
      p = PostProcessor(".", inputFiles(), modules=[muonScaleRes2018(), LeptonVariablesModule(), TopMVA2018Producer(), jmeCorrections_UL2018D(),BH2018()], provenance=True,fwkJobReport=True, jsonInput=runsAndLumis(),outputbranchsel="keep_and_drop.txt")
  p.run()

if __name__ == "__main__":
    sys.exit(main())
