# res.py 
'''
This module is for the management of the data retrieved from the other modules.

Initially it was set to print:
        stat_ status code reply from the GET response
                This remains, because if there is an error this code could help
        inputer - The body of the respnse

Write the inputer(XML object) to a JSON file rather than console.
Create the JSON file with a Unique Identifier
'''
import json
import xmltodict
from datetime import datetime
import time
from main import main_function

# Create an Unique  File Name
object_name = "./extractions/Extraction-" + datetime.today().strftime('%Y-%m-%d') + '_' + \
    datetime.now().strftime("%H_%M_%S")+'.json'


def result_manager(stat, inputer):
    obj = xmltodict.parse(inputer)  # Convert XML input to JSON
    obj2 = json.dumps(obj, indent=4, sort_keys=True)  # Make it pretty JSON
    with open(object_name, 'w') as f:
        f.write(obj2)

    print(stat)
    time.sleep(5) #Pause to allow user to see the message
    main_function()

# GPL-3.0-or-later