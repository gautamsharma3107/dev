"""
MINI PROJECT 3: Secure Configuration Manager
============================================
Build a complete configuration management system

Requirements:
1. Load settings from multiple sources (env vars, .env files, defaults)
2. Validate all settings with Pydantic
3. Support different environments (dev, staging, prod)
4. Implement secrets management patterns
5. Add security headers middleware
6. Complete CORS setup

This project ties together all Day 19 concepts!
"""

print("=" * 60)
print("SECURE CONFIGURATION MANAGER")
print("=" * 60)

# TODO: Implement the configuration manager

# 1. Settings class with validation
# ----------------------------------
# from pydantic_settings import BaseSettings
# from pydantic import Field, field_validator
# from typing import List, Literal
#
# class DatabaseSettings(BaseSettings):
#     url: str
#     pool_size: int = Field(default=5, ge=1, le=100)
#     
#     class Config:
#         env_prefix = "DB_"
#
# class SecuritySettings(BaseSettings):
#     secret_key: str
#     algorithm: str = "HS256"
#     access_token_expire_minutes: int = 30
#     
#     class Config:
#         env_prefix = "SECURITY_"
#
# class CORSSettings(BaseSettings):
#     origins: List[str] = ["http://localhost:3000"]
#     allow_credentials: bool = True
#     allow_methods: List[str] = ["*"]
#     allow_headers: List[str] = ["*"]
#     
#     @field_validator("origins", mode="before")
#     def parse_origins(cls, v):
#         if isinstance(v, str):
#             return [o.strip() for o in v.split(",")]
#         return v
#     
#     class Config:
#         env_prefix = "CORS_"
#
# class Settings(BaseSettings):
#     app_name: str = "MyApp"
#     environment: Literal["development", "staging", "production"] = "development"
#     debug: bool = False
#     
#     # Nested settings
#     database: DatabaseSettings = DatabaseSettings()
#     security: SecuritySettings = SecuritySettings()
#     cors: CORSSettings = CORSSettings()
#     
#     @property
#     def is_production(self) -> bool:
#         return self.environment == "production"
#     
#     class Config:
#         env_file = ".env"


# 2. Environment-specific loading
# -------------------------------
# import os
# from functools import lru_cache
#
# @lru_cache()
# def get_settings() -> Settings:
#     env = os.getenv("ENVIRONMENT", "development")
#     env_file = f".env.{env}"
#     return Settings(_env_file=env_file if os.path.exists(env_file) else ".env")


# 3. Security headers middleware
# ------------------------------
# from starlette.middleware.base import BaseHTTPMiddleware
# from fastapi import Request
#
# class SecurityHeadersMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         response = await call_next(request)
#         
#         # Add security headers
#         response.headers["X-Content-Type-Options"] = "nosniff"
#         response.headers["X-Frame-Options"] = "DENY"
#         response.headers["X-XSS-Protection"] = "1; mode=block"
#         
#         if settings.is_production:
#             response.headers["Strict-Transport-Security"] = "max-age=31536000"
#         
#         return response


# 4. Complete FastAPI app setup
# -----------------------------
# from fastapi import FastAPI, Depends
# from fastapi.middleware.cors import CORSMiddleware
#
# settings = get_settings()
# app = FastAPI(title=settings.app_name, debug=settings.debug)
#
# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.cors.origins,
#     allow_credentials=settings.cors.allow_credentials,
#     allow_methods=settings.cors.allow_methods,
#     allow_headers=settings.cors.allow_headers,
# )
#
# # Security headers middleware
# app.add_middleware(SecurityHeadersMiddleware)
#
# @app.get("/config")
# def get_config(settings: Settings = Depends(get_settings)):
#     """Return non-sensitive configuration."""
#     return {
#         "app_name": settings.app_name,
#         "environment": settings.environment,
#         "debug": settings.debug,
#         # Never expose secrets!
#     }


# 5. Example .env file structure
# ------------------------------
# .env.development
# ================
# ENVIRONMENT=development
# DEBUG=true
# DB_URL=postgresql://localhost/dev_db
# SECURITY_SECRET_KEY=dev-secret-key-change-in-prod
# CORS_ORIGINS=http://localhost:3000,http://localhost:5173
#
# .env.production
# ===============
# ENVIRONMENT=production
# DEBUG=false
# DB_URL=postgresql://prod-server/prod_db
# SECURITY_SECRET_KEY=${SECRET_FROM_VAULT}
# CORS_ORIGINS=https://myapp.com,https://www.myapp.com


# BONUS: Add these features
# -------------------------
# - Secret rotation support
# - Configuration validation on startup
# - Hot reload for development
# - Configuration diff between environments


print("\nImplement your configuration manager above!")
