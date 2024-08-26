from fastapi import APIRouter, HTTPException, Form
from app.services.embedding_service import get_embedding, find_most_similar_card
from app.services.file_service import load_excel_file, save_excel_file
from app.models.card_models import CardInput
import pandas as pd
import numpy as np

router = APIRouter()


@router.post("/find_similar_card/")
async def find_similar_card(card_input: CardInput):
    try:
        df = load_excel_file()

        # Generate embedding for the input text
        input_embedding = get_embedding(card_input.sample_text)

        # Find the most similar card
        most_similar_card, similarity = find_most_similar_card(input_embedding, df)

        return {
            "most_similar_card": most_similar_card,
            "similarity": similarity
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_new_card/")
async def add_new_card(card_name: str = Form(...), sample_text: str = Form(...)):
    try:
        df = load_excel_file()

        # Generate embedding for the new card's sample text
        new_embedding = get_embedding(sample_text)

        # Append the new card to the DataFrame
        new_row = pd.DataFrame({
            'Card Name': [card_name],
            'Sample Text': [sample_text],
            'Embedding': [new_embedding]
        })
        df = pd.concat([df, new_row], ignore_index=True)

        # Save the updated DataFrame back to the CSV file
        save_excel_file(df)

        return {"message": "New card added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
