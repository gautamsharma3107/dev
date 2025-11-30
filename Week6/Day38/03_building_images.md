# Building Docker Images

## 🎯 Learning Objectives
- Master the `docker build` command
- Understand build context and caching
- Learn to tag and version images
- Optimize image build process

---

## 📖 Building Your First Image

### Basic Build Command

```bash
# Build from current directory
docker build -t myapp .

# Breakdown:
# docker build  - Command to build image
# -t myapp      - Tag/name the image
# .             - Build context (current directory)
```

### The Build Context

The **build context** is the set of files at the specified path:

```bash
# Current directory as context
docker build -t myapp .

# Specific directory
docker build -t myapp ./app

# From a URL
docker build -t myapp https://github.com/user/repo.git
```

**Important:** All files in the context are sent to the Docker daemon.

---

## 🏷️ Tagging Images

### Tag Format

```
[registry/]repository[:tag]

# Examples:
myapp                      # Default tag: latest
myapp:1.0                  # Version tag
myapp:latest               # Latest tag
myuser/myapp:v1.0          # User/repository with tag
registry.com/myapp:prod    # Custom registry
```

### Tagging During Build

```bash
# Single tag
docker build -t myapp:1.0 .

# Multiple tags
docker build -t myapp:1.0 -t myapp:latest .

# With registry
docker build -t myregistry.com/myapp:1.0 .
```

### Tagging Existing Images

```bash
# Add a new tag to existing image
docker tag myapp:1.0 myapp:latest

# Tag for a registry
docker tag myapp:1.0 docker.io/myuser/myapp:1.0
```

---

## 🔧 Build Options

### Common Build Flags

```bash
# Build with no cache
docker build --no-cache -t myapp .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t myapp .

# Build with build arguments
docker build --build-arg VERSION=1.0 -t myapp .

# Build with target stage (multi-stage)
docker build --target builder -t myapp-builder .

# Suppress build output
docker build -q -t myapp .

# Add labels
docker build --label version=1.0 -t myapp .

# Set memory limit for build
docker build --memory=1g -t myapp .
```

### Full Example

```bash
docker build \
  --no-cache \
  --build-arg VERSION=3.9 \
  --build-arg ENV=production \
  -t mycompany/myapp:1.0 \
  -t mycompany/myapp:latest \
  -f Dockerfile.prod \
  .
```

---

## 📊 Understanding Build Cache

Docker caches each layer to speed up subsequent builds.

### How Caching Works

```dockerfile
FROM python:3.9-slim          # Cached if unchanged
WORKDIR /app                  # Cached if unchanged
COPY requirements.txt .       # Cached if file unchanged
RUN pip install -r req...     # Cached if previous layers unchanged
COPY . .                      # Often busts cache (code changes)
CMD ["python", "app.py"]      # Cached if previous layers unchanged
```

### Cache Invalidation

Cache is invalidated when:
1. Instruction changes
2. Files being copied change
3. Previous layer cache is invalidated

```bash
# Build output showing cache usage
Step 1/6 : FROM python:3.9-slim
 ---> Using cache
Step 2/6 : WORKDIR /app
 ---> Using cache
Step 3/6 : COPY requirements.txt .
 ---> abc123def456  # New layer - file changed
Step 4/6 : RUN pip install -r requirements.txt
 ---> Running in xyz789...  # Rebuilding
```

### Optimize for Caching

```dockerfile
# BAD: Changes to any file bust the cache
COPY . .
RUN pip install -r requirements.txt

# GOOD: Dependencies cached separately
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

---

## 📏 Image Layers

Each instruction creates a layer:

```bash
# View image layers
docker history myapp

IMAGE          CREATED       SIZE      INSTRUCTION
abc123         1 min ago     0B        CMD ["python" "app.py"]
def456         1 min ago     50MB      RUN pip install...
ghi789         2 min ago     5KB       COPY . .
jkl012         2 min ago     5B        WORKDIR /app
mno345         2 weeks ago   120MB     FROM python:3.9-slim
```

### Minimize Layers

```dockerfile
# BAD: Multiple layers
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get clean

# GOOD: Single layer
RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

---

## 🔍 Inspecting Images

### List Images

```bash
# List all images
docker images

# List with specific format
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# Filter images
docker images --filter "dangling=true"
docker images myapp
```

### Inspect Image Details

```bash
# Full details
docker inspect myapp

# Specific info
docker inspect --format='{{.Config.Cmd}}' myapp
docker inspect --format='{{.Config.Env}}' myapp

# Image size
docker images myapp --format "{{.Size}}"
```

### View Image Layers

```bash
# Show all layers
docker history myapp

# Without truncation
docker history --no-trunc myapp

# Quiet mode (just IDs)
docker history -q myapp
```

---

## 🗑️ Managing Images

### Remove Images

```bash
# Remove specific image
docker rmi myapp:1.0

# Remove by image ID
docker rmi abc123def456

# Force remove (even if containers exist)
docker rmi -f myapp:1.0

# Remove multiple images
docker rmi myapp:1.0 myapp:2.0 nginx
```

### Clean Up Images

```bash
# Remove dangling images (no tag)
docker image prune

# Remove all unused images
docker image prune -a

# Remove images older than 24h
docker image prune -a --filter "until=24h"
```

---

## 📤 Saving and Loading Images

### Save to File

```bash
# Save image to tar file
docker save -o myapp.tar myapp:1.0

# Save multiple images
docker save -o images.tar myapp:1.0 nginx:latest
```

### Load from File

```bash
# Load image from tar
docker load -i myapp.tar
```

### Export/Import Containers

```bash
# Export running container
docker export container_id > container.tar

# Import as image
docker import container.tar myimage:tag
```

---

## 🚀 Pushing Images to Registry

### Docker Hub

```bash
# Login to Docker Hub
docker login

# Tag image for Docker Hub
docker tag myapp:1.0 username/myapp:1.0

# Push to Docker Hub
docker push username/myapp:1.0
```

### Private Registry

```bash
# Login to private registry
docker login registry.example.com

# Tag for private registry
docker tag myapp:1.0 registry.example.com/myapp:1.0

# Push to private registry
docker push registry.example.com/myapp:1.0
```

---

## 🏗️ Multi-Stage Build Example

### Without Multi-Stage (Large Image)

```dockerfile
FROM python:3.9
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
# Result: ~900MB image
```

### With Multi-Stage (Small Image)

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
# Result: ~200MB image
```

### Build Specific Stage

```bash
# Build only the builder stage
docker build --target builder -t myapp-builder .
```

---

## 📊 Build Statistics

### Show Build Time

```bash
# Time the build
time docker build -t myapp .

# Build with progress
docker build --progress=plain -t myapp .
```

### Analyze Image Size

```bash
# Show image size
docker images myapp

# Use dive tool for detailed analysis
docker run --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  wagoodman/dive:latest myapp:1.0
```

---

## 📝 Practical Exercise: Build a Python App Image

### Step 1: Create the Application

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```
# requirements.txt
flask==2.3.0
```

### Step 2: Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Step 3: Build the Image

```bash
# Build with tag
docker build -t myflaskapp:1.0 .

# Verify
docker images myflaskapp
```

### Step 4: Test the Image

```bash
# Run container
docker run -d -p 5000:5000 --name test_app myflaskapp:1.0

# Test
curl http://localhost:5000

# Clean up
docker stop test_app && docker rm test_app
```

---

## ✅ Best Practices Summary

1. **Use specific base image tags** (not `latest`)
2. **Order instructions** for optimal caching
3. **Minimize layers** by combining RUN commands
4. **Use multi-stage builds** for smaller images
5. **Clean up** in the same layer as install
6. **Use .dockerignore** to exclude unnecessary files
7. **Don't include secrets** in images
8. **Tag images** with version numbers

---

## 🎯 Key Takeaways

1. `docker build -t name:tag .` builds images
2. **Build context** matters - use `.dockerignore`
3. **Caching** speeds up builds - order matters
4. **Multi-stage builds** reduce final image size
5. **Tag versions** for better management

---

## 📚 Next Steps

Move on to `04_running_containers.md` to learn how to run and manage containers!

---
**Practice building images for your own applications!** 🐳
