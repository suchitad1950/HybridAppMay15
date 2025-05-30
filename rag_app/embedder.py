

from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
#import os
#from dotenv import load_dotenv
#load_dotenv() 
#openai_embed = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Load OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Load Mistral API key
mistral_api_key = os.getenv("MISTRAL_API_KEY")
if not mistral_api_key:
    raise ValueError("MISTRAL_API_KEY is not set in the environment variables.")

# Initialize OpenAI embeddings
openai_embed = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Initialize Mistral embeddings (assuming HuggingFace embeddings do not require an API key)
mistral_embed = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def embed_chunks(chunks):
    # Use OpenAI embeddings for the chunks
    openai_vecs = openai_embed.embed_documents(chunks)

    # Use Mistral embeddings for the same chunks
    mistral_vecs = mistral_embed.embed_documents(chunks)

    # Simple average hybrid
    hybrid_vecs = [(o + m) / 2 for o, m in zip(openai_vecs, mistral_vecs)]

    # Normalize the vectors (optional, depending on your use case)
    # Example: hybrid_vecs = normalize_vectors(hybrid_vecs)

    return hybrid_vecs