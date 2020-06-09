FROM python:3.8-slim

COPY src/py /microservice
COPY ops/requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt

CMD python -u /microservice/app.py
