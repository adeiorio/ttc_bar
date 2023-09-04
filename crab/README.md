# Crab submission for TTC/BHplus on data/MC/signal samples

## Instruction for BHplus crab submission:

First check [mc_cfg.py](https://github.com/gourangakole/ttc_bar/blob/lep_mvaID/crab/mc_cfg.py) anf [data_cfg.py](https://github.com/gourangakole/ttc_bar/blob/lep_mvaID/crab/data_cfg.py) files. Put proper paths like below (output store location)
``config.Data.outLFNDirBase = '/store/group/phys_top/ExtraYukawa/BHplus/2017/'``

### Run for configuration files:
```
python create_crab_bhplus.py <2016apv/2016/2017/2018>
```

### Run for prepare the area for submission (within crab sandbox limit 120MB) 
``python crab_submission_preparation.py on``

### Do crab submissions etc and then once all jobs are submitted
``python crab_submission_preparation.py off``




## TTC instructions
run create_crab to set up crab configs:
python create_crab.py 2016apv

python create_crab.py 2016

python create_crab.py 2017

python create_crab.py 2018
