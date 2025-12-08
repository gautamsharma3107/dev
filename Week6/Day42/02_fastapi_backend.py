"""
Day 42 - FastAPI Backend Development
=====================================
Learn: Building REST APIs with FastAPI for ML model serving

Key Concepts:
- FastAPI application structure
- Pydantic models for validation
- Endpoint creation
- Error handling and responses
"""

# ========== SETUP ==========
print("=" * 60)
print("FASTAPI BACKEND DEVELOPMENT")
print("=" * 60)

# Note: This file demonstrates FastAPI concepts
# To run the actual server, use: uvicorn main:app --reload

print("""
FastAPI is a modern, fast web framework for building APIs with Python.
Key features:
- Automatic API documentation
- Data validation with Pydantic
- Async support
- Type hints
- Fast performance
""")

# ========== BASIC FASTAPI APPLICATION ==========
print("\n" + "=" * 60)
print("1. BASIC FASTAPI APPLICATION STRUCTURE")
print("=" * 60)

fastapi_basic = '''
# main.py - Basic FastAPI application

from fastapi import FastAPI
import uvicorn

# Create FastAPI instance
app = FastAPI(
    title="ML Prediction API",
    description="API for serving ML model predictions",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to ML Prediction API"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
print(fastapi_basic)

# ========== PYDANTIC MODELS FOR VALIDATION ==========
print("\n" + "=" * 60)
print("2. PYDANTIC MODELS FOR REQUEST/RESPONSE VALIDATION")
print("=" * 60)

pydantic_models = '''
# schemas.py - Pydantic models for data validation

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PredictionRequest(BaseModel):
    """Request model for predictions"""
    features: List[float] = Field(
        ...,
        min_length=1,
        max_length=100,
        description="List of feature values"
    )
    model_version: Optional[str] = Field(
        default="latest",
        description="Model version to use"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "features": [5.1, 3.5, 1.4, 0.2],
                "model_version": "1.0.0"
            }
        }

class PredictionResponse(BaseModel):
    """Response model for predictions"""
    prediction: float
    confidence: Optional[float] = None
    model_version: str
    timestamp: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction": 0,
                "confidence": 0.95,
                "model_version": "1.0.0",
                "timestamp": "2024-01-01T12:00:00"
            }
        }

class BatchPredictionRequest(BaseModel):
    """Request model for batch predictions"""
    samples: List[List[float]]
    
class BatchPredictionResponse(BaseModel):
    """Response model for batch predictions"""
    predictions: List[float]
    count: int
    model_version: str
'''
print(pydantic_models)

# ========== PREDICTION ENDPOINTS ==========
print("\n" + "=" * 60)
print("3. PREDICTION ENDPOINTS")
print("=" * 60)

prediction_endpoints = '''
# main.py - Prediction endpoints

from fastapi import FastAPI, HTTPException
from datetime import datetime
import pickle
import numpy as np

app = FastAPI(title="ML Prediction API")

# Load model on startup
model = None

@app.on_event("startup")
async def load_model():
    global model
    try:
        with open("ml/model.pkl", "rb") as f:
            model = pickle.load(f)
        print("Model loaded successfully")
    except FileNotFoundError:
        print("Warning: Model file not found")

# Single prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Make a single prediction"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert to numpy array
        features = np.array(request.features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Get confidence if available
        confidence = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(features)[0]
            confidence = float(max(proba))
        
        return PredictionResponse(
            prediction=float(prediction),
            confidence=confidence,
            model_version="1.0.0",
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Batch prediction endpoint
@app.post("/predict/batch", response_model=BatchPredictionResponse)
async def predict_batch(request: BatchPredictionRequest):
    """Make batch predictions"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        features = np.array(request.samples)
        predictions = model.predict(features)
        
        return BatchPredictionResponse(
            predictions=[float(p) for p in predictions],
            count=len(predictions),
            model_version="1.0.0"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
'''
print(prediction_endpoints)

# ========== ERROR HANDLING ==========
print("\n" + "=" * 60)
print("4. ERROR HANDLING")
print("=" * 60)

error_handling = '''
# Error handling in FastAPI

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

app = FastAPI()

# Custom exception
class ModelNotLoadedError(Exception):
    """Raised when model is not loaded"""
    pass

# Global exception handler
@app.exception_handler(ModelNotLoadedError)
async def model_not_loaded_handler(request: Request, exc: ModelNotLoadedError):
    return JSONResponse(
        status_code=503,
        content={"error": "Model not loaded", "detail": str(exc)}
    )

# Validation error handler
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation Error",
            "detail": exc.errors()
        }
    )

# Generic exception handler
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": str(exc)
        }
    )

# Using HTTPException
@app.post("/predict")
async def predict(request: PredictionRequest):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not available",
            headers={"X-Error": "ModelNotLoaded"}
        )
    
    if len(request.features) != expected_features:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {expected_features} features, got {len(request.features)}"
        )
    
    return {"prediction": model.predict([request.features])[0]}
'''
print(error_handling)

# ========== MIDDLEWARE AND CORS ==========
print("\n" + "=" * 60)
print("5. MIDDLEWARE AND CORS")
print("=" * 60)

middleware_cors = '''
# Adding middleware and CORS support

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from time import time
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CORS middleware - allows frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom middleware for request logging
@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time()
    
    # Process request
    response = await call_next(request)
    
    # Calculate processing time
    process_time = time() - start_time
    
    # Log request details
    logger.info(
        f"{request.method} {request.url.path} "
        f"completed in {process_time:.4f}s "
        f"status={response.status_code}"
    )
    
    # Add processing time header
    response.headers["X-Process-Time"] = str(process_time)
    
    return response

# Timing middleware for monitoring
@app.middleware("http")
async def add_timing_header(request, call_next):
    start = time()
    response = await call_next(request)
    response.headers["X-Response-Time"] = f"{(time() - start) * 1000:.2f}ms"
    return response
'''
print(middleware_cors)

# ========== DEPENDENCY INJECTION ==========
print("\n" + "=" * 60)
print("6. DEPENDENCY INJECTION")
print("=" * 60)

dependency_injection = '''
# Dependency injection in FastAPI

from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Optional

app = FastAPI()

# Simple dependency
async def get_model():
    """Dependency that provides the ML model"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return model

# Authentication dependency
async def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Verify API key from header"""
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="API key missing")
    if x_api_key != "your-secret-key":
        raise HTTPException(status_code=403, detail="Invalid API key")
    return x_api_key

# Rate limiting dependency
from collections import defaultdict
from datetime import datetime, timedelta

request_counts = defaultdict(list)

async def rate_limiter(request):
    """Simple rate limiting"""
    client_ip = request.client.host
    now = datetime.now()
    
    # Clean old requests
    request_counts[client_ip] = [
        t for t in request_counts[client_ip]
        if now - t < timedelta(minutes=1)
    ]
    
    # Check rate limit
    if len(request_counts[client_ip]) >= 100:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    request_counts[client_ip].append(now)

# Using dependencies
@app.post("/predict")
async def predict(
    request: PredictionRequest,
    model = Depends(get_model),
    api_key: str = Depends(verify_api_key)
):
    """Protected prediction endpoint"""
    prediction = model.predict([request.features])
    return {"prediction": float(prediction[0])}

# Class-based dependency
class ModelService:
    def __init__(self, model_path: str):
        self.model = self._load_model(model_path)
    
    def _load_model(self, path):
        with open(path, "rb") as f:
            return pickle.load(f)
    
    def predict(self, features):
        return self.model.predict([features])[0]

# Dependency provider
def get_model_service():
    return ModelService("ml/model.pkl")

@app.post("/predict")
async def predict(
    request: PredictionRequest,
    service: ModelService = Depends(get_model_service)
):
    return {"prediction": service.predict(request.features)}
'''
print(dependency_injection)

# ========== COMPLETE API EXAMPLE ==========
print("\n" + "=" * 60)
print("7. COMPLETE API EXAMPLE")
print("=" * 60)

complete_api = '''
# complete_api.py - Full FastAPI ML serving application

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import pickle
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="ML Prediction Service",
    description="Production-ready ML model serving API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model variable
model = None
model_metadata = {
    "version": "1.0.0",
    "loaded_at": None,
    "features": 4
}

# Pydantic models
class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_length=1)
    
class PredictionResponse(BaseModel):
    prediction: float
    model_version: str
    timestamp: datetime

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    version: str

# Startup event
@app.on_event("startup")
async def startup_event():
    global model, model_metadata
    try:
        with open("ml/model.pkl", "rb") as f:
            model = pickle.load(f)
        model_metadata["loaded_at"] = datetime.now().isoformat()
        logger.info("Model loaded successfully")
    except FileNotFoundError:
        logger.warning("Model file not found - API will return 503")

# Dependency
async def get_model():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return model

# Endpoints
@app.get("/", tags=["General"])
async def root():
    """Welcome endpoint"""
    return {"message": "ML Prediction Service", "docs": "/docs"}

@app.get("/health", response_model=HealthResponse, tags=["General"])
async def health():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        model_loaded=model is not None,
        version=model_metadata["version"]
    )

@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
async def predict(
    request: PredictionRequest,
    loaded_model = Depends(get_model)
):
    """
    Make a prediction using the ML model.
    
    - **features**: List of numeric feature values
    """
    try:
        features = np.array(request.features).reshape(1, -1)
        prediction = float(loaded_model.predict(features)[0])
        
        logger.info(f"Prediction made: {prediction}")
        
        return PredictionResponse(
            prediction=prediction,
            model_version=model_metadata["version"],
            timestamp=datetime.now()
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/model/info", tags=["Model"])
async def model_info():
    """Get model information"""
    return model_metadata

# Run with: uvicorn complete_api:app --host 0.0.0.0 --port 8000
'''
print(complete_api)

# ========== TESTING THE API ==========
print("\n" + "=" * 60)
print("8. TESTING THE API")
print("=" * 60)

testing_api = '''
# test_api.py - Testing FastAPI endpoints

import requests

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health check: {response.json()}")
    assert response.status_code == 200

def test_predict():
    """Test prediction endpoint"""
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    print(f"Prediction: {response.json()}")
    assert response.status_code == 200

def test_predict_invalid():
    """Test with invalid input"""
    payload = {"features": []}  # Empty features
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    print(f"Invalid input response: {response.status_code}")
    assert response.status_code == 422

# Using pytest with FastAPI TestClient
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_prediction():
    response = client.post(
        "/predict",
        json={"features": [1.0, 2.0, 3.0, 4.0]}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()

# Run tests: pytest test_api.py -v
'''
print(testing_api)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. FastAPI Basics
   - Create app with FastAPI()
   - Define endpoints with decorators
   - Use async functions for handlers

2. Pydantic Models
   - Define request/response schemas
   - Automatic validation
   - Documentation generation

3. Error Handling
   - Use HTTPException for errors
   - Custom exception handlers
   - Proper status codes

4. Middleware
   - CORS for frontend access
   - Request logging
   - Performance monitoring

5. Dependencies
   - Dependency injection
   - Authentication
   - Rate limiting

6. Best Practices
   - Use type hints
   - Document endpoints
   - Test thoroughly
   - Handle errors gracefully
""")

print("\n" + "=" * 60)
print("✅ FastAPI Backend Development - Complete!")
print("=" * 60)
