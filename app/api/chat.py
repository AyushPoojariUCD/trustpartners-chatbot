from fastapi import APIRouter, Depends
from pydantic import BaseModel
from chromadb.api.models.Collection import Collection
from openai import OpenAI

from knowledge.chroma_client import get_chroma_collection
from knowledge.retriever import retrieve_context

router = APIRouter()
client = OpenAI()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(
    req: ChatRequest,
    collection: Collection = Depends(get_chroma_collection)
):
    # Retrieve relevant knowledge
    context = retrieve_context(collection, req.question)

    # Inject context into OpenAI
    prompt = f"""
You are a professional assistant.
Answer ONLY using the context below.
If the answer is not present, say "I don’t know."

Context:
{context}

Question:
{req.question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return {
        "answer": response.choices[0].message.content
    }
