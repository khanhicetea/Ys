FROM python:3-alpine

ADD requirements.txt /

RUN pip install -r /requirements.txt

ADD . /web

WORKDIR /web

CMD ["/usr/local/bin/gunicorn", "-b 0.0.0.0:8000", "server:api"]