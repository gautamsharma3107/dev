"""
Day 31 - Training CNN on MNIST
==============================
Learn: Complete workflow for training a CNN on the MNIST dataset

Key Concepts:
- Loading and preprocessing MNIST
- Building the CNN model
- Training with callbacks
- Evaluating performance
- Making predictions
"""

import numpy as np

print("=" * 60)
print("TRAINING CNN ON MNIST")
print("=" * 60)

# ========== COMPLETE TRAINING SCRIPT ==========
print("\n" + "=" * 60)
print("COMPLETE TRAINING SCRIPT")
print("=" * 60)

print("""
# Complete MNIST Training Script

# ==========================================
# STEP 1: IMPORTS
# ==========================================

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
)
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical

# ==========================================
# STEP 2: LOAD AND PREPROCESS DATA
# ==========================================

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f"Training data shape: {x_train.shape}")
print(f"Training labels shape: {y_train.shape}")
print(f"Test data shape: {x_test.shape}")
print(f"Test labels shape: {y_test.shape}")

# Preprocess images
# Reshape: Add channel dimension (28, 28) -> (28, 28, 1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Normalize: Scale pixel values from [0, 255] to [0, 1]
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

print(f"\\nAfter preprocessing:")
print(f"x_train shape: {x_train.shape}")
print(f"x_test shape: {x_test.shape}")
print(f"Pixel range: [{x_train.min()}, {x_train.max()}]")

# ==========================================
# STEP 3: BUILD THE MODEL
# ==========================================

def create_model():
    model = Sequential([
        # First Conv Block
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        
        # Second Conv Block
        Conv2D(64, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        
        # Third Conv Block
        Conv2D(64, (3, 3), activation='relu'),
        BatchNormalization(),
        
        # Classification Head
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    
    return model

model = create_model()
model.summary()

# ==========================================
# STEP 4: COMPILE THE MODEL
# ==========================================

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Use this for integer labels
    metrics=['accuracy']
)

# ==========================================
# STEP 5: DEFINE CALLBACKS
# ==========================================

callbacks = [
    # Stop early if validation loss doesn't improve
    EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True,
        verbose=1
    ),
    # Save best model
    ModelCheckpoint(
        'best_mnist_cnn.h5',
        monitor='val_accuracy',
        save_best_only=True,
        verbose=1
    )
]

# ==========================================
# STEP 6: TRAIN THE MODEL
# ==========================================

history = model.fit(
    x_train, y_train,
    epochs=20,                # Maximum epochs
    batch_size=128,           # Batch size
    validation_split=0.1,     # Use 10% for validation
    callbacks=callbacks,
    verbose=1
)

# ==========================================
# STEP 7: EVALUATE THE MODEL
# ==========================================

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"\\nTest Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

# ==========================================
# STEP 8: VISUALIZE TRAINING
# ==========================================

# Plot training history
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Accuracy plot
axes[0].plot(history.history['accuracy'], label='Training')
axes[0].plot(history.history['val_accuracy'], label='Validation')
axes[0].set_title('Model Accuracy')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Accuracy')
axes[0].legend()

# Loss plot
axes[1].plot(history.history['loss'], label='Training')
axes[1].plot(history.history['val_loss'], label='Validation')
axes[1].set_title('Model Loss')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].legend()

plt.tight_layout()
plt.savefig('training_history.png')
plt.show()

# ==========================================
# STEP 9: MAKE PREDICTIONS
# ==========================================

# Predict on test samples
predictions = model.predict(x_test[:10])

print("\\nPredictions for first 10 test images:")
for i in range(10):
    pred_class = np.argmax(predictions[i])
    confidence = np.max(predictions[i])
    actual = y_test[i]
    status = "✓" if pred_class == actual else "✗"
    print(f"Image {i}: Predicted={pred_class}, Actual={actual}, "
          f"Confidence={confidence:.2%} {status}")

# ==========================================
# STEP 10: SAVE THE MODEL
# ==========================================

# Save entire model
model.save('mnist_cnn_final.h5')
print("\\nModel saved as 'mnist_cnn_final.h5'")

# To load later:
# from tensorflow.keras.models import load_model
# loaded_model = load_model('mnist_cnn_final.h5')
""")

# ========== DATA PREPROCESSING DETAILS ==========
print("\n" + "=" * 60)
print("DATA PREPROCESSING DETAILS")
print("=" * 60)

print("""
Why Each Preprocessing Step Matters:

1. RESHAPING (-1, 28, 28, 1):
   - -1: Keeps batch size flexible
   - 28, 28: Height and width
   - 1: Single channel (grayscale)
   - CNNs expect 4D input: (batch, height, width, channels)

2. NORMALIZING (/ 255.0):
   - Raw pixels: 0-255 (uint8)
   - After normalization: 0.0-1.0 (float32)
   - Benefits:
     * Helps gradient descent converge faster
     * Prevents large weight values
     * Consistent input scale

3. CONVERTING TO FLOAT32:
   - Neural networks work with floating point
   - float32 is standard (float64 is overkill)
   - Saves memory vs float64

Alternative Preprocessing:
# Standardization (zero mean, unit variance)
mean = x_train.mean()
std = x_train.std()
x_train_standardized = (x_train - mean) / std
x_test_standardized = (x_test - mean) / std  # Use training stats!
""")

# ========== CALLBACKS EXPLAINED ==========
print("\n" + "=" * 60)
print("CALLBACKS EXPLAINED")
print("=" * 60)

print("""
Callbacks are functions called during training:

1. EARLY STOPPING:
   EarlyStopping(
       monitor='val_loss',      # What to monitor
       patience=3,              # Wait N epochs before stopping
       restore_best_weights=True,  # Restore best model weights
       verbose=1                # Print messages
   )
   - Stops training when no improvement
   - Prevents overfitting
   - Saves time

2. MODEL CHECKPOINT:
   ModelCheckpoint(
       'best_model.h5',
       monitor='val_accuracy',
       save_best_only=True,
       verbose=1
   )
   - Saves model during training
   - save_best_only: Only save if improved
   - Can save weights only or entire model

3. LEARNING RATE SCHEDULER:
   from tensorflow.keras.callbacks import ReduceLROnPlateau
   
   ReduceLROnPlateau(
       monitor='val_loss',
       factor=0.5,        # Multiply LR by this
       patience=2,        # Wait N epochs
       min_lr=1e-6        # Minimum learning rate
   )
   - Reduces learning rate when stuck

4. TENSORBOARD:
   from tensorflow.keras.callbacks import TensorBoard
   
   TensorBoard(log_dir='./logs')
   - Visualize training in browser
   - Run: tensorboard --logdir=./logs
""")

# ========== TRAINING PARAMETERS ==========
print("\n" + "=" * 60)
print("TRAINING PARAMETERS EXPLAINED")
print("=" * 60)

print("""
Key Training Parameters:

1. EPOCHS:
   - Number of times to see entire dataset
   - Too few: Underfitting
   - Too many: Overfitting
   - Use early stopping to find optimal

2. BATCH SIZE:
   - Number of samples per gradient update
   - Common values: 32, 64, 128, 256
   - Larger batch = more memory, stable gradients
   - Smaller batch = less memory, more noise (can help generalize)

3. VALIDATION SPLIT:
   - Fraction of training data for validation
   - 0.1-0.2 is common
   - Used to monitor overfitting

4. LEARNING RATE (in optimizer):
   - How big steps in gradient descent
   - Too high: Overshooting, unstable
   - Too low: Slow convergence
   - Adam default (0.001) usually good

Example Configurations:
# Quick experiment
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.1)

# Full training
model.fit(x_train, y_train, epochs=100, batch_size=32, 
          validation_split=0.2, callbacks=callbacks)
""")

# ========== HANDLING DIFFERENT LABEL FORMATS ==========
print("\n" + "=" * 60)
print("HANDLING DIFFERENT LABEL FORMATS")
print("=" * 60)

print("""
Two Common Label Formats:

1. INTEGER LABELS (what MNIST uses):
   y_train = [5, 0, 4, 1, 9, 2, ...]  # Shape: (60000,)
   
   Use:
   loss='sparse_categorical_crossentropy'

2. ONE-HOT ENCODED LABELS:
   y_train = [[0,0,0,0,0,1,0,0,0,0],  # 5
              [1,0,0,0,0,0,0,0,0,0],  # 0
              ...]                     # Shape: (60000, 10)
   
   To convert:
   from tensorflow.keras.utils import to_categorical
   y_train_onehot = to_categorical(y_train, num_classes=10)
   
   Use:
   loss='categorical_crossentropy'

Tip: sparse_categorical_crossentropy is more memory efficient
for large number of classes.
""")

# ========== EVALUATING THE MODEL ==========
print("\n" + "=" * 60)
print("EVALUATING THE MODEL")
print("=" * 60)

print("""
After Training, Evaluate Performance:

# Basic evaluation
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")

# Detailed predictions
predictions = model.predict(x_test)

# Get predicted classes
predicted_classes = np.argmax(predictions, axis=1)

# Confusion Matrix
from sklearn.metrics import confusion_matrix, classification_report

cm = confusion_matrix(y_test, predicted_classes)
print(confusion_matrix)

# Classification Report
print(classification_report(y_test, predicted_classes))

# Precision, recall, F1-score for each class
# Useful to see which digits are harder to classify

# Find misclassified examples
misclassified = np.where(predicted_classes != y_test)[0]
print(f"Misclassified {len(misclassified)} out of {len(y_test)}")
""")

# ========== IMPROVING MODEL PERFORMANCE ==========
print("\n" + "=" * 60)
print("TIPS FOR IMPROVING PERFORMANCE")
print("=" * 60)

print("""
If Model Underfits (low training accuracy):
1. Add more layers or filters
2. Train for more epochs
3. Reduce regularization (dropout)
4. Increase model capacity

If Model Overfits (high training, low validation accuracy):
1. Add data augmentation
2. Increase dropout
3. Add more regularization (L2)
4. Use early stopping
5. Get more training data
6. Simplify the model

Data Augmentation Example:
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1
)

# Train with augmentation
model.fit(datagen.flow(x_train, y_train, batch_size=32),
          epochs=20, validation_data=(x_test, y_test))

Expected Performance:
- Simple CNN: 98-99% accuracy
- With augmentation: 99%+
- State of the art: 99.8%+
""")

# ========== MAKING PREDICTIONS ON NEW IMAGES ==========
print("\n" + "=" * 60)
print("MAKING PREDICTIONS ON NEW IMAGES")
print("=" * 60)

print("""
After training, predict on new images:

# Load and preprocess new image
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def predict_digit(model, image_path):
    # Load image as grayscale, resize to 28x28
    img = load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    
    # Convert to array and preprocess
    img_array = img_to_array(img)           # (28, 28, 1)
    img_array = img_array / 255.0           # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # (1, 28, 28, 1)
    
    # Predict
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])
    
    return predicted_class, confidence

# Usage
digit, conf = predict_digit(model, 'my_digit.png')
print(f"Predicted: {digit} with {conf:.2%} confidence")

# For MNIST test samples
sample_idx = 0
sample = x_test[sample_idx:sample_idx+1]  # Keep batch dimension
prediction = model.predict(sample)
print(f"Predicted: {np.argmax(prediction[0])}")
print(f"Actual: {y_test[sample_idx]}")
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("MNIST TRAINING SUMMARY")
print("=" * 60)

print("""
Complete Training Workflow:
---------------------------
1. Load data: mnist.load_data()
2. Preprocess: Reshape (-1, 28, 28, 1), Normalize (/ 255.0)
3. Build model: Sequential with Conv2D, MaxPooling2D, Dense
4. Compile: optimizer='adam', loss='sparse_categorical_crossentropy'
5. Train: model.fit() with callbacks
6. Evaluate: model.evaluate() on test set
7. Predict: model.predict() on new images
8. Save: model.save()

Expected Results:
- Training accuracy: 99%+
- Test accuracy: 98-99%
- Training time: 2-5 minutes (with GPU)

Next Steps:
- Try CIFAR-10 (color images, 10 classes)
- Experiment with architectures
- Add data augmentation
- Try transfer learning
""")

print("\n" + "=" * 60)
print("✅ Training CNN on MNIST - Complete!")
print("=" * 60)
