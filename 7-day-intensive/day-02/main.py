import json
import os
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# Diretório onde os dados serão armazenados
DATA_DIR = "/app/data"
DATA_FILE = os.path.join(DATA_DIR, "messages.json")

os.makedirs(DATA_DIR, exist_ok=True)
def load_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_messages(messages):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4)

@app.get("/")
def home():
    return jsonify({
        "message": "Docker Intensive - Dia 02",
        "storage": DATA_FILE
    })

@app.get("/messages")
def list_messages():
    return jsonify(load_messages())

@app.post("/messages")
def create_message():
    body = request.get_json()
    messages = load_messages()
    message = {
        "id": len(messages) + 1,
        "text": body["text"],
        "created_at": datetime.now().isoformat()
    }
    messages.append(message)
    save_messages(messages)
    return jsonify(message), 201


@app.delete("/messages")
def clear_messages():
    save_messages([])
    return jsonify({
        "message": "Todos os registros foram removidos."
    })

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)