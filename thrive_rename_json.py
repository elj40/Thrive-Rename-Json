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

def find_ignore_dir(path, ignore_dict):
    for (root, dirs, files) in os.walk(path):
        for f in files:
            if f.find(".json") > 0:
                find_ignore_file(os.path.join(root,f), ignore_dict)
        for d in dirs:
            find_ignore_dir(os.path.join(root,d), ignore_dict)

def find_ignore_file(path, ignore_dict):
    FILE = open(path, encoding='utf-8-sig')
    data = FILE.read()
    json_data = json.loads(data)
    FILE.close()
    for key in json_data:
        ignore_dict[key] = True

def convertJson(indent, baseDict, ignore):
    newDict = {}

    for key in baseDict:
        newKey = PascalCasify(key) if len(key)>1  and not key in ignore else key
        if type(baseDict[key]) is dict:
            newDict[newKey] = convertJson(indent + 1, baseDict[key], ignore)
        elif type(baseDict[key]) is list:
            newDict[newKey] = []
            for i in range(len(baseDict[key])):
                if type(baseDict[key][i]) is dict:
                    newDict[newKey].append(convertJson(indent + 1, baseDict[key][i], ignore))
                else:
                    newDict[newKey].append(baseDict[key][i])
        else:
            newDict[newKey] = baseDict[key]

    return newDict

def process_dir(path, ignore):
    for (root, dirs, files) in os.walk(path):
        for f in files:
            if f.find(".json") > 0:
                print(f)
                process_file(os.path.join(root,f), ignore)
        for d in dirs:
            process_dir(os.path.join(root, d), ignore)

def process_file(path, ignore):
    FILE = open(path, "r", encoding='utf-8-sig')
    DATA = FILE.read()
    FILE.close()
    JSON_DATA = json.loads(DATA)

    jsonConverted = convertJson(0, JSON_DATA, ignore)
    
    jsonConvertedText = json.dumps(jsonConverted, indent=2)

    FILE = open(path, "w", encoding='utf-8-sig')
    FILE.write(jsonConvertedText + "\n")
    FILE.close()
    print("JSON Converted")
        
def main():
    if sys.argv[1] == "help":
        print_help()
        sys.exit()

    IGNORE = {}
    PATH_TO_FILE = '\\'.join(sys.argv[1:])

    if os.path.isdir(PATH_TO_FILE):
        find_ignore_dir(PATH_TO_FILE, IGNORE)
        process_dir(PATH_TO_FILE, IGNORE)
    elif os.path.isfile(PATH_TO_FILE):
        find_ignore_file(PATH_TO_FILE, IGNORE)
        print(IGNORE)
        process_file(PATH_TO_FILE, IGNORE)
    else:
        print("Could not find file...")
    


if __name__ == "__main__":
    main()