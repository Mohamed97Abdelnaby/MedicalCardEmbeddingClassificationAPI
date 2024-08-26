import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EXCEL_FILE_PATH = "D:\\EmbeddingClassification\\MedicalCards_with_embeddings.csv"


config = Config()
