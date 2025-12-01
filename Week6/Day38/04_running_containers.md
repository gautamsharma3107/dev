# Running Containers

## 🎯 Learning Objectives
- Master the `docker run` command
- Understand container lifecycle
- Learn port mapping and volume mounting
- Manage running containers effectively

---

## 📖 Docker Run Basics

### Basic Run Command

```bash
# Run a container
docker run nginx

# Run and name the container
docker run --name my_nginx nginx

# Run in detached mode (background)
docker run -d nginx

# Run interactively
docker run -it python:3.9 bash
```

### Understanding Run Output

```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

# What happened:
# 1. Docker pulled the hello-world image
# 2. Created a new container from the image
# 3. Ran the container
# 4. Container printed output and exited
```

---

## 🚀 Common Run Options

### Detached Mode (-d)

Run container in the background:

```bash
# Run nginx in background
docker run -d nginx

# Returns container ID
# abc123def456...

# Check running containers
docker ps
```

### Interactive Mode (-it)

Run container with interactive terminal:

```bash
# Start interactive shell
docker run -it ubuntu bash

# Inside the container
root@container:/# ls
root@container:/# exit
```

### Naming Containers (--name)

```bash
# Name your container
docker run --name my_app myimage

# Easier to manage
docker stop my_app
docker start my_app
docker logs my_app
```

### Auto-Remove (--rm)

Remove container when it exits:

```bash
# Container removed after exit
docker run --rm python:3.9 python -c "print('Hello')"

# Useful for one-off commands
```

---

## 🔌 Port Mapping (-p)

Map container ports to host ports:

```bash
# Syntax: -p HOST_PORT:CONTAINER_PORT
docker run -p 8080:80 nginx

# Now access: http://localhost:8080

# Multiple ports
docker run -p 8080:80 -p 8443:443 nginx

# Random host port
docker run -p 80 nginx
docker port container_id  # See assigned port

# Bind to specific interface
docker run -p 127.0.0.1:8080:80 nginx
```

### Practical Example

```bash
# Run nginx on port 8080
docker run -d --name web -p 8080:80 nginx

# Access in browser or curl
curl http://localhost:8080

# Clean up
docker stop web && docker rm web
```

---

## 📁 Volume Mounting (-v)

Persist data and share files with containers:

### Bind Mounts (Host Path)

```bash
# Mount host directory to container
docker run -v /host/path:/container/path nginx

# Example: Share current directory
docker run -v $(pwd):/app python:3.9 python /app/script.py

# Read-only mount
docker run -v /host/path:/container/path:ro nginx
```

### Named Volumes

```bash
# Create a named volume
docker volume create mydata

# Use named volume
docker run -v mydata:/app/data myimage

# List volumes
docker volume ls

# Inspect volume
docker volume inspect mydata

# Remove volume
docker volume rm mydata
```

### Practical Example

```bash
# Create a volume for database data
docker volume create postgres_data

# Run PostgreSQL with persistent storage
docker run -d \
  --name mydb \
  -v postgres_data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:13

# Data persists even if container is removed
docker rm -f mydb
docker run -d \
  --name mydb_new \
  -v postgres_data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:13
```

---

## 🌍 Environment Variables (-e)

Pass configuration to containers:

```bash
# Single variable
docker run -e MY_VAR=value myimage

# Multiple variables
docker run -e VAR1=value1 -e VAR2=value2 myimage

# From file
docker run --env-file .env myimage

# Common example: Database configuration
docker run -d \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=myapp \
  postgres:13
```

### Environment File Example

```bash
# .env file
DATABASE_URL=postgres://localhost/mydb
SECRET_KEY=my-secret-key
DEBUG=false

# Use with Docker
docker run --env-file .env myimage
```

---

## 🔄 Container Lifecycle

### Start/Stop/Restart

```bash
# Start a stopped container
docker start container_name

# Stop a running container
docker stop container_name

# Stop with timeout
docker stop -t 30 container_name

# Force stop (SIGKILL)
docker kill container_name

# Restart
docker restart container_name
```

### Pause/Unpause

```bash
# Pause container (freeze processes)
docker pause container_name

# Unpause
docker unpause container_name
```

### Remove Containers

```bash
# Remove stopped container
docker rm container_name

# Force remove running container
docker rm -f container_name

# Remove all stopped containers
docker container prune

# Remove all containers (careful!)
docker rm -f $(docker ps -aq)
```

---

## 📋 Viewing Containers

### List Containers

```bash
# Running containers
docker ps

# All containers (including stopped)
docker ps -a

# Only container IDs
docker ps -q

# Custom format
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}"

# Filter containers
docker ps --filter "status=running"
docker ps --filter "name=web"
```

### Container Details

```bash
# Full container info
docker inspect container_name

# Specific info
docker inspect --format='{{.State.Status}}' container_name
docker inspect --format='{{.NetworkSettings.IPAddress}}' container_name
```

### Container Logs

```bash
# View logs
docker logs container_name

# Follow logs (like tail -f)
docker logs -f container_name

# Last 100 lines
docker logs --tail 100 container_name

# With timestamps
docker logs -t container_name

# Since a time
docker logs --since 1h container_name
```

### Container Stats

```bash
# Real-time stats for all containers
docker stats

# Specific container
docker stats container_name

# One-time snapshot
docker stats --no-stream
```

---

## 🖥️ Executing Commands in Containers

### Using docker exec

```bash
# Run command in running container
docker exec container_name command

# Interactive shell
docker exec -it container_name bash

# As specific user
docker exec -u root -it container_name bash

# With environment variable
docker exec -e VAR=value container_name command
```

### Practical Examples

```bash
# Start a web server container
docker run -d --name web nginx

# Check nginx config
docker exec web cat /etc/nginx/nginx.conf

# Open shell
docker exec -it web bash

# Install a package
docker exec web apt-get update && apt-get install -y curl
```

---

## 🌐 Container Networking

### Network Modes

```bash
# Bridge (default)
docker run nginx

# Host network
docker run --network host nginx

# None (no networking)
docker run --network none nginx

# Custom network
docker network create mynet
docker run --network mynet nginx
```

### Create and Use Networks

```bash
# Create network
docker network create mynetwork

# Run containers in the same network
docker run -d --name db --network mynetwork postgres:13
docker run -d --name app --network mynetwork myapp

# Containers can communicate by name
# From app container: postgres://db:5432
```

### List and Inspect Networks

```bash
# List networks
docker network ls

# Inspect network
docker network inspect mynetwork

# Connect container to network
docker network connect mynetwork container_name

# Disconnect
docker network disconnect mynetwork container_name
```

---

## 📋 Full Run Example

### Complete Application Stack

```bash
# Create network
docker network create app_network

# Run database
docker run -d \
  --name db \
  --network app_network \
  -v postgres_data:/var/lib/postgresql/data \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=myapp \
  postgres:13

# Run application
docker run -d \
  --name app \
  --network app_network \
  -p 5000:5000 \
  -e DATABASE_URL=postgres://admin:secret@db:5432/myapp \
  --restart unless-stopped \
  myapp:1.0

# Run Redis for caching
docker run -d \
  --name redis \
  --network app_network \
  redis:alpine
```

---

## 🔄 Restart Policies

Control container restart behavior:

```bash
# Never restart (default)
docker run nginx

# Always restart
docker run --restart always nginx

# Restart on failure
docker run --restart on-failure nginx

# Restart on failure with max retries
docker run --restart on-failure:3 nginx

# Restart unless stopped manually
docker run --restart unless-stopped nginx
```

---

## 📊 Resource Limits

Control container resources:

```bash
# Limit memory
docker run -m 512m nginx

# Limit CPU
docker run --cpus 1.5 nginx

# Memory and CPU
docker run -m 1g --cpus 2 nginx

# Memory swap
docker run -m 512m --memory-swap 1g nginx
```

---

## 📝 Practical Exercises

### Exercise 1: Run and Test Nginx

```bash
# Run nginx
docker run -d --name web -p 8080:80 nginx

# Verify
curl http://localhost:8080

# View logs
docker logs web

# Clean up
docker stop web && docker rm web
```

### Exercise 2: Interactive Python

```bash
# Run Python interactively
docker run -it --rm python:3.9

# Inside Python
>>> print("Hello from Docker!")
>>> import sys
>>> sys.version
>>> exit()
```

### Exercise 3: Share Files

```bash
# Create a test file
echo "Hello Docker" > /tmp/test.txt

# Mount and read
docker run -v /tmp:/data alpine cat /data/test.txt
```

### Exercise 4: Environment Variables

```bash
# Pass variables
docker run -e NAME=Docker alpine sh -c 'echo Hello $NAME'
```

---

## ✅ Best Practices

1. **Use `--name`** for easier management
2. **Use `-d`** for long-running services
3. **Use `--rm`** for one-off commands
4. **Use named volumes** for persistent data
5. **Use networks** for container communication
6. **Set restart policies** for production
7. **Limit resources** to prevent issues

---

## 🎯 Key Takeaways

1. `docker run` creates and starts containers
2. **-d** for background, **-it** for interactive
3. **-p** maps ports, **-v** mounts volumes
4. **-e** passes environment variables
5. Use **exec** to run commands in running containers

---

## 📚 Next Steps

Move on to `05_docker_compose_basics.md` to learn about multi-container applications!

---
**Practice running different types of containers!** 🐳
