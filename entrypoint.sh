python manage.py collectstatic
python manage.py migrate
#python manage.py loaddata data.json
gunicorn config.wsgi:application --bind 0.0.0.0:8000
