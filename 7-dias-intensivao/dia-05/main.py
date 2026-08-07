from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Docker Intensive - Dia 01",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/users")
def users():
    return jsonify([
        {
            "id": 1,
            "name": "Alice"
        },
        {
            "id": 2,
            "name": "Bob"
        },
        {
            "id": 3,
            "name": "Charlie"
        },
        {
            "id": 4,
            "name": "Outro Nome"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    