FROM python:3.10.6-slim-bullseye

COPY requirements.txt requirements.txt
COPY slow.py slow.py

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=slow.py

ENTRYPOINT flask run --host=0.0.0.0

