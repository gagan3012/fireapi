import uvicorn
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
    return {'message': 'Welcome to the sentiment analysis API'}


@app.get('/api/v1/st')
def sentiment_analysis(data: str):
    """
    Sentiment Analysis API
    :param data:
    :return: sentiment
    """
    sentiment = generate(data)

    return sentiment[0]


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
