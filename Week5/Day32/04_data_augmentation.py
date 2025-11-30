"""
Day 32 - Data Augmentation
==========================
Learn: Techniques to artificially expand training data

Key Concepts:
- Data augmentation creates variations of existing images
- Helps prevent overfitting with limited data
- Essential for transfer learning success
"""

# ========== WHAT IS DATA AUGMENTATION? ==========
print("=" * 60)
print("WHAT IS DATA AUGMENTATION?")
print("=" * 60)

intro = """
Data Augmentation artificially expands your training dataset by
creating modified versions of existing images through various
transformations.

Why use Data Augmentation?
1. Increases effective training data size
2. Reduces overfitting
3. Makes model more robust to variations
4. Essential when you have limited data

Common Image Augmentations:
• Rotation          • Brightness changes
• Horizontal flip   • Contrast changes
• Vertical flip     • Crop and resize
• Zoom             • Noise injection
• Shear            • Color jitter
• Translation      • Cutout/Random erasing
"""
print(intro)

# ========== KERAS IMAGE DATA GENERATOR ==========
print("\n" + "=" * 60)
print("KERAS IMAGEDATAGENERATOR (Classic Approach)")
print("=" * 60)

try:
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    import numpy as np
    
    print("\nCreating augmentation pipeline with ImageDataGenerator:")
    
    # Define augmentation parameters
    train_datagen = ImageDataGenerator(
        rescale=1./255,           # Normalize pixel values to [0, 1]
        rotation_range=30,        # Random rotation up to 30 degrees
        width_shift_range=0.2,    # Horizontal shift up to 20%
        height_shift_range=0.2,   # Vertical shift up to 20%
        shear_range=0.2,          # Shear transformation
        zoom_range=0.2,           # Random zoom in/out
        horizontal_flip=True,     # Random horizontal flip
        vertical_flip=False,      # Don't flip vertically (for faces, animals)
        fill_mode='nearest',      # How to fill new pixels
        brightness_range=[0.8, 1.2]  # Random brightness
    )
    
    print("Augmentation parameters:")
    print(f"  Rescale: 1/255 (normalize to [0,1])")
    print(f"  Rotation: ±30 degrees")
    print(f"  Width/Height shift: ±20%")
    print(f"  Shear: 0.2")
    print(f"  Zoom: ±20%")
    print(f"  Horizontal flip: Yes")
    print(f"  Brightness: 0.8x to 1.2x")
    
    # For validation - only rescale, no augmentation!
    val_datagen = ImageDataGenerator(rescale=1./255)
    
    print("\nValidation data: Only rescaling (no augmentation)")
    
except ImportError:
    print("TensorFlow not installed. Install with: pip install tensorflow")

# ========== USING DATA GENERATOR ==========
print("\n" + "=" * 60)
print("USING DATA GENERATOR WITH DIRECTORIES")
print("=" * 60)

data_generator_usage = """
Directory structure for flow_from_directory:
data/
├── train/
│   ├── cats/
│   │   ├── cat001.jpg
│   │   └── cat002.jpg
│   └── dogs/
│       ├── dog001.jpg
│       └── dog002.jpg
└── validation/
    ├── cats/
    │   └── cat101.jpg
    └── dogs/
        └── dog101.jpg

Code to load data:
```python
train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(224, 224),    # Resize images
    batch_size=32,             # Images per batch
    class_mode='categorical',  # One-hot encoded labels
    shuffle=True               # Shuffle data
)

val_generator = val_datagen.flow_from_directory(
    'data/validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False  # Don't shuffle validation
)

# Training
model.fit(
    train_generator,
    epochs=10,
    validation_data=val_generator
)
```
"""
print(data_generator_usage)

# ========== KERAS PREPROCESSING LAYERS (MODERN) ==========
print("\n" + "=" * 60)
print("KERAS PREPROCESSING LAYERS (Modern Approach)")
print("=" * 60)

try:
    import tensorflow as tf
    from tensorflow.keras import layers
    
    print("\nCreating augmentation with Keras preprocessing layers:")
    
    # Create augmentation model
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),           # Random horizontal flip
        layers.RandomRotation(0.1),                # Random rotation ±10%
        layers.RandomZoom(0.2),                    # Random zoom ±20%
        layers.RandomContrast(0.2),                # Random contrast
        layers.RandomBrightness(0.2),              # Random brightness
        layers.RandomTranslation(0.1, 0.1),        # Random shift
    ])
    
    print("Augmentation layers created:")
    for layer in data_augmentation.layers:
        print(f"  - {layer.name}")
    
    # Apply to sample image
    sample_image = tf.random.uniform((224, 224, 3))
    sample_batch = tf.expand_dims(sample_image, 0)
    
    augmented = data_augmentation(sample_batch, training=True)
    print(f"\nInput shape: {sample_batch.shape}")
    print(f"Output shape: {augmented.shape}")
    
except Exception as e:
    print(f"Note: {e}")

# ========== INTEGRATING AUGMENTATION IN MODEL ==========
print("\n" + "=" * 60)
print("INTEGRATING AUGMENTATION IN MODEL")
print("=" * 60)

try:
    from tensorflow.keras.applications import MobileNetV2
    
    # Create augmentation layer
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.2),
    ])
    
    # Load pre-trained model
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    base_model.trainable = False
    
    # Build model WITH augmentation
    model = tf.keras.Sequential([
        # Input
        layers.Input(shape=(224, 224, 3)),
        
        # Augmentation (only during training)
        data_augmentation,
        
        # Preprocessing
        layers.Rescaling(1./127.5, offset=-1),  # Scale to [-1, 1] for MobileNetV2
        
        # Pre-trained base
        base_model,
        
        # Classification head
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax')
    ])
    
    print("Model with integrated augmentation created!")
    print("\nModel architecture:")
    for layer in model.layers:
        print(f"  - {layer.name}")
    
    print("\nNote: Augmentation is ONLY applied during training!")
    
except Exception as e:
    print(f"Note: {e}")

# ========== AUGMENTATION TECHNIQUES EXPLAINED ==========
print("\n" + "=" * 60)
print("AUGMENTATION TECHNIQUES EXPLAINED")
print("=" * 60)

techniques = """
1. GEOMETRIC TRANSFORMATIONS

   RandomFlip("horizontal")
   • Flips image left-right
   • Good for: Most natural images
   • Bad for: Text, directional objects
   
   RandomRotation(0.1)
   • Rotates image by random angle
   • Range: -0.1*360° to +0.1*360° = ±36°
   • Good for: Natural scenes, objects
   • Bad for: Face detection, OCR
   
   RandomZoom(0.2)
   • Zooms in/out by up to 20%
   • Simulates distance variation
   
   RandomTranslation(0.1, 0.1)
   • Shifts image horizontally/vertically
   • Simulates different positions

2. COLOR/INTENSITY TRANSFORMATIONS

   RandomBrightness(0.2)
   • Changes brightness by ±20%
   • Simulates lighting conditions
   
   RandomContrast(0.2)
   • Changes contrast by ±20%
   • Helps with varied lighting
   
   RandomSaturation(lower, upper)
   • Changes color saturation
   • Simulates color variations

3. ADVANCED AUGMENTATIONS

   CutOut / RandomErasing
   • Randomly removes rectangular regions
   • Forces model to look at all parts
   
   MixUp
   • Blends two images together
   • Labels also blended proportionally
   
   CutMix
   • Replaces region with patch from another image
   • Combines benefits of CutOut and MixUp
"""
print(techniques)

# ========== CHOOSING AUGMENTATION STRATEGIES ==========
print("\n" + "=" * 60)
print("CHOOSING AUGMENTATION STRATEGIES")
print("=" * 60)

choosing = """
Task-Specific Recommendations:

GENERAL IMAGE CLASSIFICATION
• Horizontal flip ✓
• Rotation (small) ✓
• Zoom ✓
• Brightness/Contrast ✓

MEDICAL IMAGING (X-rays, MRI)
• Rotation ✓
• Zoom ✓
• Horizontal/Vertical flip (carefully!)
• Brightness/Contrast ✓
• No: Excessive color changes

SATELLITE/AERIAL IMAGERY
• Rotation (any angle) ✓
• Flip (both directions) ✓
• Zoom ✓
• No: Excessive shear

FACE DETECTION/RECOGNITION
• Small rotation only
• Brightness/Contrast ✓
• No: Horizontal flip (asymmetric features)
• No: Large rotations

TEXT/DOCUMENT IMAGES
• Small rotation ✓
• Brightness/Contrast ✓
• Scale variations ✓
• No: Flip
• No: Large rotations

How much augmentation?
• More data → Less augmentation needed
• Less data → More augmentation helps
• Start conservative, increase if overfitting
"""
print(choosing)

# ========== COMPLETE AUGMENTATION EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE AUGMENTATION EXAMPLE")
print("=" * 60)

complete_example = """
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2

# Define augmentation
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
    layers.RandomBrightness(0.1),
])

# Load and prepare data
train_ds = tf.keras.utils.image_dataset_from_directory(
    'data/train',
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical'
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    'data/validation',
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical'
)

# Optimize data pipeline
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

# Load pre-trained model
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
base_model.trainable = False

# Build complete model
model = tf.keras.Sequential([
    # Augmentation (training only)
    data_augmentation,
    
    # Preprocessing for MobileNetV2
    layers.Rescaling(1./127.5, offset=-1),
    
    # Pre-trained base
    base_model,
    
    # Classification head
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

# Compile and train
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_ds,
    epochs=20,
    validation_data=val_ds
)
"""
print(complete_example)

# ========== VISUALIZING AUGMENTATIONS ==========
print("\n" + "=" * 60)
print("VISUALIZING AUGMENTATIONS")
print("=" * 60)

visualizing = """
Always visualize augmentations to ensure they make sense!

```python
import matplotlib.pyplot as plt

# Create sample augmented images
def visualize_augmentation(image, augmentation_layer, num_samples=9):
    plt.figure(figsize=(10, 10))
    
    for i in range(num_samples):
        ax = plt.subplot(3, 3, i + 1)
        augmented = augmentation_layer(tf.expand_dims(image, 0))
        plt.imshow(augmented[0].numpy().astype("uint8"))
        plt.axis("off")
    
    plt.suptitle("Augmented Versions of Same Image")
    plt.show()

# Load a sample image
sample_image = tf.keras.utils.load_img("sample.jpg", target_size=(224, 224))
sample_image = tf.keras.utils.img_to_array(sample_image)

# Visualize
visualize_augmentation(sample_image, data_augmentation)
```

This helps you:
• Verify augmentations are reasonable
• Ensure images still look like valid samples
• Adjust parameters if needed
"""
print(visualizing)

# ========== TIPS FOR AUGMENTATION ==========
print("\n" + "=" * 60)
print("TIPS FOR DATA AUGMENTATION")
print("=" * 60)

tips = """
✅ DO:
• Always augment training data only, NOT validation/test
• Visualize augmentations before training
• Start with conservative augmentation, increase if needed
• Use task-appropriate augmentations
• Combine multiple augmentation techniques
• Use augmentation layers inside model (faster)

❌ DON'T:
• Apply same augmentation to validation data
• Over-augment (creates unrealistic images)
• Use flip for asymmetric objects
• Use heavy rotation for oriented objects
• Forget to normalize pixel values

Performance Tips:
• Use tf.data pipeline with prefetch
• Apply augmentation as model layer (GPU accelerated)
• Cache data if it fits in memory
• Use mixed precision training for speed

```python
# Efficient data pipeline
train_ds = train_ds.cache()
train_ds = train_ds.shuffle(1000)
train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
```
"""
print(tips)

print("\n" + "=" * 60)
print("✅ Data Augmentation - Complete!")
print("=" * 60)
