from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # allow requests from any frontend

# store chat messages in memory
chat_log = []

@app.route("/api/chat", methods=["GET"])
def get_chat():
    """Return all chat messages"""
    return jsonify(chat_log)

@app.route("/api/chat", methods=["POST"])
def send_message():
    """Add a message to chat"""
    data = request.json
    user = data.get("user", "Anonymous")
    message = data.get("message", "")
    timestamp = time.strftime("%H:%M:%S")
    chat_entry = {"user": user, "message": message, "time": timestamp}
    chat_log.append(chat_entry)
    return jsonify(chat_entry)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
