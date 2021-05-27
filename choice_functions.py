# choice_functions.py
'''
Directed from main.py
Each function is a sub selection from the initial coices in main_function

On completeion of the choice information is sent to the request_functions module
request_functions constructs and actions the GEt request
The request_functions returns the status and body text from the server reply
The choice module then forwards the information onto res.py
res.py will manipulate the information into a desired format
'''

from os import system
from request_functions import *
from res import result_manager


def environment():
    '''
    This chooses the working environment.
    It also selects the authorisation dat from  the secure file 
    '''
    system('cls')  # Clear Console
    print('''
    Smartcard TMS - Environment Choice
    Information saved in Extraction Folder

    Press:
    1: Live
    2: Staging
    7: Exit
    ''')
    env = input('Which Environment? ')
    if env == '1':
        env = 'Live'
        # main_function(env)
    elif env == '2':
        env = 'Staging'
        # main_function(env)
    elif env == '7':
        exit
    else:
        environment()
    return env


def choice01():
    env= environment()
    system("cls")  # Clear Console
    print("ISRN Choices - {env}")
    print(
        """
    1: Card Details
    2: Journey Taps
    3: Product Summary List
    7: Exit
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("ISRN Choices - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the ISRN? ')
        if card == '':
            res = card_details_ISRN(env)
        elif card == '7':
            exit
        else:
            res = card_details_ISRN(env, card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("ISRN Choices - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the ISRN? ')
        if card == '':
            res = journey_taps_ISRN()
        elif card == '7':
            exit
        else:
            res = journey_taps_ISRN(card)
    elif answer == '3':
        system("cls")  # Clear Console
        print("ISRN Choices - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the ISRN?')
        if card == '':
            res = product_summary_list_by_ISRN()
        elif card == '7':
            exit
        else:
            res = product_summary_list_by_ISRN(card)
    elif answer == '7' or '':
        exit

    result_manager(res[0], res[1])


def choice02():
    env= environment()
    system("cls")  # Clear Console
    print("Ticket Number - {env}")
    print(
        """
    1: Journeys
    2: Product Long
    7: Exit
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Ticket Number - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('What is the Ticket Number? ')
        if card == '':
            res = journey_by_ticket_ID(env)
        elif card == '7':
            exit
        else:
            journey_by_ticket_ID(env, card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("Ticket Number - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('What is the Ticket Number? ')
        if card == '':
            res = product_long_by_ticket_ID(env)
        elif card == '7':
            exit
        else:
            res = product_long_by_ticket_ID(env, card)
    elif answer == '7' or '':
        exit

    result_manager(res[0], res[1])


def choice03():
    env= environment()
    system("cls")  # Clear Console
    print("IPE ISAM ID and ISAM Sequence Numbers - {env}")
    print(
        """
    1: Product Summary List
    2: IPE Definition by ISAM Instance
    7: Exit
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("IPE ISAM ID and ISAM Sequence Numbers")
        print('Press Enter for Default')
        ipeIsamId = input('\nWhat is the IPE ISAM ID? ')
        ipeIsamSeqNum = input('What is the Sequence Number? ')
        if ipeIsamId == '' and ipeIsamSeqNum == '':
            res = products_summary_list_ISAM_instance_ID(env)
        elif ipeIsamId == '':
            ipeIsamId = "7B06DC7"
            res = products_summary_list_ISAM_instance_ID(env,
                ipeIsamId, ipeIsamSeqNum)
        elif ipeIsamSeqNum == '':
            res = products_summary_list_ISAM_instance_ID(env, ipeIsamId)
        else:
            res = products_summary_list_ISAM_instance_ID(env,
                ipeIsamId, ipeIsamSeqNum)
    elif answer == '2':
        system("cls")  # Clear Console
        print("IPE ISAM ID and ISAM Sequence Numbers")
        print('Press Enter for Default')
        ipeIsamId = input('\nWhat is the IPE ISAM ID? ')
        ipeIsamSeqNum = input('What is the Sequence Number? ')
        if ipeIsamId == '' and ipeIsamSeqNum == '':
            ipedefinition_by_ISAM_instance_ID(env,)
        elif ipeIsamId == '':
            ipeIsamId = "7B06DC7"
            ipedefinition_by_ISAM_instance_ID(env, ipeIsamId, ipeIsamSeqNum)
        elif ipeIsamSeqNum == '':
            ipedefinition_by_ISAM_instance_ID(env,ipeIsamId)
        else:
            ipedefinition_by_ISAM_instance_ID(env, ipeIsamId, ipeIsamSeqNum)
    elif answer == '7' or '':
        exit

    result_manager(res[0], res[1])


def choice04():
    env= environment()
    system("cls")  # Clear Console
    print("Fulfilment Request Reference - {env}")
    print(
        """
    1: Product Summary List
    2: IPE Definition   
    7: Exit 
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Fulfilment Request Reference - Press 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the Fulfilment Request Reference? ')
        if card == '':
            product_summary_list_by_fulfilment_request_reference(env)
        elif card == '7':
            exit
        else:
            product_summary_list_by_fulfilment_request_reference(env, card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("Fulfilment Request Reference - Press 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the Fulfilment Request Reference? ')
        if card == '':
            res = ipedefinition_by_fulfilment_request_reference(env)
        elif card == '7':
            exit
        else:
            res = ipedefinition_by_fulfilment_request_reference(env,
                card)
    elif answer == '7' or '':
        exit

    result_manager(res[0], res[1])


def choice05():
    env= environment()
    system("cls")  # Clear Console
    print(f"Passenger Surname - {env}")
    print(
        """
    1: Surname
    7: Exit
    """
    )
    answer = input("Which option do you want? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Passenger Surname - Press 7 to Exit")
        print('Default Surname = Gray - Press Enter')
        card = input('\n What is the Surname? ')
        if card == '':
            res = cardholder_by_name()
        elif card == '7':
            exit
        else:
            res = cardholder_by_name(env, card)  # Surname Search
    elif answer == '7' or '':
        exit
    result_manager(res[0], res[1])


def choice06():
    env= environment()
    system("cls")  # Clear Console
    print("Card Reference - {env}")
    print(
        """
    1: Card Details
    7: Exit
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Card Reference - Press 7 to Exit")
        print('Press Enter for Default = WLU009GB27499901919')
        card = input('\nWhat is the Card Reference? ')
        if card == '':
            res = card_details_by_card_reference(env)
        elif card == '7':
            exit
        else:
            res = card_details_by_card_reference(env, card)
    elif answer == '7' or '':
        exit
    result_manager(res[0], res[1])

# GPL-3.0-or-later
