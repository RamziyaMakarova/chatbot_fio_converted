FROM python:3.10.12

WORKDIR /home/ramziya/DrinkWater_bot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot_fioinabc.py"]