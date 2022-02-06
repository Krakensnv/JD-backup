import json
  
# Opening JSON file
with open('people.json') as json_file:
    data = json.load(json_file)
  
    # for reading nested data [0] represents
    # the index value of the list
    print(data['people1'][0])
      
    # for printing the key-value pair of
    # nested dictionary for looop can be used
    print("\nPrinting nested dicitonary as a key-value pair\n")
    for i in data['people1']:
        print("Name:", i['name'])
        print("Website:", i['website'])
        print("From:", i['from'])
        print()