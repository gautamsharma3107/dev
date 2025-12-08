"""
Day 35 - Complete Image Classification App
==========================================
Learn: Building an end-to-end image classification application

This script combines:
- CNN model training
- Model serving with FastAPI
- Simple frontend for testing

Run this to have a complete working application!
"""

import os
import sys
import numpy as np
from io import BytesIO
import threading
import time

# ========== CHECK DEPENDENCIES ==========
print("=" * 60)
print("COMPLETE IMAGE CLASSIFICATION APP")
print("=" * 60)

def check_dependencies():
    """Check and report installed dependencies"""
    deps = {}
    
    try:
        import tensorflow as tf
        deps['tensorflow'] = tf.__version__
    except ImportError:
        deps['tensorflow'] = None
    
    try:
        from PIL import Image
        deps['pillow'] = 'installed'
    except ImportError:
        deps['pillow'] = None
    
    try:
        import flask
        deps['flask'] = flask.__version__
    except ImportError:
        deps['flask'] = None
    
    try:
        import fastapi
        deps['fastapi'] = fastapi.__version__
    except ImportError:
        deps['fastapi'] = None
    
    print("\nDependency Status:")
    for dep, version in deps.items():
        status = f"✅ {version}" if version else "❌ Not installed"
        print(f"  {dep}: {status}")
    
    return deps

deps = check_dependencies()

# Check minimum requirements
if deps['tensorflow'] is None:
    print("\n⚠️ TensorFlow is required!")
    print("Install with: pip install tensorflow")
    print("\nContinuing with demo mode...")

# ========== CONFIGURATION ==========
CIFAR10_CLASSES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

MODEL_PATH = 'cifar10_complete_model.keras'
INPUT_SIZE = (32, 32)

# ========== MODEL CREATION ==========
print("\n" + "=" * 60)
print("MODEL SETUP")
print("=" * 60)

model = None

if deps['tensorflow']:
    import tensorflow as tf
    from tensorflow import keras
    from keras import layers
    from keras.preprocessing.image import ImageDataGenerator
    
    def create_model():
        """Create CNN model"""
        model = keras.Sequential([
            # Block 1
            layers.Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.Conv2D(32, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Block 2
            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.Conv2D(64, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Block 3
            layers.Conv2D(128, (3, 3), padding='same'),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Dense layers
            layers.Flatten(),
            layers.Dense(512),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.Dropout(0.5),
            layers.Dense(10, activation='softmax')
        ])
        
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def train_model(epochs=5, batch_size=64):
        """Train the model on CIFAR-10"""
        global model
        
        print("\nLoading CIFAR-10 dataset...")
        (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
        
        # Normalize
        x_train = x_train.astype('float32') / 255.0
        x_test = x_test.astype('float32') / 255.0
        
        # Validation split
        val_size = 5000
        x_val, y_val = x_train[:val_size], y_train[:val_size]
        x_train, y_train = x_train[val_size:], y_train[val_size:]
        
        print(f"Training samples: {len(x_train)}")
        print(f"Validation samples: {len(x_val)}")
        print(f"Test samples: {len(x_test)}")
        
        # Data augmentation
        datagen = ImageDataGenerator(
            rotation_range=15,
            width_shift_range=0.1,
            height_shift_range=0.1,
            horizontal_flip=True,
            zoom_range=0.1
        )
        
        # Create model
        model = create_model()
        print(f"\nModel parameters: {model.count_params():,}")
        
        # Callbacks
        callbacks = [
            keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=3,
                restore_best_weights=True
            ),
            keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=2
            )
        ]
        
        # Train
        print(f"\nTraining for {epochs} epochs...")
        history = model.fit(
            datagen.flow(x_train, y_train, batch_size=batch_size),
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=callbacks,
            verbose=1
        )
        
        # Evaluate
        print("\nEvaluating on test set...")
        test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
        print(f"Test accuracy: {test_acc:.2%}")
        
        # Save model
        model.save(MODEL_PATH)
        print(f"\n✅ Model saved to {MODEL_PATH}")
        
        return model, history
    
    def load_or_train_model():
        """Load existing model or train new one"""
        global model
        
        if os.path.exists(MODEL_PATH):
            print(f"\nLoading model from {MODEL_PATH}...")
            model = keras.models.load_model(MODEL_PATH)
            print("✅ Model loaded!")
        else:
            print("\nNo saved model found. Training new model...")
            model, _ = train_model(epochs=3)  # Quick training for demo
        
        return model
    
    # Load or create model
    print("\nInitializing model...")
    model = load_or_train_model()

else:
    print("\n⚠️ Running in demo mode (no TensorFlow)")

# ========== IMAGE PREPROCESSING ==========
def preprocess_image(image_bytes):
    """Preprocess image for prediction"""
    if deps['pillow'] is None:
        raise ImportError("Pillow is required")
    
    from PIL import Image
    
    img = Image.open(BytesIO(image_bytes))
    img = img.convert('RGB')
    img = img.resize(INPUT_SIZE)
    img_array = np.array(img, dtype='float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict(image_bytes):
    """Make prediction on image"""
    global model
    
    if model is None:
        return {'error': 'Model not loaded'}
    
    try:
        image = preprocess_image(image_bytes)
        predictions = model.predict(image, verbose=0)
        
        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(np.max(predictions[0]))
        
        top_indices = np.argsort(predictions[0])[::-1][:3]
        top_3 = [
            {
                'class': int(idx),
                'label': CIFAR10_CLASSES[idx],
                'confidence': float(predictions[0][idx])
            }
            for idx in top_indices
        ]
        
        return {
            'success': True,
            'prediction': {
                'class': predicted_class,
                'label': CIFAR10_CLASSES[predicted_class],
                'confidence': confidence
            },
            'top_3': top_3
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

# ========== WEB APPLICATION ==========
print("\n" + "=" * 60)
print("WEB APPLICATION")
print("=" * 60)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Classification App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        h1 { text-align: center; color: #333; }
        .upload-area {
            border: 3px dashed #ddd;
            border-radius: 10px;
            padding: 40px;
            text-align: center;
            margin: 20px 0;
            cursor: pointer;
        }
        .upload-area:hover { border-color: #4CAF50; }
        input[type="file"] { display: none; }
        .btn {
            background: #4CAF50;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover { background: #45a049; }
        #preview { max-width: 100%; margin: 20px 0; display: none; }
        #preview img { max-width: 100%; border-radius: 10px; }
        #result {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            display: none;
        }
        .prediction { font-size: 24px; text-align: center; }
        .bar {
            background: #e0e0e0;
            border-radius: 10px;
            margin: 10px 0;
            overflow: hidden;
        }
        .fill {
            background: #4CAF50;
            color: white;
            padding: 8px 15px;
        }
        .loading { text-align: center; display: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🖼️ Image Classifier</h1>
        <div class="upload-area" onclick="document.getElementById('file').click()">
            <p>📁 Click to upload or drag an image</p>
            <label class="btn">Choose Image</label>
            <input type="file" id="file" accept="image/*">
        </div>
        <div id="preview"><img id="img" src=""></div>
        <div class="loading" id="loading">
            <p>🔄 Analyzing...</p>
        </div>
        <div id="result">
            <div class="prediction">
                <strong id="pred"></strong>
            </div>
            <div id="bars"></div>
        </div>
    </div>
    <script>
        document.getElementById('file').onchange = async function(e) {
            const file = e.target.files[0];
            if (!file) return;
            
            // Preview
            const reader = new FileReader();
            reader.onload = e => {
                document.getElementById('img').src = e.target.result;
                document.getElementById('preview').style.display = 'block';
            };
            reader.readAsDataURL(file);
            
            // Upload
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').style.display = 'none';
            
            const formData = new FormData();
            formData.append('file', file);
            
            const res = await fetch('/predict', { method: 'POST', body: formData });
            const data = await res.json();
            
            document.getElementById('loading').style.display = 'none';
            
            if (data.success) {
                document.getElementById('pred').textContent = data.prediction.label;
                let bars = '';
                data.top_3.forEach(p => {
                    const pct = (p.confidence * 100).toFixed(1);
                    bars += '<div class="bar"><div class="fill" style="width:'+pct+'%">'+p.label+': '+pct+'%</div></div>';
                });
                document.getElementById('bars').innerHTML = bars;
                document.getElementById('result').style.display = 'block';
            } else {
                alert('Error: ' + data.error);
            }
        };
    </script>
</body>
</html>
"""

# ========== FLASK SERVER ==========
if deps['flask']:
    from flask import Flask, request, jsonify
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return HTML_TEMPLATE
    
    @app.route('/predict', methods=['POST'])
    def predict_route():
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file'})
        
        file = request.files['file']
        image_bytes = file.read()
        
        result = predict(image_bytes)
        return jsonify(result)
    
    @app.route('/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'model_loaded': model is not None
        })

# ========== MAIN ==========
def main():
    """Run the complete application"""
    print("\n" + "=" * 60)
    print("STARTING APPLICATION")
    print("=" * 60)
    
    if deps['flask'] and model is not None:
        print("\n🚀 Starting Flask server...")
        print("   Access at: http://localhost:5000")
        print("   Press Ctrl+C to stop\n")
        
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        print("\n⚠️ Cannot start server:")
        if deps['flask'] is None:
            print("  - Flask not installed (pip install flask)")
        if model is None:
            print("  - Model not loaded (install tensorflow)")
        
        print("\nDemo mode - testing with random image...")
        
        if model is not None:
            # Create random test image
            test_image = np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8)
            
            if deps['pillow']:
                from PIL import Image
                img = Image.fromarray(test_image)
                buffer = BytesIO()
                img.save(buffer, format='PNG')
                buffer.seek(0)
                
                result = predict(buffer.read())
                
                print("\nTest Prediction:")
                print(f"  Predicted: {result['prediction']['label']}")
                print(f"  Confidence: {result['prediction']['confidence']:.2%}")
                print("\n  Top 3:")
                for p in result['top_3']:
                    print(f"    {p['label']}: {p['confidence']:.2%}")

if __name__ == '__main__':
    main()
    
    print("\n" + "=" * 60)
    print("✅ Complete Image Classification App - Done!")
    print("=" * 60)
