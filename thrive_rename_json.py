import json
import sys

def PascalCasify(keyName):
    newName = keyName[0].upper() + keyName[1:]
    return newName


def convertJson(indent, baseDict, newDict):
    for key in baseDict:
        #print("\t"*indent + key + "\t" + str(type(d[key])))
        if type(baseDict[key]) is dict:
            newKey = PascalCasify(key) if indent > 0 and len(key)>1 else key
            newDict[newKey] = {}
            convertJson(indent + 1, baseDict[key], newDict[newKey])
        else:
            newDict[PascalCasify(key) if indent > 0  and len(key)>1 else key] = baseDict[key]
        
print(sys.argv[1])

PATH_TO_FILE = sys.argv[1] + "\\" + sys.argv[2]
FILE = open(PATH_TO_FILE)
DATA = FILE.read()

#data = open(r'C:\Users\elaij\OneDrive\Documents\Programming\Python\programs\Thrive\test_data.json', "r").read()
jsonData = json.loads(DATA)
jsonConverted = {}


convertedDataFile = open(r'C:\Users\elaij\OneDrive\Documents\Programming\Python\programs\Thrive\converted.json', "w")

convertJson(0, jsonData, jsonConverted)

jsonConvertedText = json.dumps(jsonConverted, indent=4)
convertedDataFile.write(jsonConvertedText)
print(jsonConverted)
