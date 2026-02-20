#!/bin/sh
    echo "Waiting for postgres to load..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done
    echo "Step 3: Running all migrations again..."
    python manage.py migrate --no-input

# 2. Create superuser
# We use || true to prevent the script from failing if the user already exists
echo "Creating superuser..."
python manage.py createsuperuser --noinput || echo "Superuser already exists or creation failed."

exec "$@"

