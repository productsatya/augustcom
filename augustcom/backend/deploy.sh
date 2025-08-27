#!/bin/bash

# Backend Deployment Script
echo "🚀 Starting backend deployment..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "🌐 Starting Gunicorn server..."
gunicorn shopcore.wsgi:application --bind 0.0.0.0:$PORT --workers 3
