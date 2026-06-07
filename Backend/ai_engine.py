import pandas as pd
import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build dataset path
dataset_path = os.path.join(
    BASE_DIR,
    "..",
    "datasets",
    "messages.csv"
)

# Load dataset
data = pd.read_csv(dataset_path)


# Split features and labels
X = data["message"]
y = data["label"]


# Convert text into numbers
vectorizer = CountVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# Train model
model = MultinomialNB()

model.fit(X_vectorized, y)


# Prediction function
def predict_message(message):

    transformed_message = vectorizer.transform([message])

    prediction = model.predict(transformed_message)

    return prediction[0]