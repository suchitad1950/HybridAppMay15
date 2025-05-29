

from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
#import os
#from dotenv import load_dotenv
#load_dotenv() 
#openai_embed = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from a .env file
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
openai_embed = OpenAIEmbeddings(openai_api_key=openai_api_key)
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
