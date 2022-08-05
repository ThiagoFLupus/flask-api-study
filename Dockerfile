FROM python:3

RUN apt-get update -y
ADD . /var/www/
WORKDIR /var/www/
RUN pip install -r backend/requirements.txt
CMD python backend/server.py