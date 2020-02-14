FROM orbitalinsight/services3:latest

ADD . /microservice

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

CMD python -u /microservice/app.py