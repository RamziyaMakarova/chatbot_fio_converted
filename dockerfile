FROM python:3.10.12

COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app

ENV TOKEN=your_token_value

CMD ["python", "bot_fioinabc.py"]
