scan_history = []


def add_scan(message,
             prediction,
             threat_level,
             risk_score):

    scan_history.append({
        "message": message,
        "prediction": prediction,
        "threat_level": threat_level,
        "risk_score": risk_score
    })


def get_history():

    return scan_history