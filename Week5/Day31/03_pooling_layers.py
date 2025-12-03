"""
Day 31 - Pooling Layers
=======================
Learn: How pooling layers work and their importance in CNNs

Key Concepts:
- Max Pooling
- Average Pooling
- Global Pooling
- Why pooling is useful
- When to use each type
"""

import numpy as np

print("=" * 60)
print("POOLING LAYERS")
print("=" * 60)

# ========== WHAT IS POOLING? ==========
print("\n" + "=" * 60)
print("WHAT IS POOLING?")
print("=" * 60)

print("""
Pooling is a downsampling operation that reduces the spatial
dimensions (width, height) while retaining important features.

Why Use Pooling?
----------------
1. REDUCES COMPUTATION: Smaller feature maps = faster processing
2. REDUCES OVERFITTING: Fewer parameters to learn
3. TRANSLATION INVARIANCE: Small shifts don't change output
4. EXTRACTS DOMINANT FEATURES: Keeps most important information

Common Pool Sizes:
- 2x2 (most common): Reduces each dimension by half
- 3x3: More aggressive reduction
- Stride usually equals pool size

Typical Usage:
Conv2D -> ReLU -> Pooling -> Conv2D -> ReLU -> Pooling -> ...
""")

# ========== MAX POOLING ==========
print("\n" + "=" * 60)
print("MAX POOLING")
print("=" * 60)

print("""
Max Pooling: Takes the MAXIMUM value from each pooling window

Example with 2x2 pool size:
---------------------------
Input (4x4):              Output (2x2):
[1, 3, 2, 4]              [9, 8]
[5, 9, 7, 8]      ->      [6, 9]
[4, 2, 6, 3]
[3, 6, 1, 9]

How it works:
- Divide input into 2x2 windows
- Take maximum from each window
- No overlap (stride = pool_size)
""")

def max_pool_2d(image, pool_size=2):
    """
    Simple max pooling demonstration.
    In practice, use tensorflow.keras.layers.MaxPooling2D
    """
    h, w = image.shape
    pool_h, pool_w = pool_size, pool_size
    
    out_h = h // pool_h
    out_w = w // pool_w
    
    output = np.zeros((out_h, out_w))
    
    for i in range(out_h):
        for j in range(out_w):
            window = image[i*pool_h:(i+1)*pool_h, j*pool_w:(j+1)*pool_w]
            output[i, j] = np.max(window)
    
    return output

# Demonstration
sample = np.array([
    [1, 3, 2, 4],
    [5, 9, 7, 8],
    [4, 2, 6, 3],
    [3, 6, 1, 9]
], dtype=np.float32)

print("\nInput (4x4):")
print(sample)

max_pooled = max_pool_2d(sample, pool_size=2)
print("\nMax Pooled Output (2x2):")
print(max_pooled)

print("""
Benefits of Max Pooling:
- Extracts the strongest activations
- Provides some translation invariance
- Most commonly used in CNNs
- Works well for detecting if a feature exists
""")

# ========== AVERAGE POOLING ==========
print("\n" + "=" * 60)
print("AVERAGE POOLING")
print("=" * 60)

print("""
Average Pooling: Takes the AVERAGE value from each pooling window

Same example with 2x2 pool size:
--------------------------------
Input (4x4):              Output (2x2):
[1, 3, 2, 4]              [4.5, 5.25]
[5, 9, 7, 8]      ->      [3.75, 4.75]
[4, 2, 6, 3]
[3, 6, 1, 9]

Calculations:
Top-left: (1+3+5+9)/4 = 4.5
Top-right: (2+4+7+8)/4 = 5.25
Bottom-left: (4+2+3+6)/4 = 3.75
Bottom-right: (6+3+1+9)/4 = 4.75
""")

def avg_pool_2d(image, pool_size=2):
    """
    Simple average pooling demonstration.
    In practice, use tensorflow.keras.layers.AveragePooling2D
    """
    h, w = image.shape
    pool_h, pool_w = pool_size, pool_size
    
    out_h = h // pool_h
    out_w = w // pool_w
    
    output = np.zeros((out_h, out_w))
    
    for i in range(out_h):
        for j in range(out_w):
            window = image[i*pool_h:(i+1)*pool_h, j*pool_w:(j+1)*pool_w]
            output[i, j] = np.mean(window)
    
    return output

avg_pooled = avg_pool_2d(sample, pool_size=2)
print("\nInput (4x4):")
print(sample)
print("\nAverage Pooled Output (2x2):")
print(avg_pooled)

print("""
When to Use Average Pooling:
- Smoothing effect (less sharp transitions)
- When you want to consider all values
- Sometimes used in the final layers
- Good for tasks where overall pattern matters
""")

# ========== MAX VS AVERAGE COMPARISON ==========
print("\n" + "=" * 60)
print("MAX VS AVERAGE POOLING")
print("=" * 60)

# Create a more illustrative example
feature_map = np.array([
    [0, 0, 10, 10],
    [0, 0, 10, 10],
    [5, 5, 1, 1],
    [5, 5, 1, 1]
], dtype=np.float32)

print("Feature Map:")
print(feature_map)

print("\nMax Pooling (2x2):")
print(max_pool_2d(feature_map))
print("-> Emphasizes strongest activations (10 and 5)")

print("\nAverage Pooling (2x2):")
print(avg_pool_2d(feature_map))
print("-> Smooths values (0.0, 10.0, 5.0, 1.0)")

print("""
Comparison Summary:
-------------------
MAX POOLING:
✓ Extracts dominant features
✓ Better for detecting if feature exists
✓ Most commonly used
✓ Good for classification

AVERAGE POOLING:
✓ Preserves background information
✓ Smoother output
✓ Sometimes used at end of network
✓ Good when all information matters
""")

# ========== GLOBAL POOLING ==========
print("\n" + "=" * 60)
print("GLOBAL POOLING")
print("=" * 60)

print("""
Global Pooling: Reduces entire feature map to a single value per channel

Global Average Pooling (GAP):
- Takes average of ALL values in the feature map
- Input: (batch, height, width, channels)
- Output: (batch, channels)

Example:
Input shape: (7, 7, 512)
After GlobalAveragePooling2D: (512,)

Why Use Global Pooling?
-----------------------
1. Reduces to fixed size regardless of input size
2. Dramatically reduces parameters before Dense layers
3. Acts as regularization (reduces overfitting)
4. Commonly used before final classification layer
""")

def global_avg_pool(feature_map):
    """Global Average Pooling: average of entire feature map"""
    return np.mean(feature_map)

def global_max_pool(feature_map):
    """Global Max Pooling: maximum of entire feature map"""
    return np.max(feature_map)

# Example with multiple channels
print("\nGlobal Pooling Example:")
print("=" * 40)

# Simulating 3 feature maps (7x7 each, representing 3 channels)
channel1 = np.random.rand(7, 7) * 10
channel2 = np.random.rand(7, 7) * 20
channel3 = np.random.rand(7, 7) * 5

print(f"Input shape: (7, 7, 3)")
print(f"Channel 1 - Mean: {np.mean(channel1):.2f}, Max: {np.max(channel1):.2f}")
print(f"Channel 2 - Mean: {np.mean(channel2):.2f}, Max: {np.max(channel2):.2f}")
print(f"Channel 3 - Mean: {np.mean(channel3):.2f}, Max: {np.max(channel3):.2f}")

print(f"\nAfter GlobalAveragePooling2D: shape (3,)")
print(f"Output: [{np.mean(channel1):.2f}, {np.mean(channel2):.2f}, {np.mean(channel3):.2f}]")

# ========== POOLING IN KERAS ==========
print("\n" + "=" * 60)
print("POOLING LAYERS IN KERAS")
print("=" * 60)

print("""
Using Pooling in TensorFlow/Keras:

from tensorflow.keras.layers import (
    MaxPooling2D, 
    AveragePooling2D,
    GlobalAveragePooling2D,
    GlobalMaxPooling2D
)

# Max Pooling
MaxPooling2D(pool_size=(2, 2))      # Default stride = pool_size
MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')

# Average Pooling
AveragePooling2D(pool_size=(2, 2))

# Global Pooling
GlobalAveragePooling2D()  # Reduces spatial dims to 1x1
GlobalMaxPooling2D()

Example Usage in a Model:
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),  # 28x28 -> 14x14
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),  # 14x14 -> 7x7 (approximately)
    GlobalAveragePooling2D(),  # 7x7 -> 1
    Dense(10, activation='softmax')
])
""")

# ========== DIMENSION CHANGES ==========
print("\n" + "=" * 60)
print("TRACKING DIMENSION CHANGES")
print("=" * 60)

def track_dimensions(input_size, operations):
    """Track how dimensions change through layers"""
    current = input_size
    print(f"Input: {current}")
    
    for op_name, op_func in operations:
        current = op_func(current)
        print(f"After {op_name}: {current}")
    
    return current

# Define operations
def conv_valid(size, kernel=3):
    return size - kernel + 1

def pool(size, pool_size=2):
    return size // pool_size

print("\nDimension Tracking Example:")
print("=" * 40)
print("Input: 28x28")

# Simulate layer by layer
dims = [28]
print(f"Input: {dims[-1]}x{dims[-1]}")

# Conv1 (valid)
dims.append(dims[-1] - 3 + 1)  # 3x3 kernel, valid padding
print(f"Conv2D(32, 3x3, valid): {dims[-1]}x{dims[-1]}")

# Pool1
dims.append(dims[-1] // 2)
print(f"MaxPooling2D(2x2): {dims[-1]}x{dims[-1]}")

# Conv2 (valid)
dims.append(dims[-1] - 3 + 1)
print(f"Conv2D(64, 3x3, valid): {dims[-1]}x{dims[-1]}")

# Pool2
dims.append(dims[-1] // 2)
print(f"MaxPooling2D(2x2): {dims[-1]}x{dims[-1]}")

# Conv3 (valid)
dims.append(dims[-1] - 3 + 1)
print(f"Conv2D(64, 3x3, valid): {dims[-1]}x{dims[-1]}")

print(f"\nFinal feature map size before Flatten: {dims[-1]}x{dims[-1]}x64")
print(f"Flattened: {dims[-1] * dims[-1] * 64} neurons")

# ========== POOLING ALTERNATIVES ==========
print("\n" + "=" * 60)
print("MODERN ALTERNATIVES TO POOLING")
print("=" * 60)

print("""
While pooling is still widely used, there are alternatives:

1. STRIDED CONVOLUTIONS:
   - Conv2D with strides=(2, 2) instead of pooling
   - Learns downsampling instead of fixed operation
   - Used in many modern architectures

2. DILATED CONVOLUTIONS:
   - Increase receptive field without reducing size
   - No downsampling

3. ATTENTION MECHANISMS:
   - Learn which parts are important
   - More flexible than fixed pooling

When to Still Use Pooling:
- Simple classification tasks
- When you want guaranteed translation invariance
- Reducing computation quickly
- Following established architectures (VGG, LeNet)

Modern architectures often use:
Conv2D(strides=2) instead of Conv2D + MaxPool
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("POOLING LAYERS SUMMARY")
print("=" * 60)

print("""
Key Takeaways:
--------------
1. Pooling reduces spatial dimensions (downsampling)
2. Max Pooling: Takes maximum value (most common)
3. Average Pooling: Takes average value
4. Global Pooling: Reduces to single value per channel
5. Typical pool size: 2x2 with stride 2

When to Use Each:
- Max Pooling: Classification, detecting feature presence
- Average Pooling: When all information matters
- Global Average Pooling: Before final Dense layer

Dimension Formula:
output_size = input_size // pool_size
(28, 28) with pool_size=2 -> (14, 14)

Common Pattern:
Conv -> ReLU -> Conv -> ReLU -> Pool -> Conv -> ReLU -> Conv -> ReLU -> Pool -> ...
""")

print("\n" + "=" * 60)
print("✅ Pooling Layers - Complete!")
print("=" * 60)
