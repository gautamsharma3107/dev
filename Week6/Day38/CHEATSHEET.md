# Day 38 Quick Reference Cheat Sheet

## Docker Architecture
```
┌─────────────────────────────────────────────────────────┐
│                      Docker Host                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Docker Daemon                        │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐         │   │
│  │  │Container│  │Container│  │Container│         │   │
│  │  │   A     │  │   B     │  │   C     │         │   │
│  │  └─────────┘  └─────────┘  └─────────┘         │   │
│  │                                                   │   │
│  │  ┌───────────────────────────────────────┐      │   │
│  │  │            Docker Images               │      │   │
│  │  │  python:3.9  nginx  postgres  redis   │      │   │
│  │  └───────────────────────────────────────┘      │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Basic Docker Commands
```bash
# Version and info
docker --version          # Check Docker version
docker info               # System-wide information

# Images
docker images             # List all images
docker pull <image>       # Download image from registry
docker build -t <name> .  # Build image from Dockerfile
docker rmi <image>        # Remove image
docker image prune        # Remove unused images

# Containers
docker ps                 # List running containers
docker ps -a              # List all containers
docker run <image>        # Create and start container
docker start <container>  # Start stopped container
docker stop <container>   # Stop running container
docker rm <container>     # Remove container
docker logs <container>   # View container logs
docker exec -it <container> bash  # Enter container
```

## Dockerfile Instructions
```dockerfile
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY . .

# Run commands during build
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_ENV=production
ENV PORT=5000

# Expose port
EXPOSE 5000

# Default command
CMD ["python", "app.py"]

# Alternative: ENTRYPOINT
ENTRYPOINT ["python"]
CMD ["app.py"]
```

## Docker Run Options
```bash
# Basic run
docker run nginx

# Run in detached mode (background)
docker run -d nginx

# Name your container
docker run --name my_container nginx

# Port mapping (host:container)
docker run -p 8080:80 nginx

# Volume mounting (host:container)
docker run -v /host/path:/container/path nginx

# Environment variables
docker run -e MY_VAR=value nginx

# Interactive mode
docker run -it python:3.9 bash

# Remove after exit
docker run --rm nginx

# Full example
docker run -d \
  --name web_server \
  -p 8080:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  -e NGINX_HOST=localhost \
  --restart unless-stopped \
  nginx
```

## Docker Compose Basics
```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

## Docker Compose Commands
```bash
# Start services
docker-compose up           # Start all services
docker-compose up -d        # Start in detached mode
docker-compose up --build   # Rebuild images

# Stop services
docker-compose down         # Stop and remove containers
docker-compose down -v      # Also remove volumes

# View status
docker-compose ps           # List running services
docker-compose logs         # View logs
docker-compose logs -f web  # Follow specific service logs

# Scale services
docker-compose up --scale web=3

# Execute commands
docker-compose exec web bash
```

## Multi-Stage Builds
```dockerfile
# Build stage
FROM python:3.9 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt

# Production stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*
COPY . .
CMD ["python", "app.py"]
```

## Common Dockerfile Patterns
```dockerfile
# Python Flask App
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

# Node.js App
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]

# FastAPI App
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## .dockerignore File
```
# .dockerignore
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
*.egg-info/
.git
.gitignore
Dockerfile
docker-compose.yml
.dockerignore
README.md
*.md
.env
.env.local
tests/
*.log
*.tmp
node_modules/
```

## Useful Patterns
```bash
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune -a

# Remove all unused volumes
docker volume prune

# Clean everything
docker system prune -a

# Copy files from container
docker cp container_id:/path/file ./local_path

# View container stats
docker stats

# Inspect container
docker inspect <container>

# Build with no cache
docker build --no-cache -t myapp .

# Tag an image
docker tag myapp:latest myapp:v1.0

# Push to registry
docker push myregistry.com/myapp:v1.0
```

## Networking
```bash
# Create network
docker network create mynetwork

# Run container in network
docker run --network mynetwork nginx

# List networks
docker network ls

# Inspect network
docker network inspect mynetwork
```

## Health Checks
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1
```

---
**Keep this handy for Docker commands!** 🐳🚀
