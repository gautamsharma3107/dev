# Day 30 Quick Reference Cheat Sheet

## TensorFlow/Keras Imports
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import numpy as np
```

## Tensor Creation
```python
# Constants (immutable)
scalar = tf.constant(5)              # 0D
vector = tf.constant([1, 2, 3])      # 1D
matrix = tf.constant([[1, 2], [3, 4]])  # 2D

# Special tensors
tf.zeros((3, 4))                     # All zeros
tf.ones((2, 3))                      # All ones
tf.fill((2, 2), 7)                   # Fill with value
tf.range(0, 10, 2)                   # Range

# Random tensors
tf.random.uniform((2, 3), 0, 10)     # Uniform distribution
tf.random.normal((2, 3), 0, 1)       # Normal distribution

# Variables (mutable - for weights)
var = tf.Variable([[1, 2], [3, 4]])
var.assign([[5, 6], [7, 8]])         # Update value
```

## Tensor Operations
```python
a + b           # Element-wise addition
a - b           # Element-wise subtraction
a * b           # Element-wise multiplication
a / b           # Element-wise division
a @ b           # Matrix multiplication
tf.matmul(a, b) # Matrix multiplication

tf.reduce_sum(x)       # Sum all elements
tf.reduce_mean(x)      # Mean of all elements
tf.reduce_max(x)       # Maximum value
tf.argmax(x, axis=1)   # Index of max

tf.reshape(x, (3, 4))  # Reshape tensor
tf.reshape(x, [-1])    # Flatten
```

## Building Sequential Models
```python
# Method 1: Constructor
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Method 2: Adding layers
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

## Common Layers
```python
Dense(units, activation)     # Fully connected
Dropout(rate)                # Regularization (e.g., 0.3)
BatchNormalization()         # Normalize activations
Flatten()                    # Flatten to 1D
```

## Activation Functions
```python
'relu'      # Hidden layers (default choice)
'sigmoid'   # Binary classification output
'softmax'   # Multi-class classification output
'tanh'      # Alternative to relu
None        # Regression output (linear)
```

## Model Compilation
```python
# Binary Classification
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Multi-class Classification
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Integer labels
    metrics=['accuracy']
)

# Regression
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)
```

## Common Optimizers
```python
'adam'                       # Best default choice
'sgd'                        # Classic gradient descent
Adam(learning_rate=0.001)    # Custom learning rate
SGD(learning_rate=0.01, momentum=0.9)
```

## Training
```python
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,    # or validation_data=(X_val, y_val)
    callbacks=[early_stopping],
    verbose=1
)
```

## Callbacks
```python
# Stop early if no improvement
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# Save best model
checkpoint = ModelCheckpoint(
    'best_model.keras',
    monitor='val_loss',
    save_best_only=True
)
```

## Evaluation & Prediction
```python
# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)

# Predict probabilities
predictions = model.predict(X_test)

# Convert to classes (binary)
classes = (predictions > 0.5).astype(int)

# Convert to classes (multi-class)
classes = np.argmax(predictions, axis=1)
```

## Saving & Loading
```python
# Save entire model
model.save('model.keras')

# Load model
model = load_model('model.keras')

# Save/load weights only
model.save_weights('weights.h5')
model.load_weights('weights.h5')
```

## Model Architecture by Task
```python
# Binary Classification
model = Sequential([
    Dense(64, activation='relu', input_shape=(n_features,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Output: 0-1 probability
])

# Multi-class Classification (n classes)
model = Sequential([
    Dense(64, activation='relu', input_shape=(n_features,)),
    Dense(32, activation='relu'),
    Dense(n_classes, activation='softmax')  # Output: n probabilities
])

# Regression
model = Sequential([
    Dense(64, activation='relu', input_shape=(n_features,)),
    Dense(32, activation='relu'),
    Dense(1)  # Linear output (no activation)
])
```

## Loss Functions
```python
'binary_crossentropy'            # Binary classification
'categorical_crossentropy'       # Multi-class (one-hot labels)
'sparse_categorical_crossentropy' # Multi-class (integer labels)
'mse'                            # Mean squared error (regression)
'mae'                            # Mean absolute error (regression)
```

## Quick Tips
```python
# Check TensorFlow version
print(tf.__version__)

# Check GPU availability
print(tf.config.list_physical_devices('GPU'))

# Set random seed
tf.random.set_seed(42)

# View model summary
model.summary()

# Get training history
history.history['loss']      # Training loss per epoch
history.history['val_loss']  # Validation loss per epoch

# NumPy conversion
tensor.numpy()               # Tensor to NumPy
tf.constant(np_array)        # NumPy to Tensor
```

## Data Preprocessing (Important!)
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Fit and transform
X_test = scaler.transform(X_test)         # Transform only!
```

---
**Keep this handy for Day 30 topics!** 🚀
