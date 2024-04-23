from fastapi import FastAPI
from twilio.twiml.messaging_response import MessagingResponse
# from twilio.rest import Client

app = FastAPI()


@app.get("/sms")
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""

    # Create a response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")

    # Add a picture message
    # msg.media(
    #     "https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg"
    # )

    # Your Twilio Account SID and Auth Token
    # account_sid = 'AC8934e412298d6b0e41de8c1789015651'
    # auth_token = '1083b10e0fe53c7e24385f10548742eb'

    # # Initialize Twilio client
    # client = Client(account_sid, auth_token)

    # # Send an SMS
    # message = client.messages.create(
    #     body='Hello, this is a test message!',
    #     from_='+12242316269',
    #     to='+251984877774'
    # )

    # print(message.sid)

    return str("///////////////////////////////////")
