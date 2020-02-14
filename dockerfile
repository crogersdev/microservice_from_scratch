FROM orbitalinsight/services3:latest

ADD app.py /
ADD api_v1.py /

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

CMD [ "python3.8", "./app.py" ]