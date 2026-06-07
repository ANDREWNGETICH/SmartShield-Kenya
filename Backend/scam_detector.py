scam_keywords = [
    "urgent",
    "verify your account",
    "click here",
    "winner",
    "free money",
    "mpesa reversal",
    "password reset",
    "limited offer",
    "bank account",
    "confirm details",
    "login now",
    "suspended"
]


def detect_scam(message):

    message = message.lower()

    detected_keywords = []

    risk_score = 0

    for keyword in scam_keywords:

        if keyword in message:

            detected_keywords.append(keyword)

            risk_score += 15


    # Limit risk score to 100
    if risk_score > 100:
        risk_score = 100


    # Determine threat level
    if risk_score >= 70:
        threat_level = "HIGH"

    elif risk_score >= 40:
        threat_level = "MEDIUM"

    elif risk_score > 0:
        threat_level = "LOW"

    else:
        threat_level = "SAFE"


    # Determine status
    if detected_keywords:
        status = "Suspicious"
    else:
        status = "Safe"


    return {
        "status": status,
        "keywords": detected_keywords,
        "risk_score": risk_score,
        "threat_level": threat_level
    }