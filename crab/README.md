# Crab submission for ``bHplus/TTC`` on data/MC/signal samples

## Instruction for bHplus crab submission:

First check [mc_cfg.py](https://github.com/ExtraYukawa/ttc_bar/blob/lxplus-9/crab/mc_cfg.py) anf [data_cfg.py](https://github.com/ExtraYukawa/ttc_bar/blob/xplus-9/crab/data_cfg.py) files. Put proper paths like below (output store location)

``config.Data.outLFNDirBase = '/store/group/phys_b2g/ExYukawa/bHplus/2017/'``

### Run for configuration files:
```
python3 create_crab_bhplus.py <2016apv/2016/2017/2018>
```

### Run for prepare the area for submission (within crab sandbox limit 120MB) 
``python3 crab_submission_preparation.py on``

### Do crab submissions etc and then once all jobs are submitted
``python3 crab_submission_preparation.py off``

### Write crab output files
In case you need to have a txt file with the list of root files produced by crab, you can use the `check_crab_status.py` macro, by doing:
```
python3 check_crab_status.py --getout
```

### Merging root file on condor
Once txt files are produced, root files can be merged, by doing:
```
python3 condor_merging.py -e ERA -f FOLDER_VERSION
```


## TTC instructions (Have NOT tested yet in python3)
run create_crab to set up crab configs:
python create_crab.py 2016apv

python create_crab.py 2016

python create_crab.py 2017

python create_crab.py 2018
