all_results = {}
json_file_list = ['03_01.json', 'file_2.json']

for file in json_file_list:
    with open(file) as json_file:
        json_data = json.load(json_file)
        for key, value in json_data.items():
            if 'result' in value:
                all_results[key] = value['result']
return all_results