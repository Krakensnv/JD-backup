import json
  
# Opening JSON file
with open('people.json') as json_file:
    data = json.load(json_file)
  
    # Print the type of data variable
    print("Type:", type(data))
  
    # Print the data of dictionary
    print("\nPeople1:", data['people1'])
    print("\nPeople2:", data['people2'])