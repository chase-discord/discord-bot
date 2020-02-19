FROM python:3.7-alpine

LABEL com.centurylinklabs.watchtower.enable="true"

RUN apk add --no-cache git

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip pipenv
RUN pipenv install --system

CMD ["python3", "-m", "index"]
