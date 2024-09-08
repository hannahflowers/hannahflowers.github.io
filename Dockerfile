FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV EMAIL_ID=hannahflowersg@gmail.com EMAIL_PW=psvidztuoloupxqh

COPY . .

CMD python manage.py runserver 0.0.0.0:8080