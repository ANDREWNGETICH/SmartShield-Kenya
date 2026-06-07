from flask import Flask, request, jsonify
from scam_detector import detect_scam

app = Flask(__name__)

@app.route('/')
def home():
    return "SmartShield Kenya Running"

@app.route('/detect', methods=['POST'])
def detect():

    data = request.json

    message = data.get("message", "")

    result = detect_scam(message)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)