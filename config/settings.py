from pydantic import BaseModel
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict,YamlConfigSettingsSource, PydanticBaseSettingsSource
import yaml

class TextSplitterSettings(BaseModel):
    chunk_size: int 
    chunk_overlap: int 

class LLMSettings(BaseModel):
    model: str
    temperature: float
    base_url: str
    provider: str


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
  accepted_file_extensions: list[str]



class Settins(BaseSettings):
   llm : LLMSettings
   embedding : EmbeddingSettings
   retriever : RetrieverSettings 
   chromadb : ChromaDBSettings
   text_splitter : TextSplitterSettings
   documents : DocumentsSettings

   model_config = SettingsConfigDict(yaml_file="config.yaml")

