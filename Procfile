web gunicorn app:app
pg:reset DATABASE_URL
release: python manage.py db init && python manage.py db migrate && python manage.py db upgrade