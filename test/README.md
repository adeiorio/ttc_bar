# To do a local run:

##for MC
```
python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test/localrun.py -m -i $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test/DY.root --year 2017 -o $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test -n 100
```

##for data
```
python $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test/localrun.py -i /eos/cms/store/group/phys_top/ExtraYukawa/input_for_tests/test_nanoAOD_Single\
EG_Run2017B.root --year 2017b -o $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test -n 10000

```
