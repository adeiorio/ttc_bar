#==============
# Last used: python crab_submission_preparation.py on/off
#==============
import sys
import os
from PhysicsTools.NanoAODTools.postprocessing.analysis.scripts.aux import colors

def join_l(l, sep):
    li = iter(l)
    string = "/"+str(next(li))
    for i in li:
        string += str(sep) + str(i)
    return string

def perform_operation(action="on"):
    # Replace this with the operation you want to perform
    l = os.environ["CMSSW_BASE"].split("/")[1:-1]
    location = join_l(l, "/")
    if action=="on":
        print("moving .git folder to before CMSSW dir...")
        print (colors.colordict['YELLOW']+"mv ../.git "+location+"/"+colors.colordict['CEND'])
        if not os.path.isdir("../.git"):
            print (colors.colordict['GREEN']+"Already moved to "+location+"/"+"  -> go ahead with crab submission"+colors.colordict['CEND'])
        else:
            os.system("mv ../.git "+location+"/") 
    elif action=="off":
        print ("moving .git folder back to analysis dir")
        print (colors.colordict['YELLOW']+"mv "+location+"/.git "+"../"+colors.colordict['CEND'])
        if not os.path.isdir(location+"/.git"):
           print (colors.colordict['GREEN']+"Already moved to Analysis dir"+colors.colordict['CEND'])
        else:
            os.system("mv "+location+"/.git "+"../")
 
# Main function
if len(sys.argv) == 2 and sys.argv[1] == "on":
    perform_operation("on")
elif len(sys.argv) == 2 and sys.argv[1] == "off":
    perform_operation("off")
else:
    print("Usage: python crab_submission_preparation.py on/off")
