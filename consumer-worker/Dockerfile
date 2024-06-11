FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "src/main.py" ]
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "15557", "--reload"]