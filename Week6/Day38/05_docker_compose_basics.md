# Docker Compose Basics

## 🎯 Learning Objectives
- Understand what Docker Compose is and why it's useful
- Learn docker-compose.yml file structure
- Define and run multi-container applications
- Use Docker Compose commands effectively

---

## 📖 What is Docker Compose?

Docker Compose is a tool for defining and running **multi-container Docker applications**.

### The Problem

Without Compose, running multiple containers is complex:

```bash
# Manual approach - lots of commands!
docker network create myapp_network

docker run -d \
  --name db \
  --network myapp_network \
  -v db_data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:13

docker run -d \
  --name redis \
  --network myapp_network \
  redis:alpine

docker run -d \
  --name web \
  --network myapp_network \
  -p 5000:5000 \
  -e DATABASE_URL=postgres://postgres:secret@db:5432/postgres \
  -e REDIS_URL=redis://redis:6379 \
  myapp:latest
```

### The Solution

With Compose, define everything in one file:

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgres://postgres:secret@db:5432/postgres
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - db_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine

volumes:
  db_data:
```

Start everything with one command:
```bash
docker-compose up -d
```

---

## 📄 Docker Compose File Structure

### Basic Structure

```yaml
version: '3.8'        # Compose file version

services:             # Container definitions
  service1:
    # ...
  service2:
    # ...

volumes:              # Named volumes
  volume1:

networks:             # Custom networks
  network1:
```

---

## 🔧 Service Configuration

### Using Pre-built Images

```yaml
services:
  nginx:
    image: nginx:latest
    ports:
      - "80:80"
```

### Building from Dockerfile

```yaml
services:
  web:
    build: .              # Build from ./Dockerfile
    
  # With custom path
  api:
    build:
      context: ./api
      dockerfile: Dockerfile.prod
      args:
        - VERSION=1.0
```

### Port Mapping

```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"           # HOST:CONTAINER
      - "443:443"
      - "8000-8005:8000-8005"  # Port range
```

### Environment Variables

```yaml
services:
  web:
    image: myapp
    environment:
      - DEBUG=true
      - SECRET_KEY=mysecret
    
  # Or from file
  api:
    image: myapp
    env_file:
      - .env
      - .env.local
```

### Volumes

```yaml
services:
  web:
    image: nginx
    volumes:
      - ./html:/usr/share/nginx/html    # Bind mount
      - nginx_config:/etc/nginx         # Named volume
      - /var/log/nginx                  # Anonymous volume
    
volumes:
  nginx_config:           # Declare named volume
```

### Dependencies

```yaml
services:
  web:
    image: myapp
    depends_on:
      - db
      - redis
    
  db:
    image: postgres:13
    
  redis:
    image: redis:alpine
```

### Networks

```yaml
services:
  web:
    image: nginx
    networks:
      - frontend
      - backend
    
  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
  backend:
```

### Restart Policy

```yaml
services:
  web:
    image: nginx
    restart: always       # always, unless-stopped, on-failure, no
```

### Health Checks

```yaml
services:
  web:
    image: myapp
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### Resource Limits

```yaml
services:
  web:
    image: myapp
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

---

## 📘 Complete Examples

### Example 1: Flask with PostgreSQL

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgres://postgres:secret@db:5432/myapp
      - FLASK_ENV=development
    volumes:
      - .:/app
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### Example 2: Full Stack Application

```yaml
# docker-compose.yml
version: '3.8'

services:
  # Frontend
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - REACT_APP_API_URL=http://localhost:8000

  # Backend API
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://postgres:secret@db:5432/app
      - REDIS_URL=redis://redis:6379
      - SECRET_KEY=my-secret-key
    volumes:
      - ./backend:/app
    depends_on:
      - db
      - redis

  # Database
  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=app
    volumes:
      - db_data:/var/lib/postgresql/data

  # Cache
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - frontend
      - backend

volumes:
  db_data:
```

### Example 3: Development with Hot Reload

```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "5000:5000"
    volumes:
      - .:/app                    # Mount source for hot reload
      - /app/__pycache__          # Exclude pycache
    environment:
      - FLASK_ENV=development
      - FLASK_DEBUG=1
    command: flask run --host=0.0.0.0 --reload
```

---

## 💻 Docker Compose Commands

### Starting Services

```bash
# Start all services
docker-compose up

# Start in detached mode
docker-compose up -d

# Start specific service
docker-compose up web

# Rebuild images and start
docker-compose up --build

# Force recreate containers
docker-compose up --force-recreate
```

### Stopping Services

```bash
# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# Also remove volumes
docker-compose down -v

# Remove images too
docker-compose down --rmi all
```

### Viewing Status

```bash
# List running services
docker-compose ps

# View logs
docker-compose logs

# Follow logs
docker-compose logs -f

# Logs for specific service
docker-compose logs -f web
```

### Executing Commands

```bash
# Run command in service
docker-compose exec web bash

# Run one-off command
docker-compose run web python manage.py migrate

# Run without starting dependencies
docker-compose run --no-deps web pytest
```

### Scaling Services

```bash
# Scale a service
docker-compose up -d --scale web=3
```

### Other Commands

```bash
# Validate docker-compose.yml
docker-compose config

# Pull images
docker-compose pull

# Build images
docker-compose build

# View images
docker-compose images

# View running processes
docker-compose top
```

---

## 📂 Multiple Compose Files

### Development vs Production

```bash
# Development
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

# Production
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Override Files

```yaml
# docker-compose.yml (base)
services:
  web:
    image: myapp
    ports:
      - "5000:5000"
```

```yaml
# docker-compose.override.yml (auto-loaded)
services:
  web:
    build: .
    volumes:
      - .:/app
    environment:
      - DEBUG=true
```

---

## 🔒 Environment Variables and Secrets

### Using .env File

```bash
# .env file
POSTGRES_PASSWORD=supersecret
SECRET_KEY=my-secret-key
```

```yaml
# docker-compose.yml
services:
  web:
    environment:
      - SECRET_KEY=${SECRET_KEY}
  
  db:
    image: postgres
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
```

### Variable Substitution

```yaml
services:
  web:
    image: myapp:${TAG:-latest}    # Default value
    ports:
      - "${PORT:-5000}:5000"
```

---

## 📝 Practical Exercise: Containerize Your App

### Step 1: Project Structure

```
myproject/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

### Step 2: Create Files

```python
# app.py
from flask import Flask
import os
import redis

app = Flask(__name__)
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    visits = cache.incr('visits')
    return f'Hello! Visit count: {visits}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```
# requirements.txt
flask==2.3.0
redis==4.5.0
```

```dockerfile
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
    depends_on:
      - redis
    restart: unless-stopped

  redis:
    image: redis:alpine
    restart: unless-stopped
```

### Step 3: Run

```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Test
curl http://localhost:5000

# Stop
docker-compose down
```

---

## ✅ Best Practices

1. **Use version 3.8+** for modern features
2. **Always define volumes** for persistent data
3. **Use depends_on** for service ordering
4. **Use environment files** for secrets
5. **Set restart policies** for reliability
6. **Use named volumes** over bind mounts in production
7. **Use health checks** for production services
8. **Separate dev and prod** configurations

---

## 🎯 Key Takeaways

1. **Docker Compose** manages multi-container apps
2. **docker-compose.yml** defines all services
3. **docker-compose up** starts everything
4. **docker-compose down** stops and removes
5. Services can **communicate by name**

---

## 📚 Next Steps

You've completed the Docker basics! Now practice by:
1. Containerizing your own Python projects
2. Creating development environments
3. Building multi-service applications

---
**You're now ready to containerize your applications!** 🐳🚀
