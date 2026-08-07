from fastapi import FastAPI
from pydantic import BaseModel
from services.chain import ask

app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    history: list = []

@app.post("/query")
def query(request: QueryRequest):
    response, docs = ask(
        {"question": request.question},
        history=request.history
    )
    return {"answer": response, "sources": docs}