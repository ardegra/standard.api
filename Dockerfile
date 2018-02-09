FROM python:3

ADD . /root/app
WORKDIR /root/app

RUN pip install -r requirements.txt

EXPOSE 8002

CMD gunicorn run:api -b 0.0.0.0:8002 --reload