#This will allow me to type a keyword and have it copy to my clipboard

import sys
import clipboard
import json 

#Creates JSON file and assigns it to a variable
SAVED_DATA = "clipboard.json"

#Allows the save function giving write access to the clipboard
def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent = 4)

#Allows the load function giving read access to the clipboard
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return data
    except:
        return {}

        
#Since the length of the command includes the name of the file
#we need to let the length = 2 and start at the "second" item
#if successful, it loads the json file
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    #saves whatever is on your clipboard to the json file
    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_items(SAVED_DATA , data)
        print('Data Saved')
    
    #pulls whatever key you choose to your clipboard    
    elif command == "load":
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print('Key does not exist')
            
    #lists all key value pairs in json file
    elif command == "list":
        print(data)
    else:
        print('Unknown command')
else:
    print('Please pass exactly one command')