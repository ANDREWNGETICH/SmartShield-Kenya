from history import add_scan, get_history
from flask import Flask, request, jsonify
from flask_cors import CORS

from scam_detector import detect_scam
from ai_engine import predict_message
from kenya_intelligence import detect_kenyan_scam
from analytics import update_analytics, get_analytics

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "SmartShield Kenya Running"


@app.route('/detect', methods=['POST'])
def detect():

    data = request.json

    message = data.get("message", "")

    keyword_result = detect_scam(message)

    ai_prediction = predict_message(message)

    kenya_result = detect_kenyan_scam(message)

    # Update analytics
    update_analytics(
        keyword_result["status"],
        keyword_result["threat_level"]
    )

    add_scan(
    message,
    ai_prediction,
    keyword_result["threat_level"],
    keyword_result["risk_score"]
)

    return jsonify({
        "confidence_score": min(
    keyword_result["risk_score"] + 10,
    99
),
        "status": keyword_result["status"],
        "keywords": keyword_result["keywords"],
        "risk_score": keyword_result["risk_score"],
        "threat_level": keyword_result["threat_level"],
        "ai_prediction": ai_prediction,
        "kenyan_detected": kenya_result["detected"],
        "kenyan_category": kenya_result["category"]
        
    })


@app.route('/analytics', methods=['GET'])
def analytics():

    return jsonify(get_analytics())


@app.route('/history', methods=['GET'])
def history():

    return jsonify(get_history())

if __name__ == '__main__':
    app.run(debug=True)