import os


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-proj-swG6WDiaeGg7zbdnBv2YT3BlbkFJFS0GuPGIEViys7FqdLNl")
    EXCEL_FILE_PATH = "D:\\EmbeddingClassification\\MedicalCards_with_embeddings.csv"


config = Config()
