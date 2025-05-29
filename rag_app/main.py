from fastapi import FastAPI
from pydantic import BaseModel
from rag_app.rag_pipeline import build_rag_pipeline

app = FastAPI()

class QueryInput(BaseModel):
    query: str
    question: str

@app.post("/ask/")
def ask(input: QueryInput):
    chain = build_rag_pipeline(input.query)
    result = chain.run(input.question)
    return {"answer": result}
    """try:
        print(f"Received input: {input}")  # Debugging log
        chain = build_rag_pipeline(input.query)
        print("Pipeline built successfully.")  # Debugging log
        result = chain.run(input.question)
        print(f"Generated result: {result}")  # Debugging log
        return {"answer": result}
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the error
        return {"error": str(e)}"""