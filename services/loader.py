
from langchain_community.document_loaders import PyPDFLoader
import asyncio
from config.settings import settings
from langchain_core.documents import Document
import os
from services.logger import log_info,log_warning,log_error,log_success

async def load_pdf(file_path:str)-> list[Document]:
    '''load a pdf file saved on DATA directory with pypdfloader and return the text content as a string'''
    try:
        loader = PyPDFLoader(file_path)
        log_info(f"Loading PDF file {file_path}...", color="blue")
        return await loader.aload()
    except Exception as e:
        log_error(f"Error loading PDF file {file_path}: {e}", color="red")
        return []
    


accepted_file_extensions = settings.documents.accepted_file_extensions

async def load_pdfs_from_directory(directory_path: str):

    '''load all pdf files from a directory and return a list of Document objects'''
    results = []
    try:
        tasks = [load_pdf(os.path.join(directory_path,f))for f in os.listdir(directory_path) if f.endswith(tuple(accepted_file_extensions))]
        all_docs = await asyncio.gather(*tasks)
        for doc in all_docs:
            if doc:
                results.extend(doc)
                log_success(f"Loaded {len(doc)} documents from {doc[0].metadata['source']}", color="green")
            else:
                log_warning(f"A File failed while loading", color="yellow")
    except Exception as e:
        log_error(f"Error loading PDF files from directory {directory_path}: {e}", color="red")
    return results




