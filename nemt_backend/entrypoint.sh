#!/bin/sh
    echo "Waiting for postgres to load..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done
    echo "Step 3: Running all migrations again..."
    python manage.py migrate --no-input

exec "$@"

