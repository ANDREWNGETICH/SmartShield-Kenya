import pandas as pd
import os

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full dataset path
dataset_path = os.path.join(
    BASE_DIR,
    "..",
    "datasets",
    "kenya_scams.csv"
)

# Load dataset
data = pd.read_csv(dataset_path)


def detect_kenyan_scam(message):

    message = message.lower()

    for index, row in data.iterrows():

        stored_message = row["message"].lower()

        if any(word in message for word in stored_message.split()):

            return {
                "detected": True,
                "category": row["category"]
            }

    return {
        "detected": False,
        "category": "None"
    }