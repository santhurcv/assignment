FROM python:3

WORKDIR /app

ENV FLASK_APP=run.py

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]