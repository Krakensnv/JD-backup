import platform
import os
import glob
import re

print(platform.platform())
print(platform.system())

file_list = [f for f in glob.glob("*.py")]
print(file_list)

print(os.getcwd())

