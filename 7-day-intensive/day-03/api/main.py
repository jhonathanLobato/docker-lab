from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "service": "api",
        "status": "running"
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.get("/notifications")
def notifications():
    response = requests.get(
        "http://notifications:5050/messages",
        timeout=5
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)