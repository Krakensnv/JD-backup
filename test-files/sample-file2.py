# Import json Python module
import json
 
# Open the sample JSON file
# Using the open() function
file = open("C:\\Users\\User\\Downloads\\linkextractor-master\\03_01.json", 'r')
 
# Convert the JSON data into Python object
# Here it is a dictionary
json_data = json.load(file)
 
# Check the type of the Python object
# Using type() function 
print(type(json_data))
 
# Iterate through the dictionary
# And print the key: value pairs
for key, value in json_data.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}\n")
 
# Close the opened sample JSON file
# Using close() function
file.close()