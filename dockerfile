FROM python:slim

WORKDIR /app

COPY requirements.txt .


ENV TOKEN='your token'

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot_fioinabc.py"]
