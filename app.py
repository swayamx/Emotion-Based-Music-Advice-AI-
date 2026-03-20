from flask import Flask, request, jsonify
from model import detect_emotion, get_response

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data["text"]

    emotion = detect_emotion(text)
    response = get_response(emotion)

    return jsonify({
        "emotion": emotion,
        "music": response["music"],
        "advice": response["advice"]
    })

if __name__ == "__main__":
    app.run(debug=True)
