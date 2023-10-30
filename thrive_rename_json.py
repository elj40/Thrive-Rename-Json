import json
import sys
import os

def print_help():
    print("Rename JSON help logs:")
    print("Format: py thrive_rename_json.py path_to_dir path_to_file ")
    print("**Note: file and dir paths are seperate to make use of cmd variables")

def PascalCasify(keyName):
    newName = keyName[0].upper() + keyName[1:]
    return newName


def convertJson(indent, baseDict):
    newDict = {}

    for key in baseDict:
        newKey = PascalCasify(key) if indent > 0  and len(key)>1 else key
        if type(baseDict[key]) is dict:
            newDict[newKey] = convertJson(indent + 1, baseDict[key])
        elif type(baseDict[key]) is list:
            newDict[newKey] = []
            for i in range(len(baseDict[key])):
                if type(baseDict[key][i]) is dict:
                    newDict[newKey][i] = convertJson(indent + 1, baseDict[key][i])
                else:
                    newDict[newKey][i] = baseDict[key][i]
        else:
            newDict[newKey] = baseDict[key]

    return newDict

def process_dir(path):
    print("Dir does nothing yet")

def process_file(path):
    FILE = open(path, "r", encoding='utf-8-sig')
    DATA = FILE.read()
    FILE.close()
    JSON_DATA = json.loads(DATA)

    jsonConverted = convertJson(0, JSON_DATA)
    
    jsonConvertedText = json.dumps(jsonConverted, indent=2)

    FILE = open(path, "w", encoding='utf-8-sig')
    FILE.write(jsonConvertedText + "\n")
    FILE.close()
    print("JSON Converted")
        
def main():
    if sys.argv[1] == "help":
        print_help()
        sys.exit()

    print(sys.argv[1] + "\\" + sys.argv[2])
    PATH_TO_FILE = sys.argv[1] + "\\" + sys.argv[2]
    if os.path.isdir(PATH_TO_FILE):
        process_dir(PATH_TO_FILE)
    elif os.path.isfile(PATH_TO_FILE):
        process_file(PATH_TO_FILE)
    


if __name__ == "__main__":
    main()