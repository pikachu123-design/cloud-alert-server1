from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    msg = data.get("message", "Alert received")

    # Send Telegram message
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=payload)

    return {"status": "ok", "sent": msg}

@app.route("/")
def home():
    return "Cloud Server Running"

