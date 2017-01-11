FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /simplemailsender
WORKDIR /simplemailsender
ADD requirements.txt /simplemailsender/
RUN pip install -r requirements.txt
ADD . /simplemailsender