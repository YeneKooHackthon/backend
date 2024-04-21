from fastapi import FastAPI
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.get("/sms")
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""

    # Create a response
    resp = MessagingResponse()
    
    return 'abcd'
