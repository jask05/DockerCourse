FROM python:2.7

WORKDIR /app

EXPOSE 5000

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD counter.py /app/counter.py

CMD ["python", "counter.py"]


