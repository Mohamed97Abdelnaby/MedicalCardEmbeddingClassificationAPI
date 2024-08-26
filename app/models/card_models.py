from pydantic import BaseModel


class CardInput(BaseModel):
    sample_text: str
