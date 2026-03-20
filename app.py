from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Response system
def get_response(emotion):
    responses = {
        "happy": {
            "music": ["Happy - Pharrell", "Good Life - OneRepublic"],
            "advice": "Keep spreading positivity!"
        },
        "sad": {
            "music": ["Fix You - Coldplay", "Let Her Go - Passenger"],
            "advice": "Take it slow. Better days will come."
        },
        "angry": {
            "music": ["Believer - Imagine Dragons"],
            "advice": "Pause and breathe. Control your energy."
        }
    }
    return responses.get(emotion, {
        "music": ["Blinding Lights"],
        "advice": "Stay balanced."
    })

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json["text"]

    # Convert text → vector
    vector = vectorizer.transform([text])

    # Predict emotion
    emotion = model.predict(vector)[0]

    response = get_response(emotion)

    return jsonify({
        "emotion": emotion,
        "music": response["music"],
        "advice": response["advice"]
    })

if __name__ == "__main__":
    app.run(debug=True)
