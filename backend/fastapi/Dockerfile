FROM python:3.9-slim-buster

WORKDIR /code/app

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD [ "python", "main.py" ]
