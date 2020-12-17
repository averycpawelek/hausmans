#!/bin/bash

echo "Running entrypoint script.."

if [ $ENVIRONMENT == "dev" ]; then
    echo "DEBUG is enabled!"
    python3 manage.py runserver 0.0.0.0:8000
else
    echo "DEBUG is disabled!"
    python3 manage.py migrate
    python3 manage.py collectstatic --no-input
    gunicorn hausmans.wsgi -b 0.0.0.0:8000
fi
