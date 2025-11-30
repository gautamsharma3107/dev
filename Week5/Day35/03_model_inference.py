"""
Day 35 - Model Inference
========================
Learn: Loading trained models and making predictions

Key Concepts:
- Loading saved models
- Image preprocessing for inference
- Making predictions
- Interpreting results
"""

import numpy as np
import os
from io import BytesIO

# TensorFlow import with fallback
try:
    import tensorflow as tf
    from tensorflow import keras
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("TensorFlow not installed. Install with: pip install tensorflow")

# PIL for image handling
try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL not installed. Install with: pip install Pillow")

# ========== CLASS LABELS ==========
print("=" * 60)
print("MODEL INFERENCE")
print("=" * 60)

# CIFAR-10 class names
CIFAR10_CLASSES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

print("\nCIFAR-10 Classes:")
for i, name in enumerate(CIFAR10_CLASSES):
    print(f"  {i}: {name}")

# ========== IMAGE PREPROCESSING ==========
print("\n" + "=" * 60)
print("IMAGE PREPROCESSING")
print("=" * 60)

print("""
Preprocessing Steps for Inference:
1. Load image from file/bytes
2. Resize to model input size (32x32 for CIFAR-10)
3. Convert to RGB (3 channels)
4. Normalize pixel values to [0, 1]
5. Add batch dimension
""")

def preprocess_image_from_file(image_path, target_size=(32, 32)):
    """
    Preprocess an image file for model prediction
    
    Args:
        image_path: Path to the image file
        target_size: Target dimensions (height, width)
    
    Returns:
        Preprocessed numpy array ready for prediction
    """
    if not PIL_AVAILABLE:
        raise ImportError("PIL is required for image preprocessing")
    
    # Load image
    img = Image.open(image_path)
    
    # Convert to RGB (handles grayscale and RGBA)
    img = img.convert('RGB')
    
    # Resize to target size
    img = img.resize(target_size)
    
    # Convert to numpy array and normalize
    img_array = np.array(img, dtype='float32') / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array


def preprocess_image_from_bytes(image_bytes, target_size=(32, 32)):
    """
    Preprocess image from bytes (for API endpoints)
    
    Args:
        image_bytes: Image data as bytes
        target_size: Target dimensions (height, width)
    
    Returns:
        Preprocessed numpy array ready for prediction
    """
    if not PIL_AVAILABLE:
        raise ImportError("PIL is required for image preprocessing")
    
    # Load image from bytes
    img = Image.open(BytesIO(image_bytes))
    
    # Convert to RGB
    img = img.convert('RGB')
    
    # Resize
    img = img.resize(target_size)
    
    # Convert to numpy array and normalize
    img_array = np.array(img, dtype='float32') / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array


def preprocess_image_from_array(img_array, target_size=(32, 32)):
    """
    Preprocess numpy array image for model prediction
    
    Args:
        img_array: Image as numpy array (H, W, C)
        target_size: Target dimensions (height, width)
    
    Returns:
        Preprocessed numpy array ready for prediction
    """
    if not PIL_AVAILABLE:
        raise ImportError("PIL is required for image preprocessing")
    
    # If array is not in right format, convert
    if img_array.dtype != np.uint8:
        img_array = (img_array * 255).astype(np.uint8)
    
    # Convert to PIL Image
    img = Image.fromarray(img_array)
    
    # Ensure RGB
    img = img.convert('RGB')
    
    # Resize
    img = img.resize(target_size)
    
    # Convert back to array and normalize
    processed = np.array(img, dtype='float32') / 255.0
    
    # Add batch dimension
    processed = np.expand_dims(processed, axis=0)
    
    return processed


# ========== LOADING THE MODEL ==========
print("\n" + "=" * 60)
print("LOADING THE MODEL")
print("=" * 60)

print("""
Loading Options:
1. model = keras.models.load_model('model.keras')
2. model = keras.models.load_model('model.h5')
3. model = tf.saved_model.load('saved_model/')
""")

class ImageClassifier:
    """
    Image Classifier class for easy inference
    """
    
    def __init__(self, model_path=None, model=None, class_names=None):
        """
        Initialize the classifier
        
        Args:
            model_path: Path to saved model file
            model: Pre-loaded Keras model
            class_names: List of class names
        """
        if model is not None:
            self.model = model
        elif model_path is not None and TF_AVAILABLE:
            print(f"Loading model from {model_path}...")
            self.model = keras.models.load_model(model_path)
            print("✅ Model loaded successfully!")
        else:
            self.model = None
            print("⚠️ No model provided or TensorFlow not available")
        
        self.class_names = class_names or CIFAR10_CLASSES
        self.input_shape = (32, 32)  # Default for CIFAR-10
    
    def predict(self, image):
        """
        Make prediction on a single image
        
        Args:
            image: Preprocessed image array with batch dimension
        
        Returns:
            Dictionary with prediction results
        """
        if self.model is None:
            return {'error': 'Model not loaded'}
        
        # Make prediction
        predictions = self.model.predict(image, verbose=0)
        
        # Get top prediction
        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(predictions[0][predicted_class])
        
        # Get all class probabilities
        all_probs = {
            self.class_names[i]: float(predictions[0][i])
            for i in range(len(self.class_names))
        }
        
        return {
            'predicted_class': predicted_class,
            'predicted_label': self.class_names[predicted_class],
            'confidence': confidence,
            'all_probabilities': all_probs
        }
    
    def predict_from_file(self, image_path):
        """
        Make prediction from image file path
        """
        image = preprocess_image_from_file(image_path, self.input_shape)
        return self.predict(image)
    
    def predict_from_bytes(self, image_bytes):
        """
        Make prediction from image bytes
        """
        image = preprocess_image_from_bytes(image_bytes, self.input_shape)
        return self.predict(image)
    
    def predict_top_k(self, image, k=3):
        """
        Get top-k predictions
        """
        if self.model is None:
            return {'error': 'Model not loaded'}
        
        predictions = self.model.predict(image, verbose=0)
        
        # Get top-k indices
        top_indices = np.argsort(predictions[0])[::-1][:k]
        
        results = []
        for idx in top_indices:
            results.append({
                'class': int(idx),
                'label': self.class_names[idx],
                'confidence': float(predictions[0][idx])
            })
        
        return results


# ========== DEMONSTRATION ==========
print("\n" + "=" * 60)
print("INFERENCE DEMONSTRATION")
print("=" * 60)

if TF_AVAILABLE:
    # Create a simple model for demonstration
    print("\nCreating a demo model...")
    
    demo_model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    
    demo_model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Create classifier
    classifier = ImageClassifier(model=demo_model, class_names=CIFAR10_CLASSES)
    
    # Create a random test image
    print("\nTesting with random image...")
    random_image = np.random.rand(1, 32, 32, 3).astype('float32')
    
    # Make prediction
    result = classifier.predict(random_image)
    
    print(f"\nPrediction Result:")
    print(f"  Predicted Class: {result['predicted_label']}")
    print(f"  Confidence: {result['confidence']:.2%}")
    
    print(f"\nTop 3 Predictions:")
    top_k = classifier.predict_top_k(random_image, k=3)
    for i, pred in enumerate(top_k, 1):
        print(f"  {i}. {pred['label']}: {pred['confidence']:.2%}")
    
    # Test with CIFAR-10 sample
    print("\nTesting with CIFAR-10 sample...")
    (_, _), (x_test, y_test) = keras.datasets.cifar10.load_data()
    
    sample_image = x_test[0:1].astype('float32') / 255.0
    sample_label = CIFAR10_CLASSES[y_test[0][0]]
    
    result = classifier.predict(sample_image)
    
    print(f"\nActual Class: {sample_label}")
    print(f"Predicted Class: {result['predicted_label']}")
    print(f"Confidence: {result['confidence']:.2%}")
    
    # Note: Accuracy will be random since model is not trained

else:
    print("\nDemo skipped (TensorFlow not available)")
    print("With a trained model, inference would produce:")
    print("""
    Prediction Result:
      Predicted Class: cat
      Confidence: 87.34%
    
    Top 3 Predictions:
      1. cat: 87.34%
      2. dog: 8.21%
      3. bird: 2.15%
    """)

# ========== BATCH PREDICTIONS ==========
print("\n" + "=" * 60)
print("BATCH PREDICTIONS")
print("=" * 60)

print("""
For multiple images, batch predictions are faster:

# Preprocess all images
images = [preprocess_image(path) for path in image_paths]
batch = np.vstack(images)  # Stack into single array

# Predict all at once
predictions = model.predict(batch)

# Process results
for i, pred in enumerate(predictions):
    class_idx = np.argmax(pred)
    confidence = pred[class_idx]
    print(f"Image {i}: {class_names[class_idx]} ({confidence:.2%})")
""")

if TF_AVAILABLE:
    print("\nBatch prediction example:")
    
    # Create batch of random images
    batch_images = np.random.rand(5, 32, 32, 3).astype('float32')
    
    # Predict batch
    batch_predictions = demo_model.predict(batch_images, verbose=0)
    
    print(f"Batch shape: {batch_images.shape}")
    print(f"Predictions shape: {batch_predictions.shape}")
    
    for i, pred in enumerate(batch_predictions):
        class_idx = np.argmax(pred)
        confidence = pred[class_idx]
        print(f"  Image {i+1}: {CIFAR10_CLASSES[class_idx]} ({confidence:.2%})")

# ========== INFERENCE API HELPER ==========
print("\n" + "=" * 60)
print("INFERENCE API HELPER FUNCTION")
print("=" * 60)

def get_prediction_response(model, image_bytes, class_names=CIFAR10_CLASSES):
    """
    Helper function for API endpoints
    
    Returns a dictionary suitable for JSON response
    """
    try:
        # Preprocess image
        image = preprocess_image_from_bytes(image_bytes)
        
        # Make prediction
        predictions = model.predict(image, verbose=0)
        
        # Get results
        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(np.max(predictions[0]))
        
        # Get top 3 predictions
        top_indices = np.argsort(predictions[0])[::-1][:3]
        top_predictions = [
            {
                'class': int(idx),
                'label': class_names[idx],
                'confidence': float(predictions[0][idx])
            }
            for idx in top_indices
        ]
        
        return {
            'success': True,
            'prediction': {
                'class': predicted_class,
                'label': class_names[predicted_class],
                'confidence': confidence
            },
            'top_3': top_predictions
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

print("""
Usage in Flask/FastAPI:

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image_bytes = file.read()
    
    result = get_prediction_response(model, image_bytes)
    return jsonify(result)
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Inference Pipeline Checklist:
✅ Load the trained model
✅ Preprocess input images (resize, normalize, batch)
✅ Make predictions with model.predict()
✅ Interpret results (argmax for class, confidence)
✅ Handle errors gracefully
✅ Use batch predictions for multiple images

Key Functions:
- preprocess_image_from_file(path) - For file uploads
- preprocess_image_from_bytes(bytes) - For API requests
- model.predict(image) - Get predictions
- np.argmax(predictions) - Get predicted class

Next: Build the API endpoint!
""")

print("\n" + "=" * 60)
print("✅ Model Inference - Complete!")
print("=" * 60)
