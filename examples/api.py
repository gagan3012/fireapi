from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Sentiment(BaseModel):
    sentiment: str
    sentiment_probability: float

