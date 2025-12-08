"""
Day 42 - Database Integration
==============================
Learn: Setting up database for storing ML prediction results

Key Concepts:
- SQLAlchemy ORM setup
- Database models for predictions
- CRUD operations
- FastAPI integration with database
"""

# ========== SETUP ==========
print("=" * 60)
print("DATABASE INTEGRATION")
print("=" * 60)

print("""
Database integration allows us to:
- Store prediction history
- Track model performance
- Enable analytics
- Provide audit trails
""")

# ========== SQLALCHEMY SETUP ==========
print("\n" + "=" * 60)
print("1. SQLALCHEMY DATABASE SETUP")
print("=" * 60)

database_setup = '''
# database.py - Database configuration

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL from environment or default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./predictions.db")

# For PostgreSQL:
# DATABASE_URL = "postgresql://user:password@localhost:5432/mlapp"

# Create engine
engine = create_engine(
    DATABASE_URL,
    # SQLite specific settings
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)
'''
print(database_setup)

# ========== DATABASE MODELS ==========
print("\n" + "=" * 60)
print("2. DATABASE MODELS")
print("=" * 60)

models = '''
# models.py - SQLAlchemy models

from sqlalchemy import Column, Integer, Float, String, DateTime, JSON, Boolean
from sqlalchemy.sql import func
from database import Base

class Prediction(Base):
    """Model to store prediction results"""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    input_features = Column(JSON, nullable=False)
    prediction = Column(Float, nullable=False)
    confidence = Column(Float, nullable=True)
    model_version = Column(String(50), default="1.0.0")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<Prediction(id={self.id}, prediction={self.prediction})>"

class ModelMetrics(Base):
    """Model to store model performance metrics"""
    __tablename__ = "model_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    model_version = Column(String(50), nullable=False)
    accuracy = Column(Float, nullable=True)
    precision_score = Column(Float, nullable=True)
    recall = Column(Float, nullable=True)
    f1_score = Column(Float, nullable=True)
    evaluation_date = Column(DateTime(timezone=True), server_default=func.now())
    notes = Column(String(500), nullable=True)

class User(Base):
    """Model for API users"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    api_key = Column(String(200), unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    request_count = Column(Integer, default=0)
'''
print(models)

# ========== CRUD OPERATIONS ==========
print("\n" + "=" * 60)
print("3. CRUD OPERATIONS")
print("=" * 60)

crud = '''
# crud.py - Database operations

from sqlalchemy.orm import Session
from sqlalchemy import desc
from datetime import datetime, timedelta
from typing import List, Optional
import models
import schemas

# ========== PREDICTION CRUD ==========

def create_prediction(
    db: Session,
    input_features: list,
    prediction: float,
    confidence: float = None,
    model_version: str = "1.0.0"
) -> models.Prediction:
    """Create a new prediction record"""
    db_prediction = models.Prediction(
        input_features=input_features,
        prediction=prediction,
        confidence=confidence,
        model_version=model_version
    )
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

def get_prediction(db: Session, prediction_id: int) -> Optional[models.Prediction]:
    """Get a prediction by ID"""
    return db.query(models.Prediction).filter(
        models.Prediction.id == prediction_id
    ).first()

def get_predictions(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> List[models.Prediction]:
    """Get list of predictions with pagination"""
    return db.query(models.Prediction).order_by(
        desc(models.Prediction.created_at)
    ).offset(skip).limit(limit).all()

def get_predictions_by_date_range(
    db: Session,
    start_date: datetime,
    end_date: datetime
) -> List[models.Prediction]:
    """Get predictions within a date range"""
    return db.query(models.Prediction).filter(
        models.Prediction.created_at >= start_date,
        models.Prediction.created_at <= end_date
    ).all()

def get_prediction_stats(db: Session) -> dict:
    """Get prediction statistics"""
    from sqlalchemy import func
    
    total = db.query(func.count(models.Prediction.id)).scalar()
    avg_prediction = db.query(func.avg(models.Prediction.prediction)).scalar()
    avg_confidence = db.query(func.avg(models.Prediction.confidence)).scalar()
    
    return {
        "total_predictions": total,
        "average_prediction": float(avg_prediction) if avg_prediction else None,
        "average_confidence": float(avg_confidence) if avg_confidence else None
    }

def delete_old_predictions(db: Session, days: int = 30) -> int:
    """Delete predictions older than specified days"""
    cutoff_date = datetime.now() - timedelta(days=days)
    deleted = db.query(models.Prediction).filter(
        models.Prediction.created_at < cutoff_date
    ).delete()
    db.commit()
    return deleted

# ========== MODEL METRICS CRUD ==========

def create_model_metrics(
    db: Session,
    model_version: str,
    accuracy: float,
    precision_score: float = None,
    recall: float = None,
    f1_score: float = None,
    notes: str = None
) -> models.ModelMetrics:
    """Create model metrics record"""
    metrics = models.ModelMetrics(
        model_version=model_version,
        accuracy=accuracy,
        precision_score=precision_score,
        recall=recall,
        f1_score=f1_score,
        notes=notes
    )
    db.add(metrics)
    db.commit()
    db.refresh(metrics)
    return metrics

def get_latest_metrics(db: Session, model_version: str) -> Optional[models.ModelMetrics]:
    """Get latest metrics for a model version"""
    return db.query(models.ModelMetrics).filter(
        models.ModelMetrics.model_version == model_version
    ).order_by(desc(models.ModelMetrics.evaluation_date)).first()
'''
print(crud)

# ========== PYDANTIC SCHEMAS ==========
print("\n" + "=" * 60)
print("4. PYDANTIC SCHEMAS FOR DATABASE")
print("=" * 60)

schemas_code = '''
# schemas.py - Pydantic schemas for database models

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ========== PREDICTION SCHEMAS ==========

class PredictionBase(BaseModel):
    """Base schema for prediction"""
    input_features: List[float]

class PredictionCreate(PredictionBase):
    """Schema for creating prediction"""
    pass

class PredictionResponse(PredictionBase):
    """Schema for prediction response"""
    id: int
    prediction: float
    confidence: Optional[float] = None
    model_version: str
    created_at: datetime
    
    class Config:
        from_attributes = True  # Pydantic v2

class PredictionList(BaseModel):
    """Schema for list of predictions"""
    predictions: List[PredictionResponse]
    total: int
    page: int
    per_page: int

class PredictionStats(BaseModel):
    """Schema for prediction statistics"""
    total_predictions: int
    average_prediction: Optional[float]
    average_confidence: Optional[float]

# ========== MODEL METRICS SCHEMAS ==========

class ModelMetricsCreate(BaseModel):
    """Schema for creating model metrics"""
    model_version: str
    accuracy: float
    precision_score: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    notes: Optional[str] = None

class ModelMetricsResponse(ModelMetricsCreate):
    """Schema for model metrics response"""
    id: int
    evaluation_date: datetime
    
    class Config:
        from_attributes = True
'''
print(schemas_code)

# ========== FASTAPI INTEGRATION ==========
print("\n" + "=" * 60)
print("5. FASTAPI DATABASE INTEGRATION")
print("=" * 60)

fastapi_db = '''
# main.py - FastAPI with database integration

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import pickle
import numpy as np

from database import get_db, init_db
import models
import schemas
import crud

app = FastAPI(title="ML Prediction API with Database")

# Initialize database on startup
@app.on_event("startup")
async def startup():
    init_db()
    print("Database initialized")

# Load model
model = None
@app.on_event("startup")
async def load_model():
    global model
    try:
        with open("ml/model.pkl", "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        print("Model not found")

# ========== ENDPOINTS ==========

@app.post("/predict", response_model=schemas.PredictionResponse)
async def predict(
    request: schemas.PredictionCreate,
    db: Session = Depends(get_db)
):
    """Make prediction and store in database"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # Make prediction
    features = np.array(request.input_features).reshape(1, -1)
    prediction = float(model.predict(features)[0])
    
    # Calculate confidence if available
    confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(features)[0]
        confidence = float(max(proba))
    
    # Store in database
    db_prediction = crud.create_prediction(
        db=db,
        input_features=request.input_features,
        prediction=prediction,
        confidence=confidence
    )
    
    return db_prediction

@app.get("/predictions", response_model=schemas.PredictionList)
async def get_predictions(
    page: int = 1,
    per_page: int = 10,
    db: Session = Depends(get_db)
):
    """Get prediction history with pagination"""
    skip = (page - 1) * per_page
    predictions = crud.get_predictions(db, skip=skip, limit=per_page)
    total = db.query(models.Prediction).count()
    
    return {
        "predictions": predictions,
        "total": total,
        "page": page,
        "per_page": per_page
    }

@app.get("/predictions/{prediction_id}", response_model=schemas.PredictionResponse)
async def get_prediction(
    prediction_id: int,
    db: Session = Depends(get_db)
):
    """Get specific prediction by ID"""
    prediction = crud.get_prediction(db, prediction_id)
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction

@app.get("/predictions/stats", response_model=schemas.PredictionStats)
async def get_stats(db: Session = Depends(get_db)):
    """Get prediction statistics"""
    return crud.get_prediction_stats(db)

@app.delete("/predictions/cleanup")
async def cleanup_old_predictions(
    days: int = 30,
    db: Session = Depends(get_db)
):
    """Delete predictions older than specified days"""
    deleted = crud.delete_old_predictions(db, days)
    return {"deleted": deleted, "message": f"Deleted {deleted} old predictions"}
'''
print(fastapi_db)

# ========== WORKING EXAMPLE ==========
print("\n" + "=" * 60)
print("6. WORKING DATABASE EXAMPLE")
print("=" * 60)

# Simple demonstration using SQLite
import sqlite3
import json
from datetime import datetime

# Create in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_features TEXT NOT NULL,
    prediction REAL NOT NULL,
    confidence REAL,
    model_version TEXT DEFAULT '1.0.0',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

print("Created predictions table")

# Insert sample predictions
sample_predictions = [
    ([1.0, 2.0, 3.0, 4.0], 0.85, 0.92),
    ([2.0, 3.0, 4.0, 5.0], 0.72, 0.88),
    ([3.0, 4.0, 5.0, 6.0], 0.91, 0.95),
]

for features, pred, conf in sample_predictions:
    cursor.execute(
        'INSERT INTO predictions (input_features, prediction, confidence) VALUES (?, ?, ?)',
        (json.dumps(features), pred, conf)
    )

conn.commit()
print(f"Inserted {len(sample_predictions)} predictions")

# Query predictions
cursor.execute('SELECT * FROM predictions')
rows = cursor.fetchall()

print("\nStored predictions:")
for row in rows:
    print(f"  ID: {row[0]}, Prediction: {row[2]:.2f}, Confidence: {row[3]:.2f}")

# Get statistics
cursor.execute('''
SELECT 
    COUNT(*) as total,
    AVG(prediction) as avg_pred,
    AVG(confidence) as avg_conf
FROM predictions
''')
stats = cursor.fetchone()
print(f"\nStatistics:")
print(f"  Total: {stats[0]}")
print(f"  Avg Prediction: {stats[1]:.3f}")
print(f"  Avg Confidence: {stats[2]:.3f}")

conn.close()

# ========== ASYNC DATABASE (BONUS) ==========
print("\n" + "=" * 60)
print("7. ASYNC DATABASE WITH SQLALCHEMY 2.0")
print("=" * 60)

async_db = '''
# async_database.py - Async database setup

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

# Async engine
DATABASE_URL = "sqlite+aiosqlite:///./predictions.db"
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_async_db():
    async with async_session() as session:
        yield session

# Async CRUD operations
async def async_create_prediction(
    db: AsyncSession,
    input_features: list,
    prediction: float
):
    db_prediction = Prediction(
        input_features=input_features,
        prediction=prediction
    )
    db.add(db_prediction)
    await db.commit()
    await db.refresh(db_prediction)
    return db_prediction

async def async_get_predictions(db: AsyncSession, limit: int = 100):
    result = await db.execute(
        select(Prediction).order_by(Prediction.created_at.desc()).limit(limit)
    )
    return result.scalars().all()

# FastAPI async endpoint
@app.post("/predict")
async def predict(
    request: PredictionCreate,
    db: AsyncSession = Depends(get_async_db)
):
    prediction = await async_create_prediction(
        db,
        request.input_features,
        model.predict([request.input_features])[0]
    )
    return prediction
'''
print(async_db)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. Database Setup
   - SQLAlchemy for ORM
   - Support SQLite, PostgreSQL, MySQL
   - Session management with dependency injection

2. Database Models
   - Define tables as Python classes
   - Use appropriate column types
   - Add timestamps and indexes

3. CRUD Operations
   - Create, Read, Update, Delete
   - Query with filters
   - Pagination support

4. FastAPI Integration
   - Dependency injection for sessions
   - Store predictions automatically
   - Retrieve history via API

5. Best Practices
   - Use migrations (Alembic)
   - Connection pooling
   - Handle transactions properly
   - Clean up old data periodically
""")

print("\n" + "=" * 60)
print("✅ Database Integration - Complete!")
print("=" * 60)
