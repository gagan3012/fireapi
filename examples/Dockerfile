FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt .

COPY ./model /model/

COPY ./api .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "api.py"]