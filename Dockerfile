FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc libpq-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY backend/ .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Gunicorn server
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
