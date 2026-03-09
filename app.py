from flask import Flask, request, jsonify, render_template
from rag_pipeline import search, generate_answer

app = Flask(__name__)

# Store conversation sessions
sessions = {}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.json

    session_id = data.get("sessionId")
    message = data.get("message")

    if not session_id or not message:
        return jsonify({"error": "Invalid input"}), 400

    # Create session if not exists
    if session_id not in sessions:
        sessions[session_id] = []

    # Get last 5 messages
    history = sessions[session_id][-5:]

    # -----------------------------
    # Retrieve relevant document chunks
    # -----------------------------
    chunks, scores = search(message)

    print("\nUser Question:", message)
    print("Retrieved Chunks:", chunks)
    print("Similarity Scores:", scores)

    # If no good match found
    if not scores or max(scores) < 0.05:
        return jsonify({
            "reply": "Sorry, I do not have enough information.",
            "retrievedChunks": 0,
            "tokensUsed": 0
        })

    # -----------------------------
    # Generate response from LLM
    # -----------------------------
    reply = generate_answer(chunks, message, history)

    # Save conversation
    sessions[session_id].append({
        "user": message,
        "assistant": reply
    })

    return jsonify({
        "reply": reply,
        "retrievedChunks": len(chunks),
        "tokensUsed": 120
    })


if __name__ == "__main__":
    app.run(debug=True)