from services.llm import llm
from services.retriever import retrive_documents
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


SYSTEM_PROMPT = (
    "You are a helpful assistant that provides accurate and concise answers. "
    "Use the conversation history to understand references like 'it' or 'that' in the user's question. "
    "Also use the provided context and history to understand the user's question and provide an accurate answer. "
    "If the answer is not in the context, respond with 'I don't know.' "
    "You can answer in any language, but you must answer in the same language as the question. "
    "If the question is not clear, ask for clarification. "
    "you can use the context and history to understand the question, but do not assume any information that is  provided in the context or history because it could be wrong use only the information provided as vectorstore to formulate the answer. "
    "search for the answer in the vectorstore and provide the answer based on the retrieved documents; history and context are provided to help you understand the question. "
    "Do not assume any information that is not provided in the context."
    "Even if you already know the answer from your own training, you must NOT use that knowledge."
    "If answering the question requires connecting or inferring a relationship between pieces of information that is not explicitly stated together in the context, respond with 'I don't know.'"
    "search in the history and context for the answer for questions made by the user around the same context, if you cannot find the answer in the context or history, respond with 'I don't know.'"
    "you should always answer as the retrieved data from the vectorstore is your first option, if you cannot find the answer in the context or history, respond with 'I don't know.'"
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Context:\n{context}\n\nQuestion: {question}"),
])

retrieval_chain = (
    prompt_template
    | llm
    | StrOutputParser()
)


def ask(query: dict, history: list = None) -> tuple[str, list[dict]]:
    '''retrieval chain that retrieves documents from the vectorstore and uses llm to answer the query
    '''
    content, serialized_docs = retrive_documents(query["question"])
    if history is None:
        history = []
    print("HISTORY DENTRO DE ASK:", history)
    response = retrieval_chain.invoke({"question": query["question"], "context": content, "history": history})
    return response, serialized_docs


