import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

def load_data(file_path):
    data = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" ::: ")

            if len(parts) >= 4:
                movie_id = parts[0]
                title = parts[1]
                genre = parts[2]
                description = " ::: ".join(parts[3:])

                data.append([title, genre, description])

    return pd.DataFrame(
        data,
        columns=["title", "genre", "description"]
    )

df = load_data("dataset/train_data.txt")

X = df["description"]
y = df["genre"]

tfidf = TfidfVectorizer(
    stop_words="english",
    max_features=10000
)

X_tfidf = tfidf.fit_transform(X)

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_tfidf, y)

joblib.dump(model, "model/genre_model.pkl")
joblib.dump(tfidf, "model/tfidf.pkl")

print("Model saved successfully")