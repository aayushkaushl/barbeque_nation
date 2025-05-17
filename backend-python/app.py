from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from chatbot import get_response

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip().lower()
    session = data.get("session", {})

    if "location" not in session:
        if message in ["delhi", "bangalore"]:
            session["location"] = message
            return jsonify({
                "response": f"✅ Welcome to Barbeque Nation {message.capitalize()}! How can I assist you?",
                "session": session
            })
        else:
            return jsonify({
                "response": "🏙️ Please enter your location: Delhi or Bangalore.",
                "session": session
            })
    location = session["location"]
    try:
        with open(f"knowledge_base/{location}.json", "r") as f:
            kb_data = json.load(f)
    except FileNotFoundError:
        return jsonify({
            "response": "❌ Knowledge base for that city not found.",
            "session": session
        })

    response = get_response(message, kb_data)
    return jsonify({"response": response, "session": session})

if __name__ == "__main__":
    app.run(debug=True)
