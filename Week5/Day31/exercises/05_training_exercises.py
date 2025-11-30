"""
EXERCISES: Training CNN
=======================
Complete all 5 exercises below
"""

# Note: These exercises are code templates.
# To run them, ensure TensorFlow is installed:
# pip install tensorflow

print("Exercise 1: Data Loading and Preprocessing")
print("-" * 40)

# Exercise 1: Complete Data Pipeline
# TODO: Load MNIST and preprocess for training

print("""
Complete the data pipeline:
1. Load MNIST using keras.datasets
2. Print original shapes
3. Reshape to add channel dimension
4. Normalize to [0, 1]
5. Print final shapes and verify pixel range
""")

# Your code here:
# from tensorflow.keras.datasets import mnist
# 
# # Load data
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# 
# # TODO: Complete preprocessing
# # ...



print("\n\nExercise 2: Compile with Different Optimizers")
print("-" * 40)

# Exercise 2: Compare Optimizers
# TODO: Create functions to compile models with different optimizers

print("""
Create three versions of the same model compiled with:
1. SGD with learning_rate=0.01
2. Adam with learning_rate=0.001
3. RMSprop with learning_rate=0.001

Note how to specify learning rate explicitly.
""")

# Your code here:
# from tensorflow.keras.optimizers import SGD, Adam, RMSprop
# 
# def compile_with_sgd(model):
#     model.compile(
#         optimizer=SGD(learning_rate=0.01),
#         loss='sparse_categorical_crossentropy',
#         metrics=['accuracy']
#     )
#     return model
# 
# # Add functions for Adam and RMSprop



print("\n\nExercise 3: Implement Callbacks")
print("-" * 40)

# Exercise 3: Set Up Training Callbacks
# TODO: Create a list of useful callbacks

print("""
Set up the following callbacks:
1. EarlyStopping: monitor val_loss, patience=5, restore_best_weights=True
2. ModelCheckpoint: save best model to 'best_model.h5'
3. ReduceLROnPlateau: reduce LR by 0.5 if val_loss doesn't improve for 3 epochs

Return them as a list to pass to model.fit()
""")

# Your code here:
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
# 
# callbacks = [
#     EarlyStopping(...),
#     ModelCheckpoint(...),
#     ReduceLROnPlateau(...)
# ]



print("\n\nExercise 4: Data Augmentation")
print("-" * 40)

# Exercise 4: Set Up Data Augmentation
# TODO: Create an ImageDataGenerator with augmentation

print("""
Create an ImageDataGenerator with the following augmentations:
- Rotation: up to 10 degrees
- Width shift: up to 10%
- Height shift: up to 10%
- Zoom: up to 10%

Then show how to use it with model.fit()
""")

# Your code here:
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# 
# datagen = ImageDataGenerator(
#     rotation_range=10,
#     # Add more augmentations...
# )
# 
# # Fit the generator to training data (computes statistics if needed)
# # datagen.fit(x_train)
# 
# # Training with augmentation
# # model.fit(datagen.flow(x_train, y_train, batch_size=32), ...)



print("\n\nExercise 5: Complete Training Script")
print("-" * 40)

# Exercise 5: Put It All Together
# TODO: Write a complete training script

print("""
Write a complete training script that:
1. Loads and preprocesses MNIST
2. Creates a CNN model
3. Compiles with Adam optimizer
4. Sets up EarlyStopping callback
5. Trains for up to 20 epochs with validation split of 0.1
6. Evaluates on test set
7. Prints test accuracy
8. Saves the final model

This should be runnable as a standalone script.
""")

# Your code here:
# Complete training script template:
"""
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# 1. Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Preprocess
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# 3. Build model
model = Sequential([
    # TODO: Add layers
])

# 4. Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Callbacks
callbacks = [
    EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
]

# 6. Train
history = model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=128,
    validation_split=0.1,
    callbacks=callbacks
)

# 7. Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')

# 8. Save
model.save('mnist_cnn.h5')
"""

