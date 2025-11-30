# Day 32 Quick Reference Cheat Sheet

## Transfer Learning Basics
```python
import tensorflow as tf
from tensorflow.keras.applications import VGG16, ResNet50, MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Load pre-trained model WITHOUT top layer
base_model = VGG16(
    weights='imagenet',      # Pre-trained weights
    include_top=False,       # Remove classifier
    input_shape=(224, 224, 3)
)
```

## Feature Extraction (Freeze All Layers)
```python
# Freeze all layers in base model
base_model.trainable = False

# Add custom classifier
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

## Fine-Tuning (Unfreeze Some Layers)
```python
# Unfreeze the top layers for fine-tuning
base_model.trainable = True

# Freeze all layers except last N
for layer in base_model.layers[:-10]:
    layer.trainable = False

# Use lower learning rate for fine-tuning
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

## Pre-trained Models Comparison
```python
# VGG16 - Good baseline, large model
base = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# ResNet50 - Skip connections, good performance
base = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# MobileNetV2 - Lightweight, good for mobile
base = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# EfficientNetB0 - Best accuracy/efficiency ratio
from tensorflow.keras.applications import EfficientNetB0
base = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
```

## Data Augmentation
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create augmentation generator
train_datagen = ImageDataGenerator(
    rescale=1./255,           # Normalize pixel values
    rotation_range=20,        # Random rotation
    width_shift_range=0.2,    # Horizontal shift
    height_shift_range=0.2,   # Vertical shift
    horizontal_flip=True,     # Random flip
    zoom_range=0.2,           # Random zoom
    shear_range=0.2,          # Shear transformation
    fill_mode='nearest'       # Fill mode for new pixels
)

# For validation - only rescale
val_datagen = ImageDataGenerator(rescale=1./255)

# Load data from directory
train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
```

## Keras Preprocessing Layers (Modern Approach)
```python
from tensorflow.keras import layers

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2),
    layers.RandomContrast(0.2),
])

# Apply in model
model = tf.keras.Sequential([
    data_augmentation,
    layers.Rescaling(1./255),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])
```

## Complete Transfer Learning Pipeline
```python
# 1. Load and prepare data
train_ds = tf.keras.utils.image_dataset_from_directory(
    'data/train',
    image_size=(224, 224),
    batch_size=32
)

# 2. Load pre-trained model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

# 3. Build model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# 4. Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_ds, epochs=10, validation_data=val_ds)

# 5. Fine-tune (optional)
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_ds, epochs=5, validation_data=val_ds)
```

## Callbacks for Training
```python
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras',
        monitor='val_accuracy',
        save_best_only=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.2,
        patience=2
    )
]

model.fit(train_ds, epochs=20, validation_data=val_ds, callbacks=callbacks)
```

## Save and Load Models
```python
# Save entire model
model.save('my_model.keras')

# Load model
loaded_model = tf.keras.models.load_model('my_model.keras')

# Save only weights
model.save_weights('model_weights.weights.h5')

# Load weights
model.load_weights('model_weights.weights.h5')
```

## Quick Tips
```python
# Check layer names
for i, layer in enumerate(base_model.layers):
    print(f"{i}: {layer.name}, trainable: {layer.trainable}")

# Check model summary
model.summary()

# Preprocessing for specific models
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg_preprocess
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as mobilenet_preprocess
```

---
**Keep this handy for quick reference!** 🚀
