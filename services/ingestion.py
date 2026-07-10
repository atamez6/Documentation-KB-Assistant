import asyncio
from settings import settings
import os
import ssl
from typing import Any, Dict, List
import uuid

import certifi
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.documents import Document

from loader import load_pdf,load_pdfs_from_directory


from logger import log_header, log_info, log_warning, log_error, log_success
from get_vectorstore import vectorstore,embeddings

load_dotenv()


text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.text_splitter.chunk_size,
        chunk_overlap=settings.text_splitter.chunk_overlap,
        length_function=len,
    )



#load, split, embed, and store documents in the vectorstore

#añadir, try, await, except, log_error, log_success, log_info, log_warning, log_header
#debo suar tasks? await asyncio.gather? asyncio.create_task? asyncio.run? asyncio.sleep? asyncio.wait? asyncio.as_completed?
#docs #processed, docs failed, docs skipped, docs embedded, docs stored, docs retrieved, docs deleted, 
#create document to langchain
#langgraph for memory save
#asyng gather to upload many files in parallel, but not too many to avoid overloading the system


async def main():
    '''main async funct to orchestrate the ingestion process
    '''
    log_header("Starting the ingestion process...", color="purple")
    
    file_path=settings.documents.source_directory
    documents= await load_pdfs_from_directory(directory_path=file_path)
    chunks = text_splitter.split_documents(documents)
    
    ids = [f"doc_{uuid.uuid4()}" for i in enumerate(chunks)]

    log_info("Loading documents from the 'data' directory...", color="blue")
    print(f"Loaded {len(documents)} documents from the 'data' directory.")
    log_info("Splitting documents into chunks...", color="blue")
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    log_info("Embedding and storing chunks in the vectorstore...", color="blue")
    await vectorstore.aadd_documents(chunks, ids=ids)

    log_success("Ingestion process completed successfully!", color="green")
    return {
        "documents_loaded": len(documents),
        "chunks_created": len(chunks),
        "chunks_stored": len(chunks),
    }
    
    

if __name__ == "__main__":
    asyncio.run(main())