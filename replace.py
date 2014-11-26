

"""
1. creates a list of [input_files] in a folder with the name "project_name" and with the requried "filetype" based on "start_folder"

2. For each file.
	2. a. Create a list of the "original_file_lines" in memory which is a list of all the lines in the file
	2. b.  create a new list of "new_file_lines" which are a copy of the original lines but replacing each 'find_pattern' with a 'replace_pattern' based on an array of "find_replace_patterns" 
	2. c. Write the list of lines to a new file in a "destination_folder" the "output_file" name should be the orginal file name with the "filetype" suffix removed and replaced with "new_suffix".

"""

import os
import glob

import re
import yesno


project_name = "Full Scale Lab 2"
filetype = ".txt"
new_filetype = ".cfg"
start_folder = r"/home/vmfs/GNS/projects/INE.CCIE.SPv3.Lab.Workbook.GNS3.Initial.Configs"
replace_folder = r"/windows/vmfs/GNS/projects/CCIE-V3-FullLab2/configs"

patterns = [[r"!!conf t", r"conf t"],
            [r"duplex full", "duplex full \n no shut"],
            [r"Ethernet1/0", r"Ethernet0/0"],
            [r"interface POS0/7/0/0", r"interface GigabitEthernet0/0/0/2 "],
            [r"interface POS0/6/0/0", r"interface GigabitEthernet0/0/0/2 "],
            [r"interface GigabitEthernet0/1/0/0", r"interface GigabitEthernet0/0/0/0"],
            [r"interface GigabitEthernet0/4/0/0", r"interface GigabitEthernet0/0/0/0"],
            [r"interface GigabitEthernet0/1/0/1", r"interface GigabitEthernet0/0/0/1"]]



def get_input_files():
    #creates a list of [input_files] from the folder with the name "project_name" and with the requried "filetype" based on "start_folder"
    print("searching folder: ", os.path.join(start_folder, project_name), "\n============")
    files = (glob.glob(os.path.join(start_folder, project_name, "*" + filetype)))
    print("found ", len(files), " files")
    return files


def create_new_page(filename):
    print("opening File :  ", filename)
    with open(filename, "rU") as tempfile:
        original_file = tempfile.read()
    new_file = ""
    for pattern in patterns:
        print("Finding pattern:  ", pattern[0], "replacing with :  ", pattern[1])
        new_file, matches = re.subn(pattern[0],pattern[1],original_file)
        print("THERE WERE :", matches, " in file :", filename)
        original_file = new_file
    return new_file

def write_files(new_file_path, file):
            print("writing file : ", new_file_name)
            f = open(new_file_path, 'w')
            f.write(create_new_page(file))
            f.close()

for file in get_input_files():
    print("checking file : " , file)
    new_file_name = os.path.splitext(os.path.split(file)[1])[0] + new_filetype
    if os.path.exists(replace_folder) and os.path.isdir(replace_folder):
        print(replace_folder," :  folder exists  the target file will be: ", new_file_name)
        new_file_path = os.path.join(replace_folder, new_file_name)
        skipped= False
        if not yesno.yesno("Do you really want to write this file? "):
            print("Skipped writing file")
            continue
        if os.path.isfile(new_file_path):
            if yesno.yesno("This file already exists, do you want to overwrite it? "):
                print("Overeriting file", new_file_path,"\n\n=============")
                write_files(new_file_path, file)
                print("Completed writing file.", file, "/n/n")
            else:
                print("Skipped OVER nowriting file")
                skipped = True
                continue
        else:
            if not skipped:
                print("Creating new file :", new_file_path)
                write_files(new_file_path, file)
                print("Completed writing file", file)
    print("Finished n\n=============")
 
            
                  



