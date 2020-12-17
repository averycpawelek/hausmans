FROM python:3
MAINTAINER "Avery Pawelek"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /
COPY ./packaging/docker/docker-entrypoint.sh /

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./src/hausmans /app/

RUN mkdir /app/media/
RUN adduser --disabled-password --gecos "" django
RUN chown -R django:django /app/

USER django
ENTRYPOINT ["/docker-entrypoint.sh"]
