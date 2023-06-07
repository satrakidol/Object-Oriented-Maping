FROM python:alpine3.17

WORKDIR /data

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]