import json
import re

# data = json.load(open('03_01.json', 'r'))
with open ("C:\\Users\\User\\Downloads\\linkextractor-master\\03_01.json") as file:
    for line in file:
       # urls = re.findall('https://(?:[-\www.]|(?:%[\da-fA-F]{2}))+', line)
        urls = re.findall("(https?://[^\s]+)", line)
        print(str(urls))

        
        