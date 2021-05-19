# main.py


from os import system
from choice_functions import *


def main_function():
    system('cls') # Clear Console
    print('''
    Press:
    1: If you have the ISRN
    2: If you have the Ticket Number
    3: If you have IPE ISAM ID and ISAM Sequence Numbers
    4: If you have the fulfilment request reference
    5: If you have the Passenger Surname
    6: If you have the card reference
    7: Exit
    ''')
    answer = input('What option do you want to choose? ')

    if answer == '1':
        choice01()
    elif answer =='2':
        choice02()
    elif answer =='3':
        choice03()
    elif answer =='4':
        choice04()
    elif answer =='5':
        choice05()
    elif answer =='6':
        choice06()
    elif answer =='7':
        system('cls') 
        exit
    else:
        print('Blah')
        main_function()



main_function()
