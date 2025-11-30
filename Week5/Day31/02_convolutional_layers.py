"""
Day 31 - Convolutional Layers Explained
=======================================
Learn: How convolutional layers work and why they're essential for image processing

Key Concepts:
- Convolution operation
- Filters/Kernels
- Feature maps
- Stride and padding
- Parameter sharing
"""

import numpy as np

print("=" * 60)
print("CONVOLUTIONAL LAYERS EXPLAINED")
print("=" * 60)

# ========== WHAT IS CONVOLUTION? ==========
print("\n" + "=" * 60)
print("WHAT IS CONVOLUTION?")
print("=" * 60)

print("""
Convolution is a mathematical operation that slides a small matrix
(called a kernel or filter) over an image to extract features.

Why Use Convolution for Images?
-------------------------------
1. LOCAL CONNECTIVITY: Each neuron only looks at a small region
2. PARAMETER SHARING: Same filter used across entire image
3. TRANSLATION INVARIANCE: Detects patterns anywhere in image
4. FEATURE HIERARCHY: Low-level to high-level features

Traditional Neural Network vs CNN:
- Dense layer on 28x28 image: 28*28*neurons = huge parameters
- Conv layer with 3x3 filter: only 3*3*channels + bias = few parameters
""")

# ========== FILTERS/KERNELS ==========
print("\n" + "=" * 60)
print("FILTERS/KERNELS")
print("=" * 60)

print("""
A filter (kernel) is a small matrix that detects specific patterns:

Common Filter Sizes:
- 3x3: Most common, captures fine details
- 5x5: Larger receptive field
- 7x7: Often used in first layer for larger patterns
- 1x1: Dimensionality reduction, channel mixing

Example 3x3 Filters:
""")

# Edge detection filters
vertical_edge = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

horizontal_edge = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

sharpen = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

blur = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

print("Vertical Edge Filter:")
print(vertical_edge)
print("\nHorizontal Edge Filter:")
print(horizontal_edge)
print("\nSharpen Filter:")
print(sharpen)
print("\nBlur Filter:")
print(blur.round(3))

# ========== CONVOLUTION OPERATION ==========
print("\n" + "=" * 60)
print("CONVOLUTION OPERATION")
print("=" * 60)

def convolve2d_demo(image, kernel):
    """
    Simple 2D convolution demonstration.
    In practice, use tensorflow.keras.layers.Conv2D
    """
    img_h, img_w = image.shape
    k_h, k_w = kernel.shape
    
    # Output size (valid padding)
    out_h = img_h - k_h + 1
    out_w = img_w - k_w + 1
    
    output = np.zeros((out_h, out_w))
    
    for i in range(out_h):
        for j in range(out_w):
            # Extract region and apply filter
            region = image[i:i+k_h, j:j+k_w]
            output[i, j] = np.sum(region * kernel)
    
    return output

# Create a simple 5x5 image
sample_image = np.array([
    [10, 20, 30, 40, 50],
    [15, 25, 35, 45, 55],
    [20, 30, 40, 50, 60],
    [25, 35, 45, 55, 65],
    [30, 40, 50, 60, 70]
], dtype=np.float32)

# Simple averaging filter
avg_filter = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

print("Input Image (5x5):")
print(sample_image)
print(f"\nFilter (3x3):")
print(avg_filter.round(3))

# Apply convolution
output = convolve2d_demo(sample_image, avg_filter)
print(f"\nOutput Feature Map (3x3):")
print(output.round(2))

print("""
How Convolution Works:
----------------------
1. Place filter at top-left of image
2. Element-wise multiply filter with image region
3. Sum all products to get single output value
4. Slide filter to next position
5. Repeat until entire image is covered
""")

# ========== STRIDE ==========
print("\n" + "=" * 60)
print("STRIDE")
print("=" * 60)

print("""
Stride = How many pixels the filter moves each step

Stride = 1: Filter moves 1 pixel at a time (most common)
Stride = 2: Filter moves 2 pixels, output size is halved
Stride = 3: Filter moves 3 pixels, further reduces size

Output Size Formula (no padding):
output_size = (input_size - kernel_size) / stride + 1

Examples with 7x7 input, 3x3 kernel:
- Stride 1: (7-3)/1 + 1 = 5x5 output
- Stride 2: (7-3)/2 + 1 = 3x3 output
""")

def calculate_output_size(input_size, kernel_size, stride=1, padding=0):
    """Calculate output size after convolution"""
    return int((input_size - kernel_size + 2*padding) / stride + 1)

# Examples
print("\nOutput Size Calculations:")
print(f"Input: 28, Kernel: 3, Stride: 1 -> Output: {calculate_output_size(28, 3, 1)}")
print(f"Input: 28, Kernel: 3, Stride: 2 -> Output: {calculate_output_size(28, 3, 2)}")
print(f"Input: 28, Kernel: 5, Stride: 1 -> Output: {calculate_output_size(28, 5, 1)}")
print(f"Input: 28, Kernel: 5, Stride: 2 -> Output: {calculate_output_size(28, 5, 2)}")

# ========== PADDING ==========
print("\n" + "=" * 60)
print("PADDING")
print("=" * 60)

print("""
Padding = Adding pixels around the image border

Types of Padding:
1. VALID (no padding): Output is smaller than input
2. SAME: Pad so output size = input size (with stride=1)
3. FULL: Maximum padding

Why Use Padding?
----------------
1. Preserve spatial dimensions
2. Don't lose edge information
3. Allow deeper networks without shrinking too fast

Zero Padding Example (padding=1 for 3x3 kernel):
Original 4x4 -> Padded 6x6 -> Convolution -> Output 4x4
""")

# Demonstrate padding
def add_zero_padding(image, padding):
    """Add zero padding around image"""
    h, w = image.shape
    padded = np.zeros((h + 2*padding, w + 2*padding))
    padded[padding:padding+h, padding:padding+w] = image
    return padded

small_img = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=np.float32)

print("Original (3x3):")
print(small_img)

padded_img = add_zero_padding(small_img, padding=1)
print("\nWith Zero Padding (5x5):")
print(padded_img)

# Calculate sizes with different padding
print("\nOutput Sizes with Different Padding (28x28 input, 3x3 kernel, stride=1):")
print(f"Valid (padding=0): {calculate_output_size(28, 3, 1, 0)}x{calculate_output_size(28, 3, 1, 0)}")
print(f"Same (padding=1):  {calculate_output_size(28, 3, 1, 1)}x{calculate_output_size(28, 3, 1, 1)}")

# ========== MULTIPLE FILTERS ==========
print("\n" + "=" * 60)
print("MULTIPLE FILTERS (OUTPUT CHANNELS)")
print("=" * 60)

print("""
In CNNs, we use MULTIPLE filters to detect different features:

Conv2D(32, (3, 3)) means:
- 32 different 3x3 filters
- Each filter produces one output channel
- Input: (28, 28, 1) -> Output: (26, 26, 32)

Each filter learns to detect different patterns:
- Filter 1: Horizontal edges
- Filter 2: Vertical edges
- Filter 3: Corners
- Filter 4: Textures
- ... and so on

The network learns these filters during training!
""")

# Demonstrate multi-channel output
print("\nMulti-Filter Example:")
print("Input shape: (28, 28, 1)")
print("Conv2D with 32 filters of size 3x3:")
print("Output shape: (26, 26, 32)")
print("\nEach of the 32 filters produces a (26, 26) feature map")

# ========== MULTI-CHANNEL INPUT ==========
print("\n" + "=" * 60)
print("MULTI-CHANNEL INPUT (RGB IMAGES)")
print("=" * 60)

print("""
For RGB images (3 channels), each filter is also 3D:

Input: (height, width, 3) - RGB image
Filter: (kernel_h, kernel_w, 3) - One filter for all channels

How it works:
1. Filter has separate 2D kernel for each input channel
2. Convolve each kernel with corresponding channel
3. Sum all results to get single output value
4. Add bias

Example:
- Input: (32, 32, 3) - RGB image
- Filter: (3, 3, 3) - 3x3 filter, depth 3
- One filter produces: (30, 30) output
- 64 filters produce: (30, 30, 64) output
""")

# Parameter count
def count_conv_params(filters, kernel_size, input_channels, use_bias=True):
    """Count parameters in a Conv2D layer"""
    weights = filters * kernel_size[0] * kernel_size[1] * input_channels
    biases = filters if use_bias else 0
    return weights + biases

print("\nParameter Count Examples:")
print(f"Conv2D(32, (3,3)) on (28,28,1): {count_conv_params(32, (3,3), 1)} parameters")
print(f"Conv2D(64, (3,3)) on (28,28,32): {count_conv_params(64, (3,3), 32)} parameters")
print(f"Conv2D(128, (3,3)) on (32,32,3): {count_conv_params(128, (3,3), 3)} parameters")

# ========== CONV2D IN KERAS ==========
print("\n" + "=" * 60)
print("CONV2D IN KERAS")
print("=" * 60)

print("""
Using Conv2D in TensorFlow/Keras:

from tensorflow.keras.layers import Conv2D

# Basic usage
conv_layer = Conv2D(
    filters=32,              # Number of output channels
    kernel_size=(3, 3),      # Filter size
    strides=(1, 1),          # Step size (default: 1)
    padding='valid',         # 'valid' or 'same'
    activation='relu',       # Activation function
    input_shape=(28, 28, 1)  # Only for first layer
)

# Common configurations:
Conv2D(32, (3, 3), activation='relu', padding='same')
Conv2D(64, (3, 3), activation='relu', padding='valid')
Conv2D(128, (5, 5), strides=(2, 2), activation='relu')
""")

# ========== FEATURE MAPS VISUALIZATION ==========
print("\n" + "=" * 60)
print("UNDERSTANDING FEATURE MAPS")
print("=" * 60)

print("""
Feature Maps = Output of Convolutional Layers

Early Layers (close to input):
- Detect low-level features
- Edges, colors, textures
- Easy to interpret visually

Middle Layers:
- Detect mid-level features
- Shapes, patterns, parts of objects
- Combinations of low-level features

Later Layers (close to output):
- Detect high-level features
- Object parts, entire objects
- Abstract, harder to interpret

Example Feature Hierarchy (Face Recognition):
Layer 1: Edges, color gradients
Layer 2: Eyes, noses, mouths (parts)
Layer 3: Faces, poses
Layer 4: Specific identities
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("CONVOLUTIONAL LAYERS SUMMARY")
print("=" * 60)

print("""
Key Takeaways:
--------------
1. Convolution slides a filter over an image to extract features
2. Filters are learned during training (not hand-crafted)
3. Multiple filters = multiple feature maps
4. Stride controls how much the filter moves
5. Padding controls output size

Best Practices:
- Start with 3x3 kernels (most efficient)
- Use padding='same' to preserve dimensions
- Double filters when spatial size halves
- Common pattern: 32 -> 64 -> 128 filters

Formula:
output_size = (input_size - kernel_size + 2*padding) / stride + 1
""")

print("\n" + "=" * 60)
print("✅ Convolutional Layers - Complete!")
print("=" * 60)
