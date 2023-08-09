FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV TOKEN='6045201299:AAGgT6aR7avmn3BCCMmt8HV5N8aHu78S3SI'

CMD ["python", "bot_fioinabc.py"]
