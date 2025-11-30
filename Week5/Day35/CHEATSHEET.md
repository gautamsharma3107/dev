# Day 35 Quick Reference Cheat Sheet

## CNN Model Architecture
```python
import tensorflow as tf
from tensorflow import keras
from keras import layers

# Basic CNN Model
model = keras.Sequential([
    # Convolutional layers
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Dense layers
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')  # 10 classes
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

## Model Training
```python
# Training with validation
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(x_val, y_val)
)

# Save model
model.save('model.h5')
# or
model.save('model.keras')

# Load model
loaded_model = keras.models.load_model('model.h5')
```

## Image Preprocessing
```python
from PIL import Image
import numpy as np

def preprocess_image(image_path, target_size=(32, 32)):
    """Preprocess image for model prediction"""
    img = Image.open(image_path)
    img = img.resize(target_size)
    img = img.convert('RGB')
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Make prediction
prediction = model.predict(preprocessed_image)
predicted_class = np.argmax(prediction[0])
confidence = prediction[0][predicted_class]
```

## Flask API
```python
from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    img = preprocess_image(file)
    prediction = model.predict(img)
    
    return jsonify({
        'class': int(np.argmax(prediction[0])),
        'confidence': float(np.max(prediction[0]))
    })

if __name__ == '__main__':
    app.run(debug=True)
```

## FastAPI API
```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf

app = FastAPI()
model = tf.keras.models.load_model('model.h5')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = preprocess_image_from_bytes(contents)
    prediction = model.predict(img)
    
    return JSONResponse({
        "class": int(np.argmax(prediction[0])),
        "confidence": float(np.max(prediction[0]))
    })
```

## HTML Frontend Template
```html
<!DOCTYPE html>
<html>
<head>
    <title>Image Classifier</title>
</head>
<body>
    <h1>Image Classification App</h1>
    <form id="upload-form" enctype="multipart/form-data">
        <input type="file" id="image-input" accept="image/*">
        <button type="submit">Classify</button>
    </form>
    <div id="result"></div>
    
    <script>
        document.getElementById('upload-form').onsubmit = async (e) => {
            e.preventDefault();
            const formData = new FormData();
            formData.append('file', document.getElementById('image-input').files[0]);
            
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            document.getElementById('result').innerHTML = 
                `Class: ${result.class}, Confidence: ${(result.confidence * 100).toFixed(2)}%`;
        };
    </script>
</body>
</html>
```

## CIFAR-10 Classes
```python
CIFAR10_CLASSES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]
```

## Evaluation Metrics
```python
from sklearn.metrics import classification_report, confusion_matrix

# Get predictions
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Classification report
print(classification_report(y_test, y_pred_classes))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_classes)
```

## Data Augmentation
```python
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    zoom_range=0.1
)

# Fit on training data
datagen.fit(x_train)

# Train with augmentation
model.fit(datagen.flow(x_train, y_train, batch_size=32),
          epochs=10,
          validation_data=(x_val, y_val))
```

## Transfer Learning Quick Setup
```python
# Use pre-trained model
base_model = keras.applications.MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base layers
base_model.trainable = False

# Add custom layers
model = keras.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])
```

## Common Issues & Solutions
```python
# Memory issues - Use generator
train_generator = datagen.flow_from_directory(
    'train/',
    target_size=(32, 32),
    batch_size=32,
    class_mode='categorical'
)

# Model file loading issues
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF warnings

# Image format issues - Convert to RGB
img = img.convert('RGB')
```

---
**Keep this handy for quick reference!** 🚀
