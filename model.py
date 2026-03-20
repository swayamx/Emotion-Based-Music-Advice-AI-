import random

# simple keyword-based emotion detection
def detect_emotion(text):
    text = text.lower()

    if "happy" in text or "good" in text:
        return "happy"
    elif "sad" in text or "depressed" in text:
        return "sad"
    elif "angry" in text:
        return "angry"
    else:
        return "neutral"

# suggestions
def get_response(emotion):
    responses = {
        "happy": {
            "music": ["Happy - Pharrell", "Good Life - OneRepublic"],
            "advice": "Keep spreading positivity!"
        },
        "sad": {
            "music": ["Let Her Go - Passenger", "Fix You - Coldplay"],
            "advice": "It’s okay to feel low. Take small steps forward."
        },
        "angry": {
            "music": ["Stronger - Kanye West", "Believer - Imagine Dragons"],
            "advice": "Take a deep breath and channel your energy wisely."
        },
        "neutral": {
            "music": ["Blinding Lights - The Weeknd"],
            "advice": "Stay balanced and focused."
        }
    }

    return responses[emotion]
