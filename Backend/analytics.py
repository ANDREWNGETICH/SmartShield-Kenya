analytics_data = {
    "total_scans": 0,
    "scam_detected": 0,
    "safe_messages": 0,
    "high_risk": 0
}


def update_analytics(status, threat_level):

    analytics_data["total_scans"] += 1

    if status == "Suspicious":
        analytics_data["scam_detected"] += 1
    else:
        analytics_data["safe_messages"] += 1

    if threat_level == "HIGH":
        analytics_data["high_risk"] += 1


def get_analytics():

    return analytics_data