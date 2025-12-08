# Day 42 Quick Reference Cheat Sheet

## ML Model Saving & Loading
```python
import pickle
import joblib

# Save model with pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load model with pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Save model with joblib (better for large arrays)
joblib.dump(model, 'model.joblib')

# Load model with joblib
model = joblib.load('model.joblib')
```

## FastAPI Backend Basics
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="ML API")

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    result = model.predict([request.features])
    return {"prediction": result[0], "confidence": 0.95}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## SQLAlchemy Database Setup
```python
from sqlalchemy import create_engine, Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./predictions.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    input_features = Column(String)
    prediction = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)
```

## Database Dependency Injection
```python
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/predict")
async def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    # Save prediction to database
    db_prediction = Prediction(
        input_features=str(request.features),
        prediction=result
    )
    db.add(db_prediction)
    db.commit()
    return {"prediction": result}
```

## Simple HTML Frontend
```html
<!DOCTYPE html>
<html>
<head>
    <title>ML Prediction App</title>
</head>
<body>
    <h1>ML Prediction Service</h1>
    <form id="predictForm">
        <input type="text" id="features" placeholder="Enter features (comma-separated)">
        <button type="submit">Predict</button>
    </form>
    <div id="result"></div>
    
    <script>
        document.getElementById('predictForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const features = document.getElementById('features').value.split(',').map(Number);
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({features})
            });
            const data = await response.json();
            document.getElementById('result').innerHTML = `Prediction: ${data.prediction}`;
        });
    </script>
</body>
</html>
```

## Serving Static Files with FastAPI
```python
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
```

## Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Docker Compose
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    environment:
      - DATABASE_URL=sqlite:///./data/predictions.db
    
  # Optional: PostgreSQL
  db:
    image: postgres:14
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mlapp
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Docker Commands
```bash
# Build image
docker build -t ml-app .

# Run container
docker run -d -p 8000:8000 ml-app

# Docker Compose
docker-compose up -d
docker-compose down
docker-compose logs -f

# View running containers
docker ps

# Stop container
docker stop <container_id>
```

## Testing the API
```python
import requests

# Test prediction endpoint
response = requests.post(
    "http://localhost:8000/predict",
    json={"features": [1.0, 2.0, 3.0, 4.0]}
)
print(response.json())

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())
```

## Environment Variables
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./predictions.db")
MODEL_PATH = os.getenv("MODEL_PATH", "./ml/model.pkl")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
```

## Requirements.txt
```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.2
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
python-multipart==0.0.6
jinja2==3.1.2
python-dotenv==1.0.0
joblib==1.3.2
```

## Common Patterns

### Error Handling
```python
from fastapi import HTTPException

@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        result = model.predict([request.features])
        return {"prediction": float(result[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Health Check Endpoint
```python
@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": model is not None}
```

### CORS Configuration
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---
**Keep this handy while building your Full-Stack ML Application! 🚀**
