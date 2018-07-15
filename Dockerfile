FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapp
WORKDIR /webapp
ADD . /webapp
RUN pip3 install -r requirements.txt