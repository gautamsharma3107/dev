"""
Day 19 - Environment Variables and Secrets
==========================================
Learn: Managing configuration and sensitive data securely

Key Concepts:
- What are environment variables
- Why use environment variables
- Loading environment variables
- Using .env files
- Secrets management best practices
- Pydantic settings for validation
"""

import os

print("=" * 60)
print("ENVIRONMENT VARIABLES AND SECRETS")
print("=" * 60)

# ========== WHAT ARE ENVIRONMENT VARIABLES? ==========
print("\n" + "=" * 60)
print("WHAT ARE ENVIRONMENT VARIABLES?")
print("=" * 60)

print("""
Environment variables are key-value pairs stored at the 
OS level that can be accessed by any program.

WHY USE THEM?
1. SECURITY
   - Keep secrets out of code
   - Don't commit passwords to git

2. CONFIGURATION
   - Different values for dev/staging/prod
   - Easy to change without code changes

3. PORTABILITY
   - Same code works in any environment
   - 12-factor app methodology

4. DEPLOYMENT
   - Cloud platforms use env vars for config
   - Docker, Kubernetes, Heroku all support them

COMMON USE CASES:
- Database connection strings
- API keys and secrets
- Feature flags
- Debug mode settings
- Service URLs
""")

# ========== ACCESSING ENVIRONMENT VARIABLES ==========
print("\n" + "=" * 60)
print("ACCESSING ENVIRONMENT VARIABLES")
print("=" * 60)

# Get environment variable (returns None if not found)
home = os.getenv("HOME")
print(f"HOME: {home}")

# Get with default value
debug = os.getenv("DEBUG", "False")
print(f"DEBUG (with default): {debug}")

# Using os.environ (raises KeyError if not found)
try:
    path = os.environ["PATH"]
    print(f"PATH exists: {len(path)} characters")
except KeyError:
    print("PATH not found")

# Check if variable exists
if os.getenv("MY_SECRET"):
    print("MY_SECRET is set")
else:
    print("MY_SECRET is not set")

# Get all environment variables
print(f"\nTotal environment variables: {len(os.environ)}")

# ========== SETTING ENVIRONMENT VARIABLES ==========
print("\n" + "=" * 60)
print("SETTING ENVIRONMENT VARIABLES")
print("=" * 60)

# Set in Python (only for current process)
os.environ["MY_APP_MODE"] = "development"
os.environ["MY_APP_DEBUG"] = "true"

print(f"MY_APP_MODE: {os.getenv('MY_APP_MODE')}")
print(f"MY_APP_DEBUG: {os.getenv('MY_APP_DEBUG')}")

# Remove environment variable
if "MY_APP_MODE" in os.environ:
    del os.environ["MY_APP_MODE"]

print("""
SETTING FROM COMMAND LINE:
==========================

# Linux/Mac (temporary for command)
$ DEBUG=true python app.py

# Linux/Mac (export for session)
$ export DATABASE_URL="postgresql://localhost/db"
$ python app.py

# Windows (cmd)
> set DATABASE_URL=postgresql://localhost/db
> python app.py

# Windows (PowerShell)
> $env:DATABASE_URL = "postgresql://localhost/db"
> python app.py
""")

# ========== USING .ENV FILES ==========
print("\n" + "=" * 60)
print("USING .ENV FILES WITH python-dotenv")
print("=" * 60)

dotenv_code = '''
# Install: pip install python-dotenv

# .env file (in project root)
# =========================
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
SECRET_KEY=super-secret-key-12345
DEBUG=True
API_KEY=abc123xyz789
REDIS_URL=redis://localhost:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1,myapp.com

# app.py
# ======
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()  # Loads from .env in current directory

# Or specify path
load_dotenv("/path/to/.env")

# Now access variables
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
debug = os.getenv("DEBUG", "False").lower() == "true"

print(f"Database: {database_url}")
print(f"Debug mode: {debug}")


# Advanced: Load different files for different environments
# ========================================================
import os

env = os.getenv("ENVIRONMENT", "development")

if env == "production":
    load_dotenv(".env.production")
elif env == "staging":
    load_dotenv(".env.staging")
else:
    load_dotenv(".env.development")
'''

print("Using .env files:")
print(dotenv_code)

# ========== .ENV FILE FORMAT ==========
print("\n" + "=" * 60)
print(".ENV FILE FORMAT AND EXAMPLES")
print("=" * 60)

print("""
# .env file format
# ================

# Basic key=value
DATABASE_URL=postgresql://localhost/db
SECRET_KEY=my-secret-key

# With quotes (for values with spaces)
MESSAGE="Hello World"
GREETING='Welcome to the app'

# Multiline (use quotes)
PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA
-----END RSA PRIVATE KEY-----"

# Comments start with #
# This is a comment
API_KEY=abc123  # This is also a comment

# Empty values
EMPTY_VAR=

# Boolean values (parse as strings!)
DEBUG=true
VERBOSE=1
ENABLED=yes

# List values (parse as string, split in code)
ALLOWED_HOSTS=localhost,127.0.0.1,myapp.com

# JSON values (as string)
CONFIG='{"key": "value", "number": 42}'


IMPORTANT: Never commit .env to git!
Add to .gitignore:
    .env
    .env.local
    .env.*.local
""")

# ========== PYDANTIC SETTINGS (RECOMMENDED) ==========
print("\n" + "=" * 60)
print("PYDANTIC SETTINGS FOR VALIDATION")
print("=" * 60)

pydantic_settings_code = '''
# Install: pip install pydantic-settings

# config.py
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List

class Settings(BaseSettings):
    """Application settings with validation."""
    
    # Required fields (no default = must be set)
    database_url: str
    secret_key: str
    
    # Optional with defaults
    debug: bool = False
    api_version: str = "v1"
    
    # With validation
    port: int = Field(default=8000, ge=1, le=65535)
    
    # List parsing (comma-separated string → list)
    allowed_hosts: List[str] = ["localhost"]
    
    # Field alias (env var name different from attribute)
    db_url: str = Field(alias="DATABASE_URL")
    
    # Nested settings
    redis_host: str = "localhost"
    redis_port: int = 6379
    
    class Config:
        # Load from .env file
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        # Case-insensitive env var names
        case_sensitive = False
        
        # Prefix for all env vars
        # env_prefix = "MYAPP_"  # Would look for MYAPP_DEBUG, etc.


# Create settings instance (loads on import)
settings = Settings()


# Usage in your app
# ================
from config import settings

print(f"Debug mode: {settings.debug}")
print(f"Database: {settings.database_url}")
print(f"Port: {settings.port}")

# FastAPI dependency
from fastapi import FastAPI, Depends

def get_settings():
    return settings

@app.get("/info")
def info(settings: Settings = Depends(get_settings)):
    return {"debug": settings.debug, "version": settings.api_version}


# Testing with different settings
# ==============================
from config import Settings

test_settings = Settings(
    database_url="sqlite:///test.db",
    secret_key="test-key",
    debug=True
)
'''

print("Pydantic Settings (recommended):")
print(pydantic_settings_code)

# ========== SECRETS MANAGEMENT ==========
print("\n" + "=" * 60)
print("SECRETS MANAGEMENT BEST PRACTICES")
print("=" * 60)

print("""
❌ DON'T:
   - Commit secrets to git (even in .env)
   - Log secrets
   - Pass secrets in URLs
   - Share secrets in plain text
   - Use same secrets for dev/prod
   - Store secrets in code

✅ DO:
   - Use environment variables
   - Use secret management services
   - Rotate secrets regularly
   - Use different secrets per environment
   - Encrypt secrets at rest
   - Audit secret access


SECRET MANAGEMENT SERVICES:
===========================
1. AWS Secrets Manager
2. HashiCorp Vault
3. Azure Key Vault
4. Google Secret Manager
5. Docker Secrets
6. Kubernetes Secrets
""")

# ========== CLOUD SECRET MANAGERS ==========
print("\n" + "=" * 60)
print("USING CLOUD SECRET MANAGERS")
print("=" * 60)

cloud_secrets_code = '''
# AWS Secrets Manager
# ==================
import boto3
import json

def get_aws_secret(secret_name: str) -> dict:
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

secrets = get_aws_secret("myapp/production/db")
db_password = secrets["password"]


# Google Secret Manager
# ====================
from google.cloud import secretmanager

def get_gcp_secret(project_id: str, secret_id: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

api_key = get_gcp_secret("my-project", "api-key")


# Azure Key Vault
# ==============
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_azure_secret(vault_url: str, secret_name: str) -> str:
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    return client.get_secret(secret_name).value

password = get_azure_secret(
    "https://myvault.vault.azure.net/",
    "db-password"
)
'''

print("Cloud secret managers:")
print(cloud_secrets_code)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: COMPLETE CONFIG SETUP")
print("=" * 60)

complete_example_code = '''
# Project structure:
# ==================
# myapp/
# ├── .env                 # Local development (gitignored)
# ├── .env.example         # Template (committed)
# ├── config.py
# ├── main.py
# └── ...

# .env.example (commit this as template)
# =====================================
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=change-this-in-production
DEBUG=true
API_KEY=your-api-key-here
REDIS_URL=redis://localhost:6379/0
ALLOWED_HOSTS=localhost,127.0.0.1

# config.py
# =========
from pydantic_settings import BaseSettings
from pydantic import Field, field_validator
from typing import List
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    database_url: str
    
    # Security
    secret_key: str
    debug: bool = False
    
    # API
    api_key: str
    api_version: str = "v1"
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # Server
    host: str = "0.0.0.0"
    port: int = Field(default=8000, ge=1, le=65535)
    allowed_hosts: List[str] = ["localhost"]
    
    @field_validator("allowed_hosts", mode="before")
    def parse_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [h.strip() for h in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Cached settings (singleton)."""
    return Settings()

# main.py
# ========
from fastapi import FastAPI, Depends
from config import Settings, get_settings

app = FastAPI()

@app.get("/health")
def health(settings: Settings = Depends(get_settings)):
    return {
        "status": "healthy",
        "debug": settings.debug,
        "version": settings.api_version
    }

# When deploying, set env vars in your platform:
# - Heroku: heroku config:set DATABASE_URL=...
# - Docker: docker run -e DATABASE_URL=...
# - Kubernetes: ConfigMaps and Secrets
'''

print("Complete config setup:")
print(complete_example_code)

# ========== DOCKER AND ENVIRONMENT VARIABLES ==========
print("\n" + "=" * 60)
print("DOCKER AND ENVIRONMENT VARIABLES")
print("=" * 60)

docker_env_code = '''
# Dockerfile - set default env vars
ENV DEBUG=false
ENV PORT=8000

# docker-compose.yml - pass env vars
version: "3.8"
services:
  web:
    build: .
    environment:
      - DEBUG=true
      - DATABASE_URL=postgresql://db:5432/mydb
    env_file:
      - .env.docker
    ports:
      - "8000:8000"

# Run with env vars
docker run -e DATABASE_URL=... -e SECRET_KEY=... myapp

# Using .env file with docker-compose
docker-compose --env-file .env.production up

# Docker secrets (Swarm/Kubernetes)
# More secure - secrets mounted as files
services:
  web:
    secrets:
      - db_password
secrets:
  db_password:
    file: ./secrets/db_password.txt
'''

print("Docker environment variables:")
print(docker_env_code)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY: ENVIRONMENT VARIABLES BEST PRACTICES")
print("=" * 60)

print("""
1. USE .env FILES FOR LOCAL DEVELOPMENT
   - Never commit actual .env files
   - Commit .env.example as template

2. USE PYDANTIC SETTINGS FOR VALIDATION
   - Type checking and validation
   - Default values
   - Easy testing

3. DIFFERENT CONFIGS FOR DIFFERENT ENVIRONMENTS
   - .env.development
   - .env.staging
   - .env.production

4. SECRETS MANAGEMENT
   - Use cloud secret managers in production
   - Rotate secrets regularly
   - Audit access

5. DOCKER/KUBERNETES
   - Use environment variables or secrets
   - Don't bake secrets into images

6. NEVER DO
   - Commit secrets to git
   - Log sensitive values
   - Use same secrets everywhere
""")

print("\n" + "=" * 60)
print("✅ Environment Variables and Secrets - Complete!")
print("=" * 60)
