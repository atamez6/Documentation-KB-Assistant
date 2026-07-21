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

async def get_context(query:str):
    '''get context from the vectorstore based on a query
    '''
    content, _ = await retrive_documents(query["question"])
    return content


async def get_serialized_docs(query:str):
    '''get serialized documents from the vectorstore based on a query
    '''
    _, serialized_docs = await retrive_documents(query)
    return serialized_docs


retrieval_chain = (RunnablePassthrough.assign(context=get_context)
                    |prompt_template
                    |llm
                    |StrOutputParser())


async def ask(query: str):
    '''retrieval chain that retrieves documents from the vectorstore and uses llm to answer the query
    '''
    response = await retrieval_chain.ainvoke({"question": query})                                             
    return response




print(asyncio.run(ask("what is the capital of Japan?")))