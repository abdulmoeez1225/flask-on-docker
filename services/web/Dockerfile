# pull official base image
FROM python:3.10.7-slim-buster

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install python3-numpy python3-scipy 
RUN apt install -y netcat



# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

RUN ls -lsa

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
