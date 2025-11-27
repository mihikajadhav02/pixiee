#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations (skip if DATABASE_URL is not set during build)
if [ -n "$DATABASE_URL" ] || [ -n "$POSTGRES_URL" ]; then
    echo "Running migrations..."
    python manage.py migrate --noinput || echo "Migrations will run on first request"
fi

# Collect static files
python manage.py collectstatic --noinput
