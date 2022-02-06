import json

with open("03_01.json") as json_file:
    json_data = json.load(json_file)

    for key, value in json_data.items():
        result = value['url']
