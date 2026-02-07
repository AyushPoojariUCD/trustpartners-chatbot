import os
from dotenv import load_dotenv
from chromadb.utils import embedding_functions

load_dotenv()

openai_embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-large"
)
