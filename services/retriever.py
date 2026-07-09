import asyncio
from typing import Any, Dict, List
from langchain_core.documents import Document
from logger import log_header, log_info, log_warning, log_error, log_success
from get_vectorstore import vectorstore

def serialize_documents(documents: List[Document]) -> List[Dict[str, Any]]:
        '''serialize documents to a list of dictionaries
        '''
        serialized_docs = []
        for doc in documents:
            serialized_doc = {
                "page_content": doc.page_content,
                "metadata": doc.metadata,
            }
            serialized_docs.append(serialized_doc)
        return serialized_docs
    


async def retrive_documents(query: str, k: int = 2) -> tuple[str, List[Dict]]:
        
        '''retrive documents from the vectorstore based on a query
        '''
        log_info(f"Retrieving documents for query: {query}", color="blue")
        results = await vectorstore.asimilarity_search(query, k=k)
        log_success(f"Retrieved {len(results)} documents for query: {query}", color="green")
        content = "\n\n".join(doc.page_content for doc in results)
        return content, serialize_documents(results)