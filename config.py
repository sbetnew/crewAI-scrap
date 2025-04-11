import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Configurações iniciais
load_dotenv()

# Configuração do LLM
def get_llm():
    return ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.6  # 0 a 1
    )