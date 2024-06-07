from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from correctionlib import _core
import os

class muIDISOSF(Module):
    def __init__(self, repo, era):
        self.era = era
        self.evaluator = _core.CorrectionSet.from_file('/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/MUO/' + repo + '/muon_Z.json.gz')
        sfdir = os.path.join(os.path.dirname(__file__), '../data/leptonmva/scale_factor/muon_v1/')
        if not os.path.exists(sfdir):
            sfdir = 'data/leptonmva/scale_factor/muon_v1/'
        self.evaluator_topMVA = _core.CorrectionSet.from_file(sfdir + repo + '/muon_sf_schemaV2.json.gz')

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch('Muon_CutBased_LooseID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_LooseID_SFerr','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_MediumID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_MediumID_SFerr','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_MediumPromptID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_MediumPromptID_SFerr','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_TightID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_TightID_SFerr','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_SoftID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_SoftID_SFerr','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_HighPtID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_HighPtID_SFerr','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_TrkHighPtID_SF','F', lenVar='nMuon')
        self.out.branch('Muon_CutBased_TrkHighPtID_SFerr','F', lenVar='nMuon')
        
        self.out.branch('Muon_LooseRelIso_LooseID_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_LooseID_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_MediumID_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_MediumID_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_MediumPromptID_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_MediumPromptID_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_TightIDandIPCut_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelIso_TightIDandIPCut_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelTkIso_HighPtIDandIPCut_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelTkIso_HighPtIDandIPCut_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelIso_MediumID_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelIso_MediumID_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelIso_MediumPromptID_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelIso_MediumPromptID_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelIso_TightIDandIPCut_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelIso_TightIDandIPCut_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelTkIso_HighPtIDandIPCut_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelTkIso_HighPtIDandIPCut_SFerr', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelTkIso_TrkHighPtIDandIPCut_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_TightRelTkIso_TrkHighPtIDandIPCut_SFerr', 'F', lenVar='nMuon')

        self.out.branch('Muon_topMVA_Tight_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Tight_SFerr_syst', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Tight_SFerr_stat', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Medium_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Medium_SFerr_syst', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Medium_SFerr_stat', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Loose_SF', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Loose_SFerr_syst', 'F', lenVar='nMuon')
        self.out.branch('Muon_topMVA_Loose_SFerr_stat', 'F', lenVar='nMuon')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        muons = Collection(event, "Muon")
        Muon_CutBased_LooseID_SF = []
        Muon_CutBased_LooseID_SFerr = []
        Muon_CutBased_MediumID_SF = []
        Muon_CutBased_MediumID_SFerr = []
        Muon_CutBased_MediumPromptID_SF = []
        Muon_CutBased_MediumPromptID_SFerr = []
        Muon_CutBased_TightID_SF = []
        Muon_CutBased_TightID_SFerr = []
        Muon_CutBased_SoftID_SF = []
        Muon_CutBased_SoftID_SFerr = []
        Muon_CutBased_HighPtID_SF = []
        Muon_CutBased_HighPtID_SFerr = []
        Muon_CutBased_TrkHighPtID_SF = []
        Muon_CutBased_TrkHighPtID_SFerr = []
        
        Muon_LooseRelIso_LooseID_SF = []
        Muon_LooseRelIso_MediumID_SF = []
        Muon_LooseRelIso_MediumPromptID_SF = []
        Muon_LooseRelIso_TightIDandIPCut_SF = []
        Muon_LooseRelTkIso_HighPtIDandIPCut_SF = []
        Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SF = []
        Muon_TightRelIso_MediumID_SF = []
        Muon_TightRelIso_MediumPromptID_SF = []
        Muon_TightRelIso_TightIDandIPCut_SF = []
        Muon_TightRelTkIso_HighPtIDandIPCut_SF = []
        Muon_TightRelTkIso_TrkHighPtIDandIPCut_SF = []
        Muon_LooseRelIso_LooseID_SFerr = []
        Muon_LooseRelIso_MediumID_SFerr = []
        Muon_LooseRelIso_MediumPromptID_SFerr = []
        Muon_LooseRelIso_TightIDandIPCut_SFerr = []
        Muon_LooseRelTkIso_HighPtIDandIPCut_SFerr = []
        Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SFerr = []
        Muon_TightRelIso_MediumID_SFerr = []
        Muon_TightRelIso_MediumPromptID_SFerr = []
        Muon_TightRelIso_TightIDandIPCut_SFerr = []
        Muon_TightRelTkIso_HighPtIDandIPCut_SFerr = []
        Muon_TightRelTkIso_TrkHighPtIDandIPCut_SFerr = []

        Muon_topMVA_Tight_SF = []
        Muon_topMVA_Tight_SFerr_syst = []
        Muon_topMVA_Tight_SFerr_stat = []
        Muon_topMVA_Medium_SF = []
        Muon_topMVA_Medium_SFerr_syst = []
        Muon_topMVA_Medium_SFerr_stat = []
        Muon_topMVA_Loose_SF = []
        Muon_topMVA_Loose_SFerr_syst = []
        Muon_topMVA_Loose_SFerr_stat = []

        value = 1.0
        error = 0.0
        for mu in muons:
            #print("pt ", mu.pt, " eta ", mu.eta, " abs eta ", abs(mu.eta))
            if abs(mu.eta) > 2.4:
                mu.eta = 2.39
            #print("pt ", mu.pt, " eta ", mu.eta, " abs eta ", abs(mu.eta))
            if mu.pt < 15:
                Muon_CutBased_LooseID_SF.append(value)
                Muon_CutBased_LooseID_SFerr.append(error)
                Muon_CutBased_MediumID_SF.append(value)
                Muon_CutBased_MediumID_SFerr.append(error)
                Muon_CutBased_MediumPromptID_SF.append(value)
                Muon_CutBased_MediumPromptID_SFerr.append(error)
                Muon_CutBased_TightID_SF.append(value)
                Muon_CutBased_TightID_SFerr.append(error)
                Muon_CutBased_SoftID_SF.append(value)
                Muon_CutBased_SoftID_SFerr.append(error)
                Muon_CutBased_HighPtID_SF.append(value)
                Muon_CutBased_HighPtID_SFerr.append(error)
                Muon_CutBased_TrkHighPtID_SF.append(value)
                Muon_CutBased_TrkHighPtID_SFerr.append(error)
                Muon_LooseRelIso_LooseID_SF.append(value)
                Muon_LooseRelIso_LooseID_SFerr.append(error)
                Muon_LooseRelIso_MediumID_SF.append(value)
                Muon_LooseRelIso_MediumID_SFerr.append(error)
                Muon_LooseRelIso_MediumPromptID_SF.append(value)
                Muon_LooseRelIso_MediumPromptID_SFerr.append(error)
                Muon_LooseRelIso_TightIDandIPCut_SF.append(value)
                Muon_LooseRelIso_TightIDandIPCut_SFerr.append(error)
                Muon_LooseRelTkIso_HighPtIDandIPCut_SF.append(value)
                Muon_LooseRelTkIso_HighPtIDandIPCut_SFerr.append(error)
                Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SF.append(value)
                Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SFerr.append(error)
                Muon_TightRelIso_MediumID_SF.append(value)
                Muon_TightRelIso_MediumID_SFerr.append(error)
                Muon_TightRelIso_MediumPromptID_SF.append(value)
                Muon_TightRelIso_MediumPromptID_SFerr.append(error)
                Muon_TightRelIso_TightIDandIPCut_SF.append(value)
                Muon_TightRelIso_TightIDandIPCut_SFerr.append(error)
                Muon_TightRelTkIso_HighPtIDandIPCut_SF.append(value)
                Muon_TightRelTkIso_HighPtIDandIPCut_SFerr.append(error)
                Muon_TightRelTkIso_TrkHighPtIDandIPCut_SF.append(value)
                Muon_TightRelTkIso_TrkHighPtIDandIPCut_SFerr.append(error)
                Muon_topMVA_Tight_SF.append(value)
            else: 
                Muon_CutBased_LooseID_SF.append(self.evaluator["NUM_LooseID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_LooseID_SFerr.append(self.evaluator["NUM_LooseID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_CutBased_MediumID_SF.append(self.evaluator["NUM_MediumID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_MediumID_SFerr.append(self.evaluator["NUM_MediumID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_CutBased_MediumPromptID_SF.append(self.evaluator["NUM_MediumPromptID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_MediumPromptID_SFerr.append(self.evaluator["NUM_MediumPromptID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_CutBased_TightID_SF.append(self.evaluator["NUM_TightID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_TightID_SFerr.append(self.evaluator["NUM_TightID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_CutBased_SoftID_SF.append(self.evaluator["NUM_SoftID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_SoftID_SFerr.append(self.evaluator["NUM_SoftID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_CutBased_HighPtID_SF.append(self.evaluator["NUM_HighPtID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_HighPtID_SFerr.append(self.evaluator["NUM_HighPtID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_CutBased_TrkHighPtID_SF.append(self.evaluator["NUM_TrkHighPtID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_CutBased_TrkHighPtID_SFerr.append(self.evaluator["NUM_TrkHighPtID_DEN_TrackerMuons"].evaluate(abs(mu.eta), mu.pt, "syst"))

                Muon_LooseRelIso_LooseID_SF.append(self.evaluator["NUM_LooseRelIso_DEN_LooseID"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_LooseRelIso_LooseID_SFerr.append(self.evaluator["NUM_LooseRelIso_DEN_LooseID"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_LooseRelIso_MediumID_SF.append(self.evaluator["NUM_LooseRelIso_DEN_MediumID"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_LooseRelIso_MediumID_SFerr.append(self.evaluator["NUM_LooseRelIso_DEN_MediumID"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_LooseRelIso_MediumPromptID_SF.append(self.evaluator["NUM_LooseRelIso_DEN_MediumPromptID"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_LooseRelIso_MediumPromptID_SFerr.append(self.evaluator["NUM_LooseRelIso_DEN_MediumPromptID"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_LooseRelIso_TightIDandIPCut_SF.append(self.evaluator["NUM_LooseRelIso_DEN_TightIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_LooseRelIso_TightIDandIPCut_SFerr.append(self.evaluator["NUM_LooseRelIso_DEN_TightIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_LooseRelTkIso_HighPtIDandIPCut_SF.append(self.evaluator["NUM_LooseRelTkIso_DEN_HighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_LooseRelTkIso_HighPtIDandIPCut_SFerr.append(self.evaluator["NUM_LooseRelTkIso_DEN_HighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SF.append(self.evaluator["NUM_LooseRelTkIso_DEN_TrkHighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SFerr.append(self.evaluator["NUM_LooseRelTkIso_DEN_TrkHighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_TightRelIso_MediumID_SF.append(self.evaluator["NUM_TightRelIso_DEN_MediumID"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_TightRelIso_MediumID_SFerr.append(self.evaluator["NUM_TightRelIso_DEN_MediumID"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_TightRelIso_MediumPromptID_SF.append(self.evaluator["NUM_TightRelIso_DEN_MediumPromptID"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_TightRelIso_MediumPromptID_SFerr.append(self.evaluator["NUM_TightRelIso_DEN_MediumPromptID"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_TightRelIso_TightIDandIPCut_SF.append(self.evaluator["NUM_TightRelIso_DEN_TightIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_TightRelIso_TightIDandIPCut_SFerr.append(self.evaluator["NUM_TightRelIso_DEN_TightIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_TightRelTkIso_HighPtIDandIPCut_SF.append(self.evaluator["NUM_TightRelTkIso_DEN_HighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_TightRelTkIso_HighPtIDandIPCut_SFerr.append(self.evaluator["NUM_TightRelTkIso_DEN_HighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "syst"))
                Muon_TightRelTkIso_TrkHighPtIDandIPCut_SF.append(self.evaluator["NUM_TightRelTkIso_DEN_TrkHighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "nominal"))
                Muon_TightRelTkIso_TrkHighPtIDandIPCut_SFerr.append(self.evaluator["NUM_TightRelTkIso_DEN_TrkHighPtIDandIPCut"].evaluate(abs(mu.eta), mu.pt, "syst"))
               
                Muon_topMVA_Tight_SF.append(self.evaluator_topMVA["NUM_LeptonMvaTight_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "sf"))
                Muon_topMVA_Tight_SFerr_syst.append(self.evaluator_topMVA["NUM_LeptonMvaTight_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "combined_syst"))
                Muon_topMVA_Tight_SFerr_stat.append(self.evaluator_topMVA["NUM_LeptonMvaTight_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "staterr"))
                Muon_topMVA_Medium_SF.append(self.evaluator_topMVA["NUM_LeptonMvaMedium_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "sf"))
                Muon_topMVA_Medium_SFerr_syst.append(self.evaluator_topMVA["NUM_LeptonMvaMedium_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "combined_syst"))
                Muon_topMVA_Medium_SFerr_stat.append(self.evaluator_topMVA["NUM_LeptonMvaMedium_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "staterr"))
                Muon_topMVA_Loose_SF.append(self.evaluator_topMVA["NUM_LeptonMvaLoose_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "sf"))
                Muon_topMVA_Loose_SFerr_syst.append(self.evaluator_topMVA["NUM_LeptonMvaLoose_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "combined_syst"))
                Muon_topMVA_Loose_SFerr_stat.append(self.evaluator_topMVA["NUM_LeptonMvaLoose_DEN_TrackerMuons_abseta_pt"].evaluate(abs(mu.eta), mu.pt, "staterr"))

        #print(Muon_CutBased_LooseID_SF)
        self.out.fillBranch('Muon_CutBased_LooseID_SF', Muon_CutBased_LooseID_SF)
        self.out.fillBranch('Muon_CutBased_LooseID_SFerr', Muon_CutBased_LooseID_SFerr)
        self.out.fillBranch('Muon_CutBased_MediumID_SF', Muon_CutBased_MediumID_SF)
        self.out.fillBranch('Muon_CutBased_MediumID_SFerr', Muon_CutBased_MediumID_SFerr)
        self.out.fillBranch('Muon_CutBased_MediumPromptID_SF', Muon_CutBased_MediumPromptID_SF)
        self.out.fillBranch('Muon_CutBased_MediumPromptID_SFerr', Muon_CutBased_MediumPromptID_SFerr)
        self.out.fillBranch('Muon_CutBased_TightID_SF', Muon_CutBased_TightID_SF)
        self.out.fillBranch('Muon_CutBased_TightID_SFerr', Muon_CutBased_TightID_SFerr)
        self.out.fillBranch('Muon_CutBased_SoftID_SF', Muon_CutBased_SoftID_SF)
        self.out.fillBranch('Muon_CutBased_SoftID_SFerr', Muon_CutBased_SoftID_SFerr)
        self.out.fillBranch('Muon_CutBased_HighPtID_SF', Muon_CutBased_HighPtID_SF)
        self.out.fillBranch('Muon_CutBased_HighPtID_SFerr', Muon_CutBased_HighPtID_SFerr)
        self.out.fillBranch('Muon_CutBased_TrkHighPtID_SF', Muon_CutBased_TrkHighPtID_SF)
        self.out.fillBranch('Muon_CutBased_TrkHighPtID_SFerr', Muon_CutBased_TrkHighPtID_SFerr)
        
        self.out.fillBranch('Muon_LooseRelIso_LooseID_SF', Muon_LooseRelIso_LooseID_SF)
        self.out.fillBranch('Muon_LooseRelIso_LooseID_SFerr', Muon_LooseRelIso_LooseID_SFerr)
        self.out.fillBranch('Muon_LooseRelIso_MediumID_SF', Muon_LooseRelIso_MediumID_SF)
        self.out.fillBranch('Muon_LooseRelIso_MediumID_SFerr', Muon_LooseRelIso_MediumID_SFerr)
        self.out.fillBranch('Muon_LooseRelIso_MediumPromptID_SF', Muon_LooseRelIso_MediumPromptID_SF)
        self.out.fillBranch('Muon_LooseRelIso_MediumPromptID_SFerr', Muon_LooseRelIso_MediumPromptID_SFerr)
        self.out.fillBranch('Muon_LooseRelIso_TightIDandIPCut_SF', Muon_LooseRelIso_TightIDandIPCut_SF)
        self.out.fillBranch('Muon_LooseRelIso_TightIDandIPCut_SFerr', Muon_LooseRelIso_TightIDandIPCut_SFerr)
        self.out.fillBranch('Muon_LooseRelTkIso_HighPtIDandIPCut_SF', Muon_LooseRelTkIso_HighPtIDandIPCut_SF)
        self.out.fillBranch('Muon_LooseRelTkIso_HighPtIDandIPCut_SFerr', Muon_LooseRelTkIso_HighPtIDandIPCut_SFerr)
        self.out.fillBranch('Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SF', Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SF)
        self.out.fillBranch('Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SFerr', Muon_LooseRelTkIso_TrkHighPtIDandIPCut_SFerr)
        self.out.fillBranch('Muon_TightRelIso_MediumID_SF', Muon_TightRelIso_MediumID_SF)
        self.out.fillBranch('Muon_TightRelIso_MediumID_SFerr', Muon_TightRelIso_MediumID_SFerr)
        self.out.fillBranch('Muon_TightRelIso_MediumPromptID_SF',Muon_TightRelIso_MediumPromptID_SF)
        self.out.fillBranch('Muon_TightRelIso_MediumPromptID_SFerr',Muon_TightRelIso_MediumPromptID_SFerr)
        self.out.fillBranch('Muon_TightRelIso_TightIDandIPCut_SF',Muon_TightRelIso_TightIDandIPCut_SF)
        self.out.fillBranch('Muon_TightRelIso_TightIDandIPCut_SFerr',Muon_TightRelIso_TightIDandIPCut_SFerr)
        self.out.fillBranch('Muon_TightRelTkIso_HighPtIDandIPCut_SF',Muon_TightRelTkIso_HighPtIDandIPCut_SF)
        self.out.fillBranch('Muon_TightRelTkIso_HighPtIDandIPCut_SFerr',Muon_TightRelTkIso_HighPtIDandIPCut_SFerr)
        self.out.fillBranch('Muon_TightRelTkIso_TrkHighPtIDandIPCut_SF',Muon_TightRelTkIso_TrkHighPtIDandIPCut_SF)
        self.out.fillBranch('Muon_TightRelTkIso_TrkHighPtIDandIPCut_SFerr',Muon_TightRelTkIso_TrkHighPtIDandIPCut_SFerr)

        self.out.fillBranch('Muon_topMVA_Tight_SF', Muon_topMVA_Tight_SF)
        self.out.fillBranch('Muon_topMVA_Tight_SFerr_syst', Muon_topMVA_Tight_SFerr_syst)
        self.out.fillBranch('Muon_topMVA_Tight_SFerr_stat', Muon_topMVA_Tight_SFerr_stat)
        self.out.fillBranch('Muon_topMVA_Medium_SF', Muon_topMVA_Medium_SF)
        self.out.fillBranch('Muon_topMVA_Medium_SFerr_syst', Muon_topMVA_Medium_SFerr_syst)
        self.out.fillBranch('Muon_topMVA_Medium_SFerr_stat', Muon_topMVA_Medium_SFerr_stat)
        self.out.fillBranch('Muon_topMVA_Loose_SF', Muon_topMVA_Loose_SF)
        self.out.fillBranch('Muon_topMVA_Loose_SFerr_syst', Muon_topMVA_Loose_SFerr_syst)
        self.out.fillBranch('Muon_topMVA_Loose_SFerr_stat', Muon_topMVA_Loose_SFerr_stat)

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid
# having them loaded when not needed
mu_idisosf_2016APV = lambda: muIDISOSF("2016preVFP_UL", "2016preVFP_UL")
mu_idisosf_2016 = lambda: muIDISOSF("2016postVFP_UL", "2016postVFP_UL")
mu_idisosf_2017 = lambda: muIDISOSF("2017_UL", "2017_UL")
mu_idisosf_2018 = lambda: muIDISOSF("2018_UL", "2018_UL")
