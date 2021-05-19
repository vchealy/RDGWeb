# res.py
'''
This module is for the management of the data retrieved from the other modules.

Initially it was set to print:
        stat_ status code reply from the GET response
                This remains, because if there is an error this code could help
        inputer - The body of the respnse

Write the inputer(XML object) to a JSON file rather than console.
'''
import xmltodict, json

def result_manager(stat,inputer):
        obj = xmltodict.parse(inputer) # Convert XML input to JSON
        obj2 = json.dumps(obj, indent=4, sort_keys=True) # Make it pretty JSON
        with open('body.json', 'w') as f:
                f.write(obj2)
                
        print(stat)

