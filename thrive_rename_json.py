import json;

def printKeys(indent, d):
    for key in d:
        print("\t"*indent + key + "\t" + str(type(d[key])))
        if type(d[key]) is dict:
            #print("")
            printKeys(indent + 1, d[key])

data = open(r'C:\Users\elaij\OneDrive\Documents\Programming\Python\programs\Thrive\test_data.json', "r").read()
jsonData = json.loads(data)
jsonConverted = {}


convertedDataFile = open(r'C:\Users\elaij\OneDrive\Documents\Programming\Python\programs\Thrive\converted.json', "w")

printKeys(0, jsonData)

#print(jsonData)