from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from correctionlib import _core
import os

class eleRECOIDSF(Module):
    def __init__(self, repo, era):
        self.era = era
        self.evaluator = _core.CorrectionSet.from_file('/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/' + repo + '/electron.json.gz')
        sfdir = os.path.join(os.path.dirname(__file__), '../data/leptonmva/scale_factor/egm_v1/')
        if not os.path.exists(sfdir):
            sfdir = 'data/leptonmva/scale_factor/egm_v1/'
        self.evaluator_topMVA = _core.CorrectionSet.from_file(sfdir + repo + '/egm_sf_schemaV2.json.gz')

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch('Electron_RECO_SF', "F", lenVar="nElectron")
        self.out.branch('Electron_RECO_SFerr', "F", lenVar="nElectron")
        self.out.branch('Electron_CutBased_VetoID_SF','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_VetoID_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_LooseID_SF','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_LooseID_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_MediumID_SF','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_MediumID_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_TightID_SF','F', lenVar='nElectron')
        self.out.branch('Electron_CutBased_TightID_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2Iso_WP80_SF','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2Iso_WP80_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2Iso_WP90_SF','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2Iso_WP90_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2noIso_WP80_SF','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2noIso_WP80_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2noIso_WP90_SF','F', lenVar='nElectron')
        self.out.branch('Electron_MVAFall17V2noIso_WP90_SFerr','F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Tight_SF', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Tight_SFerr_syst', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Tight_SFerr_stat', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Medium_SF', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Medium_SFerr_syst', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Medium_SFerr_stat', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Loose_SF', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Loose_SFerr_syst', 'F', lenVar='nElectron')
        self.out.branch('Electron_topMVA_Loose_SFerr_stat', 'F', lenVar='nElectron')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")

        Electron_RECO_SF = []
        Electron_RECO_SFerr = []
        Electron_CutBased_VetoID_SF = []
        Electron_CutBased_VetoID_SFerr = []
        Electron_CutBased_LooseID_SF = []
        Electron_CutBased_LooseID_SFerr = []
        Electron_CutBased_MediumID_SF = []
        Electron_CutBased_MediumID_SFerr = []
        Electron_CutBased_TightID_SF = []
        Electron_CutBased_TightID_SFerr = []
        Electron_MVAFall17V2Iso_WP80_SF = []
        Electron_MVAFall17V2Iso_WP80_SFerr = []
        Electron_MVAFall17V2Iso_WP90_SF = []
        Electron_MVAFall17V2Iso_WP90_SFerr = []
        Electron_MVAFall17V2noIso_WP80_SF = []
        Electron_MVAFall17V2noIso_WP80_SFerr = []
        Electron_MVAFall17V2noIso_WP90_SF = []
        Electron_MVAFall17V2noIso_WP90_SFerr = []   

        Electron_topMVA_Tight_SF = []
        Electron_topMVA_Tight_SFerr_syst = []
        Electron_topMVA_Tight_SFerr_stat = []
        Electron_topMVA_Medium_SF = []
        Electron_topMVA_Medium_SFerr_syst = []
        Electron_topMVA_Medium_SFerr_stat = []
        Electron_topMVA_Loose_SF = []
        Electron_topMVA_Loose_SFerr_syst = []
        Electron_topMVA_Loose_SFerr_stat = []

 
        for ele in electrons:
            # print("pt ", ele.pt, " eta ", ele.eta)
            if ele.pt <= 10:
                Electron_RECO_SF.append(1.0) #self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sf","RecoBelow20", ele.eta, 10.1))
                Electron_RECO_SFerr.append(0.0) #(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sfup","RecoBelow20", ele.eta, 10.1) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sfdown","RecoBelow20", ele.eta, 10.1))/2)
                Electron_CutBased_VetoID_SF.append(1.0)
                Electron_CutBased_VetoID_SFerr.append(0.0)
                Electron_CutBased_LooseID_SF.append(1.0)
                Electron_CutBased_LooseID_SFerr.append(0.0)
                Electron_CutBased_MediumID_SF.append(1.0)
                Electron_CutBased_MediumID_SFerr.append(0.0)
                Electron_CutBased_TightID_SF.append(1.0)
                Electron_CutBased_TightID_SFerr.append(0.0)
                Electron_MVAFall17V2Iso_WP80_SF.append(1.0)
                Electron_MVAFall17V2Iso_WP80_SFerr.append(0.0)
                Electron_MVAFall17V2Iso_WP90_SF.append(1.0)
                Electron_MVAFall17V2Iso_WP90_SFerr.append(0.0)
                Electron_MVAFall17V2noIso_WP80_SF.append(1.0)
                Electron_MVAFall17V2noIso_WP80_SFerr.append(0.0)
                Electron_MVAFall17V2noIso_WP90_SF.append(1.0)
                Electron_MVAFall17V2noIso_WP90_SFerr.append(0.0)
            elif ele.pt > 10 and ele.pt < 20: 
                Electron_RECO_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sf","RecoBelow20", ele.eta, ele.pt))
                Electron_RECO_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sfup","RecoBelow20", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sfdown","RecoBelow20", ele.eta, ele.pt)) / 2)
                Electron_CutBased_VetoID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Veto", ele.eta, ele.pt))
                Electron_CutBased_VetoID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Veto", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Veto", ele.eta, ele.pt)) / 2)
                Electron_CutBased_LooseID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Loose", ele.eta, ele.pt))
                Electron_CutBased_LooseID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Loose", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Loose", ele.eta, ele.pt)) / 2)
                Electron_CutBased_MediumID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Medium", ele.eta, ele.pt))
                Electron_CutBased_MediumID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Medium", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Medium", ele.eta, ele.pt)) / 2)
                Electron_CutBased_TightID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Tight", ele.eta, ele.pt))
                Electron_CutBased_TightID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Tight", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Tight", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2Iso_WP80_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp80iso", ele.eta, ele.pt))
                Electron_MVAFall17V2Iso_WP80_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp80iso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp80iso", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2Iso_WP90_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp90iso", ele.eta, ele.pt))
                Electron_MVAFall17V2Iso_WP90_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp90iso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp90iso", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2noIso_WP80_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp80noiso", ele.eta, ele.pt))
                Electron_MVAFall17V2noIso_WP80_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp80noiso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp80noiso", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2noIso_WP90_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp90noiso", ele.eta, ele.pt))
                Electron_MVAFall17V2noIso_WP90_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp90noiso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp90noiso", ele.eta, ele.pt)) / 2)
            else:
                Electron_RECO_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sf","RecoAbove20", ele.eta, ele.pt))
                Electron_RECO_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sfup","RecoAbove20", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era,"sfdown","RecoAbove20", ele.eta, ele.pt)) / 2)
                Electron_CutBased_VetoID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Veto", ele.eta, ele.pt))
                Electron_CutBased_VetoID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Veto", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Veto", ele.eta, ele.pt)) / 2)
                Electron_CutBased_LooseID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Loose", ele.eta, ele.pt))
                Electron_CutBased_LooseID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Loose", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Loose", ele.eta, ele.pt)) / 2)
                Electron_CutBased_MediumID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Medium", ele.eta, ele.pt))
                Electron_CutBased_MediumID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Medium", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Medium", ele.eta, ele.pt)) / 2)
                Electron_CutBased_TightID_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "Tight", ele.eta, ele.pt))
                Electron_CutBased_TightID_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "Tight", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "Tight", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2Iso_WP80_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp80iso", ele.eta, ele.pt))
                Electron_MVAFall17V2Iso_WP80_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp80iso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp80iso", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2Iso_WP90_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp90iso", ele.eta, ele.pt))
                Electron_MVAFall17V2Iso_WP90_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp90iso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp90iso", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2noIso_WP80_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp80noiso", ele.eta, ele.pt))
                Electron_MVAFall17V2noIso_WP80_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp80noiso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp80noiso", ele.eta, ele.pt)) / 2)
                Electron_MVAFall17V2noIso_WP90_SF.append(self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sf", "wp90noiso", ele.eta, ele.pt))
                Electron_MVAFall17V2noIso_WP90_SFerr.append((self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfup", "wp90noiso", ele.eta, ele.pt) - self.evaluator["UL-Electron-ID-SF"].evaluate(self.era, "sfdown", "wp90noiso", ele.eta, ele.pt)) / 2)

                Electron_topMVA_Tight_SF.append(self.evaluator_topMVA["LeptonMvaTight"].evaluate(ele.eta, ele.pt, "sf"))
                Electron_topMVA_Tight_SFerr_syst.append(self.evaluator_topMVA["LeptonMvaTight"].evaluate(ele.eta, ele.pt, "sys"))
                Electron_topMVA_Tight_SFerr_stat.append(self.evaluator_topMVA["LeptonMvaTight"].evaluate(ele.eta, ele.pt, "stat"))
                Electron_topMVA_Medium_SF.append(self.evaluator_topMVA["LeptonMvaTight"].evaluate(ele.eta, ele.pt, "sf"))
                Electron_topMVA_Medium_SFerr_syst.append(self.evaluator_topMVA["LeptonMvaMedium"].evaluate(ele.eta, ele.pt, "sys"))
                Electron_topMVA_Medium_SFerr_stat.append(self.evaluator_topMVA["LeptonMvaMedium"].evaluate(ele.eta, ele.pt, "stat"))
                Electron_topMVA_Loose_SF.append(self.evaluator_topMVA["LeptonMvaMedium"].evaluate(ele.eta, ele.pt, "sf"))
                Electron_topMVA_Loose_SFerr_syst.append(self.evaluator_topMVA["LeptonMvaLoose"].evaluate(ele.eta, ele.pt, "sys"))
                Electron_topMVA_Loose_SFerr_stat.append(self.evaluator_topMVA["LeptonMvaLoose"].evaluate(ele.eta, ele.pt, "stat"))

        #print("Electron_RECO_SF is ", Electron_RECO_SF)
        #print("Electron_RECO_SFerr is ", Electron_RECO_SFerr)
        self.out.fillBranch('Electron_RECO_SF', Electron_RECO_SF)
        self.out.fillBranch('Electron_RECO_SFerr', Electron_RECO_SFerr)
        self.out.fillBranch('Electron_CutBased_VetoID_SF', Electron_CutBased_VetoID_SF)
        self.out.fillBranch('Electron_CutBased_VetoID_SFerr', Electron_CutBased_VetoID_SFerr)
        self.out.fillBranch('Electron_CutBased_LooseID_SF', Electron_CutBased_LooseID_SF)
        self.out.fillBranch('Electron_CutBased_LooseID_SFerr', Electron_CutBased_LooseID_SFerr)
        self.out.fillBranch('Electron_CutBased_MediumID_SF', Electron_CutBased_MediumID_SF)
        self.out.fillBranch('Electron_CutBased_MediumID_SFerr', Electron_CutBased_MediumID_SFerr)
        self.out.fillBranch('Electron_CutBased_TightID_SF', Electron_CutBased_TightID_SF)
        self.out.fillBranch('Electron_CutBased_TightID_SFerr', Electron_CutBased_TightID_SFerr)
        self.out.fillBranch('Electron_MVAFall17V2Iso_WP80_SF', Electron_MVAFall17V2Iso_WP80_SF)
        self.out.fillBranch('Electron_MVAFall17V2Iso_WP80_SFerr', Electron_MVAFall17V2Iso_WP80_SFerr)
        self.out.fillBranch('Electron_MVAFall17V2Iso_WP90_SF', Electron_MVAFall17V2Iso_WP90_SF)
        self.out.fillBranch('Electron_MVAFall17V2Iso_WP90_SFerr', Electron_MVAFall17V2Iso_WP90_SFerr)
        self.out.fillBranch('Electron_MVAFall17V2noIso_WP80_SF', Electron_MVAFall17V2noIso_WP80_SF)
        self.out.fillBranch('Electron_MVAFall17V2noIso_WP80_SFerr', Electron_MVAFall17V2noIso_WP80_SFerr)
        self.out.fillBranch('Electron_MVAFall17V2noIso_WP90_SF', Electron_MVAFall17V2noIso_WP90_SF)
        self.out.fillBranch('Electron_MVAFall17V2noIso_WP90_SFerr', Electron_MVAFall17V2noIso_WP90_SFerr)
         
        self.out.fillBranch('Electron_topMVA_Tight_SF', Electron_topMVA_Tight_SF)
        self.out.fillBranch('Electron_topMVA_Tight_SFerr_syst', Electron_topMVA_Tight_SFerr_syst)
        self.out.fillBranch('Electron_topMVA_Tight_SFerr_stat', Electron_topMVA_Tight_SFerr_stat)
        self.out.fillBranch('Electron_topMVA_Medium_SF', Electron_topMVA_Medium_SF)
        self.out.fillBranch('Electron_topMVA_Medium_SFerr_syst', Electron_topMVA_Medium_SFerr_syst)
        self.out.fillBranch('Electron_topMVA_Medium_SFerr_stat', Electron_topMVA_Medium_SFerr_stat)
        self.out.fillBranch('Electron_topMVA_Loose_SF', Electron_topMVA_Loose_SF)
        self.out.fillBranch('Electron_topMVA_Loose_SFerr_syst', Electron_topMVA_Loose_SFerr_syst)
        self.out.fillBranch('Electron_topMVA_Loose_SFerr_stat', Electron_topMVA_Loose_SFerr_stat)

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid
# having them loaded when not needed
ele_recoidsf_2016APV = lambda: eleRECOIDSF("2016preVFP_UL", "2016preVFP")
ele_recoidsf_2016 = lambda: eleRECOIDSF("2016postVFP_UL", "2016postVFP")
ele_recoidsf_2017 = lambda: eleRECOIDSF("2017_UL", "2017")
ele_recoidsf_2018 = lambda: eleRECOIDSF("2018_UL", "2018")
