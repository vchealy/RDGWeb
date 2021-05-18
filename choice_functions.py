from os import system
from request_functions import *


def choice01():
    system("cls")  # Clear Console
    print("ISRN Choices")
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
            card_details_ISRN()
        elif card == '7':
            exit
        else:
            card_details_ISRN(card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("ISRN Choices - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the ISRN? ')
        if card == '':
            journey_taps_ISRN()
        elif card == '7':
            exit
        else:
            journey_taps_ISRN(card)
    elif answer == '3':
        system("cls")  # Clear Console
        print("ISRN Choices - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the ISRN?')
        if card == '':
            product_summary_list_by_ISRN()
        elif card == '7':
            exit
        else:
            product_summary_list_by_ISRN(card)
    elif answer == '7' or '':
        exit


def choice02():
    system("cls")  # Clear Console
    print("Ticket Number")
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
        journey_by_ticket_ID(card)
        if card == '':
            journey_by_ticket_ID()
        elif card == '7':
            exit
        else:
            journey_by_ticket_ID(card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("Ticket Number - Enter 7 to Exit")
        print('Press Enter for Default')
        card = input('What is the Ticket Number? ')
        if card == '':
            product_long_by_ticket_ID()
        elif card == '7':
            exit
        else:
            product_long_by_ticket_ID(card)
    elif answer == '7' or '':
        exit


def choice03():
    system("cls")  # Clear Console
    print("IPE ISAM ID and ISAM Sequence Numbers")
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
            products_summary_list_ISAM_instance_ID()
        elif ipeIsamId == '':
            ipeIsamId = "7B06DC7"
            products_summary_list_ISAM_instance_ID(ipeIsamId, ipeIsamSeqNum)
        elif ipeIsamSeqNum == '':
            products_summary_list_ISAM_instance_ID(ipeIsamId)
        else:
            products_summary_list_ISAM_instance_ID(ipeIsamId, ipeIsamSeqNum)
    elif answer == '2':
        system("cls")  # Clear Console
        print("IPE ISAM ID and ISAM Sequence Numbers")
        print('Press Enter for Default')
        ipeIsamId = input('\nWhat is the IPE ISAM ID? ')
        ipeIsamSeqNum = input('What is the Sequence Number? ')
        if ipeIsamId == '' and ipeIsamSeqNum == '':
            ipedefinition_by_ISAM_instance_ID()
        elif ipeIsamId == '':
            ipeIsamId = "7B06DC7"
            ipedefinition_by_ISAM_instance_ID(ipeIsamId, ipeIsamSeqNum)
        elif ipeIsamSeqNum == '':
            ipedefinition_by_ISAM_instance_ID(ipeIsamId)
        else:
            ipedefinition_by_ISAM_instance_ID(ipeIsamId, ipeIsamSeqNum)
    elif answer == '7' or '':
        exit


def choice04():
    system("cls")  # Clear Console
    print("Fulfilment Request Reference")
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
            product_summary_list_by_fulfilment_request_reference()
        elif card == '7':
            exit
        else:
            product_summary_list_by_fulfilment_request_reference(card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("Fulfilment Request Reference - Press 7 to Exit")
        print('Press Enter for Default')
        card = input('\nWhat is the Fulfilment Request Reference? ')
        if card == '':
            ipedefinition_by_fulfilment_request_reference()
        elif card == '7':
            exit
        else:
            ipedefinition_by_fulfilment_request_reference(
                card)  # Surname Search
    elif answer == '7' or '':
        exit


def choice05():
    system("cls")  # Clear Console
    print("Passenger Surname")
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
            cardholder_by_name()
        elif card == '7':
            exit
        else:
            cardholder_by_name(card)  # Surname Search
    elif answer == '7' or '':
        exit


def choice06():
    system("cls")  # Clear Console
    print("Card Reference")
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
        card_details_by_card_reference(card)
        if card == '':
            card_details_by_card_reference()
        elif card == '7':
            exit
        else:
            card_details_by_card_reference(card)  # Surname Search
    elif answer == '7' or '':
        exit
