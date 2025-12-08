# Mini Project: Containerize a Flask Application
# ===============================================
# This project guides you through containerizing a complete Flask application
# with a database and Redis cache.

## Project Overview

This mini project will teach you how to:
1. Create a complete Flask application
2. Write a production-ready Dockerfile
3. Create a docker-compose.yml for multi-service setup
4. Test and deploy your containerized application

## Project Structure

```
flask_docker_project/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── templates/
│   └── index.html
├── requirements.txt
├── config.py
├── run.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .env.example
```

## Step 1: Create the Flask Application

### app/__init__.py
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
import os

db = SQLAlchemy()
cache = None

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 
        'sqlite:///app.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db.init_app(app)
    
    # Initialize Redis cache
    global cache
    redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')
    cache = redis.from_url(redis_url)
    
    # Register routes
    from app.routes import main
    app.register_blueprint(main)
    
    return app
```

### app/routes.py
```python
from flask import Blueprint, render_template, jsonify
from app import db, cache
from app.models import Visit

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Increment visit count in Redis
    visits = cache.incr('visits')
    
    # Save to database
    visit = Visit()
    db.session.add(visit)
    db.session.commit()
    
    return render_template('index.html', visits=visits)

@main.route('/api/stats')
def stats():
    total_visits = cache.get('visits')
    db_count = Visit.query.count()
    return jsonify({
        'redis_visits': int(total_visits) if total_visits else 0,
        'db_count': db_count
    })

@main.route('/health')
def health():
    return jsonify({'status': 'healthy'})
```

### app/models.py
```python
from app import db
from datetime import datetime

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
```

### templates/index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Docker Demo</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: #0066cc; }
        .stats { font-size: 24px; margin: 20px; }
    </style>
</head>
<body>
    <h1>🐳 Flask Docker Demo</h1>
    <div class="stats">
        <p>Total Visits: <strong>{{ visits }}</strong></p>
    </div>
    <p>This application is running in a Docker container!</p>
</body>
</html>
```

### run.py
```python
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### config.py
```python
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
```

### requirements.txt
```
flask==2.3.0
flask-sqlalchemy==3.0.3
psycopg2-binary==2.9.6
redis==4.5.4
gunicorn==20.1.0
```

## Step 2: Create the Dockerfile

### Dockerfile
```dockerfile
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
```

## Step 3: Create docker-compose.yml

### docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=${SECRET_KEY:-super-secret-key}
      - DATABASE_URL=postgresql://postgres:${POSTGRES_PASSWORD:-secret}@db:5432/flask_app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:13-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-secret}
      - POSTGRES_DB=flask_app
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    restart: unless-stopped

volumes:
  postgres_data:
```

### docker-compose.dev.yml (for development)
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=dev-secret
      - DATABASE_URL=postgresql://postgres:secret@db:5432/flask_app
      - REDIS_URL=redis://redis:6379
      - FLASK_ENV=development
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    command: python run.py

  db:
    image: postgres:13-alpine
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=flask_app
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

## Step 4: Create .dockerignore

### .dockerignore
```
__pycache__
*.pyc
*.pyo
.git
.gitignore
.env
.env.local
*.md
Dockerfile*
docker-compose*
.dockerignore
venv/
.venv/
*.egg-info
.pytest_cache
.coverage
htmlcov/
```

## Step 5: Create .env.example

### .env.example
```
SECRET_KEY=your-secret-key-here
POSTGRES_PASSWORD=your-db-password
```

## Running the Project

### Development Mode
```bash
# Start services with hot reload
docker-compose -f docker-compose.dev.yml up

# Access at http://localhost:5000
```

### Production Mode
```bash
# Create .env file
cp .env.example .env
# Edit .env with your values

# Build and start
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## Testing Your Application

```bash
# Test the main page
curl http://localhost:5000

# Test the API
curl http://localhost:5000/api/stats

# Test health check
curl http://localhost:5000/health
```

## Challenges

1. Add a nginx reverse proxy service
2. Add SSL/TLS support
3. Add a background worker with Celery
4. Implement proper logging
5. Add database migrations with Flask-Migrate

## Learning Outcomes

After completing this project, you will have:
- ✅ Created a multi-container application
- ✅ Written a production-ready Dockerfile
- ✅ Configured Docker Compose for multiple services
- ✅ Used environment variables for configuration
- ✅ Set up persistent storage with volumes
- ✅ Implemented health checks
- ✅ Understood development vs production configurations
