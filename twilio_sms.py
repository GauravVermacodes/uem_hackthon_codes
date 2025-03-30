from twilio.rest import Client

TWILIO_SID = "AC3203fadd097fcdd559c24fa20ed9c320"
TWILIO_AUTH_TOKEN = "900c50bc35109da7e6269f4817bc7d91"
TWILIO_PHONE_NUMBER = "+19472107498"

def send_sms(to_number, message):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to_number
    )
