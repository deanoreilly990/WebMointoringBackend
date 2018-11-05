# Backend function used to communictate with the Twilio app
# https://github.com/twilio/twilio-python

from __future__ import print_function


def constructClient():
    print()
    from twilio.rest import Client
    account = "ACed40bb74aff38e88268a69384af8cd38"
    token = "a626719f8750e7043c8b4211d5d942bf"
    client = Client(account, token)

    return client
