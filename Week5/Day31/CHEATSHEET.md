# Day 31 Quick Reference Cheat Sheet

## Image Data Basics
```python
# Image representation
# Images are 3D arrays: (height, width, channels)
# Grayscale: (28, 28, 1) or (28, 28)
# RGB: (224, 224, 3)

# Pixel values: 0-255 (uint8) or 0.0-1.0 (normalized)

# Load and preprocess images
from tensorflow.keras.preprocessing.image import load_img, img_to_array

img = load_img('image.jpg', target_size=(224, 224))
img_array = img_to_array(img)  # (224, 224, 3)
img_normalized = img_array / 255.0  # Normalize to 0-1

# Using PIL
from PIL import Image
import numpy as np

img = Image.open('image.jpg')
img_array = np.array(img)
```

## Convolutional Layers
```python
from tensorflow.keras.layers import Conv2D

# Basic Conv2D layer
Conv2D(
    filters=32,           # Number of filters (output channels)
    kernel_size=(3, 3),   # Filter size
    strides=(1, 1),       # Step size
    padding='same',       # 'valid' or 'same'
    activation='relu',    # Activation function
    input_shape=(28, 28, 1)  # Only for first layer
)

# Common filter sizes: 3x3, 5x5, 7x7
# More filters = more features learned
# Smaller filters = finer details
```

## Pooling Layers
```python
from tensorflow.keras.layers import MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D

# Max Pooling - takes maximum value in window
MaxPooling2D(pool_size=(2, 2))

# Average Pooling - takes average value in window
AveragePooling2D(pool_size=(2, 2))

# Global Average Pooling - reduces to single value per channel
GlobalAveragePooling2D()

# Pooling reduces spatial dimensions by factor of pool_size
# Input: (28, 28, 32) -> MaxPooling2D(2,2) -> Output: (14, 14, 32)
```

## Building a CNN
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout
)

model = Sequential([
    # First Conv Block
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    
    # Second Conv Block
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    
    # Third Conv Block
    Conv2D(64, (3, 3), activation='relu'),
    
    # Flatten and Dense layers
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')  # 10 classes
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

## Training the Model
```python
# Load MNIST dataset
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# Train
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    callbacks=[
        EarlyStopping(patience=3, restore_best_weights=True)
    ]
)

# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')
```

## Data Augmentation
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True
)

# Train with augmentation
model.fit(
    datagen.flow(x_train, y_train, batch_size=32),
    epochs=10,
    validation_data=(x_test, y_test)
)
```

## Model Summary and Visualization
```python
# Print model architecture
model.summary()

# Visualize training history
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
```

## CNN Architecture Patterns
```python
# Common CNN pattern:
# Conv -> Conv -> Pool -> Conv -> Conv -> Pool -> Flatten -> Dense -> Output

# LeNet-5 style (simple):
# Conv(6) -> Pool -> Conv(16) -> Pool -> Flatten -> Dense -> Output

# VGG style (deep):
# Conv(64) -> Conv(64) -> Pool -> Conv(128) -> Conv(128) -> Pool -> ...
```

## Key Formulas
```
# Output size after convolution:
output_size = (input_size - kernel_size + 2*padding) / stride + 1

# Example: 28x28 input, 3x3 kernel, padding='valid', stride=1
# output = (28 - 3 + 0) / 1 + 1 = 26

# With padding='same':
# output = input_size (maintains spatial dimensions)

# Output size after pooling:
output_size = input_size / pool_size
# Example: 28x28 input, pool_size=2
# output = 28 / 2 = 14x14
```

## Saving and Loading Models
```python
# Save entire model
model.save('my_cnn_model.h5')

# Load model
from tensorflow.keras.models import load_model
loaded_model = load_model('my_cnn_model.h5')

# Save only weights
model.save_weights('my_cnn_weights.h5')
model.load_weights('my_cnn_weights.h5')
```

## Making Predictions
```python
import numpy as np

# Single image prediction
img = load_img('test.jpg', target_size=(28, 28), color_mode='grayscale')
img_array = img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

predictions = model.predict(img_array)
predicted_class = np.argmax(predictions[0])
confidence = np.max(predictions[0])

print(f'Predicted: {predicted_class}, Confidence: {confidence:.2%}')
```

## Common Issues and Solutions
```python
# Issue: Overfitting
# Solution: Add Dropout, use data augmentation, reduce model complexity

# Issue: Underfitting
# Solution: Increase model complexity, train longer, reduce regularization

# Issue: Memory errors
# Solution: Reduce batch_size, use smaller images, use generators

# Issue: Slow training
# Solution: Use GPU, reduce model size, use smaller images
```

---
**Keep this handy for quick reference!** 🚀
