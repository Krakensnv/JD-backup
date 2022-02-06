import platform
import os
import glob
import shutil

# jd install path
win = "path"
mac = "path"
nix = "path"

comp = platform.system()
print(comp)

if comp == "Windows":
    # set win path
    print("Microsoft")
elif comp == "MacOS":
    print("Apple")
else:
    print("UNIX")

# #################################
# get zip files sorted by last one
file_list = [f for f in glob.glob("linkcollector*.zip")]
# sort files:
file_list.sort(reverse=True)

print(file_list)
# print the oldest file:
print(file_list[0])

# ##############################
# make dir, copy files, extract files
# Python program to explain os.mkdir() method

# importing os module
# import os

# Directory
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

# Directory
directory = "Geeks"

# Parent Directory path
parent_dir = "C:/Users/user/Downloads/linkextractor-master"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

'''import shutil, os
files = ['file1.txt', 'file2.txt', 'file3.txt']
os.mkdir('my_new_folder')
for f in files:
    shutil.copy(f, 'my_new_folder')'''


