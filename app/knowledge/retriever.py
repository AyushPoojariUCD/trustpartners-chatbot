from knowledge.chroma_client import get_chroma_collection


def retrieve_context(
    query: str,
    k: int = 4
) -> str:
    collection = get_chroma_collection()

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    documents = results["documents"][0]
    return "\n\n".join(documents)
