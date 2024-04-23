from fastapi import FastAPI
from twilio.twiml.messaging_response import MessagingResponse
# from twilio.rest import Client
import requests

end_point=""
app = FastAPI()


# URL of the endpoint
url = 'https://api-geberekoo.onrender.com/predict?plant=corn'

# Path to the image file
image_path = 'D:\gebereKoo\example.jpg'

result = 'failed'
# Open the image file
with open(image_path, 'rb') as file:
    # Set up the form data
    files = {'file': (image_path, file, 'image/jpeg')}
    # Make the POST request
    response = requests.post(url, files=files)

# Print the response from the server
    result = response.text

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

    return result
