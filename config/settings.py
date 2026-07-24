from pydantic import BaseModel
from typing import List,Optional
from pydantic_settings import BaseSettings, SettingsConfigDict,YamlConfigSettingsSource, PydanticBaseSettingsSource
import yaml
from pathlib import Path


class TextSplitterSettings(BaseModel):
    chunk_size: int 
    chunk_overlap: int 

class LLMSettings(BaseModel):
    model: str
    temperature: float
    provider: str
    base_url: Optional[str] = None
    api_key: Optional[str] = None



class EmbeddingSettings(BaseModel):
  model_embeddings: str
  base_url_embeddings: str
  provider: str


class ChromaDBSettings(BaseModel):
    chroma_collection_name: str
    chroma_persist_directory: str


class RetrieverSettings(BaseModel):
  top_k: int

class DocumentsSettings(BaseModel):
  source_directory: str
  



class Settings(BaseSettings):
   llm : LLMSettings
   embedding : EmbeddingSettings
   retriever : RetrieverSettings 
   chromadb : ChromaDBSettings
   text_splitter : TextSplitterSettings
   documents : DocumentsSettings

   model_config = SettingsConfigDict(yaml_file=Path(__file__).parent / "config.yaml", env_nested_delimiter="__")

   
   @classmethod
   def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
        ):
        return(
            YamlConfigSettingsSource(settings_cls),
            env_settings,
              )





settings = Settings()