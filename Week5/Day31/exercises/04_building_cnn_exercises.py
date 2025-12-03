"""
EXERCISES: Building CNN Models
==============================
Complete all 5 exercises below
"""

# Note: These exercises are code templates.
# To run them, ensure TensorFlow is installed:
# pip install tensorflow

print("Exercise 1: Build Simple CNN")
print("-" * 40)

# Exercise 1: Build a Simple CNN for MNIST
# TODO: Build a CNN with the specified architecture

print("""
Build a CNN with the following architecture:
1. Conv2D: 16 filters, 3x3, ReLU, input_shape=(28, 28, 1)
2. MaxPooling2D: 2x2
3. Conv2D: 32 filters, 3x3, ReLU
4. MaxPooling2D: 2x2
5. Flatten
6. Dense: 64 units, ReLU
7. Dense: 10 units, Softmax

Write your code below:
""")

# Your code here:
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# 
# model = Sequential([
#     # Add layers here
# ])
# model.summary()



print("\n\nExercise 2: Add Regularization")
print("-" * 40)

# Exercise 2: Add Dropout for Regularization
# TODO: Modify the previous model to include Dropout

print("""
Modify the Exercise 1 model to add:
1. Dropout(0.25) after each MaxPooling layer
2. Dropout(0.5) after the first Dense layer

This helps prevent overfitting.
""")

# Your code here:
# from tensorflow.keras.layers import Dropout
# 
# model_with_dropout = Sequential([
#     # Add layers with Dropout
# ])



print("\n\nExercise 3: Use BatchNormalization")
print("-" * 40)

# Exercise 3: Add Batch Normalization
# TODO: Build a CNN with BatchNormalization

print("""
Build a CNN with BatchNormalization:
1. Conv2D(32, 3x3) -> BatchNormalization -> ReLU -> MaxPool
2. Conv2D(64, 3x3) -> BatchNormalization -> ReLU -> MaxPool
3. Flatten -> Dense(128) -> BatchNormalization -> ReLU -> Dropout(0.5)
4. Dense(10) -> Softmax

Note: When using BatchNormalization, don't use activation in Conv2D.
Instead, add activation after BatchNormalization.
""")

# Your code here:
# from tensorflow.keras.layers import BatchNormalization, Activation
# 
# model_with_bn = Sequential([
#     Conv2D(32, (3, 3), input_shape=(28, 28, 1)),  # No activation
#     BatchNormalization(),
#     Activation('relu'),
#     MaxPooling2D((2, 2)),
#     # Continue...
# ])



print("\n\nExercise 4: Use Global Average Pooling")
print("-" * 40)

# Exercise 4: Replace Flatten with GlobalAveragePooling2D
# TODO: Build a CNN using Global Average Pooling

print("""
Build a CNN that uses GlobalAveragePooling2D instead of Flatten:
1. Conv2D(32, 3x3, ReLU, padding='same')
2. MaxPooling2D(2x2)
3. Conv2D(64, 3x3, ReLU, padding='same')
4. MaxPooling2D(2x2)
5. Conv2D(64, 3x3, ReLU, padding='same')
6. GlobalAveragePooling2D()  # Instead of Flatten!
7. Dense(10, Softmax)

Benefits: Fewer parameters, acts as regularization
""")

# Your code here:
# from tensorflow.keras.layers import GlobalAveragePooling2D



print("\n\nExercise 5: Build CIFAR-10 CNN")
print("-" * 40)

# Exercise 5: Build a Deeper CNN for CIFAR-10
# TODO: Design a CNN for color images (32x32x3)

print("""
Design a CNN for CIFAR-10 (32x32 RGB images, 10 classes):

Requirements:
- Input: (32, 32, 3)
- At least 3 convolutional blocks (Conv-Conv-Pool pattern)
- Use padding='same' to maintain dimensions
- Include Dropout for regularization
- Compile with appropriate optimizer and loss

Suggested structure:
Block 1: Conv(32) -> Conv(32) -> Pool -> Dropout
Block 2: Conv(64) -> Conv(64) -> Pool -> Dropout
Block 3: Conv(128) -> Conv(128) -> Pool -> Dropout
Dense: 256 units -> Dropout -> 10 units (output)

Expected parameters: ~500,000 to 1,000,000
""")

# Your code here:
# def create_cifar10_model():
#     model = Sequential([
#         # Block 1
#         Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
#         Conv2D(32, (3, 3), activation='relu', padding='same'),
#         MaxPooling2D((2, 2)),
#         Dropout(0.25),
#         
#         # Continue with more blocks...
#     ])
#     
#     model.compile(
#         optimizer='adam',
#         loss='sparse_categorical_crossentropy',
#         metrics=['accuracy']
#     )
#     
#     return model

