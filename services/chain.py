from operator import itemgetter


from services.llm import llm
from services.retriever import retrive_documents
import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough





SYSTEM_PROMPT = (
    "You are a helpful assistant that provides accurate and concise answers "
    "based on the provided context. "
    "If the answer is not in the context, respond with 'I don't know.' "
    "You can answer in any language, but you must answer in the same "
    "language as the question. "
    "If the question is not clear, ask for clarification. "
    "Do not assume any information that is not provided in the context."
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "Context:\n{context}\n\nQuestion: {question}"),
])




retrieval_chain = (
    prompt_template
    | llm
    | StrOutputParser()
)







def ask(query: dict):
    '''retrieval chain that retrieves documents from the vectorstore and uses llm to answer the query
    '''
    content, serialized_docs = retrive_documents(query["question"])
    response =  retrieval_chain.invoke({"question": query["question"], "context": content})
    return response,serialized_docs


