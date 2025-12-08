"""
Day 35 - Flask API for Image Classification
============================================
Learn: Building a REST API with Flask for ML predictions

Key Concepts:
- Flask application setup
- File upload handling
- Model loading and inference
- JSON responses
- Error handling
"""

import os
import numpy as np
from io import BytesIO

# Flask import
try:
    from flask import Flask, request, jsonify, render_template_string
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False
    print("Flask not installed. Install with: pip install flask")

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
print("FLASK API FOR IMAGE CLASSIFICATION")
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

# ========== HELPER FUNCTIONS ==========
def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_bytes, target_size=INPUT_SIZE):
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


# ========== HTML TEMPLATES ==========
# Simple HTML template for testing
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Classifier</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .upload-form {
            text-align: center;
            margin: 30px 0;
        }
        input[type="file"] {
            margin: 10px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        #result {
            margin-top: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 5px;
            display: none;
        }
        .prediction {
            font-size: 24px;
            color: #333;
            margin: 10px 0;
        }
        .confidence {
            font-size: 18px;
            color: #666;
        }
        #preview {
            max-width: 300px;
            margin: 20px auto;
            display: none;
        }
        #preview img {
            max-width: 100%;
            border-radius: 5px;
        }
        .top-predictions {
            margin-top: 15px;
        }
        .top-predictions h4 {
            margin-bottom: 10px;
        }
        .prediction-bar {
            background: #e0e0e0;
            border-radius: 5px;
            margin: 5px 0;
            overflow: hidden;
        }
        .prediction-fill {
            background: #4CAF50;
            color: white;
            padding: 5px 10px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🖼️ Image Classification</h1>
        <p style="text-align: center; color: #666;">
            Upload an image to classify it using our CNN model
        </p>
        
        <div class="upload-form">
            <form id="upload-form" enctype="multipart/form-data">
                <input type="file" id="image-input" name="file" accept="image/*" required>
                <br><br>
                <button type="submit">🔍 Classify Image</button>
            </form>
        </div>
        
        <div id="preview">
            <img id="preview-img" src="" alt="Preview">
        </div>
        
        <div id="result">
            <div class="prediction">
                Predicted: <strong id="predicted-class"></strong>
            </div>
            <div class="confidence">
                Confidence: <span id="confidence"></span>
            </div>
            <div class="top-predictions">
                <h4>Top 3 Predictions:</h4>
                <div id="top-3"></div>
            </div>
        </div>
    </div>
    
    <script>
        // Preview image before upload
        document.getElementById('image-input').onchange = function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById('preview-img').src = e.target.result;
                    document.getElementById('preview').style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        };
        
        // Handle form submission
        document.getElementById('upload-form').onsubmit = async function(e) {
            e.preventDefault();
            
            const formData = new FormData();
            const fileInput = document.getElementById('image-input');
            formData.append('file', fileInput.files[0]);
            
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.success) {
                    document.getElementById('predicted-class').textContent = 
                        result.prediction.label;
                    document.getElementById('confidence').textContent = 
                        (result.prediction.confidence * 100).toFixed(2) + '%';
                    
                    // Show top 3 predictions
                    let top3Html = '';
                    result.top_3.forEach(pred => {
                        const percent = (pred.confidence * 100).toFixed(1);
                        top3Html += `
                            <div class="prediction-bar">
                                <div class="prediction-fill" style="width: ${percent}%">
                                    ${pred.label}: ${percent}%
                                </div>
                            </div>
                        `;
                    });
                    document.getElementById('top-3').innerHTML = top3Html;
                    
                    document.getElementById('result').style.display = 'block';
                } else {
                    alert('Error: ' + result.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        };
    </script>
</body>
</html>
"""

# ========== FLASK APPLICATION ==========
if FLASK_AVAILABLE:
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload
    
    # Global model variable
    model = None
    
    def load_model():
        """Load the trained model"""
        global model
        if model is None and TF_AVAILABLE:
            if os.path.exists(MODEL_PATH):
                print(f"Loading model from {MODEL_PATH}...")
                model = keras.models.load_model(MODEL_PATH)
                print("✅ Model loaded successfully!")
            else:
                print(f"⚠️ Model file not found: {MODEL_PATH}")
                print("Creating a demo model for testing...")
                model = create_demo_model()
        return model
    
    def create_demo_model():
        """Create a simple model for demonstration"""
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
    
    @app.route('/')
    def home():
        """Home page with upload form"""
        return render_template_string(HTML_TEMPLATE)
    
    @app.route('/health')
    def health():
        """Health check endpoint"""
        return jsonify({
            'status': 'healthy',
            'model_loaded': model is not None,
            'tensorflow_available': TF_AVAILABLE
        })
    
    @app.route('/predict', methods=['POST'])
    def predict():
        """Prediction endpoint"""
        # Check if model is loaded
        current_model = load_model()
        if current_model is None:
            return jsonify({
                'success': False,
                'error': 'Model not available'
            }), 500
        
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No file uploaded'
            }), 400
        
        file = request.files['file']
        
        # Check if file is valid
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No file selected'
            }), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'success': False,
                'error': f'Invalid file type. Allowed: {ALLOWED_EXTENSIONS}'
            }), 400
        
        try:
            # Read and preprocess image
            image_bytes = file.read()
            image = preprocess_image(image_bytes)
            
            # Make prediction
            predictions = current_model.predict(image, verbose=0)
            
            # Get results
            predicted_class = int(np.argmax(predictions[0]))
            confidence = float(np.max(predictions[0]))
            
            # Get top 3 predictions
            top_indices = np.argsort(predictions[0])[::-1][:3]
            top_3 = [
                {
                    'class': int(idx),
                    'label': CIFAR10_CLASSES[idx],
                    'confidence': float(predictions[0][idx])
                }
                for idx in top_indices
            ]
            
            return jsonify({
                'success': True,
                'prediction': {
                    'class': predicted_class,
                    'label': CIFAR10_CLASSES[predicted_class],
                    'confidence': confidence
                },
                'top_3': top_3
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/classes')
    def get_classes():
        """Get list of supported classes"""
        return jsonify({
            'classes': CIFAR10_CLASSES,
            'count': len(CIFAR10_CLASSES)
        })

# ========== API DOCUMENTATION ==========
print("""
Flask API Endpoints:
====================

GET /
    - Home page with upload form
    - Returns HTML page

GET /health
    - Health check
    - Returns: {"status": "healthy", "model_loaded": true}

POST /predict
    - Make prediction
    - Body: multipart/form-data with 'file' field
    - Returns: {
        "success": true,
        "prediction": {
            "class": 3,
            "label": "cat",
            "confidence": 0.95
        },
        "top_3": [...]
    }

GET /classes
    - Get supported classes
    - Returns: {"classes": [...], "count": 10}
""")

# ========== RUN APPLICATION ==========
if __name__ == '__main__':
    if FLASK_AVAILABLE and TF_AVAILABLE:
        print("\n" + "=" * 60)
        print("Starting Flask server...")
        print("=" * 60)
        print("\nAccess the app at: http://localhost:5000")
        print("Press Ctrl+C to stop\n")
        
        # Load model before starting
        load_model()
        
        # Run Flask app
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("\n⚠️ Cannot start server:")
        if not FLASK_AVAILABLE:
            print("  - Flask not installed")
        if not TF_AVAILABLE:
            print("  - TensorFlow not installed")
        print("\nInstall dependencies:")
        print("  pip install flask tensorflow Pillow")
