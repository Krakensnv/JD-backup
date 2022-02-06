import json

jsonFile = open("33_00")
jsonString = jsonFile.read()
jsonData = json.loads(jsonString)
type(jsonData)
print(jsonData['downloadLink'])
print(type(jsonData['downloadLink']))
print(jsonData['sourceUrls'][0])
print(type(jsonData['sourceUrls']))

#jsonFile = open("11_08")
#jsonString = jsonFile.read()
#jsonData = json.loads(jsonString)
#type(jsonData)
#print(jsonData['sourceUrls'][0])
