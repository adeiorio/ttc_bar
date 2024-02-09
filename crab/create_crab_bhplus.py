#last used:
# python create_crab_bhplus.py 2017
#
import os, sys, json
from shutil import copyfile

year = sys.argv[1]
#sampletype =  #tofix

if year=='2016apv':
  if os.path.isdir('bhplus_config_crab_2016apv') is False:
      os.system('mkdir bhplus_config_crab_2016apv')
  workdir='bhplus_config_crab_2016apv/'
  datajson='Cert_271036-284044_13TeV_Legacy2016_Collisions16_preVPF_JSON.txt'
  samplejson='bhplus_samples2016apv.json'
  scriptpath='2016apv_script'

if year=='2016':
  if os.path.isdir('bhplus_config_crab_2016') is False:
      os.system('mkdir bhplus_config_crab_2016')
  workdir='bhplus_config_crab_2016/'
  datajson='Cert_271036-284044_13TeV_Legacy2016_Collisions16_postVPF_JSON.txt'
  samplejson='bhplus_samples2016.json'
  scriptpath='2016_script'

if year=='2017':
  if os.path.isdir('bhplus_config_crab_2017') is False:
      os.system('mkdir bhplus_config_crab_2017')
  workdir='bhplus_config_crab_2017/'
  datajson='Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
  samplejson='bhplus_samples2017.json'
  scriptpath='2017_script'

if year=='2018':
  if os.path.isdir('bhplus_config_crab_2018') is False:
      os.system('mkdir bhplus_config_crab_2018')
  workdir='bhplus_config_crab_2018/'
  datajson='Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
  samplejson='bhplus_samples2018.json'
  scriptpath='2018_script'

if not os.path.exists(scriptpath):
  os.mkdirs(scriptpath)

# Create file inside <YEAR_script> (e.g. 2017_script) from template file

#for data only need to create different eras
if year == '2016apv':
  #MC
  copyfile('template/crab_script_bhplus.sh',year+'_script/crab_script_bhplus.sh')
  os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %('2016a', year+'_script/crab_script_bhplus.sh'))
  # change permission of the newly created file
  os.system("chmod 755 "+year+'_script/crab_script_bhplus.sh')

  #Data
  for subERA in ["B","C","D","E","F"]: #2016apv has B,C,D,E,F eras
    copyfile('template/crab_script_bhplus_data.sh',year+'_script/crab_script_bhplus_data'+subERA+'.sh')
    if subERA == 'F':
      os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %('2016f_apv', year+'_script/crab_script_bhplus_data'+subERA+'.sh'))
    else:
      os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %('2016'+subERA.lower(), year+'_script/crab_script_bhplus_data'+subERA+'.sh'))
    # change permission of the newly created file
    os.system("chmod 755 "+year+'_script/crab_script_bhplus_data'+subERA+'.sh')

elif year == '2016':
  #MC
  copyfile('template/crab_script_bhplus.sh',year+'_script/crab_script_bhplus.sh')
  os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %('2016b', year+'_script/crab_script_bhplus.sh'))
  # change permission of the newly created file
  os.system("chmod 755 "+year+'_script/crab_script_bhplus.sh')

  #Data
  for subERA in ["F","G","H"]: #2016 has F,G,H eras
    copyfile('template/crab_script_bhplus_data.sh',year+'_script/crab_script_bhplus_data'+subERA+'.sh')
    os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %(year+subERA.lower(), year+'_script/crab_script_bhplus_data'+subERA+'.sh'))
    # change permission of the newly created file
    os.system("chmod 755 "+year+'_script/crab_script_bhplus_data'+subERA+'.sh')

elif year == '2017':
  #MC
  copyfile('template/crab_script_bhplus.sh',year+'_script/crab_script_bhplus.sh')
  os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %(year, year+'_script/crab_script_bhplus.sh'))
  # change permission of the newly created file
  os.system("chmod 755 "+year+'_script/crab_script_bhplus.sh')

  #Data
  for subERA in ["B","C","D","E","F"]: #2017 has B,C,D,E,F eras
    copyfile('template/crab_script_bhplus_data.sh',year+'_script/crab_script_bhplus_data'+subERA+'.sh')
    os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %(year+subERA.lower(), year+'_script/crab_script_bhplus_data'+subERA+'.sh'))
    # change permission of the newly created file
    os.system("chmod 755 "+year+'_script/crab_script_bhplus_data'+subERA+'.sh')

elif year == '2018':
  #MC
  copyfile('template/crab_script_bhplus.sh',year+'_script/crab_script_bhplus.sh')
  os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %(year, year+'_script/crab_script_bhplus.sh'))
  # change permission of the newly created file
  os.system("chmod 755 "+year+'_script/crab_script_bhplus.sh')

  #Data
  for subERA in ["A","B","C","D"]: #201D has A,B,C,D, eras
    copyfile('template/crab_script_bhplus_data.sh',year+'_script/crab_script_bhplus_data'+subERA+'.sh')
    os.system(r'sed -i "26s/YEARTAG/%s/g" %s' %(year+subERA.lower(), year+'_script/crab_script_bhplus_data'+subERA+'.sh'))
    # change permission of the newly created file
    os.system("chmod 755 "+year+'_script/crab_script_bhplus_data'+subERA+'.sh')


with open(samplejson, 'r') as fin:
  data=fin.read()
  lines=json.loads(data)
  keys=lines.keys()
  for key, value in lines.items() :
    # for Data
    if len(value)==3:
      print("Data sample: ", value[1])
      copyfile('data_cfg.py',workdir+key+'_cfg.py')
      # replace crab_script.py by crab_script_bhplus.py
      os.system(r'sed -i "15s/crab_script/crab_script_bhplus/g" %s' %(workdir+key+'_cfg.py'))
      value[1]=value[1].replace('/', 'sss')
      os.system(r'sed -i "6s/dummy/%s/g" %s' %(value[0],workdir+key+'_cfg.py'))
      if '_A' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_B' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_C' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_D' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_E' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_F' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_G' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      if '_H' in value[0]:
        os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+value[2],workdir+key+'_cfg.py'))
      os.system(r'sed -i "13s/sss/\//g" %s' %(workdir+key+'_cfg.py'))
      os.system(r'sed -i "15s/dummy/%s/g" %s' %(datajson,workdir+key+'_cfg.py'))
      os.system(r'sed -i "19s/dummy/%s/g" %s' %(value[1],workdir+key+'_cfg.py'))
      os.system(r'sed -i "19s/sss/\//g" %s' %(workdir+key+'_cfg.py'))
      os.system(r'sed -i "23s/dummy/%s/g" %s' %(datajson,workdir+key+'_cfg.py'))
      os.system(r'sed -i "26s/dummy/%s/g" %s' %(value[0],workdir+key+'_cfg.py'))
    
    print ("=================================\n")
    # for MC
    if len(value)==2:
      print("MC sample: ", value[1])
      copyfile('mc_cfg.py',workdir+key+'_cfg.py')
      # replace crab_script.py by crab_script_bhplus.py
      os.system(r'sed -i "15s/crab_script/crab_script_bhplus/g" %s' %(workdir+key+'_cfg.py'))
      value[1]=value[1].replace('/', 'sss')
      os.system(r'sed -i "6s/dummy/%s/g" %s' %(value[0],workdir+key+'_cfg.py'))
      os.system(r'sed -i "13s/dummy/%s/g" %s' %(scriptpath+'sss'+'crab_script_bhplus.sh',workdir+key+'_cfg.py'))
      os.system(r'sed -i "13s/sss/\//g" %s' %(workdir+key+'_cfg.py'))
      os.system(r'sed -i "19s/dummy/%s/g" %s' %(value[1],workdir+key+'_cfg.py'))
      os.system(r'sed -i "19s/sss/\//g" %s' %(workdir+key+'_cfg.py'))
      os.system(r'sed -i "26s/dummy/%s/g" %s' %(value[0],workdir+key+'_cfg.py'))

if year=='2017':
    os.system(r'sed -i "s/TTC_version9/bhplus_2017/g" bhplus_config_crab_2017/*_cfg.py')

if year=='2018':
    os.system(r'sed -i "s/bHplus\/2017/bHplus\/2018/g" bhplus_config_crab_2018/*_cfg.py')

if year=='2016apv':
  os.system(r'sed -i "s/bHplus\/2017/bHplus\/2016apv/g" bhplus_config_crab_2016apv/*_cfg.py')

if year=='2016':
  os.system(r'sed -i "s/bHplus\/2017/bHplus\/2016/g" bhplus_config_crab_2016/*_cfg.py')
