from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
import ROOT
import os
from itertools import chain
from correctionlib import _core
ROOT.PyConfig.IgnoreCommandLineOptions = True


def is_relevant_syst_for_shape_corr(flavor_btv, syst, jesSystsForShape=["jes"]):
    """Returns true if a flavor/syst combination is relevant"""
    jesSysts = list(chain(*[("up_" + j, "down_" + j)
                            for j in jesSystsForShape]))

    if flavor_btv == 5:
        return syst in ["central",
                        "up_lf", "down_lf",
                        "up_hfstats1", "down_hfstats1",
                        "up_hfstats2", "down_hfstats2"] + jesSysts
    elif flavor_btv == 4:
        return syst in ["central",
                        "up_cferr1", "down_cferr1",
                        "up_cferr2", "down_cferr2"]
    elif flavor_btv == 0:
        return syst in ["central",
                        "up_hf", "down_hf",
                        "up_lfstats1", "down_lfstats1",
                        "up_lfstats2", "down_lfstats2"] + jesSysts
    else:
        raise ValueError("ERROR: Undefined flavor = %i!!" % flavor_btv)
    return True


class btagSFProducer(Module):
    """Calculate btagging scale factors
    """

    def __init__(
            self, era, algo='deepJet', WPs="all",
            sfFileName=None, verbose=0, jesSystsForShape=["jes"]
    ):
        self.era = era
        self.algo = algo
        if WPs == "fixed":
            self.selectedWPs = ["L", "M", "T"]
        elif WPs == "shape":
            self.selectedWPs = ["shape_corr"]
        else:
            self.selectedWPs = ["L", "M", "T", "shape_corr"]
        self.verbose = verbose
        self.jesSystsForShape = jesSystsForShape
        self.btvjson = _core.CorrectionSet.from_file(os.path.join("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/", self.era, "btagging.json.gz"))
        # in case jet abs(eta) > 2.4 !!
        self.max_abs_eta = 2.4
        # define measurement type for each flavor
        self.measurement_types = None
        self.supported_wp = None
        supported_btagSF = {
            'deepJet': {
                '2016preVFP_UL': {
                    'measurement_types': {
                        5: "comb",  # b
                        4: "comb",  # c
                        0: "incl"   # light
                    },
                    'supported_wp': ["L", "M", "T", "shape_corr"]
                },
                '2016postVFP_UL': {
                    'measurement_types': {
                        5: "comb",  # b
                        4: "comb",  # c
                        0: "incl"   # light
                    },
                    'supported_wp': ["L", "M", "T", "shape_corr"]
                },
                '2017_UL': {
                    'measurement_types': {
                        5: "comb",  # b
                        4: "comb",  # c
                        0: "incl"   # light
                    },
                    'supported_wp': ["L", "M", "T", "shape_corr"]
                },
                '2018_UL': {
                    'measurement_types': {
                        5: "comb",  # b
                        4: "comb",  # c
                        0: "incl"   # light
                    },
                    'supported_wp': ["L", "M", "T", "shape_corr"]
                },
            },
        }

        supported_algos = []
        for algo in list(supported_btagSF.keys()):
            if self.era in list(supported_btagSF[algo].keys()):
                supported_algos.append(algo)
        if self.algo in list(supported_btagSF.keys()):
            if self.era in list(supported_btagSF[self.algo].keys()):
                self.measurement_types = supported_btagSF[self.algo][self.era]['measurement_types']
                self.supported_wp = supported_btagSF[self.algo][self.era]['supported_wp']
            else:
                raise ValueError("ERROR: Algorithm '%s' not supported for era = '%s'! Please choose among { %s }." % (
                    self.algo, self.era, supported_algos))
        else:
            raise ValueError("ERROR: Algorithm '%s' not supported for era = '%s'! Please choose among { %s }." % (
                self.algo, self.era, supported_algos))
        for wp in self.selectedWPs:
            if wp not in self.supported_wp:
                raise ValueError("ERROR: Working point '%s' not supported for algo = '%s' and era = '%s'! Please choose among { %s }." % (
                    wp, self.algo, self.era, self.supported_wp))

        # define systematic uncertainties
        self.systs = []
        self.systs.append("up")
        self.systs.append("down")
        self.central_and_systs = ["central"]
        self.central_and_systs.extend(self.systs)

        self.systs_shape_corr = []
        for syst in ['lf', 'hf',
                     'hfstats1', 'hfstats2',
                     'lfstats1', 'lfstats2',
                     'cferr1', 'cferr2'] + self.jesSystsForShape:
            self.systs_shape_corr.append("up_%s" % syst)
            self.systs_shape_corr.append("down_%s" % syst)
        self.central_and_systs_shape_corr = ["central"]
        self.central_and_systs_shape_corr.extend(self.systs_shape_corr)

        self.branchNames_central_and_systs = {}
        for wp in self.selectedWPs:
            branchNames = {}
            if wp == 'shape_corr':
                central_and_systs = self.central_and_systs_shape_corr
                baseBranchName = 'Jet_btagSF_{}_shape'.format(self.algo)
            else:
                central_and_systs = self.central_and_systs
                baseBranchName = 'Jet_btagSF_{}_{}'.format(self.algo, wp)
            for central_or_syst in central_and_systs:
                if central_or_syst == "central":
                    branchNames[central_or_syst] = baseBranchName
                else:
                    branchNames[central_or_syst] = baseBranchName + \
                        '_' + central_or_syst
            self.branchNames_central_and_systs[wp] = branchNames

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for central_or_syst in list(self.branchNames_central_and_systs.values()):
            for branch in list(central_or_syst.values()):
                self.out.branch(branch, "F", lenVar="nJet")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getSFs(self, jet_data, syst, wp, measurement_type='auto', shape_corr=False):
        for idx, (pt, eta, flavor_btv, discr) in enumerate(jet_data):
            epsilon = 1.e-3
            max_abs_eta = self.max_abs_eta
            if eta <= -max_abs_eta:
                eta = -max_abs_eta + epsilon
            if eta >= +max_abs_eta:
                eta = +max_abs_eta - epsilon
            # evaluate SF
            sf = None
            if shape_corr:
                reader = self.btvjson["%s_%s" %(self.algo, "shape")]
                if is_relevant_syst_for_shape_corr(flavor_btv, syst, self.jesSystsForShape):
                    sf = reader.evaluate(syst, flavor_btv, abs(eta), pt, discr)
                else:
                    sf = reader.evaluate("central", flavor_btv, abs(eta), pt, discr)
            else:
                reader = self.btvjson["%s_%s" %(self.algo, self.measurement_types[flavor_btv])]
                sf = reader.evaluate(syst, wp, flavor_btv, abs(eta), pt)
            # check if SF is OK
            if sf < 0.01:
                if self.verbose > 0:
                    print("jet #%i: pT = %1.1f, eta = %1.1f, discr = %1.3f, flavor = %i" % (
                        idx, pt, eta, discr, flavor_btv))
                sf = 1.
            yield sf

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets = Collection(event, "Jet")
        discr = None
        if self.algo == "deepJet":
            discr = "btagDeepFlavB"
        else:
            raise ValueError("ERROR: Invalid algorithm '%s'!" % self.algo)

        preloaded_jets = [(jet.pt, jet.eta, jet.hadronFlavour, getattr(jet, discr)) for jet in jets]
        for wp in self.selectedWPs:
            isShape = (wp == 'shape_corr')
            central_and_systs = (
                self.central_and_systs_shape_corr if isShape else self.central_and_systs)
            for central_or_syst in central_and_systs:
                scale_factors = list(self.getSFs(
                    preloaded_jets, central_or_syst, wp, 'auto', isShape))
                self.out.fillBranch(
                    self.branchNames_central_and_systs[wp][central_or_syst], scale_factors)

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
btagSF2016ULapv = lambda: btagSFProducer("2016preVFP_UL", "deepJet", "all")
btagSF2016UL = lambda: btagSFProducer("2016postVFP_UL", "deepJet", "all")
btagSF2017UL = lambda: btagSFProducer("2017_UL", "deepJet", "all")
btagSF2018UL = lambda: btagSFProducer("2018_UL", "deepJet", "all")
