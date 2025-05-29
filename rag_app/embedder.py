

from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv() 
openai_embed = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
mistral_embed = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def embed_chunks(chunks):

    # Use OpenAI embeddings for the chunks
    openai_vecs = openai_embed.embed_documents(chunks)
    # Use Mistral embeddings for the same chunks
    mistral_vecs = mistral_embed.embed_documents(chunks)
    # simple average hybrid
    hybrid_vecs = [(o + m)/2 for o, m in zip(openai_vecs, mistral_vecs)]
    # normalize the vectors

    return hybrid_vecs
