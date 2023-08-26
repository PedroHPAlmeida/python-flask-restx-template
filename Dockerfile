FROM python:3.8-slim

WORKDIR /app

EXPOSE 8080

ENV HOST=$HOST \
    PORT=$PORT \
    ENV=$ENV

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python run.py
