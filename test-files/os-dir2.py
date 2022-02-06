import platform
import os
import glob
import shutil
from zipfile import ZipFile 

# jd install path
win = "C:/Users/user/AppData/Local/JDownloader 2.0/cfg"
mac = "/home/Users/user/bin/JDownloader 2.0/cfg"
nix = "path"

print(os.environ.get('USERNAME'))

comp = platform.system()
print(comp)

if comp == "Windows":
    # set win path
    print("Microsoft")
elif comp == "MacOS":
    print("Apple")
else:
    print("UNIX")

file_list = [f for f in glob.glob("linkcollector*.zip")]
file_list.sort(reverse=True)

print(file_list[0])

# shutil.copy(src, dst)
directory = "temp"

# Parent Directory path
parent_dir = "C:/Users/user/Downloads/linkextractor-master"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# '/home / User / Documents'
try:
    os.mkdir(path)
    shutil.copy(file_list[0], "temp")
except OSError as error: 
    print(error)
print("Directory '% s' created" % directory)
  
# specifying the name of the zip file
file = "archive.zip"
  
# open the zip file in read mode
with ZipFile(file, 'r') as zip: 
    # list all the contents of the zip file
    zip.printdir() 
  
    # extract all files
    print('extraction...') 
    zip.extractall() 
    print('Done!')



