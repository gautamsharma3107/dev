"""
Day 42 - Docker Basics for ML Applications
============================================
Learn: Containerizing ML applications with Docker

Key Concepts:
- Dockerfile creation
- Building images
- Running containers
- Docker Compose for multi-container apps
"""

# ========== SETUP ==========
print("=" * 60)
print("DOCKER BASICS FOR ML APPLICATIONS")
print("=" * 60)

print("""
Docker provides:
- Consistent development environments
- Easy deployment
- Isolation and reproducibility
- Scalability
""")

# ========== DOCKERFILE BASICS ==========
print("\n" + "=" * 60)
print("1. BASIC DOCKERFILE")
print("=" * 60)

dockerfile_basic = '''
# Dockerfile - Basic Python ML application

# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print(dockerfile_basic)

# ========== OPTIMIZED DOCKERFILE ==========
print("\n" + "=" * 60)
print("2. OPTIMIZED MULTI-STAGE DOCKERFILE")
print("=" * 60)

dockerfile_optimized = '''
# Dockerfile - Optimized multi-stage build

# ============ Stage 1: Build ============
FROM python:3.10-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    python3-dev \\
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============ Stage 2: Production ============
FROM python:3.10-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Create non-root user
RUN useradd --create-home appuser
USER appuser

# Copy application
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print(dockerfile_optimized)

# ========== REQUIREMENTS.TXT ==========
print("\n" + "=" * 60)
print("3. REQUIREMENTS.TXT")
print("=" * 60)

requirements = '''
# requirements.txt - Python dependencies

# Web framework
fastapi==0.104.1
uvicorn==0.24.0

# Database
sqlalchemy==2.0.23
alembic==1.12.1

# Data validation
pydantic==2.5.2

# ML libraries
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
joblib==1.3.2

# Utilities
python-multipart==0.0.6
python-dotenv==1.0.0
jinja2==3.1.2

# For async support (optional)
aiofiles==23.2.1
httpx==0.25.2
'''
print(requirements)

# ========== DOCKER COMMANDS ==========
print("\n" + "=" * 60)
print("4. DOCKER COMMANDS")
print("=" * 60)

docker_commands = '''
# ============ Building Images ============

# Build image with default name
docker build -t ml-app .

# Build with specific tag
docker build -t ml-app:v1.0.0 .

# Build with build arguments
docker build --build-arg ENV=production -t ml-app .

# Build without cache
docker build --no-cache -t ml-app .

# ============ Running Containers ============

# Run container
docker run -p 8000:8000 ml-app

# Run in detached mode
docker run -d -p 8000:8000 ml-app

# Run with name
docker run -d --name ml-service -p 8000:8000 ml-app

# Run with environment variables
docker run -d -p 8000:8000 \\
    -e DATABASE_URL=sqlite:///./data/app.db \\
    -e MODEL_PATH=/app/ml/model.pkl \\
    ml-app

# Run with volume mount
docker run -d -p 8000:8000 \\
    -v $(pwd)/data:/app/data \\
    ml-app

# ============ Container Management ============

# List running containers
docker ps

# List all containers
docker ps -a

# Stop container
docker stop ml-service

# Start stopped container
docker start ml-service

# Remove container
docker rm ml-service

# View logs
docker logs ml-service
docker logs -f ml-service  # Follow logs

# Execute command in container
docker exec -it ml-service bash
docker exec ml-service python -c "print('Hello')"

# ============ Image Management ============

# List images
docker images

# Remove image
docker rmi ml-app:v1.0.0

# Tag image
docker tag ml-app:latest ml-app:v1.0.0

# Push to registry
docker push username/ml-app:v1.0.0

# ============ Cleanup ============

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove all unused resources
docker system prune -a
'''
print(docker_commands)

# ========== DOCKER COMPOSE ==========
print("\n" + "=" * 60)
print("5. DOCKER COMPOSE")
print("=" * 60)

docker_compose = '''
# docker-compose.yml - Multi-container setup

version: '3.8'

services:
  # Main application
  web:
    build: .
    container_name: ml-web
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mlapp
      - MODEL_PATH=/app/ml/model.pkl
      - DEBUG=false
    volumes:
      - ./ml:/app/ml:ro  # Read-only model mount
      - app_data:/app/data
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Database
  db:
    image: postgres:14-alpine
    container_name: ml-db
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mlapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d mlapp"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis for caching (optional)
  redis:
    image: redis:7-alpine
    container_name: ml-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Nginx reverse proxy (optional)
  nginx:
    image: nginx:alpine
    container_name: ml-nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - web

volumes:
  postgres_data:
  redis_data:
  app_data:

networks:
  default:
    name: ml-network
'''
print(docker_compose)

# ========== DOCKER COMPOSE COMMANDS ==========
print("\n" + "=" * 60)
print("6. DOCKER COMPOSE COMMANDS")
print("=" * 60)

compose_commands = '''
# ============ Starting Services ============

# Start all services
docker-compose up

# Start in detached mode
docker-compose up -d

# Start specific service
docker-compose up -d web

# Build and start
docker-compose up -d --build

# ============ Stopping Services ============

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Stop specific service
docker-compose stop web

# ============ Managing Services ============

# View running services
docker-compose ps

# View logs
docker-compose logs
docker-compose logs -f web  # Follow specific service

# Restart service
docker-compose restart web

# Scale service
docker-compose up -d --scale web=3

# ============ Development Commands ============

# Execute command in service
docker-compose exec web bash
docker-compose exec db psql -U user -d mlapp

# Run one-off command
docker-compose run --rm web python -c "print('test')"

# View configuration
docker-compose config
'''
print(compose_commands)

# ========== .DOCKERIGNORE ==========
print("\n" + "=" * 60)
print("7. DOCKERIGNORE FILE")
print("=" * 60)

dockerignore = '''
# .dockerignore - Files to exclude from Docker build

# Git
.git
.gitignore

# Python
__pycache__
*.py[cod]
*$py.class
*.so
.Python
.env
.venv
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Build
dist/
build/
*.egg-info/

# Docker
Dockerfile
docker-compose*.yml
.docker/

# Documentation
docs/
*.md
!README.md

# Local data
data/
*.db
*.sqlite

# Logs
logs/
*.log

# Temporary files
tmp/
temp/
*.tmp
'''
print(dockerignore)

# ========== NGINX CONFIGURATION ==========
print("\n" + "=" * 60)
print("8. NGINX REVERSE PROXY CONFIG")
print("=" * 60)

nginx_config = '''
# nginx.conf - Reverse proxy configuration

events {
    worker_connections 1024;
}

http {
    upstream ml_app {
        server web:8000;
    }

    server {
        listen 80;
        server_name localhost;

        # API endpoints
        location /api {
            proxy_pass http://ml_app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Health check
        location /health {
            proxy_pass http://ml_app/health;
        }

        # Static files
        location /static {
            alias /app/static;
            expires 30d;
        }

        # Main app
        location / {
            proxy_pass http://ml_app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
'''
print(nginx_config)

# ========== ENVIRONMENT VARIABLES ==========
print("\n" + "=" * 60)
print("9. ENVIRONMENT CONFIGURATION")
print("=" * 60)

env_config = '''
# .env.example - Environment variables template

# Application
APP_NAME=ml-prediction-service
DEBUG=false
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@db:5432/mlapp
# For SQLite: sqlite:///./data/predictions.db

# Model
MODEL_PATH=/app/ml/model.pkl
MODEL_VERSION=1.0.0

# Redis (optional)
REDIS_URL=redis://redis:6379/0

# Logging
LOG_LEVEL=INFO

# CORS
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com

# .env.development
DEBUG=true
DATABASE_URL=sqlite:///./data/dev.db

# .env.production
DEBUG=false
DATABASE_URL=postgresql://user:password@db:5432/mlapp
'''
print(env_config)

# ========== COMPLETE PROJECT STRUCTURE ==========
print("\n" + "=" * 60)
print("10. COMPLETE PROJECT STRUCTURE")
print("=" * 60)

print("""
Complete Dockerized ML Application Structure:
=============================================

ml-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # Configuration management
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # Database setup
│   ├── crud.py              # CRUD operations
│   └── ml/
│       ├── __init__.py
│       ├── model.py         # ML model loading
│       └── predictor.py     # Prediction logic
├── ml/
│   ├── model.pkl            # Trained model
│   └── scaler.pkl           # Preprocessor
├── templates/
│   └── index.html           # Frontend template
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_model.py
├── data/                    # Gitignored
│   └── .gitkeep
├── Dockerfile
├── docker-compose.yml
├── docker-compose.dev.yml   # Development override
├── .dockerignore
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt     # Development dependencies
└── README.md
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. Dockerfile
   - Use multi-stage builds
   - Optimize layer caching
   - Run as non-root user
   - Add health checks

2. Docker Commands
   - build, run, ps, logs
   - exec for debugging
   - Volume mounts for data

3. Docker Compose
   - Multi-container apps
   - Service dependencies
   - Volume management
   - Network configuration

4. Best Practices
   - Use .dockerignore
   - Environment variables
   - Health checks
   - Proper logging

5. Production Considerations
   - Reverse proxy (nginx)
   - Database persistence
   - Secret management
   - Container orchestration
""")

print("\n" + "=" * 60)
print("✅ Docker Basics for ML Applications - Complete!")
print("=" * 60)
