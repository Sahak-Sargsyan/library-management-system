#!/bin/bash
set -e

# Wait for Postgres to be ready
echo "Waiting for Postgres..."
until pg_isready -h db -p 5432 -U library_user; do
  sleep 1
done

# Run migrations
echo "Running Alembic migrations..."
alembic upgrade head

# Start FastAPI app
echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
