"""
Day 30 - TensorFlow/Keras Setup
================================
Learn: TensorFlow installation, verification, and basics

Key Concepts:
- TensorFlow is Google's open-source ML framework
- Keras is integrated into TensorFlow as tf.keras
- TensorFlow 2.x uses eager execution by default
- GPU support is automatic if CUDA is installed
"""

# ========== INSTALLATION ==========
print("=" * 60)
print("TENSORFLOW/KERAS SETUP")
print("=" * 60)

# First, let's try to import TensorFlow
try:
    import tensorflow as tf
    print(f"✅ TensorFlow version: {tf.__version__}")
except ImportError:
    print("❌ TensorFlow not installed!")
    print("Run: pip install tensorflow")
    exit(1)

# Check Keras (included in TensorFlow 2.x)
print(f"✅ Keras version: {tf.keras.__version__}")

# ========== GPU CHECK ==========
print("\n" + "=" * 60)
print("GPU AVAILABILITY")
print("=" * 60)

# Check for GPU support
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"✅ GPU(s) available: {len(gpus)}")
    for gpu in gpus:
        print(f"   - {gpu.name}")
else:
    print("ℹ️  No GPU found - using CPU (slower but works fine for learning)")

# ========== BASIC TENSORFLOW INFO ==========
print("\n" + "=" * 60)
print("TENSORFLOW BASICS")
print("=" * 60)

# TensorFlow uses eager execution by default
print(f"Eager execution: {tf.executing_eagerly()}")

# Simple operation to verify
a = tf.constant(5)
b = tf.constant(3)
result = tf.add(a, b)
print(f"\nSimple operation: 5 + 3 = {result.numpy()}")

# ========== TENSORFLOW VS KERAS ==========
print("\n" + "=" * 60)
print("TENSORFLOW VS KERAS")
print("=" * 60)

print("""
TensorFlow: Low-level ML library
- More control and flexibility
- Tensors, operations, gradients
- Used for research and custom implementations

Keras (tf.keras): High-level API
- User-friendly interface
- Pre-built layers and models
- Perfect for beginners and rapid prototyping
- Recommended for most use cases

For this bootcamp, we'll use tf.keras (Keras within TensorFlow)
""")

# ========== IMPORT CONVENTIONS ==========
print("=" * 60)
print("COMMON IMPORTS")
print("=" * 60)

print("""
# Standard imports for deep learning with TensorFlow/Keras:

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Data handling
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
""")

# ========== VERIFY IMPORTS ==========
print("=" * 60)
print("VERIFYING IMPORTS")
print("=" * 60)

# Import commonly used modules
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("✅ keras imported")
print("✅ layers imported")
print("✅ Sequential imported")
print("✅ Dense imported")

# NumPy check
try:
    import numpy as np
    print(f"✅ NumPy version: {np.__version__}")
except ImportError:
    print("⚠️  NumPy not installed (recommended: pip install numpy)")

# ========== QUICK DEMO ==========
print("\n" + "=" * 60)
print("QUICK DEMO: SIMPLE MODEL")
print("=" * 60)

# Create a simple model to verify everything works
model = Sequential([
    Dense(10, activation='relu', input_shape=(5,)),
    Dense(1)
])

print("Model created successfully!")
print(f"Model layers: {len(model.layers)}")
model.summary()

# ========== TROUBLESHOOTING ==========
print("\n" + "=" * 60)
print("TROUBLESHOOTING TIPS")
print("=" * 60)

print("""
Common Issues:

1. ModuleNotFoundError: No module named 'tensorflow'
   → Run: pip install tensorflow

2. Slow performance:
   → Normal on CPU - GPU recommended for large models
   → For learning, CPU is sufficient

3. Version conflicts:
   → Create virtual environment: python -m venv tf_env
   → Activate and install fresh: pip install tensorflow

4. GPU not detected:
   → Install CUDA toolkit and cuDNN
   → Check compatibility with your TensorFlow version

5. Memory errors:
   → Reduce batch size
   → Use tf.data.Dataset for large data
""")

print("\n" + "=" * 60)
print("✅ TensorFlow/Keras Setup - Complete!")
print("=" * 60)
print("\nNext: Learn about tensors in 02_tensors_basics.py")
