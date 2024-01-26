from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from numpy import sign
import numpy as np
import os
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
from ROOT import TLorentzVector
ROOT.PyConfig.IgnoreCommandLineOptions = True


class BHProducer(Module):
    def __init__(self, year):
        self.year = year

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

    def bjet_filter(jet, era, WP): #returns collections of b jets (discriminated with btaggers)
        # b-tag working points: mistagging efficiency tight = 0.1%, medium 1% and loose = 10%
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
        threshold = WPbtagger[str(era)][str(WP)]
        if jet.btagDeepFlavB >= threshold:
            return jet._index
        else:
            return -1
    
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
                for iobj in range(0, event.nTrigObj):
                    if trgobjs[iobj].id == 11 and (trgobjs[iobj].filterBits & (1 << 10)) == (1 << 10):
                        HLT_passEle32WPTight = 1

        self.out.fillBranch("HLT_passEle32WPTight", HLT_passEle32WPTight)

        lhe_nlepton = 0
        if self.is_lhe:
            lheparticle = Collection(event, 'LHEPart')
            for ilhe in range(0, event.nLHEPart):
                if lheparticle[ilhe].status == 1 and (abs(lheparticle[ilhe].pdgId) == 11 or abs(lheparticle[ilhe].pdgId) == 13 or abs(lheparticle[ilhe].pdgId) == 15):
                    lhe_nlepton = lhe_nlepton+1

        self.out.fillBranch("lhe_nlepton", lhe_nlepton)

        # total number of ele+muon, currently require at least 1 leptons
        if ((event.nMuon + event.nElectron) < 1):
            return False
        if not event.nJet > 1:
            return False  # meant at least two jets

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
        muons = Collection(event, 'Muon')
        muon_v4_temp = TLorentzVector()

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
        jet_v4_temp = TLorentzVector()

        for imu in range(0, event.nMuon):
            dr_mu_jet = 99.
            muon_closest_jetid_temp = -1
            muon_v4_temp.SetPtEtaPhiM(
                muons[imu].pt, muons[imu].eta, muons[imu].phi, muons[imu].mass)
            for ijet in range(0, event.nJet):
                jet_v4_temp.SetPtEtaPhiM(
                    event.Jet_pt_nom[ijet], event.Jet_eta[ijet], event.Jet_phi[ijet], event.Jet_mass_nom[ijet])
                if muon_v4_temp.DeltaR(jet_v4_temp) < dr_mu_jet:
                    dr_mu_jet = muon_v4_temp.DeltaR(jet_v4_temp)
                    muon_closest_jetid_temp = ijet

            if dr_mu_jet < 0.4:
                muon_jet_Ptratio.append(
                    muons[imu].pt/(0.85*event.Jet_pt_nom[muon_closest_jetid_temp]))
                muon_closest_jetid.append(muon_closest_jetid_temp)
            else:
                muon_jet_Ptratio.append(
                    1./(1+event.Muon_miniPFRelIso_all[imu]))
                muon_closest_jetid.append(muon_closest_jetid_temp)

        # Main muon loop
        for imu in range(0, event.nMuon):
            # topMVA ID: 1:VLoose 2: Loose 3: Medium 4: Tight
            if (muons[imu].topMVA_ID > 3):
                if (abs(muons[imu].eta) < 2.4 and muons[imu].pt > muon_pt and (abs(muons[imu].dxy) < 0.05) and (abs(muons[imu].dz) < 0.1)):
                    muon_v4_temp.SetPtEtaPhiM(
                        muons[imu].pt, muons[imu].eta, muons[imu].phi, muons[imu].mass)
                    tightMuons.append(muon_v4_temp.Clone())
                    tightMuons_pdgid.append(muons[imu].pdgId)
                    tightMuons_id.append(imu)
            elif (muons[imu].topMVA_ID > 1):
                if (abs(muons[imu].eta) < 2.4 and muons[imu].pt > 10 and (abs(muons[imu].dxy) < 0.05) and (abs(muons[imu].dz) < 0.1)):
                    muon_v4_temp.SetPtEtaPhiM(
                        muons[imu].pt, muons[imu].eta, muons[imu].phi, muons[imu].mass)
                    additional_looseMuons.append(muon_v4_temp.Clone())
                    additional_looseMuons_pdgid.append(muons[imu].pdgId)
                    additional_looseMuons_id.append(imu)

        n_tight_muon = len(tightMuons)
        n_loose_muon = len(additional_looseMuons)

        # noIso muon loop
        for imu in range(0, event.nMuon):
            if (muons[imu].mediumId):
                if (abs(muons[imu].eta) < 2.4 and muons[imu].pt > muon_pt and (abs(muons[imu].dxy) < 0.05) and (abs(muons[imu].dz) < 0.1)):
                    muon_v4_temp.SetPtEtaPhiM(
                        muons[imu].pt, muons[imu].eta, muons[imu].phi, muons[imu].mass)
                    tightMuons_noIso.append(muon_v4_temp.Clone())
                    tightMuons_noIso_pdgid.append(muons[imu].pdgId)
                    tightMuons_noIso_id.append(imu)
            elif (muons[imu].topMVA_ID > 1):
                if (abs(muons[imu].eta) < 2.4 and muons[imu].pt > 10 and (abs(muons[imu].dxy) < 0.05) and (abs(muons[imu].dz) < 0.1)):
                    muon_v4_temp.SetPtEtaPhiM(
                        muons[imu].pt, muons[imu].eta, muons[imu].phi, muons[imu].mass)
                    additional_looseMuons_noIso.append(muon_v4_temp.Clone())
                    additional_looseMuons_noIso_pdgid.append(muons[imu].pdgId)
                    additional_looseMuons_noIso_id.append(imu)
        n_tight_muon_noIso = len(tightMuons_noIso)
        n_loose_muon_noIso = len(additional_looseMuons_noIso)

        self.out.fillBranch("n_tight_muon", n_tight_muon)
        self.out.fillBranch("n_loose_muon", n_loose_muon)
        tightMuons_id.extend(np.zeros(event.nMuon-len(tightMuons_id), int)-1)
        additional_looseMuons_id.extend(
            np.zeros(event.nMuon-len(additional_looseMuons_id), int)-1)
        self.out.fillBranch("tightMuons_id", tightMuons_id)
        self.out.fillBranch("additional_looseMuons_id",
                            additional_looseMuons_id)
        self.out.fillBranch("n_tight_muon_noIso", n_tight_muon_noIso)
        self.out.fillBranch("n_loose_muon_noIso", n_loose_muon_noIso)
        tightMuons_noIso_id.extend(
            np.zeros(event.nMuon-len(tightMuons_noIso_id), int)-1)
        additional_looseMuons_noIso_id.extend(
            np.zeros(event.nMuon-len(additional_looseMuons_noIso_id), int)-1)
        self.out.fillBranch("tightMuons_noIso_id", tightMuons_noIso_id)
        self.out.fillBranch("additional_looseMuons_noIso_id",
                            additional_looseMuons_noIso_id)
        self.out.fillBranch("muon_jet_Ptratio", muon_jet_Ptratio)
        self.out.fillBranch("muon_closest_jetid", muon_closest_jetid)

        # electron selection: tight (veto) cut-based ID + impact parameter cut, with pt > 15 GeV
        electrons = Collection(event, 'Electron')
        electron_v4_temp = TLorentzVector()
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
        electron_closest_jetid_temp = -1

        for iele in range(0, event.nElectron):
            dr_ele_jet = 99.
            electron_v4_temp.SetPtEtaPhiM(
                electrons[iele].pt, electrons[iele].eta, electrons[iele].phi, electrons[iele].mass)
            for ijet in range(0, event.nJet):
                jet_v4_temp.SetPtEtaPhiM(
                    event.Jet_pt_nom[ijet], event.Jet_eta[ijet], event.Jet_phi[ijet], event.Jet_mass_nom[ijet])
                if electron_v4_temp.DeltaR(jet_v4_temp) < dr_ele_jet:
                    dr_ele_jet = electron_v4_temp.DeltaR(jet_v4_temp)
                    electron_closest_jetid_temp = ijet

            if dr_ele_jet < 0.4:
                electron_jet_Ptratio.append(
                    electrons[iele].pt/(0.85*event.Jet_pt_nom[electron_closest_jetid_temp]))
                electron_closest_jetid.append(electron_closest_jetid_temp)
            else:
                electron_jet_Ptratio.append(
                    1./(1+event.Electron_miniPFRelIso_all[iele]))
                electron_closest_jetid.append(electron_closest_jetid_temp)

        # Main electron loop
        for iele in range(0, event.nElectron):
            if (electrons[iele].topMVA_ID > 3):
                if (((abs(electrons[iele].eta+electrons[iele].deltaEtaSC) < 1.4442 and abs(electrons[iele].dxy) < 0.05 and abs(electrons[iele].dz) < 0.1) or (abs(electrons[iele].eta + electrons[iele].deltaEtaSC) > 1.566 and abs(electrons[iele].eta + electrons[iele].deltaEtaSC) < 2.4 and abs(electrons[iele].dxy) < 0.1 and abs(electrons[iele].dz) < 0.2)) and electrons[iele].pt > ele_pt):
                    electron_v4_temp.SetPtEtaPhiM(
                        electrons[iele].pt, electrons[iele].eta, electrons[iele].phi, electrons[iele].mass)
                    tightElectrons.append(electron_v4_temp.Clone())
                    tightElectrons_pdgid.append(electrons[iele].pdgId)
                    tightElectrons_id.append(iele)
            elif (electrons[iele].topMVA_ID > 1):
                if (((abs(electrons[iele].eta+electrons[iele].deltaEtaSC) < 1.4442 and abs(electrons[iele].dxy) < 0.05 and abs(electrons[iele].dz) < 0.1) or (abs(electrons[iele].eta + electrons[iele].deltaEtaSC) > 1.566 and abs(electrons[iele].eta + electrons[iele].deltaEtaSC) < 2.4 and abs(electrons[iele].dxy) < 0.1 and abs(electrons[iele].dz) < 0.2)) and electrons[iele].pt > 10):
                    electron_v4_temp.SetPtEtaPhiM(
                        electrons[iele].pt, electrons[iele].eta, electrons[iele].phi, electrons[iele].mass)
                    additional_vetoElectrons.append(electron_v4_temp.Clone())
                    additional_vetoElectrons_pdgid.append(
                        electrons[iele].pdgId)
                    additional_vetoElectrons_id.append(iele)

        for iele in range(0, event.nElectron):
            if (electrons[iele].mvaFall17V2noIso_WP90):
                if (((abs(electrons[iele].eta+electrons[iele].deltaEtaSC) < 1.4442 and abs(electrons[iele].dxy) < 0.05 and abs(electrons[iele].dz) < 0.1) or (abs(electrons[iele].eta + electrons[iele].deltaEtaSC) > 1.566 and abs(electrons[iele].eta + electrons[iele].deltaEtaSC) < 2.4 and abs(electrons[iele].dxy) < 0.1 and abs(electrons[iele].dz) < 0.2)) and electrons[iele].pt > ele_pt):
                    electron_v4_temp.SetPtEtaPhiM(
                        electrons[iele].pt, electrons[iele].eta, electrons[iele].phi, electrons[iele].mass)
                    tightElectrons_noIso.append(electron_v4_temp.Clone())
                    tightElectrons_noIso_pdgid.append(electrons[iele].pdgId)
                    tightElectrons_noIso_id.append(iele)
            elif (electrons[iele].topMVA_ID > 1):
                if (((abs(electrons[iele].eta+electrons[iele].deltaEtaSC) < 1.4442 and abs(electrons[iele].dxy) < 0.05 and abs(electrons[iele].dz) < 0.1) or (abs(electrons[iele].eta + electrons[iele].deltaEtaSC) > 1.566 and abs(electrons[iele].eta + electrons[iele].deltaEtaSC) < 2.4 and abs(electrons[iele].dxy) < 0.1 and abs(electrons[iele].dz) < 0.2)) and electrons[iele].pt > 10):
                    electron_v4_temp.SetPtEtaPhiM(
                        electrons[iele].pt, electrons[iele].eta, electrons[iele].phi, electrons[iele].mass)
                    additional_vetoElectrons_noIso.append(
                        electron_v4_temp.Clone())
                    additional_vetoElectrons_noIso_pdgid.append(
                        electrons[iele].pdgId)
                    additional_vetoElectrons_noIso_id.append(iele)

        n_tight_ele = len(tightElectrons)
        n_loose_ele = len(additional_vetoElectrons)
        n_tight_ele_noIso = len(tightElectrons_noIso)
        n_loose_ele_noIso = len(additional_vetoElectrons_noIso)

        self.out.fillBranch("n_tight_ele", n_tight_ele)
        self.out.fillBranch("n_loose_ele", n_loose_ele)
        tightElectrons_id.extend(
            np.zeros(event.nElectron-len(tightElectrons_id), int)-1)
        additional_vetoElectrons_id.extend(
            np.zeros(event.nElectron-len(additional_vetoElectrons_id), int)-1)
        self.out.fillBranch("tightElectrons_id", tightElectrons_id)
        self.out.fillBranch("additional_vetoElectrons_id",
                            additional_vetoElectrons_id)
        self.out.fillBranch("n_tight_ele_noIso", n_tight_ele_noIso)
        self.out.fillBranch("n_loose_ele_noIso", n_loose_ele_noIso)
        tightElectrons_noIso_id.extend(
            np.zeros(event.nElectron-len(tightElectrons_noIso_id), int)-1)
        additional_vetoElectrons_noIso_id.extend(
            np.zeros(event.nElectron-len(additional_vetoElectrons_noIso_id), int)-1)
        self.out.fillBranch("tightElectrons_noIso_id", tightElectrons_noIso_id)
        self.out.fillBranch("additional_vetoElectrons_noIso_id",
                            additional_vetoElectrons_noIso_id)
        self.out.fillBranch("electron_jet_Ptratio", electron_jet_Ptratio)
        self.out.fillBranch("electron_closest_jetid", electron_closest_jetid)

        # tight leptons and additional loose leptons collection
        tightLeptons = tightMuons + tightElectrons
        tightLeptons.sort(key=lambda x: x.Pt(), reverse=True)
        looseLeptons = additional_looseMuons + additional_vetoElectrons
        looseLeptons.sort(key=lambda x: x.Pt(), reverse=True)

        tightLeptons_noIso = tightMuons_noIso + tightElectrons_noIso
        tightLeptons_noIso.sort(key=lambda x: x.Pt(), reverse=True)
        looseLeptons_noIso = additional_looseMuons_noIso + additional_vetoElectrons_noIso
        looseLeptons_noIso.sort(key=lambda x: x.Pt(), reverse=True)
        # gkole turn off for revert back to set-I
        '''
    if len(tightLeptons)<1:return False  
    if self.is_mc:
      if event.MET_T1Smear_pt < 30: return False
    else:
      if event.MET_T1_pt < 30: return False
    '''

        #################
        # Tau collection:
        #################
        tau_v4_temp = TLorentzVector()
        taus = Collection(event, 'Tau')
        nHad_tau = 0
        Had_tau_id = []
        for itau in range(0, event.nTau):
            tau_v4_temp.SetPtEtaPhiM(
                taus[itau].pt, taus[itau].eta, taus[itau].phi, taus[itau].mass)
            pass_tau_lep_Dr = 1
            if taus[itau].pt > 20 and abs(taus[itau].eta) < 2.3 and taus[itau].idDecayModeOldDMs and taus[itau].idDeepTau2017v2p1VSe >= 4 and taus[itau].idDeepTau2017v2p1VSjet >= 4 and taus[itau].idDeepTau2017v2p1VSmu >= 1:
                #      if taus[itau].pt>20 and abs(taus[itau].eta)<2.3 and taus[itau].idDecayModeNewDMs and taus[itau].idDeepTau2017v2p1VSe>=4 and taus[itau].idDeepTau2017v2p1VSjet>=4 and taus[itau].idDeepTau2017v2p1VSmu>=1: # use this for non-nanoaodv9
                for ilep in range(0, len(tightLeptons)):
                    if tau_v4_temp.DeltaR(tightLeptons[ilep]) < 0.4:
                        pass_tau_lep_Dr = 0
                if pass_tau_lep_Dr:
                    nHad_tau = nHad_tau+1
                    Had_tau_id.append(itau)
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

        jets = Collection(event, 'Jet')

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
        tightJets_id_in47 = []

        tightJets_b_DeepJetloose_id = []
        tightJets_b_DeepJetmedium_id = []
        tightJets_b_DeepJettight_id = []

        # require DeltaR between Jets and tight leptons greater than 0.4
        jet_v4_all = []
        for ijet in range(0, event.nJet):

            jet_is_tau = 0
            if nHad_tau > 0:
                for ita in Had_tau_id:
                    if ijet == event.Tau_jetIdx[ita]:
                        jet_is_tau = 1
            if jet_is_tau:
                continue

            pass_jet_lep_Dr = 1
            jet_v4_temp.SetPtEtaPhiM(
                event.Jet_pt_nom[ijet], event.Jet_eta[ijet], event.Jet_phi[ijet], event.Jet_mass_nom[ijet])
            for ilep in range(0, len(tightLeptons)):
                if jet_v4_temp.DeltaR(tightLeptons[ilep]) < 0.4:
                    pass_jet_lep_Dr = 0

            if not (pass_jet_lep_Dr > 0):
                continue
            if not (jets[ijet].jetId == 6 and event.Jet_pt_nom[ijet] > 30):
                continue  # tight jets with pT > 30 GeV
            if (event.Jet_pt_nom[ijet] < 50 and not (jets[ijet].puId == 7)):
                continue

            if abs(jets[ijet].eta) < 4.7 and abs(jets[ijet].eta) >= 2.4:
                tightJets_id_in47.append(ijet)
            if abs(jets[ijet].eta) < 2.4:
                tightJets_id_in24.append(ijet)
                jet_v4_all.append(jet_v4_temp.Clone())

                #Taking b-jets
                index_btag_L = bjet_filter(jet, self.year, "L")
                index_btag_M = bjet_filter(jet, self.year, "M")
                index_btag_T = bjet_filter(jet, self.year, "T")
                if index_btag_T > 0: 
                    tightJets_b_DeepJetloose_id.append(index_btag_L)
                    tightJets_b_DeepJetmedium_id.append(index_btag_M)
                    tightJets_b_DeepJettight_id.append(index_btag_T)
                elif index_btag_M > 0:
                    tightJets_b_DeepJetloose_id.append(index_btag_L)
                    tightJets_b_DeepJetmedium_id.append(index_btag_M)
                elif index_btag_L > 0:                    
                    tightJets_b_DeepJetloose_id.append(index_btag_L)


        # HT (sum of all tightjets)
        HT = 0
        for ijet in range(0, len(tightJets_id_in24)):
            HT = HT+event.Jet_pt_nom[tightJets_id_in24[ijet]]
        self.out.fillBranch("HT", HT)

        for ijet in range(0, event.nJet):
            if not (ijet in tightJets_id_in24):
                continue
            if (ijet in tightJets_b_DeepJetmedium_id):
                continue

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

        if n_tight_jet > 3:
            j4_pt = event.Jet_pt_nom[tightJets_id_in24[3]]
            j4_eta = event.Jet_eta[tightJets_id_in24[3]]
            j4_phi = event.Jet_phi[tightJets_id_in24[3]]
            j4_mass = event.Jet_mass_nom[tightJets_id_in24[3]]
            j3_pt = event.Jet_pt_nom[tightJets_id_in24[2]]
            j3_eta = event.Jet_eta[tightJets_id_in24[2]]
            j3_phi = event.Jet_phi[tightJets_id_in24[2]]
            j3_mass = event.Jet_mass_nom[tightJets_id_in24[2]]
            j2_pt = event.Jet_pt_nom[tightJets_id_in24[1]]
            j2_eta = event.Jet_eta[tightJets_id_in24[1]]
            j2_phi = event.Jet_phi[tightJets_id_in24[1]]
            j2_mass = event.Jet_mass_nom[tightJets_id_in24[1]]
            j1_pt = event.Jet_pt_nom[tightJets_id_in24[0]]
            j1_eta = event.Jet_eta[tightJets_id_in24[0]]
            j1_phi = event.Jet_phi[tightJets_id_in24[0]]
            j1_mass = event.Jet_mass_nom[tightJets_id_in24[0]]
            mj1j2 = (jet_v4_all[0]+jet_v4_all[1]).M()
            mj1j3 = (jet_v4_all[0]+jet_v4_all[2]).M()
            mj1j4 = (jet_v4_all[0]+jet_v4_all[3]).M()
            mj2j3 = (jet_v4_all[1]+jet_v4_all[2]).M()
            mj2j4 = (jet_v4_all[1]+jet_v4_all[3]).M()
            mj3j4 = (jet_v4_all[2]+jet_v4_all[3]).M()
            mj1j2j3 = (jet_v4_all[0]+jet_v4_all[1]+jet_v4_all[2]).M()
            mj1j2j4 = (jet_v4_all[0]+jet_v4_all[1]+jet_v4_all[3]).M()
            mj2j3j4 = (jet_v4_all[1]+jet_v4_all[2]+jet_v4_all[3]).M()
            mj1j2j3j4 = (jet_v4_all[0]+jet_v4_all[1] +
                         jet_v4_all[2]+jet_v4_all[3]).M()
            drj1j2 = jet_v4_all[0].DeltaR(jet_v4_all[1])
            drj1j3 = jet_v4_all[0].DeltaR(jet_v4_all[2])
            drj1j4 = jet_v4_all[0].DeltaR(jet_v4_all[3])
            drj2j3 = jet_v4_all[1].DeltaR(jet_v4_all[2])
            drj2j4 = jet_v4_all[1].DeltaR(jet_v4_all[3])
            drj3j4 = jet_v4_all[2].DeltaR(jet_v4_all[3])
        if n_tight_jet == 3:
            j3_pt = event.Jet_pt_nom[tightJets_id_in24[2]]
            j3_eta = event.Jet_eta[tightJets_id_in24[2]]
            j3_phi = event.Jet_phi[tightJets_id_in24[2]]
            j3_mass = event.Jet_mass_nom[tightJets_id_in24[2]]
            j2_pt = event.Jet_pt_nom[tightJets_id_in24[1]]
            j2_eta = event.Jet_eta[tightJets_id_in24[1]]
            j2_phi = event.Jet_phi[tightJets_id_in24[1]]
            j2_mass = event.Jet_mass_nom[tightJets_id_in24[1]]
            j1_pt = event.Jet_pt_nom[tightJets_id_in24[0]]
            j1_eta = event.Jet_eta[tightJets_id_in24[0]]
            j1_phi = event.Jet_phi[tightJets_id_in24[0]]
            j1_mass = event.Jet_mass_nom[tightJets_id_in24[0]]
            mj1j2 = (jet_v4_all[0]+jet_v4_all[1]).M()
            mj1j3 = (jet_v4_all[0]+jet_v4_all[2]).M()
            mj2j3 = (jet_v4_all[1]+jet_v4_all[2]).M()
            mj1j2j3 = (jet_v4_all[0]+jet_v4_all[1]+jet_v4_all[2]).M()
            drj1j2 = jet_v4_all[0].DeltaR(jet_v4_all[1])
            drj1j3 = jet_v4_all[0].DeltaR(jet_v4_all[2])
            drj2j3 = jet_v4_all[1].DeltaR(jet_v4_all[2])
        if n_tight_jet == 2:
            j2_pt = event.Jet_pt_nom[tightJets_id_in24[1]]
            j2_eta = event.Jet_eta[tightJets_id_in24[1]]
            j2_phi = event.Jet_phi[tightJets_id_in24[1]]
            j2_mass = event.Jet_mass_nom[tightJets_id_in24[1]]
            j1_pt = event.Jet_pt_nom[tightJets_id_in24[0]]
            j1_eta = event.Jet_eta[tightJets_id_in24[0]]
            j1_phi = event.Jet_phi[tightJets_id_in24[0]]
            j1_mass = event.Jet_mass_nom[tightJets_id_in24[0]]
            mj1j2 = (jet_v4_all[0]+jet_v4_all[1]).M()
            drj1j2 = jet_v4_all[0].DeltaR(jet_v4_all[1])
        if n_tight_jet == 1:
            j1_pt = event.Jet_pt_nom[tightJets_id_in24[0]]
            j1_eta = event.Jet_eta[tightJets_id_in24[0]]
            j1_phi = event.Jet_phi[tightJets_id_in24[0]]
            j1_mass = event.Jet_mass_nom[tightJets_id_in24[0]]

        if n_bjet_DeepB_loose > 2:
            DeepB_loose_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_eta = event.Jet_eta[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_phi = event.Jet_phi[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j2_pt = event.Jet_pt_nom[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j2_eta = event.Jet_eta[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j2_phi = event.Jet_phi[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j2_mass = event.Jet_mass_nom[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j3_pt = event.Jet_pt_nom[tightJets_b_DeepJetloose_id[2]]
            DeepB_loose_j3_eta = event.Jet_eta[tightJets_b_DeepJetloose_id[2]]
            DeepB_loose_j3_phi = event.Jet_phi[tightJets_b_DeepJetloose_id[2]]
            DeepB_loose_j3_mass = event.Jet_mass_nom[tightJets_b_DeepJetloose_id[2]]
        if n_bjet_DeepB_loose == 2:
            DeepB_loose_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_eta = event.Jet_eta[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_phi = event.Jet_phi[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j2_pt = event.Jet_pt_nom[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j2_eta = event.Jet_eta[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j2_phi = event.Jet_phi[tightJets_b_DeepJetloose_id[1]]
            DeepB_loose_j2_mass = event.Jet_mass_nom[tightJets_b_DeepJetloose_id[1]]
        if n_bjet_DeepB_loose == 1:
            DeepB_loose_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_eta = event.Jet_eta[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_phi = event.Jet_phi[tightJets_b_DeepJetloose_id[0]]
            DeepB_loose_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJetloose_id[0]]

        if n_bjet_DeepB_medium > 2:
            DeepB_medium_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_eta = event.Jet_eta[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_phi = event.Jet_phi[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j2_pt = event.Jet_pt_nom[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j2_eta = event.Jet_eta[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j2_phi = event.Jet_phi[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j2_mass = event.Jet_mass_nom[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j3_pt = event.Jet_pt_nom[tightJets_b_DeepJetmedium_id[2]]
            DeepB_medium_j3_eta = event.Jet_eta[tightJets_b_DeepJetmedium_id[2]]
            DeepB_medium_j3_phi = event.Jet_phi[tightJets_b_DeepJetmedium_id[2]]
            DeepB_medium_j3_mass = event.Jet_mass_nom[tightJets_b_DeepJetmedium_id[2]]
        if n_bjet_DeepB_medium == 2:
            DeepB_medium_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_eta = event.Jet_eta[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_phi = event.Jet_phi[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j2_pt = event.Jet_pt_nom[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j2_eta = event.Jet_eta[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j2_phi = event.Jet_phi[tightJets_b_DeepJetmedium_id[1]]
            DeepB_medium_j2_mass = event.Jet_mass_nom[tightJets_b_DeepJetmedium_id[1]]
        if n_bjet_DeepB_medium == 1:
            DeepB_medium_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_eta = event.Jet_eta[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_phi = event.Jet_phi[tightJets_b_DeepJetmedium_id[0]]
            DeepB_medium_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJetmedium_id[0]]

        if n_bjet_DeepB_tight > 2:
            DeepB_tight_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_eta = event.Jet_eta[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_phi = event.Jet_phi[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j2_pt = event.Jet_pt_nom[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j2_eta = event.Jet_eta[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j2_phi = event.Jet_phi[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j2_mass = event.Jet_mass_nom[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j3_pt = event.Jet_pt_nom[tightJets_b_DeepJettight_id[2]]
            DeepB_tight_j3_eta = event.Jet_eta[tightJets_b_DeepJettight_id[2]]
            DeepB_tight_j3_phi = event.Jet_phi[tightJets_b_DeepJettight_id[2]]
            DeepB_tight_j3_mass = event.Jet_mass_nom[tightJets_b_DeepJettight_id[2]]
        if n_bjet_DeepB_tight == 2:
            DeepB_tight_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_eta = event.Jet_eta[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_phi = event.Jet_phi[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j2_pt = event.Jet_pt_nom[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j2_eta = event.Jet_eta[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j2_phi = event.Jet_phi[tightJets_b_DeepJettight_id[1]]
            DeepB_tight_j2_mass = event.Jet_mass_nom[tightJets_b_DeepJettight_id[1]]
        if n_bjet_DeepB_tight == 1:
            DeepB_tight_j1_pt = event.Jet_pt_nom[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_eta = event.Jet_eta[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_phi = event.Jet_phi[tightJets_b_DeepJettight_id[0]]
            DeepB_tight_j1_mass = event.Jet_mass_nom[tightJets_b_DeepJettight_id[0]]

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
            np.zeros(event.nJet-len(tightJets_id_in24), int)-1)
        tightJets_id_in47.extend(
            np.zeros(event.nJet-len(tightJets_id_in47), int)-1)
        tightJets_b_DeepJetloose_id.extend(
            np.zeros(event.nJet-len(tightJets_b_DeepJetloose_id), int)-1)
        tightJets_b_DeepJetmedium_id.extend(
            np.zeros(event.nJet-len(tightJets_b_DeepJetmedium_id), int)-1)
        tightJets_b_DeepJettight_id.extend(
            np.zeros(event.nJet-len(tightJets_b_DeepJettight_id), int)-1)

        self.out.fillBranch("tightJets_id_in24", tightJets_id_in24)
        self.out.fillBranch("tightJets_id_in47", tightJets_id_in47)
        self.out.fillBranch("tightJets_b_DeepJetloose_id",
                            tightJets_b_DeepJetloose_id)
        self.out.fillBranch("tightJets_b_DeepJetmedium_id",
                            tightJets_b_DeepJetmedium_id)
        self.out.fillBranch("tightJets_b_DeepJettight_id",
                            tightJets_b_DeepJettight_id)

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
            if (n_tight_muon == 1 and tightMuons[0].Pt() > muon_pt) or (n_tight_ele == 1 and tightElectrons[0].Pt() > ele_pt):
                bh_nl = True
        # at least three jets (bjet requirement will applied at plot level)
        if bh_nl and n_tight_jet > 2:
            bh_jets = True

        if bh_nl:
            if self.is_mc:
                bh_met = event.MET_T1Smear_pt
                bh_met_phi = event.MET_T1Smear_phi
            else:
                bh_met = event.MET_T1_pt
                bh_met_phi = event.MET_T1_phi
            if len(tightMuons) == 1:
                bh_region = 1
                bh_l1_id = tightMuons_id[0]
                bh_l1_pdgid = tightMuons_pdgid[0]
                bh_l1_pt = tightMuons[0].Pt()
                bh_l1_eta = tightMuons[0].Eta()
                bh_l1_phi = tightMuons[0].Phi()
                bh_l1_mass = tightMuons[0].M()
            if len(tightElectrons) == 1:
                bh_region = 2
                bh_l1_id = tightElectrons_id[0]
                bh_l1_pdgid = tightElectrons_pdgid[0]
                bh_l1_pt = tightElectrons[0].Pt()
                bh_l1_eta = tightElectrons[0].Eta()
                bh_l1_phi = tightElectrons[0].Phi()
                bh_l1_mass = tightElectrons[0].M()

        # bh_region = 1 i.e, (muon) and bh_region = 2 i.e, (electron)
        if bh_region > 0:
            l1_v4_temp = TLorentzVector()
            l1_v4_temp.SetPtEtaPhiM(bh_l1_pt, bh_l1_eta, bh_l1_phi, bh_l1_mass)
            j1_v4_temp = TLorentzVector()
            j2_v4_temp = TLorentzVector()
            j3_v4_temp = TLorentzVector()
            j4_v4_temp = TLorentzVector()
            b1_v4_temp = TLorentzVector()
            b2_v4_temp = TLorentzVector()
            b3_v4_temp = TLorentzVector()
            if n_tight_jet > 3:
                j1_v4_temp.SetPtEtaPhiM(j1_pt, j1_eta, j1_phi, j1_mass)
                j2_v4_temp.SetPtEtaPhiM(j2_pt, j2_eta, j2_phi, j2_mass)
                j3_v4_temp.SetPtEtaPhiM(j3_pt, j3_eta, j3_phi, j3_mass)
                j4_v4_temp.SetPtEtaPhiM(j4_pt, j4_eta, j4_phi, j4_mass)
                bh_dr_l1j1 = l1_v4_temp.DeltaR(j1_v4_temp)
                bh_dr_l1j2 = l1_v4_temp.DeltaR(j2_v4_temp)
                bh_dr_l1j3 = l1_v4_temp.DeltaR(j3_v4_temp)
                bh_dr_l1j4 = l1_v4_temp.DeltaR(j4_v4_temp)
                bh_mlj1 = (l1_v4_temp+j1_v4_temp).M()
                bh_mlj2 = (l1_v4_temp+j2_v4_temp).M()
                bh_mlj3 = (l1_v4_temp+j3_v4_temp).M()
                bh_mlj4 = (l1_v4_temp+j4_v4_temp).M()
                bh_mlj1j2 = (l1_v4_temp+j1_v4_temp+j2_v4_temp).M()
                bh_mlj1j3 = (l1_v4_temp+j1_v4_temp+j3_v4_temp).M()
                bh_mlj1j4 = (l1_v4_temp+j1_v4_temp+j4_v4_temp).M()
                bh_mlj2j3 = (l1_v4_temp+j2_v4_temp+j3_v4_temp).M()
                bh_mlj2j4 = (l1_v4_temp+j2_v4_temp+j4_v4_temp).M()
                bh_mlj3j4 = (l1_v4_temp+j3_v4_temp+j4_v4_temp).M()
            if n_tight_jet == 3:
                j1_v4_temp.SetPtEtaPhiM(j1_pt, j1_eta, j1_phi, j1_mass)
                j2_v4_temp.SetPtEtaPhiM(j2_pt, j2_eta, j2_phi, j2_mass)
                j3_v4_temp.SetPtEtaPhiM(j3_pt, j3_eta, j3_phi, j3_mass)
                bh_dr_l1j1 = l1_v4_temp.DeltaR(j1_v4_temp)
                bh_dr_l1j2 = l1_v4_temp.DeltaR(j2_v4_temp)
                bh_dr_l1j3 = l1_v4_temp.DeltaR(j3_v4_temp)
                bh_mlj1 = (l1_v4_temp+j1_v4_temp).M()
                bh_mlj2 = (l1_v4_temp+j2_v4_temp).M()
                bh_mlj3 = (l1_v4_temp+j3_v4_temp).M()
                bh_mlj1j2 = (l1_v4_temp+j1_v4_temp+j2_v4_temp).M()
                bh_mlj1j3 = (l1_v4_temp+j1_v4_temp+j3_v4_temp).M()
                bh_mlj2j3 = (l1_v4_temp+j2_v4_temp+j3_v4_temp).M()
            if n_tight_jet == 2:
                j1_v4_temp.SetPtEtaPhiM(j1_pt, j1_eta, j1_phi, j1_mass)
                j2_v4_temp.SetPtEtaPhiM(j2_pt, j2_eta, j2_phi, j2_mass)
                bh_dr_l1j1 = l1_v4_temp.DeltaR(j1_v4_temp)
                bh_dr_l1j2 = l1_v4_temp.DeltaR(j2_v4_temp)
                bh_mlj1 = (l1_v4_temp+j1_v4_temp).M()
                bh_mlj2 = (l1_v4_temp+j2_v4_temp).M()
                bh_mlj1j2 = (l1_v4_temp+j1_v4_temp+j2_v4_temp).M()
            if n_tight_jet == 1:
                j1_v4_temp.SetPtEtaPhiM(j1_pt, j1_eta, j1_phi, j1_mass)
                bh_dr_l1j1 = l1_v4_temp.DeltaR(j1_v4_temp)
                bh_mlj1 = (l1_v4_temp+j1_v4_temp).M()

            if n_bjet_DeepB_medium > 2:
                b1_v4_temp.SetPtEtaPhiM(
                    DeepB_medium_j1_pt, DeepB_medium_j1_eta, DeepB_medium_j1_phi, DeepB_medium_j1_mass)
                b2_v4_temp.SetPtEtaPhiM(
                    DeepB_medium_j2_pt, DeepB_medium_j2_eta, DeepB_medium_j2_phi, DeepB_medium_j2_mass)
                b3_v4_temp.SetPtEtaPhiM(
                    DeepB_medium_j3_pt, DeepB_medium_j3_eta, DeepB_medium_j3_phi, DeepB_medium_j3_mass)
                bh_mlb1 = (l1_v4_temp+b1_v4_temp).M()
                bh_mlb2 = (l1_v4_temp+b2_v4_temp).M()
                bh_mlb3 = (l1_v4_temp+b3_v4_temp).M()
                bh_mlb1b2 = (l1_v4_temp+b1_v4_temp+b2_v4_temp).M()
                bh_mlb1b3 = (l1_v4_temp+b1_v4_temp+b3_v4_temp).M()
                bh_mlb2b3 = (l1_v4_temp+b2_v4_temp+b3_v4_temp).M()
            if n_bjet_DeepB_medium == 2:
                b1_v4_temp.SetPtEtaPhiM(
                    DeepB_medium_j1_pt, DeepB_medium_j1_eta, DeepB_medium_j1_phi, DeepB_medium_j1_mass)
                b2_v4_temp.SetPtEtaPhiM(
                    DeepB_medium_j2_pt, DeepB_medium_j2_eta, DeepB_medium_j2_phi, DeepB_medium_j2_mass)
                bh_mlb1 = (l1_v4_temp+b1_v4_temp).M()
                bh_mlb2 = (l1_v4_temp+b2_v4_temp).M()
                bh_mlb1b2 = (l1_v4_temp+b1_v4_temp+b2_v4_temp).M()
            if n_bjet_DeepB_medium == 1:
                b1_v4_temp.SetPtEtaPhiM(
                    DeepB_medium_j1_pt, DeepB_medium_j1_eta, DeepB_medium_j1_phi, DeepB_medium_j1_mass)
                bh_mlb1 = (l1_v4_temp+b1_v4_temp).M()

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
            if (n_tight_muon_noIso == 1 and tightMuons_noIso[0].Pt() > muon_pt):
                boost_region = 1
                boost_l1_id = tightMuons_noIso_id[0]
                boost_l1_pdgid = tightMuons_noIso_pdgid[0]
                boost_l1_pt = tightMuons_noIso[0].Pt()
                boost_l1_eta = tightMuons_noIso[0].Eta()
                boost_l1_phi = tightMuons_noIso[0].Phi()
                boost_l1_mass = tightMuons_noIso[0].M()
            elif (n_tight_ele_noIso == 1 and tightElectrons_noIso[0].Pt() > ele_pt):
                boost_region = 2
                boost_l1_id = tightElectrons_noIso_id[0]
                boost_l1_pdgid = tightElectrons_noIso_pdgid[0]
                boost_l1_pt = tightElectrons_noIso[0].Pt()
                boost_l1_eta = tightElectrons_noIso[0].Eta()
                boost_l1_phi = tightElectrons_noIso[0].Phi()
                boost_l1_mass = tightElectrons_noIso[0].M()
        if (boost_region > 0):
            if self.is_mc:
                boost_met = event.MET_T1Smear_pt
                boost_met_phi = event.MET_T1Smear_phi
            else:
                boost_met = event.MET_T1_pt
                boost_met_phi = event.MET_T1_phi

        self.out.fillBranch("boost_region", boost_region)
        self.out.fillBranch("boost_l1_id", boost_l1_id)
        self.out.fillBranch("boost_l1_pdgid", boost_l1_pdgid)
        self.out.fillBranch("boost_l1_pt", boost_l1_pt)
        self.out.fillBranch("boost_l1_eta", boost_l1_eta)
        self.out.fillBranch("boost_l1_phi", boost_l1_phi)
        self.out.fillBranch("boost_l1_mass", boost_l1_mass)
        self.out.fillBranch("boost_met", boost_met)
        self.out.fillBranch("boost_met_phi", boost_met_phi)
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
        if len(tightLeptons) == 3 and tightLeptons[1].Pt() > 20 and len(looseLeptons) == 0:
            WZ_nl = True
        # no bjet
        if WZ_nl and tightJets_b_DeepJetmedium_id[0] == -1:
            WZ_nb = True

        # mll>4 regardless the flavor and charge sign
        if WZ_nb and (tightLeptons[0]+tightLeptons[1]).M() > 4 and (tightLeptons[2]+tightLeptons[1]).M() > 4 and (tightLeptons[0]+tightLeptons[2]).M() > 4:
            WZ_leptons = True

        if WZ_leptons and ((self.is_mc and event.MET_T1Smear_pt > 30) or (event.MET_T1_pt > 30 and (not (self.is_mc)))):
            WZ_MET = True

        if WZ_MET:
            if self.is_mc:
                WZ_met = event.MET_T1Smear_pt
            else:
                WZ_met = event.MET_T1_pt
            # 3 muons case
            if len(tightElectrons) == 0 and abs(tightMuons_pdgid[0]+tightMuons_pdgid[1]+tightMuons_pdgid[2]) == 13:
                # two combination 0+2 or 1+2
                if (tightMuons_pdgid[0]-tightMuons_pdgid[1]) == 0:
                    if abs((tightMuons[0]+tightMuons[2]).M()-91.1876) < abs((tightMuons[1]+tightMuons[2]).M()-91.1876) and abs((tightMuons[0]+tightMuons[2]).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[1]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[1]
                        WZ_zl1_pt = tightMuons[0].Pt()
                        WZ_zl1_eta = tightMuons[0].Eta()
                        WZ_zl1_phi = tightMuons[0].Phi()
                        WZ_zl1_mass = tightMuons[0].M()
                        WZ_zl2_pt = tightMuons[2].Pt()
                        WZ_zl2_eta = tightMuons[2].Eta()
                        WZ_zl2_phi = tightMuons[2].Phi()
                        WZ_zl2_mass = tightMuons[2].M()
                        WZ_l3_pt = tightMuons[1].Pt()
                        WZ_l3_eta = tightMuons[1].Eta()
                        WZ_l3_phi = tightMuons[1].Phi()
                        WZ_l3_mass = tightMuons[1].M()
                        WZ_Z_mass = (tightMuons[0]+tightMuons[2]).M()
                        WZ_Z_pt = (tightMuons[0]+tightMuons[2]).Pt()
                        WZ_Z_eta = (tightMuons[0]+tightMuons[2]).Eta()
                        WZ_Z_phi = (tightMuons[0]+tightMuons[2]).Phi()

                    if abs((tightMuons[0]+tightMuons[2]).M()-91.1876) > abs((tightMuons[1]+tightMuons[2]).M()-91.1876) and abs((tightMuons[1]+tightMuons[2]).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[1]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[0]
                        WZ_zl1_pdgid = tightMuons_pdgid[1]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[0]
                        WZ_zl1_pt = tightMuons[1].Pt()
                        WZ_zl1_eta = tightMuons[1].Eta()
                        WZ_zl1_phi = tightMuons[1].Phi()
                        WZ_zl1_mass = tightMuons[1].M()
                        WZ_zl2_pt = tightMuons[2].Pt()
                        WZ_zl2_eta = tightMuons[2].Eta()
                        WZ_zl2_phi = tightMuons[2].Phi()
                        WZ_zl2_mass = tightMuons[2].M()
                        WZ_l3_pt = tightMuons[0].Pt()
                        WZ_l3_eta = tightMuons[0].Eta()
                        WZ_l3_phi = tightMuons[0].Phi()
                        WZ_l3_mass = tightMuons[0].M()
                        WZ_Z_mass = (tightMuons[1]+tightMuons[2]).M()
                        WZ_Z_pt = (tightMuons[1]+tightMuons[2]).Pt()
                        WZ_Z_eta = (tightMuons[1]+tightMuons[2]).Eta()
                        WZ_Z_phi = (tightMuons[1]+tightMuons[2]).Phi()
                # two combination 0+1 or 1+2
                elif (tightMuons_pdgid[0]-tightMuons_pdgid[2]) == 0:
                    if abs((tightMuons[0]+tightMuons[1]).M()-91.1876) < abs((tightMuons[1]+tightMuons[2]).M()-91.1876) and abs((tightMuons[0]+tightMuons[1]).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[1]
                        WZ_wl_id = tightMuons_id[2]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[1]
                        WZ_wl_pdgid = tightMuons_pdgid[2]
                        WZ_zl1_pt = tightMuons[0].Pt()
                        WZ_zl1_eta = tightMuons[0].Eta()
                        WZ_zl1_phi = tightMuons[0].Phi()
                        WZ_zl1_mass = tightMuons[0].M()
                        WZ_zl2_pt = tightMuons[1].Pt()
                        WZ_zl2_eta = tightMuons[1].Eta()
                        WZ_zl2_phi = tightMuons[1].Phi()
                        WZ_zl2_mass = tightMuons[1].M()
                        WZ_l3_pt = tightMuons[2].Pt()
                        WZ_l3_eta = tightMuons[2].Eta()
                        WZ_l3_phi = tightMuons[2].Phi()
                        WZ_l3_mass = tightMuons[2].M()
                        WZ_Z_mass = (tightMuons[0]+tightMuons[1]).M()
                        WZ_Z_pt = (tightMuons[0]+tightMuons[1]).Pt()
                        WZ_Z_eta = (tightMuons[0]+tightMuons[1]).Eta()
                        WZ_Z_phi = (tightMuons[0]+tightMuons[1]).Phi()

                    if abs((tightMuons[0]+tightMuons[1]).M()-91.1876) > abs((tightMuons[1]+tightMuons[2]).M()-91.1876) and abs((tightMuons[1]+tightMuons[2]).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[1]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[0]
                        WZ_zl1_pdgid = tightMuons_pdgid[1]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[0]
                        WZ_zl1_pt = tightMuons[1].Pt()
                        WZ_zl1_eta = tightMuons[1].Eta()
                        WZ_zl1_phi = tightMuons[1].Phi()
                        WZ_zl1_mass = tightMuons[1].M()
                        WZ_zl2_pt = tightMuons[2].Pt()
                        WZ_zl2_eta = tightMuons[2].Eta()
                        WZ_zl2_phi = tightMuons[2].Phi()
                        WZ_zl2_mass = tightMuons[2].M()
                        WZ_l3_pt = tightMuons[0].Pt()
                        WZ_l3_eta = tightMuons[0].Eta()
                        WZ_l3_phi = tightMuons[0].Phi()
                        WZ_l3_mass = tightMuons[0].M()
                        WZ_Z_mass = (tightMuons[1]+tightMuons[2]).M()
                        WZ_Z_pt = (tightMuons[1]+tightMuons[2]).Pt()
                        WZ_Z_eta = (tightMuons[1]+tightMuons[2]).Eta()
                        WZ_Z_phi = (tightMuons[1]+tightMuons[2]).Phi()
                # two combination 0+1 or 0+2
                else:
                    if abs((tightMuons[0]+tightMuons[1]).M()-91.1876) < abs((tightMuons[0]+tightMuons[2]).M()-91.1876) and abs((tightMuons[0]+tightMuons[1]).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[1]
                        WZ_wl_id = tightMuons_id[2]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[1]
                        WZ_wl_pdgid = tightMuons_pdgid[2]
                        WZ_zl1_pt = tightMuons[0].Pt()
                        WZ_zl1_eta = tightMuons[0].Eta()
                        WZ_zl1_phi = tightMuons[0].Phi()
                        WZ_zl1_mass = tightMuons[0].M()
                        WZ_zl2_pt = tightMuons[1].Pt()
                        WZ_zl2_eta = tightMuons[1].Eta()
                        WZ_zl2_phi = tightMuons[1].Phi()
                        WZ_zl2_mass = tightMuons[1].M()
                        WZ_l3_pt = tightMuons[2].Pt()
                        WZ_l3_eta = tightMuons[2].Eta()
                        WZ_l3_phi = tightMuons[2].Phi()
                        WZ_l3_mass = tightMuons[2].M()
                        WZ_Z_mass = (tightMuons[0]+tightMuons[1]).M()
                        WZ_Z_pt = (tightMuons[0]+tightMuons[1]).Pt()
                        WZ_Z_eta = (tightMuons[0]+tightMuons[1]).Eta()
                        WZ_Z_phi = (tightMuons[0]+tightMuons[1]).Phi()
                    if abs((tightMuons[0]+tightMuons[1]).M()-91.1876) > abs((tightMuons[0]+tightMuons[2]).M()-91.1876) and abs((tightMuons[0]+tightMuons[2]).M()-91.1876) < 15:
                        WZ_region = 1
                        WZ_zl1_id = tightMuons_id[0]
                        WZ_zl2_id = tightMuons_id[2]
                        WZ_wl_id = tightMuons_id[1]
                        WZ_zl1_pdgid = tightMuons_pdgid[0]
                        WZ_zl2_pdgid = tightMuons_pdgid[2]
                        WZ_wl_pdgid = tightMuons_pdgid[1]
                        WZ_zl1_pt = tightMuons[0].Pt()
                        WZ_zl1_eta = tightMuons[0].Eta()
                        WZ_zl1_phi = tightMuons[0].Phi()
                        WZ_zl1_mass = tightMuons[0].M()
                        WZ_zl2_pt = tightMuons[2].Pt()
                        WZ_zl2_eta = tightMuons[2].Eta()
                        WZ_zl2_phi = tightMuons[2].Phi()
                        WZ_zl2_mass = tightMuons[2].M()
                        WZ_l3_pt = tightMuons[1].Pt()
                        WZ_l3_eta = tightMuons[1].Eta()
                        WZ_l3_phi = tightMuons[1].Phi()
                        WZ_l3_mass = tightMuons[1].M()
                        WZ_Z_mass = (tightMuons[0]+tightMuons[2]).M()
                        WZ_Z_pt = (tightMuons[0]+tightMuons[2]).Pt()
                        WZ_Z_eta = (tightMuons[0]+tightMuons[2]).Eta()
                        WZ_Z_phi = (tightMuons[0]+tightMuons[2]).Phi()

            # 2 muons case
            if len(tightElectrons) == 1 and (tightMuons_pdgid[0]-tightMuons_pdgid[1]) == 0:
                if abs((tightMuons[0]+tightMuons[1]).M()-91.1876) < 15:
                    WZ_region = 2
                    WZ_zl1_id = tightMuons_id[0]
                    WZ_zl2_id = tightMuons_id[1]
                    WZ_wl_id = tightElectrons_id[0]
                    WZ_zl1_pdgid = tightMuons_pdgid[0]
                    WZ_zl2_pdgid = tightMuons_pdgid[1]
                    WZ_wl_pdgid = tightElectrons_pdgid[0]
                    WZ_zl1_pt = tightMuons[0].Pt()
                    WZ_zl1_eta = tightMuons[0].Eta()
                    WZ_zl1_phi = tightMuons[0].Phi()
                    WZ_zl1_mass = tightMuons[0].M()
                    WZ_zl2_pt = tightMuons[1].Pt()
                    WZ_zl2_eta = tightMuons[1].Eta()
                    WZ_zl2_phi = tightMuons[1].Phi()
                    WZ_zl2_mass = tightMuons[1].M()
                    WZ_l3_pt = tightElectrons[0].Pt()
                    WZ_l3_eta = tightElectrons[0].Eta()
                    WZ_l3_phi = tightElectrons[0].Phi()
                    WZ_l3_mass = tightElectrons[0].M()
                    WZ_Z_mass = (tightMuons[0]+tightMuons[1]).M()
                    WZ_Z_pt = (tightMuons[0]+tightMuons[1]).Pt()
                    WZ_Z_eta = (tightMuons[0]+tightMuons[1]).Eta()
                    WZ_Z_phi = (tightMuons[0]+tightMuons[1]).Phi()

            # 1 muon case
            if len(tightElectrons) == 2 and (tightElectrons_pdgid[0]-tightElectrons_pdgid[1]) == 0:
                if abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) < 15:
                    WZ_region = 3
                    WZ_zl1_id = tightElectrons_id[0]
                    WZ_zl2_id = tightElectrons_id[1]
                    WZ_wl_id = tightMuons_id[0]
                    WZ_zl1_pdgid = tightElectrons_pdgid[0]
                    WZ_zl2_pdgid = tightElectrons_pdgid[1]
                    WZ_wl_pdgid = tightMuons_pdgid[0]
                    WZ_zl1_pt = tightElectrons[0].Pt()
                    WZ_zl1_eta = tightElectrons[0].Eta()
                    WZ_zl1_phi = tightElectrons[0].Phi()
                    WZ_zl1_mass = tightElectrons[0].M()
                    WZ_zl2_pt = tightElectrons[1].Pt()
                    WZ_zl2_eta = tightElectrons[1].Eta()
                    WZ_zl2_phi = tightElectrons[1].Phi()
                    WZ_zl2_mass = tightElectrons[1].M()
                    WZ_l3_pt = tightMuons[0].Pt()
                    WZ_l3_eta = tightMuons[0].Eta()
                    WZ_l3_phi = tightMuons[0].Phi()
                    WZ_l3_mass = tightMuons[0].M()
                    WZ_Z_mass = (tightElectrons[0]+tightElectrons[1]).M()
                    WZ_Z_pt = (tightElectrons[0]+tightElectrons[1]).Pt()
                    WZ_Z_eta = (tightElectrons[0]+tightElectrons[1]).Eta()
                    WZ_Z_phi = (tightElectrons[0]+tightElectrons[1]).Phi()

            # 0 muon case
            if len(tightElectrons) == 3 and abs(tightElectrons_pdgid[0]+tightElectrons_pdgid[1]+tightElectrons_pdgid[2]) == 11:
                # two combination 0+2 or 1+2
                if (tightElectrons_pdgid[0]-tightElectrons_pdgid[1]) == 0:
                    if abs((tightElectrons[0]+tightElectrons[2]).M()-91.1876) < abs((tightElectrons[1]+tightElectrons[2]).M()-91.1876) and abs((tightElectrons[0]+tightElectrons[2]).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[1]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[1]
                        WZ_zl1_pt = tightElectrons[0].Pt()
                        WZ_zl1_eta = tightElectrons[0].Eta()
                        WZ_zl1_phi = tightElectrons[0].Phi()
                        WZ_zl1_mass = tightElectrons[0].M()
                        WZ_zl2_pt = tightElectrons[2].Pt()
                        WZ_zl2_eta = tightElectrons[2].Eta()
                        WZ_zl2_phi = tightElectrons[2].Phi()
                        WZ_zl2_mass = tightElectrons[2].M()
                        WZ_l3_pt = tightElectrons[1].Pt()
                        WZ_l3_eta = tightElectrons[1].Eta()
                        WZ_l3_phi = tightElectrons[1].Phi()
                        WZ_l3_mass = tightElectrons[1].M()
                        WZ_Z_mass = (tightElectrons[0]+tightElectrons[2]).M()
                        WZ_Z_pt = (tightElectrons[0]+tightElectrons[2]).Pt()
                        WZ_Z_eta = (tightElectrons[0]+tightElectrons[2]).Eta()
                        WZ_Z_phi = (tightElectrons[0]+tightElectrons[2]).Phi()
                    if abs((tightElectrons[0]+tightElectrons[2]).M()-91.1876) > abs((tightElectrons[1]+tightElectrons[2]).M()-91.1876) and abs((tightElectrons[1]+tightElectrons[2]).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[1]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[0]
                        WZ_zl1_pdgid = tightElectrons_pdgid[1]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[0]
                        WZ_zl1_pt = tightElectrons[1].Pt()
                        WZ_zl1_eta = tightElectrons[1].Eta()
                        WZ_zl1_phi = tightElectrons[1].Phi()
                        WZ_zl1_mass = tightElectrons[1].M()
                        WZ_zl2_pt = tightElectrons[2].Pt()
                        WZ_zl2_eta = tightElectrons[2].Eta()
                        WZ_zl2_phi = tightElectrons[2].Phi()
                        WZ_zl2_mass = tightElectrons[2].M()
                        WZ_l3_pt = tightElectrons[0].Pt()
                        WZ_l3_eta = tightElectrons[0].Eta()
                        WZ_l3_phi = tightElectrons[0].Phi()
                        WZ_l3_mass = tightElectrons[0].M()
                        WZ_Z_mass = (tightElectrons[1]+tightElectrons[2]).M()
                        WZ_Z_pt = (tightElectrons[1]+tightElectrons[2]).Pt()
                        WZ_Z_eta = (tightElectrons[1]+tightElectrons[2]).Eta()
                        WZ_Z_phi = (tightElectrons[1]+tightElectrons[2]).Phi()
                # two combination 0+1 or 1+2
                elif (tightElectrons_pdgid[0]-tightElectrons_pdgid[2]) == 0:
                    if abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) < abs((tightElectrons[1]+tightElectrons[2]).M()-91.1876) and abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[1]
                        WZ_wl_id = tightElectrons_id[2]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[1]
                        WZ_wl_pdgid = tightElectrons_pdgid[2]
                        WZ_zl1_pt = tightElectrons[0].Pt()
                        WZ_zl1_eta = tightElectrons[0].Eta()
                        WZ_zl1_phi = tightElectrons[0].Phi()
                        WZ_zl1_mass = tightElectrons[0].M()
                        WZ_zl2_pt = tightElectrons[1].Pt()
                        WZ_zl2_eta = tightElectrons[1].Eta()
                        WZ_zl2_phi = tightElectrons[1].Phi()
                        WZ_zl2_mass = tightElectrons[1].M()
                        WZ_l3_pt = tightElectrons[2].Pt()
                        WZ_l3_eta = tightElectrons[2].Eta()
                        WZ_l3_phi = tightElectrons[2].Phi()
                        WZ_l3_mass = tightElectrons[2].M()
                        WZ_Z_mass = (tightElectrons[0]+tightElectrons[1]).M()
                        WZ_Z_pt = (tightElectrons[0]+tightElectrons[1]).Pt()
                        WZ_Z_eta = (tightElectrons[0]+tightElectrons[1]).Eta()
                        WZ_Z_phi = (tightElectrons[0]+tightElectrons[1]).Phi()
                    if abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) > abs((tightElectrons[1]+tightElectrons[2]).M()-91.1876) and abs((tightElectrons[1]+tightElectrons[2]).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[1]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[0]
                        WZ_zl1_pdgid = tightElectrons_pdgid[1]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[0]
                        WZ_zl1_pt = tightElectrons[1].Pt()
                        WZ_zl1_eta = tightElectrons[1].Eta()
                        WZ_zl1_phi = tightElectrons[1].Phi()
                        WZ_zl1_mass = tightElectrons[1].M()
                        WZ_zl2_pt = tightElectrons[2].Pt()
                        WZ_zl2_eta = tightElectrons[2].Eta()
                        WZ_zl2_phi = tightElectrons[2].Phi()
                        WZ_zl2_mass = tightElectrons[2].M()
                        WZ_l3_pt = tightElectrons[0].Pt()
                        WZ_l3_eta = tightElectrons[0].Eta()
                        WZ_l3_phi = tightElectrons[0].Phi()
                        WZ_l3_mass = tightElectrons[0].M()
                        WZ_Z_mass = (tightElectrons[1]+tightElectrons[2]).M()
                        WZ_Z_pt = (tightElectrons[1]+tightElectrons[2]).Pt()
                        WZ_Z_eta = (tightElectrons[1]+tightElectrons[2]).Eta()
                        WZ_Z_phi = (tightElectrons[1]+tightElectrons[2]).Phi()
                # two combination 0+1 or 0+2
                else:
                    if abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) < abs((tightElectrons[0]+tightElectrons[2]).M()-91.1876) and abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[1]
                        WZ_wl_id = tightElectrons_id[2]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[1]
                        WZ_wl_pdgid = tightElectrons_pdgid[2]
                        WZ_zl1_pt = tightElectrons[0].Pt()
                        WZ_zl1_eta = tightElectrons[0].Eta()
                        WZ_zl1_phi = tightElectrons[0].Phi()
                        WZ_zl1_mass = tightElectrons[0].M()
                        WZ_zl2_pt = tightElectrons[1].Pt()
                        WZ_zl2_eta = tightElectrons[1].Eta()
                        WZ_zl2_phi = tightElectrons[1].Phi()
                        WZ_zl2_mass = tightElectrons[1].M()
                        WZ_l3_pt = tightElectrons[2].Pt()
                        WZ_l3_eta = tightElectrons[2].Eta()
                        WZ_l3_phi = tightElectrons[2].Phi()
                        WZ_l3_mass = tightElectrons[2].M()
                        WZ_Z_mass = (tightElectrons[0]+tightElectrons[1]).M()
                        WZ_Z_pt = (tightElectrons[0]+tightElectrons[1]).Pt()
                        WZ_Z_eta = (tightElectrons[0]+tightElectrons[1]).Eta()
                        WZ_Z_phi = (tightElectrons[0]+tightElectrons[1]).Phi()
                    if abs((tightElectrons[0]+tightElectrons[1]).M()-91.1876) > abs((tightElectrons[0]+tightElectrons[2]).M()-91.1876) and abs((tightElectrons[0]+tightElectrons[2]).M()-91.1876) < 15:
                        WZ_region = 4
                        WZ_zl1_id = tightElectrons_id[0]
                        WZ_zl2_id = tightElectrons_id[2]
                        WZ_wl_id = tightElectrons_id[1]
                        WZ_zl1_pdgid = tightElectrons_pdgid[0]
                        WZ_zl2_pdgid = tightElectrons_pdgid[2]
                        WZ_wl_pdgid = tightElectrons_pdgid[1]
                        WZ_zl1_pt = tightElectrons[0].Pt()
                        WZ_zl1_eta = tightElectrons[0].Eta()
                        WZ_zl1_phi = tightElectrons[0].Phi()
                        WZ_zl1_mass = tightElectrons[0].M()
                        WZ_zl2_pt = tightElectrons[2].Pt()
                        WZ_zl2_eta = tightElectrons[2].Eta()
                        WZ_zl2_phi = tightElectrons[2].Phi()
                        WZ_zl2_mass = tightElectrons[2].M()
                        WZ_l3_pt = tightElectrons[1].Pt()
                        WZ_l3_eta = tightElectrons[1].Eta()
                        WZ_l3_phi = tightElectrons[1].Phi()
                        WZ_l3_mass = tightElectrons[1].M()
                        WZ_Z_mass = (tightElectrons[0]+tightElectrons[2]).M()
                        WZ_Z_pt = (tightElectrons[0]+tightElectrons[2]).Pt()
                        WZ_Z_eta = (tightElectrons[0]+tightElectrons[2]).Eta()
                        WZ_Z_phi = (tightElectrons[0]+tightElectrons[2]).Phi()

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
        if len(tightLeptons) == 2 and tightLeptons[1].Pt() > 20 and len(looseLeptons) == 0:
            DY_nl = True
        if DY_nl:
            # 2 muons case
            if len(tightElectrons) == 0 and abs(tightMuons_pdgid[0]+tightMuons_pdgid[1]) == 0:
                DY_region = 1
                DY_l1_id = tightMuons_id[0]
                DY_l2_id = tightMuons_id[1]
                DY_l1_pdgid = tightMuons_pdgid[0]
                DY_l2_pdgid = tightMuons_pdgid[1]
                DY_l1_pt = tightMuons[0].Pt()
                DY_l1_eta = tightMuons[0].Eta()
                DY_l1_phi = tightMuons[0].Phi()
                DY_l1_mass = tightMuons[0].M()
                DY_l2_pt = tightMuons[1].Pt()
                DY_l2_eta = tightMuons[1].Eta()
                DY_l2_phi = tightMuons[1].Phi()
                DY_l2_mass = tightMuons[1].M()
                DY_z_mass = (tightLeptons[0]+tightLeptons[1]).M()
                DY_z_pt = (tightLeptons[0]+tightLeptons[1]).Pt()
                DY_z_eta = (tightLeptons[0]+tightLeptons[1]).Eta()
                DY_z_phi = (tightLeptons[0]+tightLeptons[1]).Phi()
                DY_drll = tightLeptons[0].DeltaR(tightLeptons[1])
            # 2 eles case
            if len(tightElectrons) == 2 and abs(tightElectrons_pdgid[0]+tightElectrons_pdgid[1]) == 0:
                DY_region = 3
                DY_l1_id = tightElectrons_id[0]
                DY_l2_id = tightElectrons_id[1]
                DY_l1_pdgid = tightElectrons_pdgid[0]
                DY_l2_pdgid = tightElectrons_pdgid[1]
                DY_l1_pt = tightElectrons[0].Pt()
                DY_l1_eta = tightElectrons[0].Eta()
                DY_l1_phi = tightElectrons[0].Phi()
                DY_l1_mass = tightElectrons[0].M()
                DY_l2_pt = tightElectrons[1].Pt()
                DY_l2_eta = tightElectrons[1].Eta()
                DY_l2_phi = tightElectrons[1].Phi()
                DY_l2_mass = tightElectrons[1].M()
                DY_z_mass = (tightLeptons[0]+tightLeptons[1]).M()
                DY_z_pt = (tightLeptons[0]+tightLeptons[1]).Pt()
                DY_z_eta = (tightLeptons[0]+tightLeptons[1]).Eta()
                DY_z_phi = (tightLeptons[0]+tightLeptons[1]).Phi()
                DY_drll = tightLeptons[0].DeltaR(tightLeptons[1])
            # 1 ele case
            if len(tightElectrons) == 1 and (sign(tightMuons_pdgid[0])+sign(tightElectrons_pdgid[0])) == 0:
                DY_region = 2
                DY_l1_id = tightMuons_id[0]
                DY_l2_id = tightElectrons_id[0]
                DY_l1_pdgid = tightMuons_pdgid[0]
                DY_l2_pdgid = tightElectrons_pdgid[0]
                DY_l1_pt = tightMuons[0].Pt()
                DY_l1_eta = tightMuons[0].Eta()
                DY_l1_phi = tightMuons[0].Phi()
                DY_l1_mass = tightMuons[0].M()
                DY_l2_pt = tightElectrons[0].Pt()
                DY_l2_eta = tightElectrons[0].Eta()
                DY_l2_phi = tightElectrons[0].Phi()
                DY_l2_mass = tightElectrons[0].M()
                DY_z_mass = (tightLeptons[0]+tightLeptons[1]).M()
                DY_z_pt = (tightLeptons[0]+tightLeptons[1]).Pt()
                DY_z_eta = (tightLeptons[0]+tightLeptons[1]).Eta()
                DY_z_phi = (tightLeptons[0]+tightLeptons[1]).Phi()
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

        if not (bh_nl or WZ_region > 0 or DY_region > 0 or boost_region > 0):
            return False

        return True


def BH2016apv(): return BHProducer("2016apv")
def BH2016(): return BHProducer("2016")
def BH2017(): return BHProducer("2017")
def BH2018(): return BHProducer("2018")
