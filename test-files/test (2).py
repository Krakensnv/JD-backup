import json
from collections import OrderedDict

r = json.load(open('33_00'), object_pairs_hook=OrderedDict)

print(json.dumps(r, indent=2))
print("Type:", type(r))


