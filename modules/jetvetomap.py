from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import os

class jetVetoEE(Module):
    def __init__(self, jetSelection):
        self.jetSel = jetSelection
        filename = "%s/src/PhysicsTools/NanoAODTools/data/jme/Winter22Run3_RunE_v1.root" % os.environ['CMSSW_BASE']
        histoname = "jetvetomap_eep"        
        self.jetvetomap = self.loadHisto(filename, histoname)
        pass

    def loadHisto(self, filename, hname):
        tf = ROOT.TFile.Open(filename)
        hist = tf.Get(hname)
        hist.SetDirectory(0)
        tf.Close()
        return hist

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets = Collection(event, "Jet")
        for j in filter(self.jetSel, jets):
            #print(j.eta, j.phi, self.jetvetomap.GetBinContent(self.jetvetomap.FindBin(j.eta, j.phi)))
            if self.jetvetomap.GetBinContent(self.jetvetomap.FindBin(j.eta, j.phi)) > 1.:
                isveto = True
                return False
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
jetVetoEE22E = lambda: jetVetoEE(jetSelection=lambda j: j.pt > 30)
