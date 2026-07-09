from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text", 
    base_url="http://localhost:11434",
    )


vectorstore = Chroma(       
    collection_name="kb_assistant",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
    #client_settings={"chroma_ssl_verify": ssl.create_default_context(cafile=certifi.where())},
    )