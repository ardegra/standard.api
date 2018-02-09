FROM python:3

ADD . /root/app
WORKDIR /root/app

RUN ls
RUN pip install -r requirements.txt

CMD python agent.py