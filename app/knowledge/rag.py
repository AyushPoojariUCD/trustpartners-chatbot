from openai import OpenAI
from app.knowledge.retriever import retrieve_context
from app.knowledge.retriever import get_trustpartners_collection

client = OpenAI()

def chat_with_knowledge(question: str) -> str:
    collection = get_trustpartners_collection()
    context = retrieve_context(collection, question)

    if context.strip():
        prompt = f"""
                You are a professional assistant.
                Use the context below as the primary source.
                If context is incomplete, you may rely on general knowledge.

                Context:
                {context}

                Question:
                {question}
                """
    else:
        # Fallback to pure ChatGPT
        prompt = question

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
