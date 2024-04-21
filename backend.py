from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Get the message the user sent our Twilio number
    incoming_msg = request.values.get('Body', '')

    # Create a response
    resp = MessagingResponse()

    # Determine the appropriate response
    if 'hello' in incoming_msg.lower():
        # If the user said 'hello', respond with a greeting
        resp.message("Hi there! 👋")
    else:
        # For all other messages, say you didn't understand
        resp.message("I'm sorry, I didn't understand that. Try sending 'hello'.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
