from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends

load_dotenv()

client = OpenAI()

app = FastAPI(
    title="Trust Partners RAG Chatbot API",
    description="RAG-based chatbot for Trust Partners using MOM policy content",
    version="1.0.0",
)

# Health Endpoint
@app.get("/health")
def health():
    return {
        "health": "Health endpoint running"
    }

# Chat Endpoint
@app.post("/chat")
def chat():
    return {
        "message": "Chat endpoint running"
    }

# Knowledge Base
@app.get("/knowledge-base")
def knowledge_sources():
    return {
        "message": "Knowledge Base enpoint running"
    }

# Refresh Knowledge Base
@app.post("/knowledge/refresh")
def refresh_knowledge():
    return {
        "message": "Knowledge refresh endpoint"
    }

# Knowledge Status
@app.get("/knowledge-status")
def knowledge_status():
    return {
        "message": "Knowledge status endpoint"
    }

print(client)