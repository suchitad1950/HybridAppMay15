import os
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from rag_app.embedder import embed_chunks
from rag_app.chunking import chunk_text
from rag_app.data_loader import get_wikipedia_data
#from dotenv import load_dotenv
#load_dotenv()

def build_rag_pipeline(query: str):
    raw = get_wikipedia_data(query)
    chunks = chunk_text(raw)
    embeddings = embed_chunks(chunks)

    db = FAISS.from_embeddings(chunks, embeddings)
    retriever = db.as_retriever(search_type="similarity", k=3)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="You are an expert AI. Given the context:\n{context}\nAnswer:\n{question}"
    )

    #llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
       raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
    llm = OpenAI(openai_api_key=openai_api_key)
    qa_chain = RetrievalQA(llm=llm, retriever=retriever, prompt=prompt)
    return qa_chain 

