import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#MODEL_NAME = "text-embedding-3-small"
