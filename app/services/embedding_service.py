import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from app.core.config import config

client = OpenAI(api_key=config.OPENAI_API_KEY)


def get_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    embedding = response.data[0].embedding
    return np.array(embedding)


def find_most_similar_card(extracted_embedding, df):
    similarities = df['Embedding'].apply(lambda emb: cosine_similarity([extracted_embedding], [emb])[0][0])
    max_index = similarities.idxmax()
    most_similar_card = df.iloc[max_index]['Card Name']
    similarity_score = similarities[max_index]
    return most_similar_card, similarity_score
