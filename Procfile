web: gunicorn --bind :8000 --workers 3 --threads 2 tender.wsgi:application
websocket: daphne -b 0.0.0.0 -p 5000 tender.asgi:application