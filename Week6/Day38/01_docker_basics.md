# What is Docker?

## 🎯 Learning Objectives
- Understand what Docker is and why it matters
- Learn the difference between containers and VMs
- Understand Docker architecture and components
- Know when to use Docker

---

## 📖 Introduction to Docker

### What Problem Does Docker Solve?

**The "It Works on My Machine" Problem:**
```
Developer: "It works on my machine!"
Operations: "Well, it doesn't work on the server..."
```

Docker solves this by packaging your application with all its dependencies into a standardized unit called a **container**.

### What is Docker?

Docker is a platform that enables developers to:
- **Package** applications with all dependencies
- **Ship** applications consistently across environments
- **Run** applications in isolated containers

Think of it as a **shipping container** for software:
- Just like shipping containers standardized global trade
- Docker containers standardized software deployment

---

## 🏗️ Docker Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Your Computer                        │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │                  Docker Engine                     │  │
│  │                                                    │  │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐          │  │
│  │  │Container│  │Container│  │Container│          │  │
│  │  │  App A  │  │  App B  │  │  App C  │          │  │
│  │  └─────────┘  └─────────┘  └─────────┘          │  │
│  │         ↑           ↑           ↑                 │  │
│  │         └───────────┴───────────┘                 │  │
│  │                     │                              │  │
│  │              Docker Images                        │  │
│  └──────────────────────────────────────────────────┘  │
│                         │                               │
│                   Host OS (Linux)                       │
└─────────────────────────────────────────────────────────┘
```

### Key Components

1. **Docker Daemon (dockerd)**
   - Runs on the host machine
   - Manages Docker objects (images, containers, networks)

2. **Docker Client (docker)**
   - Command-line tool you interact with
   - Sends commands to Docker daemon

3. **Docker Images**
   - Read-only templates for creating containers
   - Like a snapshot of an application

4. **Docker Containers**
   - Running instances of Docker images
   - Isolated environments for applications

5. **Docker Registry (Docker Hub)**
   - Stores Docker images
   - Like GitHub for containers

---

## 🆚 Containers vs Virtual Machines

### Virtual Machines

```
┌─────────┐ ┌─────────┐ ┌─────────┐
│  App A  │ │  App B  │ │  App C  │
├─────────┤ ├─────────┤ ├─────────┤
│Guest OS │ │Guest OS │ │Guest OS │  ← Each VM has full OS
├─────────┴─┴─────────┴─┴─────────┤
│         Hypervisor               │
├─────────────────────────────────┤
│          Host OS                 │
├─────────────────────────────────┤
│         Hardware                 │
└─────────────────────────────────┘
```

### Containers

```
┌─────────┐ ┌─────────┐ ┌─────────┐
│  App A  │ │  App B  │ │  App C  │
├─────────┤ ├─────────┤ ├─────────┤
│  Libs   │ │  Libs   │ │  Libs   │  ← Only app dependencies
├─────────┴─┴─────────┴─┴─────────┤
│       Docker Engine              │
├─────────────────────────────────┤
│          Host OS                 │
├─────────────────────────────────┤
│         Hardware                 │
└─────────────────────────────────┘
```

### Comparison Table

| Feature | Containers | Virtual Machines |
|---------|-----------|-----------------|
| Startup Time | Seconds | Minutes |
| Size | Megabytes | Gigabytes |
| Performance | Near native | Overhead |
| Isolation | Process level | Full isolation |
| OS | Shares host OS | Full guest OS |
| Portability | Very portable | Less portable |

---

## 🔑 Key Docker Concepts

### 1. Images

An image is a blueprint for containers:

```bash
# List images on your system
docker images

# Pull an image from Docker Hub
docker pull python:3.9

# Image naming convention
# [registry/]repository[:tag]
python:3.9
nginx:latest
myregistry.com/myapp:v1.0
```

### 2. Containers

A container is a running instance of an image:

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Run a container
docker run python:3.9 python --version
```

### 3. Dockerfile

A text file with instructions to build an image:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### 4. Volumes

Persistent data storage:

```bash
# Create a volume
docker volume create mydata

# Use volume in container
docker run -v mydata:/app/data myimage
```

### 5. Networks

Container communication:

```bash
# Create network
docker network create mynetwork

# Run containers in same network
docker run --network mynetwork myimage
```

---

## 💡 Why Use Docker?

### 1. **Consistency**
- Same environment everywhere (dev, test, prod)
- No more "works on my machine"

### 2. **Isolation**
- Each container is isolated
- No conflicts between applications

### 3. **Portability**
- Run anywhere Docker is installed
- Works on any OS

### 4. **Efficiency**
- Containers share the host OS
- Lightweight compared to VMs

### 5. **Scalability**
- Easy to scale applications
- Works great with Kubernetes

### 6. **Version Control**
- Track changes to your environment
- Rollback to previous versions

---

## 🚀 Getting Started with Docker

### Installing Docker

**On Ubuntu/Debian:**
```bash
# Update packages
sudo apt update

# Install Docker
sudo apt install docker.io

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (to run without sudo)
sudo usermod -aG docker $USER
```

**On macOS/Windows:**
- Download and install Docker Desktop from docker.com

### Verify Installation

```bash
# Check Docker version
docker --version

# Test Docker
docker run hello-world
```

Expected output:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## 📝 Quick Practice

### Exercise 1: Run Your First Container

```bash
# Run a simple container
docker run hello-world

# Run Python container
docker run python:3.9 python -c "print('Hello from Docker!')"
```

### Exercise 2: Interactive Container

```bash
# Run interactive Python shell
docker run -it python:3.9 bash

# Inside the container
python --version
pip list
exit
```

### Exercise 3: Explore Images

```bash
# List all images
docker images

# Pull an image
docker pull nginx:latest

# Inspect an image
docker inspect nginx
```

---

## 🎯 Key Takeaways

1. **Docker containerizes** applications with their dependencies
2. **Containers are lightweight** compared to VMs
3. **Images are blueprints**, containers are running instances
4. **Docker ensures consistency** across all environments
5. **Dockerfile defines** how to build an image

---

## 📚 Next Steps

Move on to `02_dockerfile_creation.md` to learn how to create your own Dockerfiles!

---
**Remember:** Docker is a game-changer for deployment! 🐳
