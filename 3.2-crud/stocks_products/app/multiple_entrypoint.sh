#!/bin/sh

echo "Создание миграций"
python manage.py makemigrations

echo "Применение миграций"
python manage.py migrate

echo "Запуск gunicorn сервера"
gunicorn --config gunicorn_config.py stocks_products.wsgi:application