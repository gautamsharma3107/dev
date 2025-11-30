"""
Day 31 - Building a Simple CNN
==============================
Learn: How to construct a CNN architecture step by step

Key Concepts:
- CNN architecture components
- Layer stacking patterns
- Model building in Keras
- Understanding model summary
- Best practices for CNN design
"""

print("=" * 60)
print("BUILDING A SIMPLE CNN")
print("=" * 60)

# ========== CNN ARCHITECTURE OVERVIEW ==========
print("\n" + "=" * 60)
print("CNN ARCHITECTURE OVERVIEW")
print("=" * 60)

print("""
A typical CNN consists of two main parts:

1. FEATURE EXTRACTION (Convolutional Base):
   - Conv2D layers: Extract features
   - Activation (ReLU): Add non-linearity
   - Pooling layers: Reduce dimensions
   
2. CLASSIFICATION (Dense Head):
   - Flatten: Convert 3D to 1D
   - Dense layers: Learn patterns from features
   - Output layer: Final prediction

Typical Pattern:
[Input] -> [Conv-ReLU-Pool] x N -> [Flatten] -> [Dense] x M -> [Output]
""")

# ========== BUILDING WITH KERAS SEQUENTIAL ==========
print("\n" + "=" * 60)
print("BUILDING WITH KERAS SEQUENTIAL")
print("=" * 60)

print("""
Simple CNN for MNIST (28x28 grayscale images, 10 classes):

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout
)

model = Sequential([
    # First Convolutional Block
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    
    # Second Convolutional Block
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    
    # Third Convolutional Block
    Conv2D(64, (3, 3), activation='relu'),
    
    # Classification Head
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
""")

# ========== STEP-BY-STEP EXPLANATION ==========
print("\n" + "=" * 60)
print("STEP-BY-STEP EXPLANATION")
print("=" * 60)

print("""
Let's trace through each layer:

1. INPUT: (28, 28, 1) - Grayscale MNIST image

2. Conv2D(32, (3,3), relu) + input_shape=(28,28,1)
   - 32 filters of 3x3
   - Output: (26, 26, 32)
   - Parameters: 32 * (3*3*1 + 1) = 320

3. MaxPooling2D((2,2))
   - Reduces spatial dimensions by half
   - Output: (13, 13, 32)
   - Parameters: 0

4. Conv2D(64, (3,3), relu)
   - 64 filters of 3x3
   - Output: (11, 11, 64)
   - Parameters: 64 * (3*3*32 + 1) = 18,496

5. MaxPooling2D((2,2))
   - Output: (5, 5, 64)
   - Parameters: 0

6. Conv2D(64, (3,3), relu)
   - Output: (3, 3, 64)
   - Parameters: 64 * (3*3*64 + 1) = 36,928

7. Flatten()
   - Converts 3D to 1D
   - Output: 3*3*64 = 576
   - Parameters: 0

8. Dense(64, relu)
   - Fully connected layer
   - Output: 64
   - Parameters: 576*64 + 64 = 36,928

9. Dropout(0.5)
   - Regularization (50% dropout)
   - Output: 64
   - Parameters: 0

10. Dense(10, softmax)
    - Output layer for 10 classes
    - Output: 10
    - Parameters: 64*10 + 10 = 650

Total Parameters: ~93,000
""")

# ========== MODEL VARIATIONS ==========
print("\n" + "=" * 60)
print("CNN MODEL VARIATIONS")
print("=" * 60)

print("""
1. SIMPLE CNN (Like Above):
   - Good for simple tasks (MNIST)
   - Quick to train
   - ~100K parameters

2. DEEPER CNN (for CIFAR-10):
   model = Sequential([
       Conv2D(32, (3, 3), activation='relu', padding='same', 
              input_shape=(32, 32, 3)),
       Conv2D(32, (3, 3), activation='relu', padding='same'),
       MaxPooling2D((2, 2)),
       Dropout(0.25),
       
       Conv2D(64, (3, 3), activation='relu', padding='same'),
       Conv2D(64, (3, 3), activation='relu', padding='same'),
       MaxPooling2D((2, 2)),
       Dropout(0.25),
       
       Conv2D(128, (3, 3), activation='relu', padding='same'),
       Conv2D(128, (3, 3), activation='relu', padding='same'),
       MaxPooling2D((2, 2)),
       Dropout(0.25),
       
       Flatten(),
       Dense(512, activation='relu'),
       Dropout(0.5),
       Dense(10, activation='softmax')
   ])

3. USING GLOBAL AVERAGE POOLING:
   model = Sequential([
       Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
       MaxPooling2D((2, 2)),
       Conv2D(64, (3, 3), activation='relu'),
       MaxPooling2D((2, 2)),
       Conv2D(64, (3, 3), activation='relu'),
       GlobalAveragePooling2D(),  # Instead of Flatten
       Dense(10, activation='softmax')
   ])
""")

# ========== BUILDING WITH FUNCTIONAL API ==========
print("\n" + "=" * 60)
print("BUILDING WITH FUNCTIONAL API")
print("=" * 60)

print("""
For more complex architectures, use the Functional API:

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

# Define input
inputs = Input(shape=(28, 28, 1))

# Build model
x = Conv2D(32, (3, 3), activation='relu')(inputs)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = Flatten()(x)
x = Dense(64, activation='relu')(x)
outputs = Dense(10, activation='softmax')(x)

# Create model
model = Model(inputs=inputs, outputs=outputs)

Benefits of Functional API:
- Multiple inputs/outputs
- Shared layers
- Non-sequential connections (skip connections)
- More flexible architecture design
""")

# ========== COMPILING THE MODEL ==========
print("\n" + "=" * 60)
print("COMPILING THE MODEL")
print("=" * 60)

print("""
After building, compile the model:

model.compile(
    optimizer='adam',                    # or SGD, RMSprop
    loss='sparse_categorical_crossentropy',  # for integer labels
    metrics=['accuracy']
)

Optimizer Choices:
- 'adam': Good default, adaptive learning rate
- 'sgd': Classic, may need learning rate tuning
- 'rmsprop': Good for recurrent networks

Loss Function Choices:
- 'sparse_categorical_crossentropy': Integer labels (0, 1, 2, ...)
- 'categorical_crossentropy': One-hot encoded labels
- 'binary_crossentropy': Binary classification

Learning Rate:
from tensorflow.keras.optimizers import Adam
model.compile(optimizer=Adam(learning_rate=0.001), ...)
""")

# ========== VIEWING MODEL SUMMARY ==========
print("\n" + "=" * 60)
print("MODEL SUMMARY")
print("=" * 60)

print("""
Use model.summary() to see architecture:

Model: "sequential"
_________________________________________________________________
Layer (type)                Output Shape              Param #   
=================================================================
conv2d (Conv2D)             (None, 26, 26, 32)        320       
max_pooling2d (MaxPool2D)   (None, 13, 13, 32)        0         
conv2d_1 (Conv2D)           (None, 11, 11, 64)        18496     
max_pooling2d_1 (MaxPool2D) (None, 5, 5, 64)          0         
conv2d_2 (Conv2D)           (None, 3, 3, 64)          36928     
flatten (Flatten)           (None, 576)               0         
dense (Dense)               (None, 64)                36928     
dropout (Dropout)           (None, 64)                0         
dense_1 (Dense)             (None, 10)                650       
=================================================================
Total params: 93,322
Trainable params: 93,322
Non-trainable params: 0

Key Information:
- Output Shape: Dimensions at each layer
- Param #: Trainable parameters
- None in shape means batch size (variable)
""")

# ========== DESIGN BEST PRACTICES ==========
print("\n" + "=" * 60)
print("CNN DESIGN BEST PRACTICES")
print("=" * 60)

print("""
1. FILTER PROGRESSION:
   - Start small (32), increase deeper (64, 128, 256)
   - Double filters when spatial dimensions halve
   
2. KERNEL SIZE:
   - Use 3x3 kernels (most efficient)
   - Two 3x3 = one 5x5 receptive field, fewer params
   - 1x1 for dimensionality reduction

3. PADDING:
   - Use 'same' to maintain dimensions
   - Use 'valid' when reduction is desired

4. POOLING:
   - Pool after every 2-3 conv layers
   - 2x2 with stride 2 is standard

5. REGULARIZATION:
   - Dropout before dense layers (0.25-0.5)
   - Dropout can also be used after conv layers (0.1-0.25)

6. BATCH NORMALIZATION (advanced):
   - Add after Conv2D, before activation
   - Speeds up training, acts as regularization

7. ACTIVATION:
   - ReLU for hidden layers
   - Softmax for multi-class output
   - Sigmoid for binary output
""")

# ========== COMMON MISTAKES ==========
print("\n" + "=" * 60)
print("COMMON MISTAKES TO AVOID")
print("=" * 60)

print("""
1. TOO MANY DENSE NEURONS:
   ❌ Flatten() -> Dense(4096) -> Dense(4096) -> Dense(10)
   ✓ Flatten() -> Dense(64) -> Dense(10)
   
2. FORGETTING INPUT SHAPE:
   ❌ First Conv2D without input_shape
   ✓ Conv2D(..., input_shape=(28, 28, 1))

3. WRONG LOSS FUNCTION:
   ❌ Using 'categorical_crossentropy' with integer labels
   ✓ Use 'sparse_categorical_crossentropy' for integer labels

4. NO REGULARIZATION:
   ❌ Just conv and dense layers
   ✓ Add Dropout, especially before dense layers

5. DIMENSION MISMATCH:
   ❌ Not tracking spatial dimensions through layers
   ✓ Use model.summary() to verify shapes

6. FINAL ACTIVATION:
   ❌ Dense(10, activation='relu') for classification
   ✓ Dense(10, activation='softmax') for multi-class
""")

# ========== COMPLETE EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE CNN EXAMPLE")
print("=" * 60)

print("""
# Complete CNN for MNIST Classification

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
)
from tensorflow.keras.optimizers import Adam

def create_mnist_cnn():
    model = Sequential([
        # Block 1
        Conv2D(32, (3, 3), activation='relu', padding='same',
               input_shape=(28, 28, 1)),
        BatchNormalization(),
        Conv2D(32, (3, 3), activation='relu', padding='same'),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        
        # Block 2
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        
        # Classification Head
        Flatten(),
        Dense(256, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# Create and view model
model = create_mnist_cnn()
model.summary()

# This model should achieve ~99% accuracy on MNIST
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("BUILDING CNN SUMMARY")
print("=" * 60)

print("""
Key Takeaways:
--------------
1. CNNs have two parts: feature extraction + classification
2. Use Sequential API for simple architectures
3. Use Functional API for complex architectures
4. Always check model.summary() to verify dimensions
5. Compile with appropriate optimizer and loss

Architecture Pattern:
Input -> [Conv -> ReLU -> Pool] x N -> Flatten -> Dense -> Output

Remember:
- Start simple, add complexity if needed
- More filters in deeper layers
- Regularization prevents overfitting
- Test on validation data frequently
""")

print("\n" + "=" * 60)
print("✅ Building a Simple CNN - Complete!")
print("=" * 60)
