#!/usr/bin/env python3
import platform
import os
import glob
import shutil
from zipfile import ZipFile 
import json

__author__ = "Kraken.snv"
__copyright__ = "Copyright 2022, The JD Backup"
__credits__ = ["Krakensnv", "hherglotz"]
__email__ = "Kraken.snv@protonmail.com"

iam = os.getlogin()
win = "C:/Users/" + iam + "/AppData/Local/JDownloader 2.0/cfg"
mac = "/Users/" + iam + "/bin/JDownloader 2.0/cfg"
nix = "/home/" + iam + "/jd2/cfg"

comp = platform.system()

jdown = ""
if comp == "Windows":
    jdown = win
    print("\n" + comp + " OS Detected.\n")
elif comp == "Darwin":
    jdown = mac
    print("\n" + comp + " OS Detected.\n")
elif comp == "Linux":
    jdown = nix
    print("\n" + comp + " OS Detected.\n")
else:
    print("\n" + "Unsupported OS!\n")
    
search_path = jdown
file_list = [f for f in glob.glob(search_path + "/linkcollector*.zip")]
file_list.sort(reverse=True)

print(file_list[0])
archiv = file_list[0]

new_dir = "temp"
parent_dir = jdown
path = os.path.join(parent_dir, new_dir)

destination = jdown + "/temp"

with ZipFile(archiv) as zf:
    zf.extractall(destination)
    zf.close()
    print(archiv + " was extracted successfully!")


fullPath = jdown + "/temp/"
files = os.listdir(fullPath)
links = []

ignorelist = [".git", ".zip", "README.md"]

for idx, file in enumerate(files, 1):
    print("File no: " + str(idx) + "/" + str(len(files)) + ".")
    if file in ignorelist:
        print("Skipping " + str(file))
        continue
    f = open(fullPath + file, 'r')
    try:
        jsdata = json.loads(f.read())
    except ValueError:
        print("This file is not a JSON File")
        continue
    if 'sourceUrls' in jsdata.keys():
        links.append(str(jsdata['sourceUrls'][0]))
    else:
        print("No url, going forward.")
    f.close()

file = open('my_jd_links.txt', 'w')

for link in links:
    file.write(str(link) + "\n")
    
finStep = os.path.join(jdown, new_dir)    
shutil.rmtree(finStep)
print("Done")

