import os,sys,time
import string
import re
import argparse
import textwrap
os.system('env -i KRB5CCNAME="$KRB5CCNAME" cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o cookiefile.txt --krb --reprocess')
#os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
#os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import McM
from json import dumps
from itertools import groupby
from textwrap import dedent

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
            ------------------------------------------------
               This script reads number of events from McM starting from a DAS dataset name.
               e.g. python get_number_of_events_starting_from_das_name.py --campaign RunIISummer20UL18NanoAODv9
                                                                                    '''))
parser.add_argument('--campaign', type=str, help="", required=True, nargs='+')
args = parser.parse_args()

if args.campaign is not None:
    campaign=str(args.campaign[0])
    print("campaign="+campaign)



#mcm = McM(dev=False)
mcm = McM(cookie='cookiefile.txt', dev=False, debug=False)
page = 0
res = mcm.get('requests',query='member_of_campaign='+campaign+'*&dataset_name=TAToTTQ_MA-*GeV_TuneCP5_13TeV_G2HDM-rt*-madgraphMLM-pythia8', page=page)
while len(res) !=0:
    for r in res:
        print (str(r['prepid'])+"  "+str(r['dataset_name'])+"  "+str(r['output_dataset'])+"   "+str(r['status'])+"   "+str(r['completed_events']))
    page += 1
    res = mcm.get('requests',query='member_of_campaign='+campaign+'*&dataset_name=TAToTTQ_MA-*GeV_TuneCP5_13TeV_G2HDM-rt*-madgraphMLM-pythia8', page=page)
