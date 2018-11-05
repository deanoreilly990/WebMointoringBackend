# Backend function used to communictate with the Twilio app
# https://github.com/twilio/twilio-python

from __future__ import print_function


def constructClient():
    print()
    from twilio.rest import Client
    account = ""
    token = ""
    client = Client(account, token)

    return client
