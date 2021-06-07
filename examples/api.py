from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Sentiment(BaseModel):
    sentiment: str
    sentiment_probability: float


nlp = pipeline("sentiment-analysis",
               model="distilbert-base-uncased-finetuned-sst-2-english",
               tokenizer="distilbert-base-uncased-finetuned-sst-2-english")


def generate(data):
    return nlp(data)


@app.get('/')
def get_root():


def sentiment_analysis(data: str):
    """
    :param data:
    :return: sentiment
    sentiment = generate(data)

    return sentiment[0]
