import json
import numpy as np
import os
import requests
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# -----------------------------
# Load embedding model
# -----------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# Load documents
# -----------------------------
with open("docs.json", "r", encoding="utf-8") as f:
    docs = json.load(f)


# -----------------------------
# Chunk documents
# -----------------------------
def chunk_text(text, chunk_size=80):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


# -----------------------------
# Generate embeddings
# -----------------------------
def get_embedding(text):

    return embedding_model.encode(text)


# -----------------------------
# Build vector store
# -----------------------------
vector_store = []

for doc in docs:

    chunks = chunk_text(doc["content"])

    for chunk in chunks:

        embedding = get_embedding(chunk)

        vector_store.append({
            "text": chunk,
            "embedding": embedding
        })


# -----------------------------
# Similarity Search
# -----------------------------
def search(query, top_k=3):

    query_embedding = get_embedding(query)

    similarities = []

    for item in vector_store:

        sim = cosine_similarity(
            [query_embedding],
            [item["embedding"]]
        )[0][0]

        similarities.append(sim)

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    results = [vector_store[i]["text"] for i in top_indices]
    scores = [similarities[i] for i in top_indices]

    return results, scores


# -----------------------------
# Generate Answer using LLM
# -----------------------------
def generate_answer(context, question, history):

    if not context:
        return "I do not have enough information."

    context_text = "\n".join(context)

    prompt = f"""
Answer the question using the provided context.

Context:
{context_text}

Question:
{question}
"""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(url, json=payload)
        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:

        print("LLM ERROR:", e)

        # Fallback response
        return context[0]