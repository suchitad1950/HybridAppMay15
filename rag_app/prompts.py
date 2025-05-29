from langchain.prompts import PromptTemplate

# Standard QA Prompt for RAG
rag_prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful and intelligent assistant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""
)

# Optional: Condensed prompt for summarization
summarization_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Summarize the following text into a concise paragraph:

{text}
"""
)

# Optional: Prompt for answering based on a specific dataset/domain
domain_specific_prompt = PromptTemplate(
    input_variables=["domain", "context", "question"],
    template="""
You are an expert in {domain}. Use the context below to answer the question specifically and accurately.

Context:
{context}

Question:
{question}

Answer:
"""
)