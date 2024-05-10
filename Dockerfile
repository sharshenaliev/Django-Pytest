FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000