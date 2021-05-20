# main.py 
'''
This is to consume API from a specific server.
The log in and url are contained in a separate module auth.py

main_function gives a selection of options, each is a group of options depending on the information
held by the user.
The user is then directed to another module choice_functions.py to handle the sub-menu selection
There are no other requirements of this module.

More Error management could be included but for it's current use it is expected to suffice
'''

from os import system
from choice_functions import *


def main_function():
    system('cls')  # Clear Console
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
    elif answer == '2':
        choice02()
    elif answer == '3':
        choice03()
    elif answer == '4':
        choice04()
    elif answer == '5':
        choice05()
    elif answer == '6':
        choice06()
    elif answer == '7':
        system('cls')
        exit
    else:
        print('Blah')
        main_function()


if __name__ == "__main__":
    main_function()

# GPL-3.0-or-later