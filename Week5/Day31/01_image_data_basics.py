"""
Day 31 - Image Data Basics
==========================
Learn: How images are represented and processed for deep learning

Key Concepts:
- Images as multi-dimensional arrays
- Color channels (RGB vs Grayscale)
- Pixel values and normalization
- Image loading and preprocessing
- Reshaping images for neural networks
"""

import numpy as np

print("=" * 60)
print("IMAGE DATA BASICS")
print("=" * 60)

# ========== IMAGE REPRESENTATION ==========
print("\n" + "=" * 60)
print("IMAGE REPRESENTATION")
print("=" * 60)

print("""
Images in deep learning are represented as multi-dimensional arrays:

1. GRAYSCALE IMAGE:
   - Shape: (height, width) or (height, width, 1)
   - Single channel representing intensity
   - Values: 0 (black) to 255 (white)
   - Example: MNIST digits are 28x28 grayscale

2. COLOR IMAGE (RGB):
   - Shape: (height, width, 3)
   - Three channels: Red, Green, Blue
   - Each channel: 0-255
   - Example: CIFAR-10 images are 32x32x3

3. BATCH OF IMAGES:
   - Shape: (batch_size, height, width, channels)
   - Example: 100 RGB images of 224x224: (100, 224, 224, 3)
""")

# Simulating image data with NumPy
print("\n--- Creating Sample Images with NumPy ---")

# Grayscale image simulation (28x28)
grayscale_img = np.random.randint(0, 256, size=(28, 28), dtype=np.uint8)
print(f"Grayscale image shape: {grayscale_img.shape}")
print(f"Pixel value range: {grayscale_img.min()} - {grayscale_img.max()}")

# RGB image simulation (32x32x3)
rgb_img = np.random.randint(0, 256, size=(32, 32, 3), dtype=np.uint8)
print(f"\nRGB image shape: {rgb_img.shape}")
print(f"Pixel value range: {rgb_img.min()} - {rgb_img.max()}")

# Batch of images (10 images of 28x28x1)
batch_images = np.random.randint(0, 256, size=(10, 28, 28, 1), dtype=np.uint8)
print(f"\nBatch of images shape: {batch_images.shape}")
print(f"First image shape: {batch_images[0].shape}")

# ========== PIXEL VALUES AND NORMALIZATION ==========
print("\n" + "=" * 60)
print("PIXEL VALUES AND NORMALIZATION")
print("=" * 60)

print("""
Why Normalize Pixel Values?
---------------------------
1. Raw pixel values: 0-255 (uint8)
2. Neural networks work better with small values
3. Normalization helps with gradient flow
4. Speeds up training convergence

Common Normalization Methods:
1. Scale to [0, 1]: pixel / 255.0
2. Scale to [-1, 1]: (pixel - 127.5) / 127.5
3. Standardization: (pixel - mean) / std
""")

# Demonstrating normalization
print("\n--- Normalization Examples ---")

# Original values
sample = np.array([0, 64, 128, 192, 255], dtype=np.uint8)
print(f"Original values: {sample}")

# Method 1: Scale to [0, 1]
normalized_01 = sample / 255.0
print(f"Scaled to [0, 1]: {normalized_01}")

# Method 2: Scale to [-1, 1]
normalized_11 = (sample - 127.5) / 127.5
print(f"Scaled to [-1, 1]: {normalized_11}")

# Normalizing an image
print("\n--- Normalizing a Full Image ---")
raw_image = np.random.randint(0, 256, size=(28, 28), dtype=np.uint8)
normalized_image = raw_image.astype(np.float32) / 255.0

print(f"Raw image - dtype: {raw_image.dtype}, range: [{raw_image.min()}, {raw_image.max()}]")
print(f"Normalized - dtype: {normalized_image.dtype}, range: [{normalized_image.min():.3f}, {normalized_image.max():.3f}]")

# ========== RESHAPING FOR NEURAL NETWORKS ==========
print("\n" + "=" * 60)
print("RESHAPING FOR NEURAL NETWORKS")
print("=" * 60)

print("""
CNNs expect input in specific shapes:
-------------------------------------
- TensorFlow/Keras: (batch, height, width, channels) - "channels_last"
- PyTorch: (batch, channels, height, width) - "channels_first"

Common Reshaping Operations:
1. Add batch dimension: expand_dims or reshape
2. Add channel dimension for grayscale
3. Transpose for framework compatibility
""")

print("\n--- Reshaping Examples ---")

# Original grayscale image (28, 28)
grayscale = np.random.rand(28, 28)
print(f"Original grayscale shape: {grayscale.shape}")

# Add channel dimension: (28, 28) -> (28, 28, 1)
with_channel = grayscale.reshape(28, 28, 1)
print(f"With channel dimension: {with_channel.shape}")

# Alternative: using expand_dims
with_channel_v2 = np.expand_dims(grayscale, axis=-1)
print(f"Using expand_dims: {with_channel_v2.shape}")

# Add batch dimension: (28, 28, 1) -> (1, 28, 28, 1)
with_batch = np.expand_dims(with_channel, axis=0)
print(f"With batch dimension: {with_batch.shape}")

# For a batch of images
batch_flat = np.random.rand(100, 784)  # 100 flattened images
batch_reshaped = batch_flat.reshape(100, 28, 28, 1)
print(f"\nFlattened batch: {batch_flat.shape} -> Reshaped: {batch_reshaped.shape}")

# ========== LOADING IMAGES WITH TensorFlow/Keras ==========
print("\n" + "=" * 60)
print("LOADING IMAGES (TensorFlow/Keras)")
print("=" * 60)

print("""
TensorFlow provides utilities for loading images:

from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load image from file
img = load_img('image.jpg', target_size=(224, 224))  # PIL Image
img_array = img_to_array(img)  # Convert to numpy array
img_normalized = img_array / 255.0  # Normalize

# For grayscale:
img = load_img('image.jpg', target_size=(28, 28), color_mode='grayscale')
""")

# Simulating the loading process
print("\n--- Simulated Image Loading ---")

# Simulate a loaded image (224, 224, 3)
loaded_image = np.random.randint(0, 256, size=(224, 224, 3), dtype=np.uint8)
print(f"Loaded image shape: {loaded_image.shape}")
print(f"Loaded image dtype: {loaded_image.dtype}")

# Convert and normalize
img_array = loaded_image.astype(np.float32)
img_normalized = img_array / 255.0
print(f"Normalized shape: {img_normalized.shape}")
print(f"Normalized dtype: {img_normalized.dtype}")
print(f"Normalized range: [{img_normalized.min():.3f}, {img_normalized.max():.3f}]")

# Prepare for model (add batch dimension)
img_ready = np.expand_dims(img_normalized, axis=0)
print(f"Ready for model: {img_ready.shape}")

# ========== WORKING WITH MNIST DATASET ==========
print("\n" + "=" * 60)
print("MNIST DATASET EXAMPLE")
print("=" * 60)

print("""
MNIST is the classic dataset for learning CNNs:
- 60,000 training images
- 10,000 test images
- 28x28 grayscale images
- 10 classes (digits 0-9)

Loading MNIST in Keras:
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
""")

# Simulating MNIST data
print("\n--- Simulated MNIST Data ---")

# Simulate loading MNIST
x_train = np.random.randint(0, 256, size=(60000, 28, 28), dtype=np.uint8)
y_train = np.random.randint(0, 10, size=(60000,), dtype=np.uint8)
x_test = np.random.randint(0, 256, size=(10000, 28, 28), dtype=np.uint8)
y_test = np.random.randint(0, 10, size=(10000,), dtype=np.uint8)

print(f"Training images: {x_train.shape}")
print(f"Training labels: {y_train.shape}")
print(f"Test images: {x_test.shape}")
print(f"Test labels: {y_test.shape}")

# Preprocessing steps
print("\n--- Preprocessing Steps ---")

# Step 1: Normalize
x_train_normalized = x_train.astype(np.float32) / 255.0
x_test_normalized = x_test.astype(np.float32) / 255.0
print(f"After normalization - dtype: {x_train_normalized.dtype}")

# Step 2: Reshape for CNN (add channel dimension)
x_train_final = x_train_normalized.reshape(-1, 28, 28, 1)
x_test_final = x_test_normalized.reshape(-1, 28, 28, 1)
print(f"After reshape: {x_train_final.shape}")

print(f"\nFinal training data shape: {x_train_final.shape}")
print(f"Final test data shape: {x_test_final.shape}")

# ========== IMAGE DATA SUMMARY ==========
print("\n" + "=" * 60)
print("IMAGE DATA SUMMARY")
print("=" * 60)

print("""
Key Points to Remember:
-----------------------
1. Images are multi-dimensional arrays
2. Shape: (batch, height, width, channels) for Keras
3. Always normalize: divide by 255.0 for [0,1] range
4. Add channel dimension for grayscale: (28,28) -> (28,28,1)
5. Add batch dimension for single predictions: (28,28,1) -> (1,28,28,1)

Common Image Sizes:
- MNIST: 28x28x1
- CIFAR-10: 32x32x3
- ImageNet: 224x224x3 (typically)
- Custom: Any size (usually square, power of 2)

Preprocessing Pipeline:
1. Load image
2. Resize to target size
3. Convert to array
4. Normalize (divide by 255)
5. Reshape if needed
6. Ready for model!
""")

print("\n" + "=" * 60)
print("✅ Image Data Basics - Complete!")
print("=" * 60)
