"""
EXERCISES: Docker Basics
========================
Complete all exercises below to practice Docker concepts
"""

print("=" * 60)
print("Docker Basics Exercises")
print("=" * 60)

# Exercise 1: Docker Concepts
print("""
Exercise 1: Docker Concepts
---------------------------
Answer the following questions about Docker:

1. What is the difference between a Docker image and a container?
   Your answer:


2. What problem does Docker solve?
   Your answer:


3. Name 3 advantages of using containers over virtual machines:
   Your answer:


""")

# Exercise 2: Basic Docker Commands
print("""
Exercise 2: Basic Docker Commands
---------------------------------
Write the Docker commands for the following tasks:

1. Pull the nginx:latest image:
   Command:


2. List all running containers:
   Command:


3. List all images on your system:
   Command:


4. Run nginx container in detached mode with name 'web':
   Command:


5. Stop and remove the 'web' container:
   Command:


""")

# Exercise 3: Dockerfile Analysis
print("""
Exercise 3: Dockerfile Analysis
-------------------------------
Analyze the following Dockerfile and answer questions:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
```

Questions:
1. What is the base image?
   Answer:

2. What is the working directory?
   Answer:

3. Why is requirements.txt copied before the rest of the code?
   Answer:

4. What port does the application listen on?
   Answer:

5. What command runs when the container starts?
   Answer:

""")

# Exercise 4: Write a Dockerfile
print("""
Exercise 4: Write a Dockerfile
------------------------------
Write a Dockerfile for the following Python application:

app.py:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

requirements.txt:
```
flask==2.3.0
```

Requirements:
- Use Python 3.9 slim image
- Set working directory to /app
- Install dependencies
- Expose port 8080
- Run the application

Write your Dockerfile below:
----------------------------




""")

# Exercise 5: Port Mapping
print("""
Exercise 5: Port Mapping
------------------------
Complete the following port mapping exercises:

1. Map container port 80 to host port 8080:
   docker run -p __________ nginx

2. Map container port 5000 to host port 5000:
   docker run -p __________ myapp

3. Map multiple ports (80 and 443) to the same host ports:
   docker run ___________________ nginx

4. What does -P (capital P) do?
   Answer:

""")

# Exercise 6: Volume Mounting
print("""
Exercise 6: Volume Mounting
---------------------------
Write Docker commands for the following volume scenarios:

1. Mount current directory to /app in container:
   Command:


2. Create and use a named volume 'mydata':
   Command:


3. Mount a read-only volume:
   Command:


4. What is the difference between bind mounts and named volumes?
   Answer:


""")

# Exercise 7: Environment Variables
print("""
Exercise 7: Environment Variables
---------------------------------
Complete the following exercises:

1. Run a container with environment variable DEBUG=true:
   Command:


2. Run a container using an .env file:
   Command:


3. In a Dockerfile, set environment variable APP_ENV=production:
   Instruction:


""")

print("""
=" * 60)
EXERCISE SOLUTIONS
=" * 60)

Exercise 1 Solutions:
1. Image = Blueprint/template, Container = Running instance
2. "Works on my machine" problem / Environment consistency
3. Faster startup, smaller size, better resource usage

Exercise 2 Solutions:
1. docker pull nginx:latest
2. docker ps
3. docker images
4. docker run -d --name web nginx
5. docker stop web && docker rm web

Exercise 3 Solutions:
1. python:3.9-slim
2. /app
3. For better caching - dependencies change less often than code
4. 5000
5. flask run --host=0.0.0.0

Exercise 4 Solution:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]
```

Exercise 5 Solutions:
1. -p 8080:80
2. -p 5000:5000
3. -p 80:80 -p 443:443
4. Publishes all exposed ports to random host ports

Exercise 6 Solutions:
1. docker run -v $(pwd):/app myimage
2. docker volume create mydata && docker run -v mydata:/data myimage
3. docker run -v /host/path:/container/path:ro myimage
4. Bind mounts link to host path, named volumes are managed by Docker

Exercise 7 Solutions:
1. docker run -e DEBUG=true myimage
2. docker run --env-file .env myimage
3. ENV APP_ENV=production
""")

print("\n" + "=" * 60)
print("Great job completing the Docker basics exercises!")
print("=" * 60)
