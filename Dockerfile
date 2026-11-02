FROM python:3.10.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py seed_watchlist && python manage.py init_kline && gunicorn scrapcoin.wsgi:application --bind 0.0.0.0:8000"]