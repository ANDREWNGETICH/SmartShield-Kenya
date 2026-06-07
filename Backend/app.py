from flask_cors import CORS
from flask import Flask, request, jsonify
from ai_engine import predict_message
from scam_detector import detect_scam

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

    return jsonify({
        "status": keyword_result["status"],
        "keywords": keyword_result["keywords"],
        "ai_prediction": ai_prediction
    })

if __name__ == '__main__':
    app.run(debug=True)