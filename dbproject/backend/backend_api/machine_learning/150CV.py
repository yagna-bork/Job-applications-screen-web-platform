import json
import NeutralNetwork




data = json.loads(open('cvDatasetNEW.json').read())

newfile = open("cvDatasetNEW150.json", "w")
newfile.write("[")
for i in range(100):
    newfile.write(json.dumps(data[i]))
    if i != 100-1:
        newfile.write(",")
    

newfile.write("]")