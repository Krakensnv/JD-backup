import platform
import os
import glob
import re

print(platform.platform())
print(platform.system())

file_list = [f for f in glob.glob("*.py")]
print(file_list)

results = []

for forlder in gamefolders:
	for f in os.listdir(folder):
		if re.search('.c', f):
			results += [each for each in os.listdir(folder) if each.endswith('.py')]
print(results)
