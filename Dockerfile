# Pull base image
FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get -y install libpq-dev gcc
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# SET WORK DIR
WORKDIR /code

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .