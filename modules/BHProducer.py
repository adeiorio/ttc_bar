from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from numpy import sign
import numpy as np
import os
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR, deltaPhi, closest
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True


class BHProducer(Module):
    def __init__(self, year):
        self.year = year
        self.mucheck_has_run = False
        self.echeck_has_run = False
        self.jetcheck_has_run = False
        print(year)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("HLT_passEle32WPTight", "I")
        self.out.branch("lhe_nlepton", "I")
        self.out.branch("n_tight_muon", "I")
        self.out.branch("n_tight_muon_noIso", "I")
        self.out.branch("n_loose_muon", "I")
        self.out.branch("n_loose_muon_noIso", "I")
        self.out.branch("n_tight_ele", "I")
        self.out.branch("n_tight_ele_noIso", "I")
        self.out.branch("n_loose_ele", "I")
        self.out.branch("n_loose_ele_noIso", "I")
        self.out.branch("btag_SFall", "F")
        self.out.branch("n_tight_jet", "I")
        self.out.branch("n_bjet_DeepB_loose", "I")
        self.out.branch("n_bjet_DeepB_medium", "I")
        self.out.branch("n_bjet_DeepB_tight", "I")
        self.out.branch("HT", "F")
        self.out.branch("nHad_tau", "I")
        self.out.branch("j1_pt", "F")
        self.out.branch("j1_eta", "F")
        self.out.branch("j1_phi", "F")
        self.out.branch("j1_mass", "F")
        self.out.branch("j2_pt", "F")
        self.out.branch("j2_eta", "F")
        self.out.branch("j2_phi", "F")
        self.out.branch("j2_mass", "F")
        self.out.branch("j3_pt", "F")
        self.out.branch("j3_eta", "F")
        self.out.branch("j3_phi", "F")
        self.out.branch("j3_mass", "F")
        self.out.branch("j4_pt", "F")
        self.out.branch("j4_eta", "F")
        self.out.branch("j4_phi", "F")
        self.out.branch("j4_mass", "F")
        self.out.branch("mj1j2", "F")
        self.out.branch("mj1j3", "F")
        self.out.branch("mj1j4", "F")
        self.out.branch("mj2j3", "F")
        self.out.branch("mj2j4", "F")
        self.out.branch("mj3j4", "F")
        self.out.branch("mj1j2j3", "F")
        self.out.branch("mj1j2j4", "F")
        self.out.branch("mj2j3j4", "F")
        self.out.branch("mj1j2j3j4", "F")
        self.out.branch("drj1j2", "F")
        self.out.branch("drj1j3", "F")
        self.out.branch("drj1j4", "F")
        self.out.branch("drj2j3", "F")
        self.out.branch("drj2j4", "F")
        self.out.branch("drj3j4", "F")
        # Bjets
        self.out.branch("DeepB_loose_j1_pt", "F")
        self.out.branch("DeepB_loose_j1_eta", "F")
        self.out.branch("DeepB_loose_j1_phi", "F")
        self.out.branch("DeepB_loose_j1_mass", "F")
        self.out.branch("DeepB_loose_j2_pt", "F")
        self.out.branch("DeepB_loose_j2_eta", "F")
        self.out.branch("DeepB_loose_j2_phi", "F")
        self.out.branch("DeepB_loose_j2_mass", "F")
        self.out.branch("DeepB_loose_j3_pt", "F")
        self.out.branch("DeepB_loose_j3_eta", "F")
        self.out.branch("DeepB_loose_j3_phi", "F")
        self.out.branch("DeepB_loose_j3_mass", "F")
        self.out.branch("DeepB_medium_j1_pt", "F")
        self.out.branch("DeepB_medium_j1_eta", "F")
        self.out.branch("DeepB_medium_j1_phi", "F")
        self.out.branch("DeepB_medium_j1_mass", "F")
        self.out.branch("DeepB_medium_j2_pt", "F")
        self.out.branch("DeepB_medium_j2_eta", "F")
        self.out.branch("DeepB_medium_j2_phi", "F")
        self.out.branch("DeepB_medium_j2_mass", "F")
        self.out.branch("DeepB_medium_j3_pt", "F")
        self.out.branch("DeepB_medium_j3_eta", "F")
        self.out.branch("DeepB_medium_j3_phi", "F")
        self.out.branch("DeepB_medium_j3_mass", "F")
        self.out.branch("DeepB_tight_j1_pt", "F")
        self.out.branch("DeepB_tight_j1_eta", "F")
        self.out.branch("DeepB_tight_j1_phi", "F")
        self.out.branch("DeepB_tight_j1_mass", "F")
        self.out.branch("DeepB_tight_j2_pt", "F")
        self.out.branch("DeepB_tight_j2_eta", "F")
        self.out.branch("DeepB_tight_j2_phi", "F")
        self.out.branch("DeepB_tight_j2_mass", "F")
        self.out.branch("DeepB_tight_j3_pt", "F")
        self.out.branch("DeepB_tight_j3_eta", "F")
        self.out.branch("DeepB_tight_j3_phi", "F")
        self.out.branch("DeepB_tight_j3_mass", "F")
        # bh-stuff
        self.out.branch("bh_nl", "B")
        self.out.branch("bh_jets", "B")
        self.out.branch("bh_region", "I")
        self.out.branch("bh_l1_id", "I")
        self.out.branch("bh_l1_pdgid", "I")
        self.out.branch("bh_l1_pt", "F")
        self.out.branch("bh_l1_eta", "F")
        self.out.branch("bh_l1_phi", "F")
        self.out.branch("bh_l1_mass", "F")
        self.out.branch("bh_met", "F")
        self.out.branch("bh_met_phi", "F")
        self.out.branch("bh_dr_l1j1", "F")
        self.out.branch("bh_dr_l1j2", "F")
        self.out.branch("bh_dr_l1j3", "F")
        self.out.branch("bh_dr_l1j4", "F")
        self.out.branch("bh_mlj1", "F")
        self.out.branch("bh_mlj2", "F")
        self.out.branch("bh_mlj3", "F")
        self.out.branch("bh_mlj4", "F")
        self.out.branch("bh_mlj1j2", "F")
        self.out.branch("bh_mlj1j3", "F")
        self.out.branch("bh_mlj1j4", "F")
        self.out.branch("bh_mlj2j3", "F")
        self.out.branch("bh_mlj2j4", "F")
        self.out.branch("bh_mlj3j4", "F")
        self.out.branch("bh_mlb1", "F")
        self.out.branch("bh_mlb2", "F")
        self.out.branch("bh_mlb3", "F")
        self.out.branch("bh_mlb1b2", "F")
        self.out.branch("bh_mlb1b3", "F")
        self.out.branch("bh_mlb2b3", "F")
        self.out.branch("boost_region", "I")
        self.out.branch("boost_l1_id", "I")
        self.out.branch("boost_l1_pdgid", "I")
        self.out.branch("boost_l1_pt", "F")
        self.out.branch("boost_l1_eta", "F")
        self.out.branch("boost_l1_phi", "F")
        self.out.branch("boost_l1_mass", "F")
        self.out.branch("boost_met", "F")
        self.out.branch("boost_met_phi", "F")
        self.out.branch("Trigger_derived_region", "B")
        self.out.branch("WZ_region", "I")
        self.out.branch("WZ_zl1_id", "I")
        self.out.branch("WZ_zl2_id", "I")
        self.out.branch("WZ_wl_id", "I")
        self.out.branch("WZ_zl1_pdgid", "I")
        self.out.branch("WZ_zl2_pdgid", "I")
        self.out.branch("WZ_wl_pdgid", "I")
        self.out.branch("WZ_zl1_pt", "F")
        self.out.branch("WZ_zl1_eta", "F")
        self.out.branch("WZ_zl1_phi", "F")
        self.out.branch("WZ_zl1_mass", "F")
        self.out.branch("WZ_zl2_pt", "F")
        self.out.branch("WZ_zl2_eta", "F")
        self.out.branch("WZ_zl2_phi", "F")
        self.out.branch("WZ_zl2_mass", "F")
        self.out.branch("WZ_l3_pt", "F")
        self.out.branch("WZ_l3_eta", "F")
        self.out.branch("WZ_l3_phi", "F")
        self.out.branch("WZ_l3_mass", "F")
        self.out.branch("WZ_Z_mass", "F")
        self.out.branch("WZ_Z_pt", "F")
        self.out.branch("WZ_Z_eta", "F")
        self.out.branch("WZ_Z_phi", "F")
        self.out.branch("WZ_met", "F")
        self.out.branch("DY_region", "I")
        self.out.branch("DY_l1_id", "I")
        self.out.branch("DY_l2_id", "I")
        self.out.branch("DY_l1_pdgid", "I")
        self.out.branch("DY_l2_pdgid", "I")
        self.out.branch("DY_l1_pt", "F")
        self.out.branch("DY_l1_eta", "F")
        self.out.branch("DY_l1_phi", "F")
        self.out.branch("DY_l1_mass", "F")
        self.out.branch("DY_l2_pt", "F")
        self.out.branch("DY_l2_eta", "F")
        self.out.branch("DY_l2_phi", "F")
        self.out.branch("DY_l2_mass", "F")
        self.out.branch("DY_z_mass", "F")
        self.out.branch("DY_z_pt", "F")
        self.out.branch("DY_z_eta", "F")
        self.out.branch("DY_z_phi", "F")
        self.out.branch("DY_drll", "F")
        self.out.branch("tightJets_id_in24", "I", lenVar="nJet")
        self.out.branch("tightJets_id_in47", "I", lenVar="nJet")
        self.out.branch("tightJets_b_DeepJetloose_id", "I", lenVar="nJet")
        self.out.branch("tightJets_b_DeepJetmedium_id", "I", lenVar="nJet")
        self.out.branch("tightJets_b_DeepJettight_id", "I", lenVar="nJet")
        self.out.branch("tightElectrons_id", "I", lenVar="nElectron")
        self.out.branch("tightElectrons_noIso_id", "I", lenVar="nElectron")
        self.out.branch("additional_vetoElectrons_id", "I", lenVar="nElectron")
        self.out.branch("additional_vetoElectrons_noIso_id",
                        "I", lenVar="nElectron")
        self.out.branch("tightMuons_id", "I", lenVar="nMuon")
        self.out.branch("tightMuons_noIso_id", "I", lenVar="nMuon")
        self.out.branch("additional_looseMuons_id", "I", lenVar="nMuon")
        self.out.branch("additional_looseMuons_noIso_id", "I", lenVar="nMuon")
        self.out.branch("Had_tau_id", "I", lenVar="nTau")
        self.out.branch("muon_jet_Ptratio", "F", lenVar="nMuon")
        self.out.branch("muon_closest_jetid", "I", lenVar="nMuon")
        self.out.branch("electron_jet_Ptratio", "F", lenVar="nElectron")
        self.out.branch("electron_closest_jetid", "I", lenVar="nElectron")
        self.is_mc = bool(inputTree.GetBranch("GenJet_pt"))
        self.is_lhe = bool(inputTree.GetBranch("nLHEPart"))
        self.has_cjet_tag = bool(inputTree.GetBranch("Jet_btagDeepFlavCvL"))
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        # PV selection
        if (event.PV_npvsGood < 1):
            return False

        # trigger selection
        # special action for 2017 single ele HLT, https://twiki.cern.ch/twiki/bin/viewauth/CMS/Egamma2017DataRecommendations#Single_Electron_Triggers
        HLT_passEle32WPTight = 0
        if self.year == "2017":
            trgobjs = Collection(event, 'TrigObj')
            if event.HLT_Ele32_WPTight_Gsf_L1DoubleEG == 1:
                for trgobj in trgobjs:
                    if trgobj.id == 11 and (trgobj.filterBits & (1 << 10)) == (1 << 10):
                        HLT_passEle32WPTight = 1

        self.out.fillBranch("HLT_passEle32WPTight", HLT_passEle32WPTight)
        muons = Collection(event, 'Muon')
        electrons = Collection(event, 'Electron')
        jets = Collection(event, 'Jet')
        met = Object(event, 'MET')
        lhe_nlepton = 0
        ##############################################
        ###  Checking the presence of corrections  ###
        ##############################################
        if not self.mucheck_has_run and len(muons) > 0:
            self.is_mu_corr = hasattr(muons, "corrected_pt")
            if not self.is_mu_corr:
                print("WARNING: Muon Rochester corrections not present!")
            self.mucheck_has_run = True
        if not self.echeck_has_run and len(electrons) > 0:
            self.is_ele_corr = hasattr(electrons[0], "eCorr")
            if not self.is_ele_corr:
                print("WARNING: Electron energy corrections not present!")
            self.echeck_has_run = True
        if not self.jetcheck_has_run and len(jets) > 0:
            self.is_jet_corr = hasattr(jets[0], "mass_nom")
            if not self.is_jet_corr:
                print("WARNING: Jet energy corrections not present!")
            self.jetcheck_has_run = True
        '''
        self.is_jet_corr = True
        self.is_ele_corr = True
        self.is_mu_corr = False
        '''
        
        if self.is_lhe:
            lheparticle = Collection(event, 'LHEPart')
            for lhe in lheparticle:
                if lhe.status == 1 and (abs(lhe.pdgId) == 11 or abs(lhe.pdgId) == 13 or abs(lhe.pdgId) == 15):
                    lhe_nlepton = lhe_nlepton+1
        self.out.fillBranch("lhe_nlepton", lhe_nlepton)

        # total number of ele+muon, currently require at least 1 leptons
        if ((len(muons) + len(electrons)) < 1):
            return False
        if not len(jets) > 1:
            return False  # meant at least two jets

        #Taking the right pt and mass from jets after JES corrections
        if self.is_jet_corr:
            for jet in jets:
                jet.pt = jet.pt_nom
                jet.mass = jet.mass_nom
        if self.is_mc:
            met.T1_pt = met.T1Smear_pt
            met.T1_phi = met.T1Smear_phi

        # lepton pt threshold according to the HLT
        # if self.year=="2016apv":
        #  ele_pt=30
        #  muon_pt=26
        # if self.year=="2016":
        #  ele_pt=30
        #  muon_pt=26
        # if self.year=="2017":
        #  ele_pt=35
        #  muon_pt=30
        # if self.year=="2018":
        #  ele_pt=35
        #  muon_pt=26

        ele_pt = 30
        muon_pt = 20

        # Muon selection: tight cut-based ID + tight PF iso, or loose cut-based ID + loose PF iso, with pt > 20 GeV
        tightMuons = []
        tightMuons_pdgid = []
        tightMuons_id = []
        additional_looseMuons = []
        additional_looseMuons_pdgid = []
        additional_looseMuons_id = []

        tightMuons_noIso = []
        tightMuons_noIso_pdgid = []
        tightMuons_noIso_id = []
        additional_looseMuons_noIso = []
        additional_looseMuons_noIso_pdgid = []
        additional_looseMuons_noIso_id = []

        muon_jet_Ptratio = []
        muon_closest_jetid = []

        for mu in muons:
            mu.pt_raw = mu.pt
            if self.is_mu_corr:
                mu.pt = mu.corrected_pt
            muon_closest_jet, dr_mu_jet = closest(mu, jets)
            muon_closest_jetid.append(muon_closest_jet._index)

            if dr_mu_jet < 0.4:
                muon_jet_Ptratio.append(mu.pt / (0.85 * muon_closest_jet.pt))
            else:
                muon_jet_Ptratio.append(1. / (1 + mu.miniPFRelIso_all))

            if not mu.isPFCand == 1 and not (mu.isGlobal == 1 or mu.isTracker == 1):
                continue
             # topMVA ID: 1:VLoose 2: Loose 3: Medium 4: Tight
            if (mu.topMVA_ID > 3):
                if (abs(mu.eta) < 2.4 and mu.pt > muon_pt and (abs(mu.dxy) < 0.05) and (abs(mu.dz) < 0.1) and mu.miniPFRelIso_all < 0.4 and mu.sip3d < 8.):
                    tightMuons.append(mu)
                    tightMuons_pdgid.append(mu.pdgId)
                    tightMuons_id.append(mu._index)
            elif (mu.topMVA_ID > 1):
                if (abs(mu.eta) < 2.4 and mu.pt > 10 and (abs(mu.dxy) < 0.05) and (abs(mu.dz) < 0.1) and mu.miniPFRelIso_all < 0.4 and mu.sip3d < 8.):
                    additional_looseMuons.append(mu)
                    additional_looseMuons_pdgid.append(mu.pdgId)
                    additional_looseMuons_id.append(mu._index)
            if (mu.mediumId):
                if (abs(mu.eta) < 2.4 and mu.pt > muon_pt and (abs(mu.dxy) < 0.05) and (abs(mu.dz) < 0.1) and mu.sip3d < 8.):
                    tightMuons_noIso.append(mu)
                    tightMuons_noIso_pdgid.append(mu.pdgId)
                    tightMuons_noIso_id.append(mu._index)
            elif (mu.topMVA_ID > 1):
                if (abs(mu.eta) < 2.4 and mu.pt > 10 and (abs(mu.dxy) < 0.05) and (abs(mu.dz) < 0.1) and mu.miniPFRelIso_all < 0.4 and mu.sip3d < 8.):
                    additional_looseMuons_noIso.append(mu)
                    additional_looseMuons_noIso_pdgid.append(mu.pdgId)
                    additional_looseMuons_noIso_id.append(mu._index)

        n_tight_muon_noIso = len(tightMuons_noIso)
        n_loose_muon_noIso = len(additional_looseMuons_noIso)
        n_tight_muon = len(tightMuons)
        n_loose_muon = len(additional_looseMuons)

        self.out.fillBranch("n_tight_muon", n_tight_muon)
        self.out.fillBranch("n_loose_muon", n_loose_muon)
        tightMuons_id.extend(np.zeros(len(muons)-len(tightMuons_id), int)-1)
        additional_looseMuons_id.extend(np.zeros(len(muons)-len(additional_looseMuons_id), int)-1)
        self.out.fillBranch("tightMuons_id", tightMuons_id)
        self.out.fillBranch("additional_looseMuons_id", additional_looseMuons_id)
        self.out.fillBranch("n_tight_muon_noIso", n_tight_muon_noIso)
        self.out.fillBranch("n_loose_muon_noIso", n_loose_muon_noIso)
        tightMuons_noIso_id.extend(np.zeros(len(muons)-len(tightMuons_noIso_id), int)-1)
        additional_looseMuons_noIso_id.extend(np.zeros(len(muons)-len(additional_looseMuons_noIso_id), int)-1)
        self.out.fillBranch("tightMuons_noIso_id", tightMuons_noIso_id)
        self.out.fillBranch("additional_looseMuons_noIso_id", additional_looseMuons_noIso_id)
        self.out.fillBranch("muon_jet_Ptratio", muon_jet_Ptratio)
        self.out.fillBranch("muon_closest_jetid", muon_closest_jetid)

        # electron selection: tight (veto) cut-based ID + impact parameter cut, with pt > 15 GeV
        tightElectrons = []
        tightElectrons_pdgid = []
        tightElectrons_id = []
        additional_vetoElectrons = []
        additional_vetoElectrons_pdgid = []
        additional_vetoElectrons_id = []

        tightElectrons_noIso = []
        tightElectrons_noIso_pdgid = []
        tightElectrons_noIso_id = []
        additional_vetoElectrons_noIso = []
        additional_vetoElectrons_noIso_pdgid = []
        additional_vetoElectrons_noIso_id = []

        electron_jet_Ptratio = []
        electron_closest_jetid = []

        # Main electron loop
        for ele in electrons:
            electron_closest_jet, dr_ele_jet = closest(ele, jets)
            electron_closest_jetid.append(electron_closest_jet._index)
            iele = ele._index
            if dr_ele_jet < 0.4:
                electron_jet_Ptratio.append(ele.pt / (0.85 * electron_closest_jet.pt))
            else:
                electron_jet_Ptratio.append(1. / (1 + ele.miniPFRelIso_all))

            if (((abs(ele.eta+ele.deltaEtaSC) < 1.4442) or (abs(ele.eta + ele.deltaEtaSC) > 1.566 and abs(ele.eta + ele.deltaEtaSC) < 2.5)) and abs(ele.dxy) < 0.05 and abs(ele.dz) < 0.1 and ele.lostHits <= 1 and ele.sip3d < 8):
                if (ele.topMVA_ID > 3 and ele.pt > ele_pt and ele.miniPFRelIso_all < 0.4):
                    tightElectrons.append(ele)
                    tightElectrons_pdgid.append(ele.pdgId)
                    tightElectrons_id.append(iele)
                elif (ele.topMVA_ID > 1 and ele.pt > 10 and ele.miniPFRelIso_all < 0.4):
                    additional_vetoElectrons.append(ele)
                    additional_vetoElectrons_pdgid.append(ele.pdgId)
                    additional_vetoElectrons_id.append(iele)
                if (ele.mvaFall17V2noIso_WP90 and ele.pt > ele_pt):
                    tightElectrons_noIso.append(ele)
                    tightElectrons_noIso_pdgid.append(ele.pdgId)
                    tightElectrons_noIso_id.append(iele)
                elif (ele.topMVA_ID > 1 and ele.pt > 10 and ele.miniPFRelIso_all < 0.4):
                    additional_vetoElectrons_noIso.append(ele)
                    additional_vetoElectrons_noIso_pdgid.append(ele.pdgId)
                    additional_vetoElectrons_noIso_id.append(iele)

        n_tight_ele = len(tightElectrons)
        n_loose_ele = len(additional_vetoElectrons)
        n_tight_ele_noIso = len(tightElectrons_noIso)
        n_loose_ele_noIso = len(additional_vetoElectrons_noIso)

        self.out.fillBranch("n_tight_ele", n_tight_ele)
        self.out.fillBranch("n_loose_ele", n_loose_ele)
        tightElectrons_id.extend(np.zeros(len(electrons)-len(tightElectrons_id), int)-1)
        additional_vetoElectrons_id.extend(np.zeros(len(electrons)-len(additional_vetoElectrons_id), int)-1)
        self.out.fillBranch("tightElectrons_id", tightElectrons_id)
        self.out.fillBranch("additional_vetoElectrons_id", additional_vetoElectrons_id)
        self.out.fillBranch("n_tight_ele_noIso", n_tight_ele_noIso)
        self.out.fillBranch("n_loose_ele_noIso", n_loose_ele_noIso)
        tightElectrons_noIso_id.extend(np.zeros(len(electrons)-len(tightElectrons_noIso_id), int)-1)
        additional_vetoElectrons_noIso_id.extend(np.zeros(len(electrons)-len(additional_vetoElectrons_noIso_id), int)-1)
        self.out.fillBranch("tightElectrons_noIso_id", tightElectrons_noIso_id)
        self.out.fillBranch("additional_vetoElectrons_noIso_id", additional_vetoElectrons_noIso_id)
        self.out.fillBranch("electron_jet_Ptratio", electron_jet_Ptratio)
        self.out.fillBranch("electron_closest_jetid", electron_closest_jetid)


        # tight leptons and additional loose leptons collection
        tightLeptons = tightMuons + tightElectrons
        tightLeptons.sort(key=lambda x: x.pt, reverse=True)
        looseLeptons = additional_looseMuons + additional_vetoElectrons
        looseLeptons.sort(key=lambda x: x.pt, reverse=True)

        tightLeptons_noIso = tightMuons_noIso + tightElectrons_noIso
        tightLeptons_noIso.sort(key=lambda x: x.pt, reverse=True)
        looseLeptons_noIso = additional_looseMuons_noIso + additional_vetoElectrons_noIso
        looseLeptons_noIso.sort(key=lambda x: x.pt, reverse=True)
        # gkole turn off for revert back to set-I
        '''
    if len(tightLeptons)<1:return False  
    if self.is_mc:
      if met.T1Smear_pt < 30: return False
    else:
      if met.T1_pt < 30: return False
    '''

        #################
        # Tau collection:
        #################
        taus = Collection(event, 'Tau')
        nHad_tau = 0
        Had_tau_id = []
        for tau in taus:
            pass_tau_lep_Dr = 1
            #if tau.pt > 20 and abs(tau.eta) < 2.3 and abs(tau.dz)<0.2 and tau.idDecayModeOldDMs and tau.idDeepTau2017v2p1VSe >= 4 and tau.idDeepTau2017v2p1VSjet >= 4 and tau.idDeepTau2017v2p1VSmu >= 1:
            if tau.pt>20 and abs(tau.eta)<2.3 and abs(tau.dz)<0.2 and tau.idDeepTau2017v2p1VSe>=4 and tau.idDeepTau2017v2p1VSjet>=4 and tau.idDeepTau2017v2p1VSmu>=1 and tau.decayMode!=5 and tau.decayMode!=6: # use this for non-nanoaodv9
                for tightlep in tightLeptons:
                    if tau.DeltaR(tightlep) < 0.4:
                        pass_tau_lep_Dr = 0
                if pass_tau_lep_Dr:
                    nHad_tau += 1
                    Had_tau_id.append(tau._index)
        self.out.fillBranch("nHad_tau", nHad_tau)

        # https://btv-wiki.docs.cern.ch/ScaleFactors/
        # https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD#Jets
        # *** jetId==2 means: pass tight ID, fail tightLepVeto
        # *** jetId==6 means: pass tight and tightLepVeto ID.
        # tightLepVeto PF jets (ak4), UL 2016/2017/2018 (jetId 110=6), medium B-tag WP
        # UL17 DeepCSV=(nanoaod btagDeepB) loose: 0.1355, medium: 0.4506, tight: 0.7738
        # UL18 DeepCSV=(nanoaod btagDeepB) loose: 0.1208, medium: 0.4168, tight: 0.7665
        # UL17 DeepFlavor=(nanoaod btagDeepFlavB) loose: 0.0532, medium: 0.3040, tight: 0.7476
        # UL18 DeepFlavor=(nanoaod btagDeepFlavB) loose: 0.0490, medium: 0.2783, tight: 0.7100

        # c-jet tag is based on two-D cuts, medium DeepJet WP:
        # UL17 CvsL=btagDeepFlavCvL: 0.085, CvsB=btagDeepFlavCvB: 0.34
        # UL18 CvsL=btagDeepFlavCvL: 0.099, CvsB=btagDeepFlavCvB: 0.325
        # c-tag not available in NANOAOD yet

        j1_pt = -99
        j1_eta = -99
        j1_phi = -99
        j1_mass = -99
        j2_pt = -99
        j2_eta = -99
        j2_phi = -99
        j2_mass = -99
        j3_pt = -99
        j3_eta = -99
        j3_phi = -99
        j3_mass = -99
        j4_pt = -99
        j4_eta = -99
        j4_phi = -99
        j4_mass = -99
        mj1j2 = -99
        mj1j3 = -99
        mj1j4 = -99
        mj2j3 = -99
        mj2j4 = -99
        mj3j4 = -99
        mj1j2j3 = -99
        mj1j2j4 = -99
        mj2j3j4 = -99
        mj1j2j3j4 = -99
        drj1j2 = -99
        drj1j3 = -99
        drj1j4 = -99
        drj2j3 = -99
        drj2j4 = -99
        drj3j4 = -99
        DeepB_loose_j1_pt = -99
        DeepB_loose_j1_eta = -99
        DeepB_loose_j1_phi = -99
        DeepB_loose_j1_mass = -99
        DeepB_loose_j2_pt = -99
        DeepB_loose_j2_eta = -99
        DeepB_loose_j2_phi = -99
        DeepB_loose_j2_mass = -99
        DeepB_loose_j3_pt = -99
        DeepB_loose_j3_eta = -99
        DeepB_loose_j3_phi = -99
        DeepB_loose_j3_mass = -99

        DeepB_medium_j1_pt = -99
        DeepB_medium_j1_eta = -99
        DeepB_medium_j1_phi = -99
        DeepB_medium_j1_mass = -99
        DeepB_medium_j2_pt = -99
        DeepB_medium_j2_eta = -99
        DeepB_medium_j2_phi = -99
        DeepB_medium_j2_mass = -99
        DeepB_medium_j3_pt = -99
        DeepB_medium_j3_eta = -99
        DeepB_medium_j3_phi = -99
        DeepB_medium_j3_mass = -99

        DeepB_tight_j1_pt = -99
        DeepB_tight_j1_eta = -99
        DeepB_tight_j1_phi = -99
        DeepB_tight_j1_mass = -99
        DeepB_tight_j2_pt = -99
        DeepB_tight_j2_eta = -99
        DeepB_tight_j2_phi = -99
        DeepB_tight_j2_mass = -99
        DeepB_tight_j3_pt = -99
        DeepB_tight_j3_eta = -99
        DeepB_tight_j3_phi = -99
        DeepB_tight_j3_mass = -99

        tightJets_id_in24 = []
        tightJets_in24 = []
        tightJets_id_in47 = []

        tightJets_b_DeepJetloose_id = []
        tightJets_b_DeepJetmedium_id = []
        tightJets_b_DeepJettight_id = []
        tightJets_b_DeepJetloose = []
        tightJets_b_DeepJetmedium = []
        tightJets_b_DeepJettight = []

        # https://btv-wiki.docs.cern.ch/ScaleFactors/UL2016preVFP/
        # https://btv-wiki.docs.cern.ch/ScaleFactors/UL2016postVFP/
        # https://btv-wiki.docs.cern.ch/ScaleFactors/UL2017/
        # https://btv-wiki.docs.cern.ch/ScaleFactors/UL2018/
        WPbtagger = {
            '2016apv':{'L': 0.0508, 'M': 0.2598, 'T': 0.6502},
            '2016':{'L': 0.0480, 'M': 0.2489, 'T': 0.6377},
            '2017':{'L': 0.0532, 'M': 0.3040, 'T': 0.7476},
            '2018':{'L': 0.0490, 'M': 0.2783, 'T': 0.7100}
        }
   
        # HT (sum of all tightjets)
        HT = 0
        for jet in jets:
            jet_is_tau = 0
            if nHad_tau > 0:
                for ita in Had_tau_id:
                    if jet._index == taus[ita].jetIdx:
                        jet_is_tau = 1
            if jet_is_tau:
                continue
    
            # require DeltaR between Jets and tight leptons greater than 0.4
            pass_jet_lep_Dr = 1
            for tightlep in tightLeptons:
                if jet.DeltaR(tightlep) < 0.4:
                    pass_jet_lep_Dr = 0

            if not (pass_jet_lep_Dr > 0):
                continue
            if not (jet.jetId == 6 and jet.pt > 30):
                continue  # tight jets with pT > 30 GeV
            # https://twiki.cern.ch/twiki/bin/view/CMS/JetID#nanoAOD_Flags
            # https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetIDUL#Trainings
            if (jet.pt < 50 and not (jet.puId == 7)):
                continue

            etacentraljet = {
                '2016apv':2.4,
                '2016':2.4,
                '2017':2.5,
                '2018':2.5,
            }

            if abs(jet.eta) < 4.7 and abs(jet.eta) >= etacentraljet[self.year]:
                tightJets_id_in47.append(jet._index)
            if abs(jet.eta) < etacentraljet[self.year]:
                tightJets_in24.append(jet)
                tightJets_id_in24.append(jet._index)
                HT += jet.pt
                #Taking b-jets
                if jet.btagDeepFlavB > WPbtagger[self.year]["T"]: 
                    tightJets_b_DeepJetloose.append(jet)
                    tightJets_b_DeepJetmedium.append(jet)
                    tightJets_b_DeepJettight.append(jet)
                    tightJets_b_DeepJetloose_id.append(jet._index)
                    tightJets_b_DeepJetmedium_id.append(jet._index)
                    tightJets_b_DeepJettight_id.append(jet._index)
                elif jet.btagDeepFlavB > WPbtagger[self.year]["M"]:
                    tightJets_b_DeepJetloose.append(jet)
                    tightJets_b_DeepJetmedium.append(jet)
                    tightJets_b_DeepJetloose_id.append(jet._index)
                    tightJets_b_DeepJetmedium_id.append(jet._index)
                elif jet.btagDeepFlavB > WPbtagger[self.year]["L"]:
                    tightJets_b_DeepJetloose.append(jet)
                    tightJets_b_DeepJetloose_id.append(jet._index)
        self.out.fillBranch("HT", HT)

        n_tight_jet = len(tightJets_id_in24)
        n_bjet_DeepB_loose = len(tightJets_b_DeepJetloose_id)
        n_bjet_DeepB_medium = len(tightJets_b_DeepJetmedium_id)
        n_bjet_DeepB_tight = len(tightJets_b_DeepJettight_id)

        # gkole try (28/09/2023)
        if n_tight_jet < 2:
            return False
        # if n_bjet_DeepB_medium < 1: return False

        self.out.fillBranch("n_tight_jet", n_tight_jet)
        self.out.fillBranch("n_bjet_DeepB_loose", n_bjet_DeepB_loose)
        self.out.fillBranch("n_bjet_DeepB_medium", n_bjet_DeepB_medium)
        self.out.fillBranch("n_bjet_DeepB_tight", n_bjet_DeepB_tight)

        Had_tau_id.extend(np.zeros(event.nTau-len(Had_tau_id), int)-1)
        self.out.fillBranch("Had_tau_id", Had_tau_id)

        if n_tight_jet > 0:
            j1_pt = tightJets_in24[0].pt
            j1_eta = tightJets_in24[0].eta
            j1_phi = tightJets_in24[0].phi
            j1_mass = tightJets_in24[0].mass
        if n_tight_jet > 1:
            j2_pt = tightJets_in24[1].pt
            j2_eta = tightJets_in24[1].eta
            j2_phi = tightJets_in24[1].phi
            j2_mass = tightJets_in24[1].mass
            mj1j2 = (tightJets_in24[0].p4()+tightJets_in24[1].p4()).M()
            drj1j2 = tightJets_in24[0].DeltaR(tightJets_in24[1])
        if n_tight_jet > 2:
            j3_pt = tightJets_in24[2].pt
            j3_eta = tightJets_in24[2].eta
            j3_phi = tightJets_in24[2].phi
            j3_mass = tightJets_in24[2].mass
            mj1j3 = (tightJets_in24[0].p4()+tightJets_in24[2].p4()).M()
            mj2j3 = (tightJets_in24[1].p4()+tightJets_in24[2].p4()).M()
            mj1j2j3 = (tightJets_in24[0].p4()+tightJets_in24[1].p4()+tightJets_in24[2].p4()).M()
            drj1j3 = tightJets_in24[0].DeltaR(tightJets_in24[2])
            drj2j3 = tightJets_in24[1].DeltaR(tightJets_in24[2])     
        if n_tight_jet > 3:
            j4_pt = tightJets_in24[3].pt
            j4_eta = tightJets_in24[3].eta
            j4_phi = tightJets_in24[3].phi
            j4_mass = tightJets_in24[3].mass
            mj1j4 = (tightJets_in24[0].p4() + tightJets_in24[3].p4()).M()
            mj2j4 = (tightJets_in24[1].p4() + tightJets_in24[3].p4()).M()
            mj3j4 = (tightJets_in24[2].p4() + tightJets_in24[3].p4()).M()
            mj1j2j4 = (tightJets_in24[0].p4() + tightJets_in24[1].p4() + tightJets_in24[3].p4()).M()
            mj2j3j4 = (tightJets_in24[1].p4() + tightJets_in24[2].p4() + tightJets_in24[3].p4()).M()
            mj1j2j3j4 = (tightJets_in24[0].p4() + tightJets_in24[1].p4() + tightJets_in24[2].p4() + tightJets_in24[3].p4()).M()
            drj1j4 = tightJets_in24[0].DeltaR(tightJets_in24[3])
            drj2j4 = tightJets_in24[1].DeltaR(tightJets_in24[3])
            drj3j4 = tightJets_in24[2].DeltaR(tightJets_in24[3])


        if n_bjet_DeepB_loose > 0:
            DeepB_loose_j1_pt = tightJets_b_DeepJetloose[0].pt
            DeepB_loose_j1_eta = tightJets_b_DeepJetloose[0].eta
            DeepB_loose_j1_phi = tightJets_b_DeepJetloose[0].phi
            DeepB_loose_j1_mass = tightJets_b_DeepJetloose[0].mass
        if n_bjet_DeepB_loose > 1:
            DeepB_loose_j2_pt = tightJets_b_DeepJetloose[1].pt
            DeepB_loose_j2_eta = tightJets_b_DeepJetloose[1].eta
            DeepB_loose_j2_phi = tightJets_b_DeepJetloose[1].phi
            DeepB_loose_j2_mass = tightJets_b_DeepJetloose[1].mass
        if n_bjet_DeepB_loose > 2:
            DeepB_loose_j3_pt = tightJets_b_DeepJetloose[2].pt
            DeepB_loose_j3_eta = tightJets_b_DeepJetloose[2].eta
            DeepB_loose_j3_phi = tightJets_b_DeepJetloose[2].phi
            DeepB_loose_j3_mass = tightJets_b_DeepJetloose[2].mass

        if n_bjet_DeepB_medium > 0:
            DeepB_medium_j1_pt = tightJets_b_DeepJetmedium[0].pt
            DeepB_medium_j1_eta = tightJets_b_DeepJetmedium[0].eta
            DeepB_medium_j1_phi = tightJets_b_DeepJetmedium[0].phi
            DeepB_medium_j1_mass = tightJets_b_DeepJetmedium[0].mass
        if n_bjet_DeepB_medium > 1:
            DeepB_medium_j2_pt = tightJets_b_DeepJetmedium[1].pt
            DeepB_medium_j2_eta = tightJets_b_DeepJetmedium[1].eta
            DeepB_medium_j2_phi = tightJets_b_DeepJetmedium[1].phi
            DeepB_medium_j2_mass = tightJets_b_DeepJetmedium[1].mass
        if n_bjet_DeepB_medium > 2:
            DeepB_medium_j3_pt = tightJets_b_DeepJetmedium[2].pt
            DeepB_medium_j3_eta = tightJets_b_DeepJetmedium[2].eta
            DeepB_medium_j3_phi = tightJets_b_DeepJetmedium[2].phi
            DeepB_medium_j3_mass = tightJets_b_DeepJetmedium[2].mass

        if n_bjet_DeepB_tight > 0:
            DeepB_tight_j1_pt = tightJets_b_DeepJettight[0].pt
            DeepB_tight_j1_eta = tightJets_b_DeepJettight[0].eta
            DeepB_tight_j1_phi = tightJets_b_DeepJettight[0].phi
            DeepB_tight_j1_mass = tightJets_b_DeepJettight[0].mass
        if n_bjet_DeepB_tight > 1:
            DeepB_tight_j2_pt = tightJets_b_DeepJettight[1].pt
            DeepB_tight_j2_eta = tightJets_b_DeepJettight[1].eta
            DeepB_tight_j2_phi = tightJets_b_DeepJettight[1].phi
            DeepB_tight_j2_mass = tightJets_b_DeepJettight[1].mass
        if n_bjet_DeepB_tight > 2:
            DeepB_tight_j3_pt = tightJets_b_DeepJettight[2].pt
            DeepB_tight_j3_eta = tightJets_b_DeepJettight[2].eta
            DeepB_tight_j3_phi = tightJets_b_DeepJettight[2].phi
            DeepB_tight_j3_mass = tightJets_b_DeepJettight[2].mass

        self.out.fillBranch("j1_pt", j1_pt)
        self.out.fillBranch("j1_eta", j1_eta)
        self.out.fillBranch("j1_phi", j1_phi)
        self.out.fillBranch("j1_mass", j1_mass)
        self.out.fillBranch("j2_pt", j2_pt)
        self.out.fillBranch("j2_eta", j2_eta)
        self.out.fillBranch("j2_phi", j2_phi)
        self.out.fillBranch("j2_mass", j2_mass)
        self.out.fillBranch("j3_pt", j3_pt)
        self.out.fillBranch("j3_eta", j3_eta)
        self.out.fillBranch("j3_phi", j3_phi)
        self.out.fillBranch("j3_mass", j3_mass)
        self.out.fillBranch("j4_pt", j4_pt)
        self.out.fillBranch("j4_eta", j4_eta)
        self.out.fillBranch("j4_phi", j4_phi)
        self.out.fillBranch("j4_mass", j4_mass)
        self.out.fillBranch("mj1j2", mj1j2)
        self.out.fillBranch("mj1j3", mj1j3)
        self.out.fillBranch("mj1j4", mj1j4)
        self.out.fillBranch("mj2j3", mj2j3)
        self.out.fillBranch("mj2j4", mj2j4)
        self.out.fillBranch("mj3j4", mj3j4)
        self.out.fillBranch("mj1j2j3", mj1j2j3)
        self.out.fillBranch("mj1j2j4", mj1j2j4)
        self.out.fillBranch("mj2j3j4", mj2j3j4)
        self.out.fillBranch("mj1j2j3j4", mj1j2j3j4)
        self.out.fillBranch("drj1j2", drj1j2)
        self.out.fillBranch("drj1j3", drj1j3)
        self.out.fillBranch("drj1j4", drj1j4)
        self.out.fillBranch("drj2j3", drj2j3)
        self.out.fillBranch("drj2j4", drj2j4)
        self.out.fillBranch("drj3j4", drj3j4)

        self.out.fillBranch("DeepB_loose_j1_pt", DeepB_loose_j1_pt)
        self.out.fillBranch("DeepB_loose_j1_eta", DeepB_loose_j1_eta)
        self.out.fillBranch("DeepB_loose_j1_phi", DeepB_loose_j1_phi)
        self.out.fillBranch("DeepB_loose_j1_mass", DeepB_loose_j1_mass)
        self.out.fillBranch("DeepB_loose_j2_pt", DeepB_loose_j2_pt)
        self.out.fillBranch("DeepB_loose_j2_eta", DeepB_loose_j2_eta)
        self.out.fillBranch("DeepB_loose_j2_phi", DeepB_loose_j2_phi)
        self.out.fillBranch("DeepB_loose_j2_mass", DeepB_loose_j2_mass)
        self.out.fillBranch("DeepB_loose_j3_pt", DeepB_loose_j3_pt)
        self.out.fillBranch("DeepB_loose_j3_eta", DeepB_loose_j3_eta)
        self.out.fillBranch("DeepB_loose_j3_phi", DeepB_loose_j3_phi)
        self.out.fillBranch("DeepB_loose_j3_mass", DeepB_loose_j3_mass)

        self.out.fillBranch("DeepB_medium_j1_pt", DeepB_medium_j1_pt)
        self.out.fillBranch("DeepB_medium_j1_eta", DeepB_medium_j1_eta)
        self.out.fillBranch("DeepB_medium_j1_phi", DeepB_medium_j1_phi)
        self.out.fillBranch("DeepB_medium_j1_mass", DeepB_medium_j1_mass)
        self.out.fillBranch("DeepB_medium_j2_pt", DeepB_medium_j2_pt)
        self.out.fillBranch("DeepB_medium_j2_eta", DeepB_medium_j2_eta)
        self.out.fillBranch("DeepB_medium_j2_phi", DeepB_medium_j2_phi)
        self.out.fillBranch("DeepB_medium_j2_mass", DeepB_medium_j2_mass)
        self.out.fillBranch("DeepB_medium_j3_pt", DeepB_medium_j3_pt)
        self.out.fillBranch("DeepB_medium_j3_eta", DeepB_medium_j3_eta)
        self.out.fillBranch("DeepB_medium_j3_phi", DeepB_medium_j3_phi)
        self.out.fillBranch("DeepB_medium_j3_mass", DeepB_medium_j3_mass)

        self.out.fillBranch("DeepB_loose_j1_pt", DeepB_loose_j1_pt)
        self.out.fillBranch("DeepB_loose_j1_eta", DeepB_loose_j1_eta)
        self.out.fillBranch("DeepB_loose_j1_phi", DeepB_loose_j1_phi)
        self.out.fillBranch("DeepB_loose_j1_mass", DeepB_loose_j1_mass)
        self.out.fillBranch("DeepB_loose_j2_pt", DeepB_loose_j2_pt)
        self.out.fillBranch("DeepB_loose_j2_eta", DeepB_loose_j2_eta)
        self.out.fillBranch("DeepB_loose_j2_phi", DeepB_loose_j2_phi)
        self.out.fillBranch("DeepB_loose_j2_mass", DeepB_loose_j2_mass)
        self.out.fillBranch("DeepB_loose_j3_pt", DeepB_loose_j3_pt)
        self.out.fillBranch("DeepB_loose_j3_eta", DeepB_loose_j3_eta)
        self.out.fillBranch("DeepB_loose_j3_phi", DeepB_loose_j3_phi)
        self.out.fillBranch("DeepB_loose_j3_mass", DeepB_loose_j3_mass)

        tightJets_id_in24.extend(
            np.zeros(len(jets)-len(tightJets_id_in24), int)-1)
        tightJets_id_in47.extend(
            np.zeros(len(jets)-len(tightJets_id_in47), int)-1)
        tightJets_b_DeepJetloose_id.extend(
            np.zeros(len(jets)-len(tightJets_b_DeepJetloose_id), int)-1)
        tightJets_b_DeepJetmedium_id.extend(
            np.zeros(len(jets)-len(tightJets_b_DeepJetmedium_id), int)-1)
        tightJets_b_DeepJettight_id.extend(
            np.zeros(len(jets)-len(tightJets_b_DeepJettight_id), int)-1)

        self.out.fillBranch("tightJets_id_in24", tightJets_id_in24)
        self.out.fillBranch("tightJets_id_in47", tightJets_id_in47)
        self.out.fillBranch("tightJets_b_DeepJetloose_id", tightJets_b_DeepJetloose_id)
        self.out.fillBranch("tightJets_b_DeepJetmedium_id", tightJets_b_DeepJetmedium_id)
        self.out.fillBranch("tightJets_b_DeepJettight_id", tightJets_b_DeepJettight_id)

        #  BH region (the requirement on bjet will separate this region to signal region and w-region)
        # region: only 1 tight leptons, at least three jets
        # bh region lepton number selections
        bh_nl = False
        # bh region jet and bjet selection
        bh_jets = False
        # bh region tag, 1: muon, 2:ele
        bh_region = 0
        bh_l1_id = -1
        bh_l1_pdgid = -99
        bh_l1_pt = -99
        bh_l1_eta = -99
        bh_l1_phi = -99
        bh_l1_mass = -99
        bh_met = -99
        bh_met_phi = -99
        bh_dr_l1j1 = -99
        bh_dr_l1j2 = -99
        bh_dr_l1j3 = -99
        bh_dr_l1j4 = -99
        bh_mlj1 = -99
        bh_mlj2 = -99
        bh_mlj3 = -99
        bh_mlj4 = -99
        bh_mlj1j2 = -99
        bh_mlj1j3 = -99
        bh_mlj1j4 = -99
        bh_mlj2j3 = -99
        bh_mlj2j4 = -99
        bh_mlj3j4 = -99
        bh_mlb1 = -99
        bh_mlb2 = -99
        bh_mlb3 = -99
        bh_mlb1b2 = -99
        bh_mlb1b3 = -99
        bh_mlb2b3 = -99

        # 2th lepton veto
        if len(tightLeptons) == 1 and len(looseLeptons) == 0:
            if (n_tight_muon == 1 and tightMuons[0].pt > muon_pt) or (n_tight_ele == 1 and tightElectrons[0].pt > ele_pt):
                bh_nl = True
        # at least three jets (bjet requirement will applied at plot level)
        if bh_nl and n_tight_jet > 2:
            bh_jets = True

        if bh_nl:
            bh_met = met.T1_pt
            bh_met_phi = met.T1_phi
            if len(tightMuons) == 1:
                bh_region = 1
            if len(tightElectrons) == 1:
                bh_region = 2
            bh_l1_id = tightLeptons[0]._index
            bh_l1_pdgid = tightLeptons[0].pdgId
            bh_l1_pt = tightLeptons[0].pt
            bh_l1_eta = tightLeptons[0].eta
            bh_l1_phi = tightLeptons[0].phi
            bh_l1_mass = tightLeptons[0].mass
            bh_l1 = tightLeptons[0]

        # bh_region = 1 i.e, (muon) and bh_region = 2 i.e, (electron)
        if bh_region > 0:
            if n_tight_jet > 0:
                bh_dr_l1j1 = bh_l1.DeltaR(tightJets_in24[0])
                bh_mlj1 = (bh_l1.p4()+tightJets_in24[0].p4()).M()
            if n_tight_jet > 1:
                bh_dr_l1j2 = bh_l1.DeltaR(tightJets_in24[1])
                bh_mlj2 = (bh_l1.p4()+tightJets_in24[1].p4()).M()
                bh_mlj1j2 = (bh_l1.p4()+tightJets_in24[0].p4()+tightJets_in24[1].p4()).M()
            if n_tight_jet > 2:
                bh_dr_l1j3 = bh_l1.DeltaR(tightJets_in24[2])
                bh_mlj3 = (bh_l1.p4()+tightJets_in24[2].p4()).M()
                bh_mlj1j3 = (bh_l1.p4()+tightJets_in24[0].p4()+tightJets_in24[2].p4()).M()
                bh_mlj2j3 = (bh_l1.p4()+tightJets_in24[1].p4()+tightJets_in24[2].p4()).M()
            if n_tight_jet > 3:
                bh_dr_l1j4 = bh_l1.DeltaR(tightJets_in24[3])
                bh_mlj4 = (bh_l1.p4()+tightJets_in24[3].p4()).M()
                bh_mlj1j4 = (bh_l1.p4()+tightJets_in24[0].p4()+tightJets_in24[3].p4()).M()
                bh_mlj2j4 = (bh_l1.p4()+tightJets_in24[1].p4()+tightJets_in24[3].p4()).M()
                bh_mlj3j4 = (bh_l1.p4()+tightJets_in24[2].p4()+tightJets_in24[3].p4()).M()

            if n_bjet_DeepB_medium > 0:
                bh_mlb1 = (bh_l1.p4()+tightJets_b_DeepJetmedium[0].p4()).M()
            if n_bjet_DeepB_medium > 1:
                bh_mlb2 = (bh_l1.p4()+tightJets_b_DeepJetmedium[1].p4()).M()
                bh_mlb1b2 = (bh_l1.p4()+tightJets_b_DeepJetmedium[0].p4()+tightJets_b_DeepJetmedium[1].p4()).M()
            if n_bjet_DeepB_medium > 2:
                bh_mlb3 = (bh_l1.p4()+tightJets_b_DeepJetmedium[2].p4()).M()
                bh_mlb1b3 = (bh_l1.p4()+tightJets_b_DeepJetmedium[0].p4()+tightJets_b_DeepJetmedium[2].p4()).M()
                bh_mlb2b3 = (bh_l1.p4()+tightJets_b_DeepJetmedium[1].p4()+tightJets_b_DeepJetmedium[2].p4()).M()


        self.out.fillBranch("bh_nl", bh_nl)
        self.out.fillBranch("bh_jets", bh_jets)
        self.out.fillBranch("bh_region", bh_region)
        self.out.fillBranch("bh_l1_id", bh_l1_id)
        self.out.fillBranch("bh_l1_pdgid", bh_l1_pdgid)
        self.out.fillBranch("bh_l1_pt", bh_l1_pt)
        self.out.fillBranch("bh_l1_eta", bh_l1_eta)
        self.out.fillBranch("bh_l1_phi", bh_l1_phi)
        self.out.fillBranch("bh_l1_mass", bh_l1_mass)
        self.out.fillBranch("bh_met", bh_met)
        self.out.fillBranch("bh_met_phi", bh_met_phi)
        self.out.fillBranch("bh_dr_l1j1", bh_dr_l1j1)
        self.out.fillBranch("bh_dr_l1j2", bh_dr_l1j2)
        self.out.fillBranch("bh_dr_l1j3", bh_dr_l1j3)
        self.out.fillBranch("bh_dr_l1j4", bh_dr_l1j4)
        self.out.fillBranch("bh_mlj1", bh_mlj1)
        self.out.fillBranch("bh_mlj2", bh_mlj2)
        self.out.fillBranch("bh_mlj3", bh_mlj3)
        self.out.fillBranch("bh_mlj4", bh_mlj4)
        self.out.fillBranch("bh_mlj1j2", bh_mlj1j2)
        self.out.fillBranch("bh_mlj1j3", bh_mlj1j3)
        self.out.fillBranch("bh_mlj1j4", bh_mlj1j4)
        self.out.fillBranch("bh_mlj2j3", bh_mlj2j3)
        self.out.fillBranch("bh_mlj2j4", bh_mlj2j4)
        self.out.fillBranch("bh_mlj3j4", bh_mlj3j4)
        self.out.fillBranch("bh_mlb1", bh_mlb1)
        self.out.fillBranch("bh_mlb2", bh_mlb2)
        self.out.fillBranch("bh_mlb3", bh_mlb3)
        self.out.fillBranch("bh_mlb1b2", bh_mlb1b2)
        self.out.fillBranch("bh_mlb1b3", bh_mlb1b3)
        self.out.fillBranch("bh_mlb2b3", bh_mlb2b3)

        ####################
        ## Boosted Region ##
        ####################

        boost_region = 0
        boost_l1_id = -1
        boost_l1_pdgid = -99
        boost_l1_pt = -99
        boost_l1_eta = -99
        boost_l1_phi = -99
        boost_l1_mass = -99
        boost_met = -99
        boost_met_phi = -99
        if len(tightLeptons_noIso) == 1 and len(looseLeptons_noIso) == 0:
            if (n_tight_muon_noIso == 1 and tightMuons_noIso[0].pt > muon_pt):
                boost_region = 1
            elif (n_tight_ele_noIso == 1 and tightElectrons_noIso[0].pt > ele_pt):
                boost_region = 2
            boost_l1_id = tightLeptons_noIso[0]._index
            boost_l1_pdgid = tightLeptons_noIso[0].pdgId
            boost_l1_pt = tightLeptons_noIso[0].pt
            boost_l1_eta = tightLeptons_noIso[0].eta
            boost_l1_phi = tightLeptons_noIso[0].phi
            boost_l1_mass = tightLeptons_noIso[0].mass
        if (boost_region > 0):
            boost_met = met.T1_pt
            boost_met_phi = met.T1_phi

        self.out.fillBranch("boost_region", boost_region)
        self.out.fillBranch("boost_l1_id", boost_l1_id)
        self.out.fillBranch("boost_l1_pdgid", boost_l1_pdgid)
        self.out.fillBranch("boost_l1_pt", boost_l1_pt)
        self.out.fillBranch("boost_l1_eta", boost_l1_eta)
        self.out.fillBranch("boost_l1_phi", boost_l1_phi)
        self.out.fillBranch("boost_l1_mass", boost_l1_mass)
        self.out.fillBranch("boost_met", boost_met)
        self.out.fillBranch("boost_met_phi", boost_met_phi)


        ##################
        ##  Trigger EM  ##
        ##################
        Trigger_derived_region = False
        # There are four kind of trigger scale factors ['resolved', 'boost'] (region) x ['Electron', 'Muon'](lepton) and the derivation region is more or less overlap with each others, so we only select the union of them and separate them offline.
        # Muon as "Tag"
        if (n_tight_muon == 1 and tightMuons[0].pt > muon_pt and n_loose_muon == 0):
            if (n_tight_ele == 1 and tightElectrons[0].pt > ele_pt and n_loose_ele == 0):
                Trigger_derived_region = True
            elif (n_tight_ele_noIso == 1 and tightElectrons_noIso[0].pt > ele_pt and n_loose_ele_noIso == 0):
                Trigger_derived_region = True
        # Electron as "Tag"
        elif (n_tight_ele == 1 and tightElectrons[0].pt > ele_pt and n_loose_ele == 0):
            if (n_tight_muon == 1 and tightMuons[0].pt > muon_pt and n_loose_muon == 0):
                Trigger_derived_region = True
            elif (n_tight_muon_noIso == 1 and tightMuons_noIso[0].pt > muon_pt and n_loose_muon_noIso == 0):
                Trigger_derived_region = True
        self.out.fillBranch("Trigger_derived_region", Trigger_derived_region)

        ###################
        # WZ region
        ##################

        # WZ region lepton number selections
        WZ_nl = False
        # WZ region b-jet selection
        WZ_nb = False
        # WZ region lepton kinematics selctions
        WZ_leptons = False
        # WZ region MET selection
        WZ_MET = False
        # WZ region tag, 0: fail to pass the WZ selection, 1:3 muon, 2:2muon, 3:1muon, 4:0 muon
        WZ_region = 0
        WZ_zl1_id = -1
        WZ_zl2_id = -1
        WZ_wl_id = -1
        WZ_zl1_pdgid = -99
        WZ_zl2_pdgid = -99
        WZ_wl_pdgid = -99
        WZ_zl1_pt = -99
        WZ_zl1_eta = -99
        WZ_zl1_phi = -99
        WZ_zl1_mass = -99
        WZ_zl2_pt = -99
        WZ_zl2_eta = -99
        WZ_zl2_phi = -99
        WZ_zl2_mass = -99
        WZ_l3_pt = -99
        WZ_l3_eta = -99
        WZ_l3_phi = -99
        WZ_l3_mass = -99
        WZ_Z_mass = -99
        WZ_Z_pt = -99
        WZ_Z_eta = -99
        WZ_Z_phi = -99
        WZ_met = -99
        # the first two leading leptons with pt >20, 3rd lepton pt >15, 4th lepton veto
        if len(tightLeptons) == 3 and tightLeptons[1].pt > 20 and len(looseLeptons) == 0:
            WZ_nl = True
        # no bjet
        if WZ_nl and tightJets_b_DeepJetmedium_id[0] == -1:
            WZ_nb = True

        # mll>4 regardless the flavor and charge sign
        if WZ_nb and (tightLeptons[0].p4()+tightLeptons[1].p4()).M() > 4 and (tightLeptons[1].p4()+tightLeptons[2].p4()).M() > 4 and (tightLeptons[0].p4()+tightLeptons[2].p4()).M() > 4:
            WZ_leptons = True

        if WZ_leptons and met.T1_pt > 30:
            WZ_MET = True

        if WZ_MET:
            WZ_met = met.T1_pt
            # 3 muons case
            if len(tightElectrons) == 0 and abs(tightMuons_pdgid[0]+tightMuons_pdgid[1]+tightMuons_pdgid[2]) == 13:
                # two combination 0+2 or 1+2
                if (tightMuons_pdgid[0]-tightMuons_pdgid[1]) == 0:
                    if abs((tightMuons[0].p4()+tightMuons[2].p4()).M()-91.1876) < abs((tightMuons[1].p4()+tightMuons[2].p4()).M()-91.1876) and abs((tightMuons[0].p4()+tightMuons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[1]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[1]
                        WZ_zl1_pt = tightMuons[0].pt
                        WZ_zl1_eta = tightMuons[0].eta
                        WZ_zl1_phi = tightMuons[0].phi
                        WZ_zl1_mass = tightMuons[0].mass
                        WZ_zl2_pt = tightMuons[2].pt
                        WZ_zl2_eta = tightMuons[2].eta
                        WZ_zl2_phi = tightMuons[2].phi
                        WZ_zl2_mass = tightMuons[2].mass
                        WZ_l3_pt = tightMuons[1].pt
                        WZ_l3_eta = tightMuons[1].eta
                        WZ_l3_phi = tightMuons[1].phi
                        WZ_l3_mass = tightMuons[1].mass
                        WZ_Z_mass = (tightMuons[0].p4()+tightMuons[2].p4()).M()
                        WZ_Z_pt = (tightMuons[0].p4()+tightMuons[2].p4()).Pt()
                        WZ_Z_eta = (tightMuons[0].p4()+tightMuons[2].p4()).Eta()
                        WZ_Z_phi = (tightMuons[0].p4()+tightMuons[2].p4()).Phi()

                    if abs((tightMuons[0].p4()+tightMuons[2].p4()).M()-91.1876) > abs((tightMuons[1].p4()+tightMuons[2].p4()).M()-91.1876) and abs((tightMuons[1].p4()+tightMuons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[1]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[0]
                        WZ_zl1_pdgid = tightMuons_pdgid[1]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[0]
                        WZ_zl1_pt = tightMuons[1].pt
                        WZ_zl1_eta = tightMuons[1].eta
                        WZ_zl1_phi = tightMuons[1].phi
                        WZ_zl1_mass = tightMuons[1].mass
                        WZ_zl2_pt = tightMuons[2].pt
                        WZ_zl2_eta = tightMuons[2].eta
                        WZ_zl2_phi = tightMuons[2].phi
                        WZ_zl2_mass = tightMuons[2].mass
                        WZ_l3_pt = tightMuons[0].pt
                        WZ_l3_eta = tightMuons[0].eta
                        WZ_l3_phi = tightMuons[0].phi
                        WZ_l3_mass = tightMuons[0].mass
                        WZ_Z_mass = (tightMuons[1].p4()+tightMuons[2].p4()).M()
                        WZ_Z_pt = (tightMuons[1].p4()+tightMuons[2].p4()).Pt()
                        WZ_Z_eta = (tightMuons[1].p4()+tightMuons[2].p4()).Eta()
                        WZ_Z_phi = (tightMuons[1].p4()+tightMuons[2].p4()).Phi()
                # two combination 0+1 or 1+2
                elif (tightMuons_pdgid[0]-tightMuons_pdgid[2]) == 0:
                    if abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) < abs((tightMuons[1].p4()+tightMuons[2].p4()).M()-91.1876) and abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[1]
                        WZ_wl_id = tightMuons_id[2]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[1]
                        WZ_wl_pdgid = tightMuons_pdgid[2]
                        WZ_zl1_pt = tightMuons[0].pt
                        WZ_zl1_eta = tightMuons[0].eta
                        WZ_zl1_phi = tightMuons[0].phi
                        WZ_zl1_mass = tightMuons[0].mass
                        WZ_zl2_pt = tightMuons[1].pt
                        WZ_zl2_eta = tightMuons[1].eta
                        WZ_zl2_phi = tightMuons[1].phi
                        WZ_zl2_mass = tightMuons[1].mass
                        WZ_l3_pt = tightMuons[2].pt
                        WZ_l3_eta = tightMuons[2].eta
                        WZ_l3_phi = tightMuons[2].phi
                        WZ_l3_mass = tightMuons[2].mass
                        WZ_Z_mass = (tightMuons[0].p4()+tightMuons[1].p4()).M()
                        WZ_Z_pt = (tightMuons[0].p4()+tightMuons[1].p4()).Pt()
                        WZ_Z_eta = (tightMuons[0].p4()+tightMuons[1].p4()).Eta()
                        WZ_Z_phi = (tightMuons[0].p4()+tightMuons[1].p4()).Phi()

                    if abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) > abs((tightMuons[1].p4()+tightMuons[2].p4()).M()-91.1876) and abs((tightMuons[1].p4()+tightMuons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[1]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[0]
                        WZ_zl1_pdgid = tightMuons_pdgid[1]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[0]
                        WZ_zl1_pt = tightMuons[1].pt
                        WZ_zl1_eta = tightMuons[1].eta
                        WZ_zl1_phi = tightMuons[1].phi
                        WZ_zl1_mass = tightMuons[1].mass
                        WZ_zl2_pt = tightMuons[2].pt
                        WZ_zl2_eta = tightMuons[2].eta
                        WZ_zl2_phi = tightMuons[2].phi
                        WZ_zl2_mass = tightMuons[2].mass
                        WZ_l3_pt = tightMuons[0].pt
                        WZ_l3_eta = tightMuons[0].eta
                        WZ_l3_phi = tightMuons[0].phi
                        WZ_l3_mass = tightMuons[0].mass
                        WZ_Z_mass = (tightMuons[1].p4()+tightMuons[2].p4()).M()
                        WZ_Z_pt = (tightMuons[1].p4()+tightMuons[2].p4()).Pt()
                        WZ_Z_eta = (tightMuons[1].p4()+tightMuons[2].p4()).Eta()
                        WZ_Z_phi = (tightMuons[1].p4()+tightMuons[2].p4()).Phi()
                # two combination 0+1 or 0+2
                else:
                    if abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) < abs((tightMuons[0].p4()+tightMuons[2].p4()).M()-91.1876) and abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[1]
                        WZ_wl_id = tightMuons_id[2]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[1]
                        WZ_wl_pdgid = tightMuons_pdgid[2]
                        WZ_zl1_pt = tightMuons[0].pt
                        WZ_zl1_eta = tightMuons[0].eta
                        WZ_zl1_phi = tightMuons[0].phi
                        WZ_zl1_mass = tightMuons[0].mass
                        WZ_zl2_pt = tightMuons[1].pt
                        WZ_zl2_eta = tightMuons[1].eta
                        WZ_zl2_phi = tightMuons[1].phi
                        WZ_zl2_mass = tightMuons[1].mass
                        WZ_l3_pt = tightMuons[2].pt
                        WZ_l3_eta = tightMuons[2].eta
                        WZ_l3_phi = tightMuons[2].phi
                        WZ_l3_mass = tightMuons[2].mass
                        WZ_Z_mass = (tightMuons[0].p4()+tightMuons[1].p4()).M()
                        WZ_Z_pt = (tightMuons[0].p4()+tightMuons[1].p4()).Pt()
                        WZ_Z_eta = (tightMuons[0].p4()+tightMuons[1].p4()).Eta()
                        WZ_Z_phi = (tightMuons[0].p4()+tightMuons[1].p4()).Phi()
                    if abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) > abs((tightMuons[0].p4()+tightMuons[2].p4()).M()-91.1876) and abs((tightMuons[0].p4()+tightMuons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[1]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[1]
                        WZ_zl1_pt = tightMuons[0].pt
                        WZ_zl1_eta = tightMuons[0].eta
                        WZ_zl1_phi = tightMuons[0].phi
                        WZ_zl1_mass = tightMuons[0].mass
                        WZ_zl2_pt = tightMuons[2].pt
                        WZ_zl2_eta = tightMuons[2].eta
                        WZ_zl2_phi = tightMuons[2].phi
                        WZ_zl2_mass = tightMuons[2].mass
                        WZ_l3_pt = tightMuons[1].pt
                        WZ_l3_eta = tightMuons[1].eta
                        WZ_l3_phi = tightMuons[1].phi
                        WZ_l3_mass = tightMuons[1].mass
                        WZ_Z_mass = (tightMuons[0].p4()+tightMuons[2].p4()).M()
                        WZ_Z_pt = (tightMuons[0].p4()+tightMuons[2].p4()).Pt()
                        WZ_Z_eta = (tightMuons[0].p4()+tightMuons[2].p4()).Eta()
                        WZ_Z_phi = (tightMuons[0].p4()+tightMuons[2].p4()).Phi()

            # 2 muons case
            if len(tightElectrons) == 1 and (tightMuons_pdgid[0]-tightMuons_pdgid[1]) == 0:
                if abs((tightMuons[0].p4()+tightMuons[1].p4()).M()-91.1876) < 15:
                    WZ_region = 2
                    WZ_zl1_id = tightMuons_id[0]
                    WZ_zl2_id = tightMuons_id[1]
                    WZ_wl_id = tightElectrons_id[0]
                    WZ_zl1_pdgid = tightMuons_pdgid[0]
                    WZ_zl2_pdgid = tightMuons_pdgid[1]
                    WZ_wl_pdgid = tightElectrons_pdgid[0]
                    WZ_zl1_pt = tightMuons[0].pt
                    WZ_zl1_eta = tightMuons[0].eta
                    WZ_zl1_phi = tightMuons[0].phi
                    WZ_zl1_mass = tightMuons[0].mass
                    WZ_zl2_pt = tightMuons[1].pt
                    WZ_zl2_eta = tightMuons[1].eta
                    WZ_zl2_phi = tightMuons[1].phi
                    WZ_zl2_mass = tightMuons[1].mass
                    WZ_l3_pt = tightElectrons[0].pt
                    WZ_l3_eta = tightElectrons[0].eta
                    WZ_l3_phi = tightElectrons[0].phi
                    WZ_l3_mass = tightElectrons[0].mass
                    WZ_Z_mass = (tightMuons[0].p4()+tightMuons[1].p4()).M()
                    WZ_Z_pt = (tightMuons[0].p4()+tightMuons[1].p4()).Pt()
                    WZ_Z_eta = (tightMuons[0].p4()+tightMuons[1].p4()).Eta()
                    WZ_Z_phi = (tightMuons[0].p4()+tightMuons[1].p4()).Phi()

            # 1 muon case
            if len(tightElectrons) == 2 and (tightElectrons_pdgid[0]-tightElectrons_pdgid[1]) == 0:
                if abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) < 15:
                    WZ_region = 3
                    WZ_zl1_id = tightElectrons_id[0]
                    WZ_zl2_id = tightElectrons_id[1]
                    WZ_wl_id = tightMuons_id[0]
                    WZ_zl1_pdgid = tightElectrons_pdgid[0]
                    WZ_zl2_pdgid = tightElectrons_pdgid[1]
                    WZ_wl_pdgid = tightMuons_pdgid[0]
                    WZ_zl1_pt = tightElectrons[0].pt
                    WZ_zl1_eta = tightElectrons[0].eta
                    WZ_zl1_phi = tightElectrons[0].phi
                    WZ_zl1_mass = tightElectrons[0].mass
                    WZ_zl2_pt = tightElectrons[1].pt
                    WZ_zl2_eta = tightElectrons[1].eta
                    WZ_zl2_phi = tightElectrons[1].phi
                    WZ_zl2_mass = tightElectrons[1].mass
                    WZ_l3_pt = tightMuons[0].pt
                    WZ_l3_eta = tightMuons[0].eta
                    WZ_l3_phi = tightMuons[0].phi
                    WZ_l3_mass = tightMuons[0].mass
                    WZ_Z_mass = (tightElectrons[0].p4()+tightElectrons[1].p4()).M()
                    WZ_Z_pt = (tightElectrons[0].p4()+tightElectrons[1].p4()).Pt()
                    WZ_Z_eta = (tightElectrons[0].p4()+tightElectrons[1].p4()).Eta()
                    WZ_Z_phi = (tightElectrons[0].p4()+tightElectrons[1].p4()).Phi()

            # 0 muon case
            if len(tightElectrons) == 3 and abs(tightElectrons_pdgid[0]+tightElectrons_pdgid[1]+tightElectrons_pdgid[2]) == 11:
                # two combination 0+2 or 1+2
                if (tightElectrons_pdgid[0]-tightElectrons_pdgid[1]) == 0:
                    if abs((tightElectrons[0].p4()+tightElectrons[2].p4()).M()-91.1876) < abs((tightElectrons[1].p4()+tightElectrons[2].p4()).M()-91.1876) and abs((tightElectrons[0].p4()+tightElectrons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[1]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[1]
                        WZ_zl1_pt = tightElectrons[0].pt
                        WZ_zl1_eta = tightElectrons[0].eta
                        WZ_zl1_phi = tightElectrons[0].phi
                        WZ_zl1_mass = tightElectrons[0].mass
                        WZ_zl2_pt = tightElectrons[2].pt
                        WZ_zl2_eta = tightElectrons[2].eta
                        WZ_zl2_phi = tightElectrons[2].phi
                        WZ_zl2_mass = tightElectrons[2].mass
                        WZ_l3_pt = tightElectrons[1].pt
                        WZ_l3_eta = tightElectrons[1].eta
                        WZ_l3_phi = tightElectrons[1].phi
                        WZ_l3_mass = tightElectrons[1].mass
                        WZ_Z_mass = (tightElectrons[0].p4()+tightElectrons[2].p4()).M()
                        WZ_Z_pt = (tightElectrons[0].p4()+tightElectrons[2].p4()).Pt()
                        WZ_Z_eta = (tightElectrons[0].p4()+tightElectrons[2].p4()).Eta()
                        WZ_Z_phi = (tightElectrons[0].p4()+tightElectrons[2].p4()).Phi()
                    if abs((tightElectrons[0].p4()+tightElectrons[2].p4()).M()-91.1876) > abs((tightElectrons[1].p4()+tightElectrons[2].p4()).M()-91.1876) and abs((tightElectrons[1].p4()+tightElectrons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[1]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[0]
                        WZ_zl1_pdgid = tightElectrons_pdgid[1]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[0]
                        WZ_zl1_pt = tightElectrons[1].pt
                        WZ_zl1_eta = tightElectrons[1].eta
                        WZ_zl1_phi = tightElectrons[1].phi
                        WZ_zl1_mass = tightElectrons[1].mass
                        WZ_zl2_pt = tightElectrons[2].pt
                        WZ_zl2_eta = tightElectrons[2].eta
                        WZ_zl2_phi = tightElectrons[2].phi
                        WZ_zl2_mass = tightElectrons[2].mass
                        WZ_l3_pt = tightElectrons[0].pt
                        WZ_l3_eta = tightElectrons[0].eta
                        WZ_l3_phi = tightElectrons[0].phi
                        WZ_l3_mass = tightElectrons[0].mass
                        WZ_Z_mass = (tightElectrons[1].p4()+tightElectrons[2].p4()).M()
                        WZ_Z_pt = (tightElectrons[1].p4()+tightElectrons[2].p4()).Pt()
                        WZ_Z_eta = (tightElectrons[1].p4()+tightElectrons[2].p4()).Eta()
                        WZ_Z_phi = (tightElectrons[1].p4()+tightElectrons[2].p4()).Phi()
                # two combination 0+1 or 1+2
                elif (tightElectrons_pdgid[0]-tightElectrons_pdgid[2]) == 0:
                    if abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) < abs((tightElectrons[1].p4()+tightElectrons[2].p4()).M()-91.1876) and abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[1]
                        WZ_wl_id = tightElectrons_id[2]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[1]
                        WZ_wl_pdgid = tightElectrons_pdgid[2]
                        WZ_zl1_pt = tightElectrons[0].pt
                        WZ_zl1_eta = tightElectrons[0].eta
                        WZ_zl1_phi = tightElectrons[0].phi
                        WZ_zl1_mass = tightElectrons[0].mass
                        WZ_zl2_pt = tightElectrons[1].pt
                        WZ_zl2_eta = tightElectrons[1].eta
                        WZ_zl2_phi = tightElectrons[1].phi
                        WZ_zl2_mass = tightElectrons[1].mass
                        WZ_l3_pt = tightElectrons[2].pt
                        WZ_l3_eta = tightElectrons[2].eta
                        WZ_l3_phi = tightElectrons[2].phi
                        WZ_l3_mass = tightElectrons[2].mass
                        WZ_Z_mass = (tightElectrons[0].p4()+tightElectrons[1].p4()).M()
                        WZ_Z_pt = (tightElectrons[0].p4()+tightElectrons[1].p4()).Pt()
                        WZ_Z_eta = (tightElectrons[0].p4()+tightElectrons[1].p4()).Eta()
                        WZ_Z_phi = (tightElectrons[0].p4()+tightElectrons[1].p4()).Phi()
                    if abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) > abs((tightElectrons[1].p4()+tightElectrons[2].p4()).M()-91.1876) and abs((tightElectrons[1].p4()+tightElectrons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[1]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[0]
                        WZ_zl1_pdgid = tightElectrons_pdgid[1]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[0]
                        WZ_zl1_pt = tightElectrons[1].pt
                        WZ_zl1_eta = tightElectrons[1].eta
                        WZ_zl1_phi = tightElectrons[1].phi
                        WZ_zl1_mass = tightElectrons[1].mass
                        WZ_zl2_pt = tightElectrons[2].pt
                        WZ_zl2_eta = tightElectrons[2].eta
                        WZ_zl2_phi = tightElectrons[2].phi
                        WZ_zl2_mass = tightElectrons[2].mass
                        WZ_l3_pt = tightElectrons[0].pt
                        WZ_l3_eta = tightElectrons[0].eta
                        WZ_l3_phi = tightElectrons[0].phi
                        WZ_l3_mass = tightElectrons[0].mass
                        WZ_Z_mass = (tightElectrons[1].p4()+tightElectrons[2].p4()).M()
                        WZ_Z_pt = (tightElectrons[1].p4()+tightElectrons[2].p4()).Pt()
                        WZ_Z_eta = (tightElectrons[1].p4()+tightElectrons[2].p4()).Eta()
                        WZ_Z_phi = (tightElectrons[1].p4()+tightElectrons[2].p4()).Phi()
                # two combination 0+1 or 0+2
                else:
                    if abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) < abs((tightElectrons[0].p4()+tightElectrons[2].p4()).M()-91.1876) and abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[1]
                        WZ_wl_id = tightElectrons_id[2]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[1]
                        WZ_wl_pdgid = tightElectrons_pdgid[2]
                        WZ_zl1_pt = tightElectrons[0].pt
                        WZ_zl1_eta = tightElectrons[0].eta
                        WZ_zl1_phi = tightElectrons[0].phi
                        WZ_zl1_mass = tightElectrons[0].mass
                        WZ_zl2_pt = tightElectrons[1].pt
                        WZ_zl2_eta = tightElectrons[1].eta
                        WZ_zl2_phi = tightElectrons[1].phi
                        WZ_zl2_mass = tightElectrons[1].mass
                        WZ_l3_pt = tightElectrons[2].pt
                        WZ_l3_eta = tightElectrons[2].eta
                        WZ_l3_phi = tightElectrons[2].phi
                        WZ_l3_mass = tightElectrons[2].mass
                        WZ_Z_mass = (tightElectrons[0].p4()+tightElectrons[1].p4()).M()
                        WZ_Z_pt = (tightElectrons[0].p4()+tightElectrons[1].p4()).Pt()
                        WZ_Z_eta = (tightElectrons[0].p4()+tightElectrons[1].p4()).Eta()
                        WZ_Z_phi = (tightElectrons[0].p4()+tightElectrons[1].p4()).Phi()
                    if abs((tightElectrons[0].p4()+tightElectrons[1].p4()).M()-91.1876) > abs((tightElectrons[0].p4()+tightElectrons[2].p4()).M()-91.1876) and abs((tightElectrons[0].p4()+tightElectrons[2].p4()).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[1]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[1]
                        WZ_zl1_pt = tightElectrons[0].pt
                        WZ_zl1_eta = tightElectrons[0].eta
                        WZ_zl1_phi = tightElectrons[0].phi
                        WZ_zl1_mass = tightElectrons[0].mass
                        WZ_zl2_pt = tightElectrons[2].pt
                        WZ_zl2_eta = tightElectrons[2].eta
                        WZ_zl2_phi = tightElectrons[2].phi
                        WZ_zl2_mass = tightElectrons[2].mass
                        WZ_l3_pt = tightElectrons[1].pt
                        WZ_l3_eta = tightElectrons[1].eta
                        WZ_l3_phi = tightElectrons[1].phi
                        WZ_l3_mass = tightElectrons[1].mass
                        WZ_Z_mass = (tightElectrons[0].p4()+tightElectrons[2].p4()).M()
                        WZ_Z_pt = (tightElectrons[0].p4()+tightElectrons[2].p4()).Pt()
                        WZ_Z_eta = (tightElectrons[0].p4()+tightElectrons[2].p4()).Eta()
                        WZ_Z_phi = (tightElectrons[0].p4()+tightElectrons[2].p4()).Phi()

        self.out.fillBranch("WZ_region", WZ_region)
        self.out.fillBranch("WZ_zl1_id", WZ_zl1_id)
        self.out.fillBranch("WZ_zl2_id", WZ_zl2_id)
        self.out.fillBranch("WZ_wl_id", WZ_wl_id)
        self.out.fillBranch("WZ_zl1_pdgid", WZ_zl1_pdgid)
        self.out.fillBranch("WZ_zl2_pdgid", WZ_zl2_pdgid)
        self.out.fillBranch("WZ_wl_pdgid", WZ_wl_pdgid)
        self.out.fillBranch("WZ_zl1_pt", WZ_zl1_pt)
        self.out.fillBranch("WZ_zl1_eta", WZ_zl1_eta)
        self.out.fillBranch("WZ_zl1_phi", WZ_zl1_phi)
        self.out.fillBranch("WZ_zl1_mass", WZ_zl1_mass)
        self.out.fillBranch("WZ_zl2_pt", WZ_zl2_pt)
        self.out.fillBranch("WZ_zl2_eta", WZ_zl2_eta)
        self.out.fillBranch("WZ_zl2_phi", WZ_zl2_phi)
        self.out.fillBranch("WZ_zl2_mass", WZ_zl2_mass)
        self.out.fillBranch("WZ_l3_pt", WZ_l3_pt)
        self.out.fillBranch("WZ_l3_eta", WZ_l3_eta)
        self.out.fillBranch("WZ_l3_phi", WZ_l3_phi)
        self.out.fillBranch("WZ_l3_mass", WZ_l3_mass)
        self.out.fillBranch("WZ_Z_mass", WZ_Z_mass)
        self.out.fillBranch("WZ_Z_pt", WZ_Z_pt)
        self.out.fillBranch("WZ_Z_eta", WZ_Z_eta)
        self.out.fillBranch("WZ_Z_phi", WZ_Z_phi)
        self.out.fillBranch("WZ_met", WZ_met)

        #  DDDD   YY      YY  (opposite sign) region: two opposite sign lepton, with |mll-91.1876|<15
        #  D   D    YY  YY
        #  D    D     YY
        #  D   D      YY
        #  DDDD       YY

        # DY region lepton number selections (ttbar region are similar)
        DY_nl = False
        # DY region tag, 0: fail to pass the DY selection, 1:2 muon, 2:1 muon, 3:0 muon
        DY_region = 0
        DY_l1_id = -1
        DY_l2_id = -1
        DY_l1_pdgid = -99
        DY_l2_pdgid = -99
        DY_l1_pt = -99
        DY_l1_eta = -99
        DY_l1_phi = -99
        DY_l1_mass = -99
        DY_l2_pt = -99
        DY_l2_eta = -99
        DY_l2_phi = -99
        DY_l2_mass = -99
        DY_z_mass = -99
        DY_z_pt = -99
        DY_z_eta = -99
        DY_z_phi = -99
        DY_drll = -99

        # the two leptons with pt >20, 3th lepton veto
        if len(tightLeptons) == 2 and tightLeptons[1].pt > 20 and len(looseLeptons) == 0:
            DY_nl = True
        if DY_nl:
            # 2 muons case
            if len(tightElectrons) == 0 and abs(tightMuons_pdgid[0]+tightMuons_pdgid[1]) == 0:
                DY_region = 1
            # 2 eles case
            if len(tightElectrons) == 2 and abs(tightElectrons_pdgid[0]+tightElectrons_pdgid[1]) == 0:
                DY_region = 3
             # 1 ele case
            if len(tightElectrons) == 1 and (sign(tightMuons_pdgid[0])+sign(tightElectrons_pdgid[0])) == 0:
                DY_region = 2
            DY_l1_id = tightLeptons[0]._index
            DY_l2_id = tightLeptons[1]._index
            DY_l1_pdgid = tightLeptons[0].pdgId
            DY_l2_pdgid = tightLeptons[1].pdgId
            DY_l1_pt = tightLeptons[0].pt
            DY_l1_eta = tightLeptons[0].eta
            DY_l1_phi = tightLeptons[0].phi
            DY_l1_mass = tightLeptons[0].mass
            DY_l2_pt = tightLeptons[1].pt
            DY_l2_eta = tightLeptons[1].eta
            DY_l2_phi = tightLeptons[1].phi
            DY_l2_mass = tightLeptons[1].mass
            DY_z_mass = (tightLeptons[0].p4()+tightLeptons[1].p4()).M()
            DY_z_pt = (tightLeptons[0].p4()+tightLeptons[1].p4()).Pt()
            DY_z_eta = (tightLeptons[0].p4()+tightLeptons[1].p4()).Eta()
            DY_z_phi = (tightLeptons[0].p4()+tightLeptons[1].p4()).Phi()
            DY_drll = tightLeptons[0].DeltaR(tightLeptons[1])

        self.out.fillBranch("DY_region", DY_region)
        self.out.fillBranch("DY_l1_id", DY_l1_id)
        self.out.fillBranch("DY_l2_id", DY_l2_id)
        self.out.fillBranch("DY_l1_pdgid", DY_l1_pdgid)
        self.out.fillBranch("DY_l2_pdgid", DY_l2_pdgid)
        self.out.fillBranch("DY_l1_pt", DY_l1_pt)
        self.out.fillBranch("DY_l1_eta", DY_l1_eta)
        self.out.fillBranch("DY_l1_phi", DY_l1_phi)
        self.out.fillBranch("DY_l1_mass", DY_l1_mass)
        self.out.fillBranch("DY_l2_pt", DY_l2_pt)
        self.out.fillBranch("DY_l2_eta", DY_l2_eta)
        self.out.fillBranch("DY_l2_phi", DY_l2_phi)
        self.out.fillBranch("DY_l2_mass", DY_l2_mass)
        self.out.fillBranch("DY_z_mass", DY_z_mass)
        self.out.fillBranch("DY_z_pt", DY_z_pt)
        self.out.fillBranch("DY_z_eta", DY_z_eta)
        self.out.fillBranch("DY_z_phi", DY_z_phi)
        self.out.fillBranch("DY_drll", DY_drll)

        if not (bh_nl or Trigger_derived_region or WZ_region > 0 or DY_region > 0 or boost_region > 0):
            return False

        return True


def BH2016apv(): return BHProducer("2016apv")
def BH2016(): return BHProducer("2016")
def BH2017(): return BHProducer("2017")
def BH2018(): return BHProducer("2018")
