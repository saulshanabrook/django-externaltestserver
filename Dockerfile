FROM python:3.5

COPY test_project/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt

COPY . /externalliveserver
RUN pip install -e /externalliveserver

COPY test_project /app/
