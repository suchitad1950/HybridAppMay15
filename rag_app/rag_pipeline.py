import os
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from rag_app.embedder import embed_chunks
from rag_app.chunking import chunk_text
from rag_app.data_loader import get_wikipedia_data

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

    llm = OpenAI(openai_api_key=os.getenv("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"))
    qa_chain = RetrievalQA(llm=llm, retriever=retriever, prompt=prompt)
    return qa_chain 

