from langchain.chat_models import init_chat_model
from config.settings import settings

llm = init_chat_model(
    f"{settings.llm.provider}:{settings.llm.model}", 
    temperature=settings.llm.temperature,
    base_url=settings.llm.base_url
    )


