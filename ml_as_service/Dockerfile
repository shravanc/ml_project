# pull official base image
#FROM python:3.8.0-alpine
FROM python:3.6

RUN apt-get update

RUN mkdir /app
WORKDIR /app
COPY . /app


# set work directory
#WORKDIR /usr/src/app
# set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install -U pip
RUN pip install -U setuptools

#RUN pip install --upgrade pip
#COPY ./requirements.txt /usr/src/app/requirements.txt
#RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# copy project
EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
