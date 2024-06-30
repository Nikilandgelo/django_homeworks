FROM python:3.11-alpine

WORKDIR /app
EXPOSE 5555

# Установка зависимости для psycopg2 (apk потому что alpine == apt install ubuntu)
RUN apk add postgresql-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT sh multiple_entrypoint.sh