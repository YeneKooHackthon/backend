from fastapi import FastAPI
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.get("/sms")
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""

    # Create a response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")

    # Add a picture message
    msg.media(
        "https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg"
    )

    return str(resp)
