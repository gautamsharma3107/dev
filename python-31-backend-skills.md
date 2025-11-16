# Additional Backend Skills: Complete Guide

---

## Table of Contents
1. [Configuration Management](#configuration-management)
2. [Logging](#logging)
3. [Caching](#caching)
4. [Message Queues](#message-queues)
5. [Docker](#docker)
6. [Deployment](#deployment)
7. [CI/CD](#cicd)
8. [Microservices](#microservices)
9. [Security Best Practices](#security-best-practices)
10. [Practical Examples](#practical-examples)
11. [Best Practices](#best-practices)

---

## Configuration Management

### Environment Variables

```bash
# .env file
DATABASE_URL=postgresql://user:password@localhost/mydb
DEBUG=True
SECRET_KEY=your-secret-key-here
API_KEY=api_key_123
REDIS_URL=redis://localhost:6379/0
ENVIRONMENT=development
```

### python-decouple

```bash
pip install python-decouple
```

```python
from decouple import config, Csv

# Basic usage
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASE_URL = config('DATABASE_URL')
SECRET_KEY = config('SECRET_KEY')
ENVIRONMENT = config('ENVIRONMENT', default='development')

# Cast to different types
PORT = config('PORT', default=8000, cast=int)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())

# Optional with default
API_KEY = config('API_KEY', default=None)

# Raise error if not set
REQUIRED_KEY = config('REQUIRED_KEY')  # Raises UndefinedValueError if not set
```

### Configuration Files

```python
# config.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('SECRET_KEY')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = False
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

# YAML config
import yaml

def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

# JSON config
import json

def load_json_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        return json.load(f)

# INI config
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
db_host = config.get('database', 'host')
```

---

## Logging

### Python Logging Module

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log levels
logger.debug("Debug message")       # DEBUG (10)
logger.info("Info message")         # INFO (20)
logger.warning("Warning message")   # WARNING (30)
logger.error("Error message")       # ERROR (40)
logger.critical("Critical message") # CRITICAL (50)

# With exception info
try:
    1 / 0
except Exception:
    logger.exception("An error occurred")
```

### Handlers and Formatters

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Rotating file handler
rotating_handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5        # Keep 5 backups
)

# Time-based rotating handler
time_handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',     # Rotate at midnight
    interval=1,
    backupCount=7        # Keep 7 days
)

# Custom formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

rotating_handler.setFormatter(formatter)
time_handler.setFormatter(formatter)

# Get logger and add handlers
logger = logging.getLogger(__name__)
logger.addHandler(rotating_handler)
logger.addHandler(time_handler)
```

### Structured Logging

```bash
pip install python-json-logger
```

```python
import logging
import json
from pythonjsonlogger import jsonlogger

# JSON logging
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

# Logs will be JSON
logger.info('User login', extra={'user_id': 1, 'ip': '127.0.0.1'})

# Output:
# {"message": "User login", "user_id": 1, "ip": "127.0.0.1", "levelname": "INFO"}
```

---

## Caching

### Redis Caching

```bash
pip install redis
```

```python
import redis
from functools import wraps
import json
import time

# Redis connection
cache = redis.Redis(host='localhost', port=6379, db=0)

# Simple caching
def get_user(user_id):
    cache_key = f"user:{user_id}"
    
    # Try cache
    cached = cache.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Get from database
    user = fetch_from_db(user_id)
    
    # Cache for 1 hour
    cache.setex(cache_key, 3600, json.dumps(user))
    return user

# Cache decorator
def cache_result(ttl=3600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            cached = cache.get(cache_key)
            if cached:
                return json.loads(cached)
            
            result = func(*args, **kwargs)
            cache.setex(cache_key, ttl, json.dumps(result))
            return result
        return wrapper
    return decorator

@cache_result(ttl=1800)
def expensive_operation(x, y):
    time.sleep(2)
    return x + y
```

### Application-Level Caching

```python
from functools import lru_cache

# In-memory caching
@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Flask caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/users')
@cache.cached(timeout=300)
def list_users():
    return get_users()

# Clear cache
cache.clear()
```

### HTTP Caching Headers

```python
from fastapi import FastAPI
from fastapi.responses import Response
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/data")
def get_data():
    response = Response(content="data")
    
    # Cache for 1 hour
    response.headers["Cache-Control"] = "max-age=3600, public"
    
    # Expires header
    expires = (datetime.utcnow() + timedelta(hours=1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
    response.headers["Expires"] = expires
    
    # ETag for validation
    response.headers["ETag"] = '"33a64df"'
    
    return response
```

---

## Message Queues

### RabbitMQ

```bash
pip install pika
```

```python
import pika

# Publisher
def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='my_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='my_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # Persistent
    )
    connection.close()

# Consumer
def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='my_queue', durable=True)
    
    def callback(ch, method, properties, body):
        print(f"Received: {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='my_queue', on_message_callback=callback)
    
    print('Waiting for messages...')
    channel.start_consuming()
```

### Redis Pub/Sub

```python
import redis

# Publisher
redis_client = redis.Redis(host='localhost', port=6379)

def publish_event(channel, message):
    redis_client.publish(channel, message)

# Subscriber
def subscribe_events(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received: {message['data']}")
```

---

## Docker

### Docker Basics

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    volumes:
      - .:/app

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

### Building and Running

```bash
# Build image
docker build -t myapp:1.0 .

# Run container
docker run -p 8000:8000 myapp:1.0

# Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs -f web
```

---

## Deployment

### Gunicorn/uWSGI

```bash
pip install gunicorn
```

```bash
# Run Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# With configuration file
gunicorn --config gunicorn_config.py app:app

# With multiple workers
gunicorn -w 4 --worker-class uvicorn.workers.UvicornWorker app:app
```

```python
# gunicorn_config.py
import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120
keepalive = 5
```

### Nginx Configuration

```nginx
# /etc/nginx/sites-available/myapp
upstream app {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
    server 127.0.0.1:8003;
}

server {
    listen 80;
    server_name example.com;

    client_max_body_size 20M;

    location / {
        proxy_pass http://app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    location /static/ {
        alias /app/static/;
        expires 30d;
    }

    location /media/ {
        alias /app/media/;
        expires 7d;
    }
}
```

### Heroku Deployment

```bash
# Login
heroku login

# Create app
heroku create myapp

# Set environment variables
heroku config:set DATABASE_URL=postgresql://...
heroku config:set SECRET_KEY=your-secret-key

# Deploy
git push heroku main

# View logs
heroku logs --tail

# Run command
heroku run python manage.py migrate
```

```
# Procfile
web: gunicorn app:app
worker: celery -A app.celery worker --loglevel=info
```

### AWS Deployment

```python
# Elastic Beanstalk
# Create .ebextensions/python.config
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
  aws:autoscaling:launchconfiguration:
    IamInstanceProfile: aws-elasticbeanstalk-ec2-role

# EC2
# Install Python, dependencies, and configure
# Use supervisor for process management
# Use Nginx as reverse proxy
# Use systemd for service management

# Lambda
# Package and upload function
# Set environment variables
# Configure API Gateway
```

---

## CI/CD

### GitHub Actions

```yaml
# .github/workflows/test-deploy.yml
name: Test and Deploy

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: pytest --cov=app
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
    
    - name: Upload coverage
      uses: codecov/codecov-action@v2

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
        heroku_app_name: ${{ secrets.HEROKU_APP_NAME }}
        heroku_email: ${{ secrets.HEROKU_EMAIL }}
```

---

## Microservices

### Architecture

```
Microservices Architecture:

┌─────────────────┐
│   API Gateway   │
└────────┬────────┘
         │
    ┌────┴────┬──────────┬──────────┐
    │         │          │          │
┌───▼──┐ ┌───▼──┐ ┌────▼───┐ ┌───▼──┐
│User  │ │Order │ │Product │ │Auth  │
│Service    Service     Service    Service
└──────┘ └──────┘ └────────┘ └──────┘
    │         │          │          │
    ├─────────┴──────────┴──────────┤
    │                                │
┌───▼──────────────────────────┐ ┌─▼──────┐
│      Message Queue           │ │ Cache  │
│   (RabbitMQ / Kafka)        │ │(Redis) │
└──────────────────────────────┘ └────────┘
```

### Service Communication

```python
# User Service
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Alice"}

# Order Service calling User Service
import httpx

async def get_user_info(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://user-service:8000/users/{user_id}")
        return response.json()

@app.post("/orders")
async def create_order(user_id: int, items: list):
    user = await get_user_info(user_id)
    # Create order...
    return {"user": user, "items": items}
```

### API Gateway

```python
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Route to user service
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8001/users/{user_id}")
        return response.json()

# Route to order service
@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8002/orders/{order_id}")
        return response.json()

# Route to product service
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8003/products/{product_id}")
        return response.json()
```

---

## Security Best Practices

### Input Validation

```python
from pydantic import BaseModel, validator, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=0, le=150)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'Username must be alphanumeric'
        return v
    
    @validator('password')
    def password_strong(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain uppercase')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain digit')
        return v
```

### SQL Injection Prevention

```python
# ✗ BAD - Vulnerable to SQL injection
@app.get("/users/{username}")
def get_user_bad(username: str):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = db.execute(query)
    return result

# ✓ GOOD - Parameterized query
from sqlalchemy import text

@app.get("/users/{username}")
def get_user_good(username: str):
    query = text("SELECT * FROM users WHERE username = :username")
    result = db.execute(query, {"username": username})
    return result

# ✓ GOOD - ORM (automatic parameterization)
@app.get("/users/{username}")
def get_user_orm(username: str):
    user = session.query(User).filter(User.username == username).first()
    return user
```

### XSS Prevention

```python
from markupsafe import escape

# ✗ BAD - Vulnerable to XSS
@app.get("/search")
def search_bad(q: str):
    return f"<h1>Results for {q}</h1>"

# ✓ GOOD - Escape output
@app.get("/search")
def search_good(q: str):
    return f"<h1>Results for {escape(q)}</h1>"

# ✓ GOOD - Template auto-escape (Jinja2)
# {{ user_input }}  # Auto-escaped
# {{ user_input|safe }}  # Only if trusted
```

### CSRF Protection

```python
from fastapi import FastAPI
from fastapi_csrf_protect import CsrfProtect

@CsrfProtect.load_config
def get_csrf_config():
    return CsrfConfig(secret_key="secret")

@app.post("/form")
async def submit_form(csrf_protect: CsrfProtect = Depends()):
    csrf_token = await csrf_protect.get_csrf_token()
    return {"csrf_token": csrf_token}
```

### Secure Headers

```python
from fastapi import FastAPI
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        # Security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        
        return response

app.add_middleware(SecurityHeadersMiddleware)
```

### Rate Limiting

```bash
pip install slowapi
```

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/login")
@limiter.limit("5/minute")
def login(request: Request, credentials: LoginRequest):
    # Limit login attempts
    return {"token": "..."}

@app.get("/api/data")
@limiter.limit("100/minute")
def get_data(request: Request):
    return {"data": [...]}
```

### Secrets Management

```python
from dotenv import load_dotenv
import os

# Load from .env
load_dotenv()

# Access secrets
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# Never commit .env to git
# Use .gitignore:
# .env
# secrets.json

# In production, use:
# - Environment variables
# - Secrets management services (AWS Secrets Manager, HashiCorp Vault)
# - Configuration servers
```

---

## Practical Examples

### Complete Deployment Setup

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
  
  redis:
    image: redis:7
```

### Logging Setup

```python
import logging
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

def setup_logging():
    logger = logging.getLogger(__name__)
    
    # JSON formatter
    class JsonFormatter(logging.Formatter):
        def format(self, record):
            log_obj = {
                'timestamp': datetime.utcnow().isoformat(),
                'level': record.levelname,
                'logger': record.name,
                'message': record.getMessage(),
            }
            if record.exc_info:
                log_obj['exception'] = self.formatException(record.exc_info)
            return json.dumps(log_obj)
    
    handler = RotatingFileHandler(
        'app.log',
        maxBytes=10*1024*1024,
        backupCount=10
    )
    handler.setFormatter(JsonFormatter())
    
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    return logger
```

---

## Best Practices

### Configuration

```
✓ Use environment variables
✓ Never commit secrets
✓ Use .env files locally
✓ Different configs per environment
✓ Validate on startup
✓ Document all config
```

### Logging

```
✓ Use structured logging
✓ Include context
✓ Don't log sensitive data
✓ Use appropriate levels
✓ Rotate log files
✓ Monitor logs
```

### Deployment

```
✓ Use containerization
✓ Automated deployment
✓ Blue-green deployment
✓ Database migrations
✓ Backward compatibility
✓ Monitoring and alerts
```

### Security

```
✓ Validate all input
✓ Use parameterized queries
✓ Escape output
✓ HTTPS everywhere
✓ CSRF tokens
✓ Secure headers
✓ Rate limiting
✓ Secrets management
```

---

# End of Notes
