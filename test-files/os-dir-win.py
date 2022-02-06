import platform
import os
import glob
import shutil
from zipfile import ZipFile 

# JDownloader default install path
win = "C:/Users/user/AppData/Local/JDownloader 2.0/cfg"
mac = "/Users/user/bin/JDownloader 2.0/cfg"
nix = "/home/users/user/bin/JDownloader 2.0/cfg"

print(os.getlogin())

comp = platform.system()
print(comp)

if comp == "Windows":
    # set win path
    print("Microsoft")
elif comp == "Darwin":
    print("Apple")
else:
    print("UNIX")
    
search_path = win
file_list = [f for f in glob.glob(search_path + "/linkcollector*.zip")]
file_list.sort(reverse=True)

print(file_list[0])
# print(glob.glob(search_path + "/linkcollector*.zip"))
archiv = file_list[0]

# shutil.copy(src, dst)
new_dir = "temp"
parent_dir = win
path = os.path.join(parent_dir, new_dir)

destination = win + "/temp"
# pwd = '<YOUR_PASSWORD>'

with ZipFile(archiv) as zf:
    # zf.extractall(destination, pwd=pwd.encode())
    zf.extractall(destination)
    zf.close()
    print(file_list[0] + " was extracted successfully!")






