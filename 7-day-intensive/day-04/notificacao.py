from flask import Flask, jsonify

app = Flask(__name__)

MESSAGES = [
    {
        "id": 1,
        "title": "Bem-vindo"
    },
    {
        "id": 2,
        "title": "Docker Intensive"
    },
    {
        "id": 3,
        "title": "Dia 03"
    }
]

@app.get("/")
def home():
    return jsonify({
        "service": "notifications",
        "status": "running"
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.get("/messages")
def messages():
    return jsonify(MESSAGES)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)