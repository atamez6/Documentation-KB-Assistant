from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredExcelLoader
import asyncio
from config.settings import settings
from langchain_core.documents import Document
import os
from langchain_community.document_loaders import Docx2txtLoader
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


async def load_docx(file_path:str)-> list[Document]:
    '''load a docx file saved on DATA directory with docxloader and return the text content as a string'''
    try:

        loader = Docx2txtLoader(file_path)
        log_info(f"Loading DOCX file {file_path}...", color="blue")
        return await loader.aload()
    except Exception as e:
        log_error(f"Error loading DOCX file {file_path}: {e}", color="red")
        return []

async def load_txt(file_path:str)-> list[Document]:
    '''load a txt file saved on DATA directory with textloader and return the text content as a string'''
    try:
        loader = TextLoader(file_path,autodetect_encoding=True)
        log_info(f"Loading TXT file {file_path}...", color="blue")
        return await loader.aload()
    except Exception as e:
        log_error(f"Error loading TXT file {file_path}: {e}", color="red")
        return []

async def load_xlsx(file_path:str)-> list[Document]:
    '''load a xlsx file saved on DATA directory with textloader and return the text content as a string'''
    try:
        loader = UnstructuredExcelLoader(file_path)
        log_info(f"Loading XLSX file {file_path}...", color="blue")
        return await loader.aload()
    except Exception as e:
        log_error(f"Error loading XLSX file {file_path}: {e}", color="red")
        return []

loaders = {
    '.pdf': load_pdf,
    '.docx': load_docx,
    '.txt': load_txt,
    '.md': load_txt,
    '.xlsx': load_xlsx,
}

accepted_file_extensions = loaders.keys()


async def load_pdfs_from_directory(directory_path: str):

    '''load  accepted files from a directory and return a list of Document objects'''
    results = []
    try:
        tasks = [loaders[os.path.splitext(f)[1].lower()](os.path.join(directory_path,f)) for f in os.listdir(directory_path) if f.lower().endswith(tuple(accepted_file_extensions))]
        all_docs = await asyncio.gather(*tasks)
        for doc in all_docs:
            if doc:
                results.extend(doc)
                log_success(f"Loaded {len(doc)} documents from {doc[0].metadata['source']}", color="green")
            else:
                log_warning(f"A File failed while loading", color="yellow")
    except Exception as e:
        log_error(f"Error loading files from directory {directory_path}: {e}", color="red")
    return results




