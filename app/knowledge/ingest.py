from uuid import uuid4
from knowledge.chroma_client import get_chroma_collection


def add_documents(
    texts: list[str],
    metadatas: list[dict] | None = None
):
    collection = get_chroma_collection()

    ids = [str(uuid4()) for _ in texts]

    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )
