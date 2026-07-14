from langchain_core.prompts import ChatPromptTemplate

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