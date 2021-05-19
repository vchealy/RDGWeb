# request_functions.py
"""
Create an API GET Request
and save to JSON
"""
import requests
from auth import headers, url


def card_details_ISRN(queried="633597024930003352"):
    "Staging Get Card Details by ISRN"
    path = "/tms/cm/shell/"
    query = str(queried)
    target = url + path + query

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def journey_taps_ISRN(queried="633597024930003014"):
    "Staging Get Journey Taps by ISRN"
    path = "/portal/history"
    query = "?isrn="
    query2 = str(queried)
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def journey_by_ticket_ID(queried="66698"):
    "Staging Get Journey by Ticket ID"
    path = "generic/ipe/pj"
    query = "?ticketId="
    query2 = str(queried)
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def product_long_by_ticket_ID(queried="66697"):
    "Staging Get Product Long by Ticket ID"
    path = "/generic/ipe/"
    query = str(queried)
    target = url + path + query

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def products_summary_list_ISAM_instance_ID(
    ipeIsamId="07C06DC7", ipeIsamSeqNum="000072"
):
    "Staging Get ProductSummaryList by ISAM Instance ID"
    path = "/generic/ipe/search"
    query = "?ipeIsamId="
    query1b = str(ipeIsamId)
    query = query + query1b
    query2 = "&ipeIsamSeqNum="
    query2b = ipeIsamSeqNum
    query2 = query2 + query2b
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def product_summary_list_by_fulfilment_request_reference(
    fulfilmentRequestReference="WLU00abcb26-79ce-4d0f-a343-e1492131cf20",
):
    "Staging Get ProductSummaryList by Fulfilment Request Refrence"
    path = "/generic/ipe/search"
    query = "?fulfilmentRequestReference="
    query2 = str(fulfilmentRequestReference)
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def product_summary_list_by_ISRN(isrn="633597024930003733"):
    "Staging Get ProductSummaryList by ISRN"
    path = "/generic/ipe/search"
    query = "?isrn="
    query2 = str(isrn)
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def ipedefinition_by_ISAM_instance_ID(ipeIsamId="7B06DC7", ipeIsamSeqNum="000072"):
    "Staging Get IpeDefinition by ISAM Instance ID"
    path = "/generic/ipe/id?ipeIsamId=07B06DC7&ipeIsamSeqNum=000072"
    query = "?ipeIsamId="
    query1b = str(ipeIsamId)
    query = query + query1b
    query2 = "&ipeIsamSeqNum="
    query2b = str(ipeIsamSeqNum)
    query2 = query2 + query2b
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def ipedefinition_by_fulfilment_request_reference(queried="WLP012GW95BKR320208"):
    "Staging Get ipeDefinition by Fulfilment Request Refrence"
    path = "/generic/ipe/id"
    query = "?fulfilmentRequestReference="
    query2 = str(queried)
    target = url + path + query + query2

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def cardholder_by_name(lastname="Gray"):
    "Staging Get CardHolder by Name"
    path = "/generic/cardholder/search"
    query = "?surname="
    query2 = str(lastname)
    print(lastname)
    target = url + path + query + query2
    print(target)

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text


def card_details_by_card_reference(queried="WLU009GB27499901919"):
    "Staging Get CardDetails by Card Reference"
    path = "/tms/cm/"
    query = str(queried)
    print(queried)
    target = url + path + query

    x = requests.get(target, headers=headers)

    if x:
        print("Response OK")
    else:
        print("Response Failed")

    return x.status_code, x.text
