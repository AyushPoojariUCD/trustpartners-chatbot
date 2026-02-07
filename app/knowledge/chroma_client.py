import os
import chromadb
from dotenv import load_dotenv
from chromadb.api import ClientAPI
from chromadb.api.models.Collection import Collection
from knowledge.embeddings import openai_embedding_function

load_dotenv()

_client: ClientAPI | None = None
_collection: Collection | None = None


def get_chroma_client() -> ClientAPI:
    global _client
    if _client is None:
        _client = chromadb.CloudClient(
            api_key=os.getenv("CHROMA_API_KEY"),
            tenant=os.getenv("CHROMA_TENANT"),
            database=os.getenv("CHROMA_DATABASE")
        )
    return _client


def get_chroma_collection() -> Collection:
    global _collection

    if _collection is None:
        client = get_chroma_client()
        _collection = client.get_or_create_collection(
            name="knowledge_base",
            embedding_function=openai_embedding_function
        )

    return _collection
