from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from settings import settings

embeddings = OllamaEmbeddings(
    model=settings.embedding.model_embeddings, 
    base_url=settings.embedding.base_url_embeddings,
    )


vectorstore = Chroma(       
    collection_name=settings.chromadb.chroma_collection_name,
    embedding_function=embeddings,
    persist_directory=settings.chromadb.chroma_persist_directory,
    )