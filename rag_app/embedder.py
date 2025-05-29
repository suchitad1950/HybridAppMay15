

from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
import os
openai_embed = OpenAIEmbeddings(openai_api_key="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")
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
