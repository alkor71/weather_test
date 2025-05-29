FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "weather.wsgi:application", "--bind", "0.0.0.0:8000"]
