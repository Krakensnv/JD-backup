import json

array = '{"Technology": ["AI", "ML", "DataScience"]}'
data = json.loads(array)
print(data['Technology'][1])

with open('03_01.json') as f:
    data = list(json.load(f).items())
print(data)
