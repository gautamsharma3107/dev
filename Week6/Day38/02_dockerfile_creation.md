# Dockerfile Creation

## 🎯 Learning Objectives
- Understand Dockerfile syntax and structure
- Learn all essential Dockerfile instructions
- Write efficient Dockerfiles
- Apply best practices for Dockerfile creation

---

## 📖 What is a Dockerfile?

A Dockerfile is a **text file** containing instructions to build a Docker image. It's like a recipe for your container.

```dockerfile
# This is a simple Dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## 📝 Dockerfile Instructions

### 1. FROM - Base Image

Every Dockerfile starts with FROM. It specifies the base image.

```dockerfile
# Official Python image
FROM python:3.9

# Specific version with slim variant (smaller)
FROM python:3.9-slim

# Alpine Linux (very small)
FROM python:3.9-alpine

# Ubuntu base
FROM ubuntu:22.04

# Start from scratch (empty image)
FROM scratch
```

**Best Practice:** Use specific tags, not `latest`:
```dockerfile
# Bad
FROM python:latest

# Good
FROM python:3.9-slim
```

### 2. WORKDIR - Working Directory

Sets the working directory for subsequent instructions.

```dockerfile
WORKDIR /app

# All following commands run in /app
COPY . .        # Copies to /app
RUN npm install # Runs in /app
```

**Best Practice:** Always use WORKDIR instead of `RUN cd`:
```dockerfile
# Bad
RUN cd /app && do_something

# Good
WORKDIR /app
RUN do_something
```

### 3. COPY - Copy Files

Copies files from host to container.

```dockerfile
# Copy single file
COPY app.py .

# Copy directory
COPY src/ ./src/

# Copy multiple files
COPY requirements.txt app.py ./

# Copy with specific ownership
COPY --chown=user:group files/ ./

# Copy all files
COPY . .
```

### 4. ADD - Add Files (with extras)

Similar to COPY but with additional features:

```dockerfile
# Download from URL
ADD https://example.com/file.tar.gz /app/

# Auto-extract tar files
ADD app.tar.gz /app/

# Regular copy (use COPY instead)
ADD file.txt /app/
```

**Best Practice:** Use COPY unless you need ADD's features:
```dockerfile
# Prefer COPY
COPY requirements.txt .

# Use ADD only for extraction
ADD archive.tar.gz /app/
```

### 5. RUN - Execute Commands

Executes commands during image build.

```dockerfile
# Shell form
RUN pip install flask

# Exec form (recommended)
RUN ["pip", "install", "flask"]

# Multiple commands (single layer)
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

**Best Practice:** Combine RUN commands to reduce layers:
```dockerfile
# Bad (3 layers)
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# Good (1 layer)
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean
```

### 6. CMD - Default Command

Specifies the default command when container starts.

```dockerfile
# Exec form (recommended)
CMD ["python", "app.py"]

# Shell form
CMD python app.py

# With arguments
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
```

**Note:** Only one CMD per Dockerfile. Last one wins.

### 7. ENTRYPOINT - Container Executable

Sets the container's main executable.

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]

# Can be combined
# docker run myapp        → python app.py
# docker run myapp test.py → python test.py
```

**ENTRYPOINT vs CMD:**
```dockerfile
# ENTRYPOINT: Always runs
# CMD: Can be overridden

ENTRYPOINT ["python"]
CMD ["--version"]

# docker run myapp        → python --version
# docker run myapp app.py → python app.py
```

### 8. ENV - Environment Variables

Sets environment variables.

```dockerfile
# Single variable
ENV MY_VAR=value

# Multiple variables
ENV MY_VAR1=value1 \
    MY_VAR2=value2

# Use in subsequent commands
ENV APP_HOME=/app
WORKDIR $APP_HOME
```

### 9. EXPOSE - Declare Ports

Documents which ports the container listens on.

```dockerfile
# Single port
EXPOSE 5000

# Multiple ports
EXPOSE 80 443

# UDP port
EXPOSE 53/udp
```

**Note:** EXPOSE is documentation only. Use `-p` to publish ports.

### 10. ARG - Build Arguments

Defines variables for build time.

```dockerfile
# Define argument
ARG VERSION=3.9

# Use in FROM
FROM python:${VERSION}

# Use in other instructions
ARG APP_NAME=myapp
ENV APP_NAME=$APP_NAME
```

Build with:
```bash
docker build --build-arg VERSION=3.10 -t myapp .
```

### 11. VOLUME - Mount Points

Declares mount points for volumes.

```dockerfile
VOLUME /data
VOLUME ["/data", "/logs"]
```

### 12. USER - Set User

Sets the user for subsequent commands.

```dockerfile
# Create and use non-root user
RUN useradd -m appuser
USER appuser
```

### 13. LABEL - Metadata

Adds metadata to the image.

```dockerfile
LABEL maintainer="you@example.com"
LABEL version="1.0"
LABEL description="My awesome app"
```

### 14. HEALTHCHECK - Container Health

Defines how to check container health.

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1
```

---

## 🐍 Complete Python Dockerfile Examples

### Basic Flask Application

```dockerfile
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
```

### FastAPI Application

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Django Application

```dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
```

---

## 🏗️ Multi-Stage Builds

Multi-stage builds create smaller, more secure images.

```dockerfile
# Stage 1: Build
FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements.txt

# Stage 2: Production
FROM python:3.9-slim

WORKDIR /app

# Copy only the wheels from builder
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

COPY . .

CMD ["python", "app.py"]
```

**Benefits:**
- Smaller final image
- No build tools in production
- Faster deployment

---

## 📁 .dockerignore File

Exclude files from the build context:

```
# .dockerignore

# Python
__pycache__
*.pyc
*.pyo
*.pyd
.Python
venv/
.venv/
env/
*.egg-info/

# Git
.git
.gitignore

# Docker
Dockerfile
docker-compose*.yml
.dockerignore

# IDE
.idea/
.vscode/
*.swp

# Tests
tests/
*.test.py

# Documentation
README.md
docs/

# Environment
.env
.env.local
*.local

# Logs
*.log
logs/

# Build artifacts
dist/
build/
```

---

## ✅ Dockerfile Best Practices

### 1. Order Instructions for Caching

```dockerfile
# Good: Less frequently changed first
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .  # Changes often, at the end
```

### 2. Minimize Layers

```dockerfile
# Combine related commands
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        package1 \
        package2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### 3. Use Specific Tags

```dockerfile
# Use specific versions
FROM python:3.9.16-slim-bullseye

# Not
FROM python:latest
```

### 4. Don't Run as Root

```dockerfile
RUN useradd -m appuser
USER appuser
```

### 5. Use .dockerignore

Always include a `.dockerignore` file.

### 6. Add Health Checks

```dockerfile
HEALTHCHECK --interval=30s CMD curl -f http://localhost:5000/health || exit 1
```

### 7. Clean Up in Same Layer

```dockerfile
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*  # Clean in same layer
```

---

## 📝 Quick Practice

### Exercise 1: Basic Dockerfile

Create a Dockerfile for a simple Python script:

```python
# app.py
print("Hello from Docker!")
```

```dockerfile
# Your Dockerfile here
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

### Exercise 2: Flask Dockerfile

Create a Dockerfile for a Flask application.

### Exercise 3: Multi-stage Build

Convert a Dockerfile to use multi-stage builds.

---

## 🎯 Key Takeaways

1. **FROM** sets the base image
2. **COPY** before **RUN** for better caching
3. **CMD** provides default command
4. **Multi-stage builds** reduce image size
5. Always use **.dockerignore**

---

## 📚 Next Steps

Move on to `03_building_images.md` to learn how to build Docker images!

---
**Practice creating Dockerfiles for your own projects!** 🐳
