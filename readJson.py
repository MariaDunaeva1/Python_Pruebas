import json

def readJsonFile(fileName):
    data=""
    try:
        with open ('files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
    
import jsonFileHandler

data = jsonFileHandlersonFileHandler.readJsonFile('insulin.json')

if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")
    