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
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("ISRN Choices")
        card = input('What is the ISRN? ')
        card_details_ISRN(card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("ISRN Choices")
        card = input('What is the ISRN? ')
    elif answer == '3':
        system("cls")  # Clear Console
        print("ISRN Choices")
        card = input('What is the ISRN?')
        product_summary_list_by_ISRN(card)




def choice02():
    system("cls")  # Clear Console
    print("Ticket Number")
    print(
        """
    1: Journeys
    2: Product Long
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Ticket Number")
        card = input('What is the Ticket Number? ')
        journey_by_ticket_ID(card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("Ticket Number")
        card = input('What is the Ticket Number? ')
        product_long_by_ticket_ID(card)


# elif answer ==3:
#     choice03()


def choice03():
    system("cls")  # Clear Console
    print("IPE ISAM ID and ISAM Sequence Numbers")
    print(
        """
    1: Product Summary List
    2: IPE Definition by ISAM Instance
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("IPE ISAM ID and ISAM Sequence Numbers")
        ipeIsamId = input('What is the IPE ISAM ID? ')
        ipeIsamSeqNum = input('What is the Sequence Number? ')
        products_summary_list_ISAM_instance_ID(ipeIsamId, ipeIsamSeqNum)
    elif answer == '2':
        system("cls")  # Clear Console
        print("IPE ISAM ID and ISAM Sequence Numbers")
        ipeIsamId = input('What is the IPE ISAM ID? ')
        ipeIsamSeqNum = input('What is the Sequence Number? ')
        ipedefinition_by_ISAM_instance_ID(ipeIsamId, ipeIsamSeqNum)


# elif answer ==3:
#     choice03()


def choice04():
    system("cls")  # Clear Console
    print("Fulfilment Request Reference")
    print(
        """
    1: Product Summary List
    2: IPE Definition    
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Fulfilment Request Reference")
        card = input('What is the Fulfilment Request Reference? ')
        product_summary_list_by_fulfilment_request_reference(card)
    elif answer == '2':
        system("cls")  # Clear Console
        print("Fulfilment Request Reference")
        card = input('What is the Fulfilment Request Reference? ')
        ipedefinition_by_fulfilment_request_reference(card)


# elif answer ==3:
#     choice03()


def choice05():
    system("cls")  # Clear Console
    print("Passenger Surname")
    print(
        """
    1: Surname
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Passenger Surname")
        card = input('What is the Surname? ')
        cardholder_by_name(card) # Surname Search


# elif answer ==2:
#     choice02()


def choice06():
    system("cls")  # Clear Console
    print("Card Reference")
    print(
        """
    1: Card Details
    """
    )
    answer = input("What option do you want to choose? ")

    if answer == '1':
        system("cls")  # Clear Console
        print("Card Reference")
        card = input('What is the Card Reference? ')
        card_details_by_card_reference(card)


# elif answer ==2:
