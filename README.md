README.md
# 🧠 GenAI RAG Chat Assistant

A **Production-Style Generative AI Chat Assistant** built using **Retrieval-Augmented Generation (RAG)**.

This assistant answers user questions by retrieving relevant information from a document knowledge base and generating grounded responses using a Large Language Model (LLM).

The project demonstrates how to combine **embeddings, similarity search, and LLM prompting** to create a reliable AI assistant.

---

# 🚀 Live Demo

Try the deployed application on Hugging Face:

https://huggingface.co/spaces/prasad799596/rag-chat-assistant

---

# 🛠 Tech Stack

Backend:
- Python

AI / ML:
- Sentence Transformers (Embeddings)
- Cosine Similarity Search
- Gemini API (LLM)

Frontend:
- Gradio Chat Interface

Deployment:
- Hugging Face Spaces

---

# 📚 How the System Works

This project follows a **Retrieval-Augmented Generation (RAG)** workflow.

User Question  
↓  
Generate Query Embedding  
↓  
Similarity Search in Vector Store  
↓  
Retrieve Top Relevant Document Chunks  
↓  
Inject Context into LLM Prompt  
↓  
Generate Grounded Answer  

This approach reduces hallucinations and ensures responses are based on the knowledge base.

---

# 📂 Project Structure


rag-chat-assistant
│
├── app.py # Gradio chat interface
├── rag_pipeline.py # RAG pipeline implementation
├── docs.json # Knowledge base documents
├── requirements.txt # Project dependencies
└── README.md


---

# 📄 Document Knowledge Base

Documents are stored in **docs.json**.

Example:

```json
{
  "title": "Reset Password",
  "content": "Users can reset their password from Settings > Security."
}

These documents are:

Chunked into smaller pieces

Converted into embeddings

Stored in a vector store for retrieval

🔎 Similarity Search

The system uses Cosine Similarity to find the most relevant document chunks.

Steps:

Convert user query into embedding

Compare with document embeddings

Retrieve top 3 relevant chunks

Send them to the LLM

🤖 LLM Integration

The assistant uses Google Gemini API to generate responses.

The prompt includes:

Retrieved context

User question

Grounding rules

Example prompt:

Answer the question using the provided context.

Context:
{retrieved_documents}

Question:
{user_question}

If the answer is not found in the context, the assistant responds:

I do not have enough information.
💬 Chat Interface

The user interacts with the assistant through a Gradio-based chat interface.

Features:

Real-time chat

Context-aware responses

Retrieval-based answers

Simple UI

⚙️ Local Setup
1 Install dependencies
pip install -r requirements.txt
2 Set Gemini API key

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Get API key from:

https://aistudio.google.com/app/apikey

3 Run the application
python app.py

Open:

http://localhost:7860
🧪 Example Queries

You can ask questions like:

How can I reset my password?

How do I delete my account?

What payment methods are supported?

How can I cancel my subscription?

📦 Deployment

This project is deployed using Hugging Face Spaces.

Steps:

Create a Space

Upload project files

Install dependencies from requirements.txt

Run app.py

🎯 Assignment Objectives Achieved

✔ Document knowledge base
✔ Embedding generation
✔ Vector similarity search
✔ Retrieval-Augmented Generation
✔ LLM integration
✔ Chat interface
✔ Production-style architecture

👨‍💻 Author

Venkata Siva Prasad
