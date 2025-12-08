"""
EXERCISES: Docker Compose
=========================
Complete all exercises to practice Docker Compose concepts
"""

print("=" * 60)
print("Docker Compose Exercises")
print("=" * 60)

# Exercise 1: Docker Compose Concepts
print("""
Exercise 1: Docker Compose Concepts
-----------------------------------
Answer the following questions:

1. What is Docker Compose used for?
   Your answer:


2. What is the default name of the Docker Compose file?
   Your answer:


3. What command starts all services defined in docker-compose.yml?
   Your answer:


4. What does 'depends_on' do in a docker-compose.yml file?
   Your answer:


""")

# Exercise 2: Analyze docker-compose.yml
print("""
Exercise 2: Analyze docker-compose.yml
--------------------------------------
Analyze this docker-compose.yml and answer questions:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      - POSTGRES_PASSWORD=pass
      - POSTGRES_USER=user
      - POSTGRES_DB=mydb
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

Questions:
1. How many services are defined?
   Answer:

2. Where does the 'web' service get its image from?
   Answer:

3. What port is exposed on the host?
   Answer:

4. What volume is being used and what does it persist?
   Answer:

5. Why does 'web' depend on 'db'?
   Answer:

""")

# Exercise 3: Write docker-compose.yml
print("""
Exercise 3: Write docker-compose.yml
------------------------------------
Write a docker-compose.yml for the following requirements:

Requirements:
1. A web service that:
   - Builds from current directory
   - Maps port 8080 to container port 80
   - Has environment variable NODE_ENV=production

2. A redis service that:
   - Uses redis:alpine image
   - Maps port 6379 to 6379

3. Web service should depend on redis

Write your docker-compose.yml below:
------------------------------------




""")

# Exercise 4: Docker Compose Commands
print("""
Exercise 4: Docker Compose Commands
-----------------------------------
Write the Docker Compose commands for these tasks:

1. Start all services in detached mode:
   Command:


2. View logs of all services (following):
   Command:


3. Stop all services and remove containers:
   Command:


4. Rebuild images and start services:
   Command:


5. Execute bash in the 'web' service:
   Command:


6. Scale the 'web' service to 3 instances:
   Command:


""")

# Exercise 5: Environment Variables
print("""
Exercise 5: Environment Variables
---------------------------------
Show different ways to pass environment variables:

1. Using environment key in YAML:
   Example:


2. Using env_file:
   Example:


3. Using variable substitution from .env file:
   Example:


""")

# Exercise 6: Debug This Configuration
print("""
Exercise 6: Debug This Configuration
------------------------------------
Find and fix the errors in this docker-compose.yml:

```yaml
version: 3.8  # Error 1

services:
  web
    image: nginx  # Error 2
    port:  # Error 3
      - "80:80"
    volumes:
      ./html:/usr/share/nginx/html  # Error 4
```

Fixed version:




""")

print("""
=" * 60)
EXERCISE SOLUTIONS
=" * 60)

Exercise 1 Solutions:
1. Defining and running multi-container Docker applications
2. docker-compose.yml
3. docker-compose up
4. Specifies service dependencies/startup order

Exercise 2 Solutions:
1. 2 services (web and db)
2. Builds from Dockerfile in current directory
3. Port 5000
4. db_data volume persists PostgreSQL data
5. Web needs database to be available first

Exercise 3 Solution:
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8080:80"
    environment:
      - NODE_ENV=production
    depends_on:
      - redis

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

Exercise 4 Solutions:
1. docker-compose up -d
2. docker-compose logs -f
3. docker-compose down
4. docker-compose up --build
5. docker-compose exec web bash
6. docker-compose up -d --scale web=3

Exercise 5 Solutions:
1. environment:
     - VAR_NAME=value

2. env_file:
     - .env

3. environment:
     - VAR_NAME=${VAR_FROM_ENV}

Exercise 6 Solution:
```yaml
version: '3.8'  # Fixed: needs quotes

services:
  web:          # Fixed: added colon
    image: nginx
    ports:      # Fixed: ports not port
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html  # Fixed: added dash
```
""")

print("\n" + "=" * 60)
print("Great job completing the Docker Compose exercises!")
print("=" * 60)
