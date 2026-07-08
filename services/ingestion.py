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

from services.logger import log_header, log_info, log_warning, log_error, log_success

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






#load, split, embed, and store documents in the vectorstore

#añadir, try, await, except, log_error, log_success, log_info, log_warning, log_header
#debo suar tasks? await asyncio.gather? asyncio.create_task? asyncio.run? asyncio.sleep? asyncio.wait? asyncio.as_completed?
#docs #processed, docs failed, docs skipped, docs embedded, docs stored, docs retrieved, docs deleted, 
#create document to langchain
#langgraph for memory save

async def main():
    '''main async funct to orchestrate the ingestion process
    '''
    log_header("Starting the ingestion process...", color="purple")
    log_info("Loading documents from the 'data' directory...", color="blue")

    


    log_success("Ingestion process completed successfully!", color="green")


if __name__ == "__main__":
    asyncio.run(main())