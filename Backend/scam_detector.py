scam_keywords = [
    "urgent",
    "verify your account",
    "click here",
    "winner",
    "free money",
    "mpesa reversal",
    "password reset",
    "limited offer"
]

def detect_scam(message):

    message = message.lower()

    detected_keywords = []

    for keyword in scam_keywords:
        if keyword in message:
            detected_keywords.append(keyword)

    if detected_keywords:
        return {
            "status": "Suspicious",
            "keywords": detected_keywords
        }

    return {
        "status": "Safe",
        "keywords": []
    }