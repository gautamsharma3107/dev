"""
Day 35 - FastAPI for Image Classification
==========================================
Learn: Building a modern async REST API with FastAPI

Key Concepts:
- FastAPI application setup
- Async file handling
- Automatic API documentation
- Pydantic models for validation
- Error handling
"""

import os
import numpy as np
from io import BytesIO
from typing import List, Optional

# FastAPI imports
try:
    from fastapi import FastAPI, File, UploadFile, HTTPException
    from fastapi.responses import JSONResponse, HTMLResponse
    from pydantic import BaseModel
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    print("FastAPI not installed. Install with: pip install fastapi uvicorn python-multipart")

# TensorFlow import
try:
    import tensorflow as tf
    from tensorflow import keras
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("TensorFlow not installed. Install with: pip install tensorflow")

# PIL import
try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not installed. Install with: pip install Pillow")

# ========== CONFIGURATION ==========
print("=" * 60)
print("FASTAPI FOR IMAGE CLASSIFICATION")
print("=" * 60)

# Class names for CIFAR-10
CIFAR10_CLASSES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# Configuration
MODEL_PATH = 'cifar10_model.keras'
INPUT_SIZE = (32, 32)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# ========== PYDANTIC MODELS ==========
if FASTAPI_AVAILABLE:
    class PredictionResult(BaseModel):
        """Single prediction result"""
        class_id: int
        label: str
        confidence: float
    
    class PredictionResponse(BaseModel):
        """API response for predictions"""
        success: bool
        prediction: Optional[PredictionResult] = None
        top_predictions: Optional[List[PredictionResult]] = None
        error: Optional[str] = None
    
    class HealthResponse(BaseModel):
        """Health check response"""
        status: str
        model_loaded: bool
        tensorflow_available: bool
    
    class ClassesResponse(BaseModel):
        """Supported classes response"""
        classes: List[str]
        count: int

# ========== HELPER FUNCTIONS ==========
def preprocess_image(image_bytes: bytes, target_size=INPUT_SIZE):
    """Preprocess image bytes for model prediction"""
    if not PIL_AVAILABLE:
        raise ImportError("PIL is required")
    
    # Open image from bytes
    img = Image.open(BytesIO(image_bytes))
    
    # Convert to RGB
    img = img.convert('RGB')
    
    # Resize
    img = img.resize(target_size)
    
    # Convert to array and normalize
    img_array = np.array(img, dtype='float32') / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array


def validate_file(filename: str) -> bool:
    """Check if file extension is allowed"""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS


# ========== HTML TEMPLATE ==========
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI Image Classifier</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .badge {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
        }
        .upload-area {
            border: 3px dashed #ddd;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            margin: 20px 0;
            transition: all 0.3s;
        }
        .upload-area:hover {
            border-color: #667eea;
            background: #f8f9ff;
        }
        .upload-area.dragover {
            border-color: #667eea;
            background: #f0f2ff;
        }
        input[type="file"] {
            display: none;
        }
        .upload-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-size: 18px;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .upload-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        #preview {
            max-width: 300px;
            margin: 20px auto;
            display: none;
        }
        #preview img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        #result {
            margin-top: 30px;
            padding: 30px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 15px;
            display: none;
        }
        .prediction-main {
            font-size: 32px;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        .confidence-bar {
            background: #e0e0e0;
            border-radius: 10px;
            height: 30px;
            overflow: hidden;
            margin: 10px 0;
        }
        .confidence-fill {
            height: 100%;
            display: flex;
            align-items: center;
            padding-left: 15px;
            color: white;
            font-weight: bold;
            transition: width 0.5s;
        }
        .top-1 { background: linear-gradient(90deg, #667eea, #764ba2); }
        .top-2 { background: linear-gradient(90deg, #f093fb, #f5576c); }
        .top-3 { background: linear-gradient(90deg, #4facfe, #00f2fe); }
        .api-docs {
            margin-top: 30px;
            text-align: center;
        }
        .api-docs a {
            color: #667eea;
            text-decoration: none;
        }
        .loading {
            display: none;
            text-align: center;
            margin: 20px 0;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 FastAPI Image Classifier</h1>
        <p class="subtitle">
            Powered by <span class="badge">FastAPI</span> + 
            <span class="badge">TensorFlow</span>
        </p>
        
        <div class="upload-area" id="drop-area">
            <p>📁 Drag & drop an image here or</p>
            <label for="image-input">
                <span class="upload-btn">Choose File</span>
            </label>
            <input type="file" id="image-input" accept="image/*">
        </div>
        
        <div id="preview">
            <img id="preview-img" src="" alt="Preview">
        </div>
        
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p>Classifying image...</p>
        </div>
        
        <div id="result">
            <div class="prediction-main">
                Predicted: <strong id="predicted-class"></strong>
            </div>
            <h4>All Predictions:</h4>
            <div id="predictions"></div>
        </div>
        
        <div class="api-docs">
            <p>📚 <a href="/docs" target="_blank">Interactive API Documentation (Swagger)</a></p>
            <p>📖 <a href="/redoc" target="_blank">Alternative Docs (ReDoc)</a></p>
        </div>
    </div>
    
    <script>
        const dropArea = document.getElementById('drop-area');
        const fileInput = document.getElementById('image-input');
        
        // Drag and drop
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            dropArea.addEventListener(eventName, () => dropArea.classList.add('dragover'));
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, () => dropArea.classList.remove('dragover'));
        });
        
        dropArea.addEventListener('drop', handleDrop);
        fileInput.addEventListener('change', handleFiles);
        
        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            handleFiles({ target: { files: files } });
        }
        
        function handleFiles(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            // Preview
            const reader = new FileReader();
            reader.onload = (e) => {
                document.getElementById('preview-img').src = e.target.result;
                document.getElementById('preview').style.display = 'block';
            };
            reader.readAsDataURL(file);
            
            // Upload
            uploadFile(file);
        }
        
        async function uploadFile(file) {
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').style.display = 'none';
            
            const formData = new FormData();
            formData.append('file', file);
            
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                document.getElementById('loading').style.display = 'none';
                
                if (result.success) {
                    document.getElementById('predicted-class').textContent = 
                        result.prediction.label;
                    
                    let html = '';
                    result.top_predictions.forEach((pred, i) => {
                        const percent = (pred.confidence * 100).toFixed(1);
                        html += `
                            <div class="confidence-bar">
                                <div class="confidence-fill top-${i+1}" style="width: ${percent}%">
                                    ${pred.label}: ${percent}%
                                </div>
                            </div>
                        `;
                    });
                    document.getElementById('predictions').innerHTML = html;
                    document.getElementById('result').style.display = 'block';
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                document.getElementById('loading').style.display = 'none';
                alert('Error: ' + error.message);
            }
        }
    </script>
</body>
</html>
"""

# ========== FASTAPI APPLICATION ==========
if FASTAPI_AVAILABLE:
    app = FastAPI(
        title="Image Classification API",
        description="A CNN-based image classification API built with FastAPI",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Global model variable
    model = None
    
    def get_model():
        """Get or load the model"""
        global model
        if model is None and TF_AVAILABLE:
            if os.path.exists(MODEL_PATH):
                print(f"Loading model from {MODEL_PATH}...")
                model = keras.models.load_model(MODEL_PATH)
            else:
                print("Creating demo model...")
                model = create_demo_model()
        return model
    
    def create_demo_model():
        """Create a simple demo model"""
        demo = keras.Sequential([
            keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        demo.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
        return demo
    
    @app.on_event("startup")
    async def startup_event():
        """Load model on startup"""
        get_model()
        print("✅ Model loaded on startup")
    
    @app.get("/", response_class=HTMLResponse)
    async def home():
        """Home page with upload interface"""
        return HTML_TEMPLATE
    
    @app.get("/health", response_model=HealthResponse)
    async def health_check():
        """Health check endpoint"""
        return HealthResponse(
            status="healthy",
            model_loaded=model is not None,
            tensorflow_available=TF_AVAILABLE
        )
    
    @app.get("/classes", response_model=ClassesResponse)
    async def get_classes():
        """Get list of supported classes"""
        return ClassesResponse(
            classes=CIFAR10_CLASSES,
            count=len(CIFAR10_CLASSES)
        )
    
    @app.post("/predict", response_model=PredictionResponse)
    async def predict(file: UploadFile = File(...)):
        """
        Make a prediction on an uploaded image
        
        - **file**: Image file (PNG, JPG, JPEG, GIF)
        
        Returns prediction with confidence scores
        """
        # Validate file type
        if not validate_file(file.filename):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file type. Allowed: {ALLOWED_EXTENSIONS}"
            )
        
        # Check model
        current_model = get_model()
        if current_model is None:
            raise HTTPException(
                status_code=500,
                detail="Model not available"
            )
        
        try:
            # Read file contents
            contents = await file.read()
            
            # Preprocess image
            image = preprocess_image(contents)
            
            # Make prediction
            predictions = current_model.predict(image, verbose=0)
            
            # Get results
            predicted_class = int(np.argmax(predictions[0]))
            confidence = float(np.max(predictions[0]))
            
            # Get all predictions sorted
            sorted_indices = np.argsort(predictions[0])[::-1]
            top_predictions = [
                PredictionResult(
                    class_id=int(idx),
                    label=CIFAR10_CLASSES[idx],
                    confidence=float(predictions[0][idx])
                )
                for idx in sorted_indices[:5]  # Top 5
            ]
            
            return PredictionResponse(
                success=True,
                prediction=PredictionResult(
                    class_id=predicted_class,
                    label=CIFAR10_CLASSES[predicted_class],
                    confidence=confidence
                ),
                top_predictions=top_predictions
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )
    
    @app.post("/predict/batch")
    async def predict_batch(files: List[UploadFile] = File(...)):
        """
        Make predictions on multiple images
        
        - **files**: Multiple image files
        
        Returns predictions for each image
        """
        current_model = get_model()
        if current_model is None:
            raise HTTPException(status_code=500, detail="Model not available")
        
        results = []
        
        for file in files:
            if not validate_file(file.filename):
                results.append({
                    'filename': file.filename,
                    'success': False,
                    'error': 'Invalid file type'
                })
                continue
            
            try:
                contents = await file.read()
                image = preprocess_image(contents)
                predictions = current_model.predict(image, verbose=0)
                
                predicted_class = int(np.argmax(predictions[0]))
                confidence = float(np.max(predictions[0]))
                
                results.append({
                    'filename': file.filename,
                    'success': True,
                    'prediction': {
                        'class_id': predicted_class,
                        'label': CIFAR10_CLASSES[predicted_class],
                        'confidence': confidence
                    }
                })
            except Exception as e:
                results.append({
                    'filename': file.filename,
                    'success': False,
                    'error': str(e)
                })
        
        return {'results': results}

# ========== API DOCUMENTATION ==========
print("""
FastAPI Endpoints:
==================

GET /
    - Home page with drag-and-drop upload
    - Returns HTML page

GET /docs
    - Interactive Swagger documentation
    - Test API endpoints directly

GET /redoc
    - ReDoc documentation
    - Alternative API documentation

GET /health
    - Health check
    - Returns: {"status": "healthy", "model_loaded": true}

GET /classes
    - Get supported classes
    - Returns: {"classes": [...], "count": 10}

POST /predict
    - Make single prediction
    - Body: multipart/form-data with 'file'
    - Returns: {
        "success": true,
        "prediction": {"class_id": 3, "label": "cat", "confidence": 0.95},
        "top_predictions": [...]
    }

POST /predict/batch
    - Make batch predictions
    - Body: multipart/form-data with multiple 'files'
    - Returns: {"results": [...]}
""")

# ========== RUN APPLICATION ==========
if __name__ == '__main__':
    if FASTAPI_AVAILABLE and TF_AVAILABLE:
        try:
            import uvicorn
            
            print("\n" + "=" * 60)
            print("Starting FastAPI server...")
            print("=" * 60)
            print("\nAccess the app at: http://localhost:8000")
            print("API Documentation: http://localhost:8000/docs")
            print("Press Ctrl+C to stop\n")
            
            uvicorn.run(app, host="0.0.0.0", port=8000)
            
        except ImportError:
            print("\n⚠️ uvicorn not installed")
            print("Install with: pip install uvicorn")
    else:
        print("\n⚠️ Cannot start server:")
        if not FASTAPI_AVAILABLE:
            print("  - FastAPI not installed")
        if not TF_AVAILABLE:
            print("  - TensorFlow not installed")
        print("\nInstall dependencies:")
        print("  pip install fastapi uvicorn python-multipart tensorflow Pillow")
