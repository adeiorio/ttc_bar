#Last used:
# python private_production_test.py --batch 1 --indir /eos/cms/store/group/phys_b2g/ExYukawa/ntu_prod/TBarZQB_2017UL/ --outdir /eos/cms/store/group/phys_b2g/ExYukawa/bHplus/2017/TBarZQB --fpjob 3
##########

import os, sys
import argparse
from termcolor import colored

# Define the directory path
#directory = "/eos/cms/store/group/phys_b2g/ExYukawa/ntu_prod/TZQBBar_2017UL/"
directory = "/eos/cms/store/group/phys_b2g/ExYukawa/ntu_prod/TBarZQB_2017UL/"

# Define the list of file types you're interested in
file_types = [".txt", ".csv", ".xlsx", ".root"]


# Function to perform some action with each file
def run_skimming(file_path, outdir):
    # Example action: print the file path
    print (colored("Skimming file: ", 'cyan'))
    print (colored(file_path, 'yellow', attrs=["bold"]))
    if 'eos' in file_path and 'root://eosuser.cern.ch//' not in file_path:
        file_path = 'root://eosuser.cern.ch//' + file_path
    # Here you can perform any action you want with the file
    # os.system("python localrun_bhplus.py -m -i {} --year 2017 -o $CMSSW_BASE/src/PhysicsTools/NanoAODTools/python/postprocessing/analysis/test".format(str(file_path)))
    os.system("python localrun_bhplus.py -m -i {} --year 2017 -o {}".format(str(file_path), outdir))
    # print (outdir)

def process_files(start_index, batch_size, indir, outdir):
    # Counter variable to track the number of processed files
    processed_files = 0

    # Loop over files in the directory starting from the start index
    for file_name in os.listdir(indir)[start_index:]:
        # Check if the maximum number of processed files is reached
        if processed_files >= batch_size:
            break

        # Check if the file has one of the specified file types
        for file_type in file_types:
            if file_name.endswith(file_type):
                # Construct the full file path
                file_path = os.path.join(indir, file_name)
                # Perform the action with the file
                run_skimming(file_path, outdir)
                # Increment the counter for processed files
                processed_files += 1
                break  # Move to the next file type

    # Print a message indicating the end of file processing for the batch
    print("Processed", processed_files, "files.")

if __name__ == "__main__":
    
    usage  = 'usage: %prog [options]'
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('-batch', '--batch', dest='batch', help='which batch to run', default=1, type=int)
    parser.add_argument('-fpjob', '--fpjob', dest='fpjob', help='Files per job', default=2, type=int)
    parser.add_argument('-indir', '--indir', dest='inDir', help='input directory', default='./', type=str)
    parser.add_argument('-outdir', '--outdir', dest='outDir', help='ouput directory', default='/eos/cms/store/group/phys_b2g/ExYukawa/bHplus/', type=str)
    args = parser.parse_args()
    
    # Get the batch number from command-line arguments (default to 1 if not provided)
    # batch_number = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    batch_number = args.batch
    inDir = args.inDir
    outDir = args.outDir    
    # Define the batch size (2 files per batch is default)
    batch_size = args.fpjob

    # Calculate the start index for the specified batch
    start_index = (batch_number - 1) * batch_size

    # Process files for the specified batch
    process_files(start_index, batch_size, inDir, outDir)
