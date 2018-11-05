# Backend function used to communictate with the Twilio app
# https://github.com/twilio/twilio-python



def constructClient():
    from controller import logger_Global
    logger = logger_Global()
    logger.info('Client contructed TWilio - 200')
    from twilio.rest import Client
    import json
    with open('config.json') as f:
        data = json.load(f)
    account = data['twilio']['accessKey']
    token = data['twilio']['secretKey']
    outboundNumber = data['twilio']['outboundNumber']
    InboundNumber = data['twilio']['TwilioNumber']
    client = Client(account, token)
    return client, outboundNumber, InboundNumber


def sendEmergencyMessage(EmegencyMessage):
    # Function designed to send an emergency SMS to endpoint
    from controller import logger_Global
    logger = logger_Global()
    logger.info('Emergency Message Invoked - Emergency In Place')
    logger.info(EmegencyMessage)
    client, outbound, TwilioNum = constructClient()
    message = client.messages.create(to=outbound, from_=TwilioNum,
                                     body=EmegencyMessage)
    logger.info(message)
