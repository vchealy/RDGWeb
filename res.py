# res.py
'''
This module is for the management of the data retrieved from the other modules.

Initially it is set to print:
        stat_ status code reply from the GET response
        inputer - The body of the respnse

This will be changed to write to file rather than console.
'''
def result_manager(stat,inputer):
    print(stat)
    print(inputer)
