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
FILE = open(PATH_TO_FILE, "r+")
DATA = FILE.read()
JSON_DATA = json.loads(DATA)

jsonConverted = {}


convertJson(0, JSON_DATA, jsonConverted)


jsonConvertedText = json.dumps(jsonConverted, indent=4)
print(jsonConvertedText)
FILE.write(jsonConvertedText)
FILE.close()
print("JSON Converted")
