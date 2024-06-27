FROM python:3.11-alpine

ENTRYPOINT ["python", "manage.py" , "runserver", "0.0.0.0:5555"]

EXPOSE 5555

WORKDIR /stocks_products

COPY . .

RUN pip install -r requirements.txt