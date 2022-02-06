import os
import json

# C:\Users\user\AppData\Local\JDownloader 2.0\cfg   get username as a variable
# find linkcollector*.zip files
# sort by date
# extract
# get path to the extracted folder
# get links for Windows
# for MacOS
# for Linux

files = os.listdir('.')

links = []

ignorelist = [".idea", ".zip", "README.md"]

for idx, file in enumerate(files, 1):
    print("File no: " + str(idx) + "/" + str(len(files)) + ".")
    if file in ignorelist:
        print("Skipping " + str(file))
        continue
    f = open(file, 'r')
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

file = open('jd-links.txt', 'w')

for link in links:
    file.write(str(link) + "\n")

print("Done")
