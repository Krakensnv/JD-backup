import os
import json

files = os.listdir('.')
print(files)
links = []

ignorelist = [".idea", ".git", "README.md"]

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
