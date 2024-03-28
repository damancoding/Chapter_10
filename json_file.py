#Amanda M
#3/27/2024
# very confused on how to see the JSON file

import json
#f = open('data.json')
#data=json.load(f)
#for i in data['contacts']:
#    print(i)

#f.close()

def write_json(new_data,filename='data.json'):
    with open(filename,'r+')as file:
        file_data = json.load(file)
        file_data["contacts"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent = 4)
y = { "fname": "Sam",
     "lname": "Cooke",
     "phone": "404-123-0005",
     "email": "scooke@noemail.com"}