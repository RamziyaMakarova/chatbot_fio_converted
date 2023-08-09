FROM python:slim

WORKDIR /app

COPY requirements.txt .


ENV TOKEN='6509267030:AAFahfIPO2efBen5dLLjmjJ7s5uYy6hGmVY'

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot_fioinabc.py"]
