import asyncio
import os
import ssl
from typing import Any, Dict, List

import certifi
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

from services.logger import log_info, log_warning, log_error, log_success

load_dotenv()


embeddings = OllamaEmbeddings(
    model="text-embedding-3-small", 
    base_url="http://localhost:11434",
    show_progress_bar=True,
    chunk_size=800,
    retriever_kwargs={"search_kwargs": {"k": 3}},
    retry_min_seconds=2,
    )


vectorstore = Chroma(       
    collection_name="kb_assistant",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
    client_settings={"chroma_ssl_verify": ssl.create_default_context(cafile=certifi.where())},
    )










async def main():
    '''main async funct to orchestrate the ingestion process
    '''


if __name__ == "__main__":
    asyncio.run(main())