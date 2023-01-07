from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random
app = Flask(__name__)
quotes=[
    "Stop Doubting Yourself, Work hard and Make it happen.",
    "Work hard in silence. Let your succes make noise.",
    "Everything looks tough until it's done. Don't give up.",
    "Present is the result of past, but the future is still in your hand.",
    "East or West......You can do it:)",
    "Quitters never win and winners never quit.",
    "There are no shortcuts to any place worth going.",
    "You need not to be perfect, Just be better.",
    "It's the possibility of having a dream come true that makes life interesting.",
    "A winner is a dreamer who never gives up.",
    "Hardwork beats talent when talent doesn't work hard.",
    "Live life king size.",
    "This shall too pass.",
    "Sab ho hi jaata hai bro...Tension na lo:)",
    "Go one step at a time"

]
@app.route("/")
def hello():
    return "Hello"

@app.route("/sms", methods=['POST'])
def sms_reply():
    
    # Fetch the message
    msg = request.form.get('Body')
    # Create reply
    r= random.randint(0,14)
    resp = MessagingResponse()
    resp.message(quotes[r])

    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)