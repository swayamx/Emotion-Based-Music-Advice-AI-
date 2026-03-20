import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset (you can expand this)
data = {
    "text": [
        "I feel very happy today",
        "I am so sad and tired",
        "I am angry right now",
        "I feel amazing and joyful",
        "I am depressed and lonely",
        "I am frustrated and mad"
    ],
    "emotion": [
        "happy",
        "sad",
        "angry",
        "happy",
        "sad",
        "angry"
    ]
}

df = pd.DataFrame(data)

# Convert text → numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["emotion"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model + vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved!")
