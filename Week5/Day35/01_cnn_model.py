"""
Day 35 - CNN Model Architecture
================================
Learn: Building Convolutional Neural Networks for Image Classification

Key Concepts:
- Convolutional layers extract features from images
- Pooling layers reduce spatial dimensions
- Dense layers perform classification
- Activation functions introduce non-linearity
"""

import numpy as np

# Note: TensorFlow/Keras import with fallback for environments without GPU
try:
    import tensorflow as tf
    from tensorflow import keras
    from keras import layers, models
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("TensorFlow not installed. Install with: pip install tensorflow")

# ========== CNN ARCHITECTURE BASICS ==========
print("=" * 60)
print("CNN ARCHITECTURE BASICS")
print("=" * 60)

print("""
CNN Components:
1. INPUT LAYER: Receives the image (e.g., 32x32x3 for CIFAR-10)

2. CONVOLUTIONAL LAYERS:
   - Apply filters/kernels to detect features
   - Extract patterns like edges, shapes, textures
   - Output: Feature maps

3. ACTIVATION FUNCTION (ReLU):
   - Introduces non-linearity
   - ReLU(x) = max(0, x)

4. POOLING LAYERS:
   - Reduce spatial dimensions
   - MaxPooling: Takes max value in window
   - Reduces computation and prevents overfitting

5. FLATTEN LAYER:
   - Converts 2D feature maps to 1D vector
   - Prepares data for dense layers

6. DENSE (FULLY CONNECTED) LAYERS:
   - Perform classification
   - Final layer has neurons = number of classes

7. OUTPUT LAYER:
   - Softmax activation for multi-class
   - Sigmoid activation for binary
""")

# ========== BUILDING A SIMPLE CNN ==========
print("\n" + "=" * 60)
print("BUILDING A SIMPLE CNN")
print("=" * 60)

if TF_AVAILABLE:
    def build_simple_cnn(input_shape=(32, 32, 3), num_classes=10):
        """
        Build a simple CNN for image classification
        
        Architecture:
        Conv2D -> ReLU -> MaxPool -> Conv2D -> ReLU -> MaxPool -> 
        Conv2D -> ReLU -> Flatten -> Dense -> ReLU -> Dropout -> Dense -> Softmax
        """
        model = keras.Sequential([
            # First Convolutional Block
            layers.Conv2D(32, (3, 3), activation='relu', 
                         input_shape=input_shape, 
                         padding='same',
                         name='conv1'),
            layers.MaxPooling2D((2, 2), name='pool1'),
            
            # Second Convolutional Block
            layers.Conv2D(64, (3, 3), activation='relu', 
                         padding='same',
                         name='conv2'),
            layers.MaxPooling2D((2, 2), name='pool2'),
            
            # Third Convolutional Block
            layers.Conv2D(64, (3, 3), activation='relu', 
                         padding='same',
                         name='conv3'),
            
            # Classification Head
            layers.Flatten(name='flatten'),
            layers.Dense(64, activation='relu', name='dense1'),
            layers.Dropout(0.5, name='dropout'),
            layers.Dense(num_classes, activation='softmax', name='output')
        ])
        
        return model
    
    # Build and display model
    print("\n1. Building Simple CNN Model:")
    simple_cnn = build_simple_cnn()
    simple_cnn.summary()
    
else:
    print("\nSkipping model building (TensorFlow not available)")
    print("Model architecture would be:")
    print("""
    Layer (type)                Output Shape              Param #
    ==============================================================
    conv1 (Conv2D)              (None, 32, 32, 32)        896
    pool1 (MaxPooling2D)        (None, 16, 16, 32)        0
    conv2 (Conv2D)              (None, 16, 16, 64)        18496
    pool2 (MaxPooling2D)        (None, 8, 8, 64)          0
    conv3 (Conv2D)              (None, 8, 8, 64)          36928
    flatten (Flatten)           (None, 4096)              0
    dense1 (Dense)              (None, 64)                262208
    dropout (Dropout)           (None, 64)                0
    output (Dense)              (None, 10)                650
    ==============================================================
    Total params: 319,178
    """)

# ========== UNDERSTANDING CONVOLUTION ==========
print("\n" + "=" * 60)
print("UNDERSTANDING CONVOLUTION")
print("=" * 60)

print("""
What happens in a Conv2D layer:

Input Image: 32x32x3 (Height x Width x Channels)
Kernel/Filter: 3x3x3 (small matrix)

The kernel slides across the image:
1. At each position, multiply kernel values with image values
2. Sum all products to get one output value
3. Creates a "feature map" showing where features are detected

Example with 32 filters (3x3):
- Input: 32x32x3
- Each filter produces: 32x32x1 feature map
- 32 filters produce: 32x32x32 output
""")

# Visual demonstration
print("\nSimple Convolution Example (Edge Detection):")

# Create a simple 5x5 image
simple_image = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
])

# Edge detection kernel
edge_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

print("\nOriginal Image (5x5):")
print(simple_image)
print("\nEdge Detection Kernel (3x3):")
print(edge_kernel)

# Manual convolution (simplified)
def simple_convolve(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    output = np.zeros((h-kh+1, w-kw+1))
    
    for i in range(h-kh+1):
        for j in range(w-kw+1):
            region = image[i:i+kh, j:j+kw]
            output[i, j] = np.sum(region * kernel)
    
    return output

result = simple_convolve(simple_image, edge_kernel)
print("\nConvolution Result (detects edges):")
print(result)

# ========== POOLING EXPLAINED ==========
print("\n" + "=" * 60)
print("POOLING EXPLAINED")
print("=" * 60)

print("""
MaxPooling2D with pool_size=(2, 2):
- Divides feature map into 2x2 regions
- Takes maximum value from each region
- Reduces dimensions by half

Example:
Input 4x4:          MaxPool Output 2x2:
[1, 2, 3, 4]        [5, 7]
[5, 6, 7, 8]   ->   [13, 15]
[9, 10, 11, 12]
[13, 14, 15, 16]

Benefits:
- Reduces computation
- Provides translation invariance
- Prevents overfitting
""")

# MaxPooling demonstration
print("\nMaxPooling Example:")
sample = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Input (4x4):")
print(sample)

# Manual max pooling
def max_pool_2d(image, pool_size=2):
    h, w = image.shape
    output = np.zeros((h // pool_size, w // pool_size))
    
    for i in range(0, h, pool_size):
        for j in range(0, w, pool_size):
            region = image[i:i+pool_size, j:j+pool_size]
            output[i // pool_size, j // pool_size] = np.max(region)
    
    return output

pooled = max_pool_2d(sample)
print("\nAfter MaxPool (2x2):")
print(pooled.astype(int))

# ========== ACTIVATION FUNCTIONS ==========
print("\n" + "=" * 60)
print("ACTIVATION FUNCTIONS")
print("=" * 60)

print("""
Common Activation Functions:

1. ReLU (Rectified Linear Unit):
   f(x) = max(0, x)
   - Most common in hidden layers
   - Fast, simple, effective

2. Softmax (Output layer for multi-class):
   f(x_i) = exp(x_i) / sum(exp(x_j))
   - Outputs probabilities that sum to 1
   - Use for multi-class classification

3. Sigmoid (Output layer for binary):
   f(x) = 1 / (1 + exp(-x))
   - Output between 0 and 1
   - Use for binary classification
""")

# Activation function demonstrations
def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
    return exp_x / exp_x.sum()

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Examples
print("\nReLU Examples:")
values = np.array([-2, -1, 0, 1, 2])
print(f"Input:  {values}")
print(f"ReLU:   {relu(values)}")

print("\nSoftmax Example (model output):")
logits = np.array([2.0, 1.0, 0.1])
probs = softmax(logits)
print(f"Logits:       {logits}")
print(f"Probabilities: {probs.round(3)}")
print(f"Sum:          {probs.sum():.3f}")

# ========== ADVANCED CNN ARCHITECTURE ==========
print("\n" + "=" * 60)
print("ADVANCED CNN ARCHITECTURE")
print("=" * 60)

if TF_AVAILABLE:
    def build_advanced_cnn(input_shape=(32, 32, 3), num_classes=10):
        """
        Build an advanced CNN with batch normalization
        """
        model = keras.Sequential([
            # Block 1
            layers.Conv2D(32, (3, 3), padding='same', input_shape=input_shape),
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
            
            # Classification Head
            layers.Flatten(),
            layers.Dense(512),
            layers.BatchNormalization(),
            layers.Activation('relu'),
            layers.Dropout(0.5),
            layers.Dense(num_classes, activation='softmax')
        ])
        
        return model
    
    print("\n2. Advanced CNN with Batch Normalization:")
    advanced_cnn = build_advanced_cnn()
    print(f"Total parameters: {advanced_cnn.count_params():,}")
    
else:
    print("\nAdvanced CNN architecture includes:")
    print("- Batch Normalization after each Conv2D")
    print("- Dropout layers for regularization")
    print("- Multiple convolutional blocks")
    print("- ~500K parameters")

# ========== MODEL COMPILATION ==========
print("\n" + "=" * 60)
print("MODEL COMPILATION")
print("=" * 60)

print("""
Compile settings for image classification:

model.compile(
    optimizer='adam',                           # Adaptive learning rate
    loss='sparse_categorical_crossentropy',     # For integer labels
    metrics=['accuracy']                        # Track accuracy
)

Alternative loss functions:
- 'categorical_crossentropy' - For one-hot encoded labels
- 'binary_crossentropy' - For binary classification

Common optimizers:
- 'adam' - Most popular, works well by default
- 'sgd' - Stochastic Gradient Descent
- 'rmsprop' - Good for RNNs
""")

if TF_AVAILABLE:
    print("\nCompiling simple CNN:")
    simple_cnn.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    print("✅ Model compiled successfully!")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
CNN Architecture Checklist:
✅ Input shape matches your data (e.g., 32x32x3)
✅ Conv2D layers extract features
✅ MaxPooling reduces dimensions
✅ Flatten before Dense layers
✅ Dropout prevents overfitting
✅ Output neurons = number of classes
✅ Softmax activation for multi-class

Next: Train the model with data!
""")

print("\n" + "=" * 60)
print("✅ CNN Model Architecture - Complete!")
print("=" * 60)
