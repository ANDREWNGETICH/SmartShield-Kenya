import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB


# Load dataset
data = pd.read_csv("../datasets/messages.csv")


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