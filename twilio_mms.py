# from fastapi import FastAPI
# from twilio.twiml.messaging_response import MessagingResponse
# # from twilio.rest import Client
# import requests

# end_point=""
# app = FastAPI()


# # URL of the endpoint
# url = 'https://api-geberekoo.onrender.com/predict?plant=corn'

# # Path to the image file
# image_path = 'D:\gebereKoo\example.jpg'

# result = 'failed'
# # Open the image file
# with open(image_path, 'rb') as file:
#     # Set up the form data
#     files = {'file': (image_path, file, 'image/jpeg')}
#     # Make the POST request
#     response = requests.post(url, files=files)

# # Print the response from the server
#     result = response.text

# @app.get("/sms")
# def sms_reply():
#     """Respond to incoming messages with a friendly SMS."""

#     # Create a response
#     resp = MessagingResponse()

#     # Add a text message
#     # msg = resp.message("The Robots are coming! Head for the hills!")


#     return result
from fastapi import FastAPI, HTTPException
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = FastAPI()

@app.get("/sms")
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""

    # URL of the endpoint
    url = 'https://api-geberekoo.onrender.com/predict?plant=corn'

    # Path to the image file
    image_path = 'example.jpg'

    try:
        # Open the image file
        with open(image_path, 'rb') as file:
            # Set up the form data
            files = {'file': (image_path, file, 'image/jpeg')}
            # Make the POST request
            response = requests.post(url, files=files)
            # Get the result
            result = response.text
            return result
    except Exception as e:
        # If an error occurs, return an HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail=str(e))
