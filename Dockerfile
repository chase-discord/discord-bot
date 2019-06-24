FROM python:alpine

LABEL Name=chase-discord-bot Version=0.0.1

WORKDIR /app
ADD . /app

RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile
CMD ["pipenv", "run", "python3", "-m", "index"]
