"""
Day 32 - Transfer Learning Basics
=================================
Learn: What is transfer learning and why it's powerful

Key Concepts:
- Transfer learning reuses knowledge from one task to another
- Pre-trained models provide excellent feature extraction
- Much less data and compute required vs training from scratch
"""

# ========== WHAT IS TRANSFER LEARNING? ==========
print("=" * 60)
print("WHAT IS TRANSFER LEARNING?")
print("=" * 60)

intro = """
Transfer Learning is a machine learning technique where a model
trained on one task is reused as the starting point for a model
on a different but related task.

Example: A model trained to recognize cats and dogs can be
adapted to recognize different breeds of cats with minimal
additional training.

Key Benefits:
1. Less Data Required - Leverage knowledge from large datasets
2. Faster Training - Pre-trained weights give you a head start
3. Better Performance - Features learned transfer well
4. Resource Efficient - No need for expensive GPU clusters
"""
print(intro)

# ========== HOW IT WORKS ==========
print("\n" + "=" * 60)
print("HOW TRANSFER LEARNING WORKS")
print("=" * 60)

how_it_works = """
Neural networks learn in a hierarchical manner:

Layer 1-2: Low-level features (edges, colors, textures)
    - These features are universal and transfer well

Layer 3-4: Mid-level features (shapes, patterns)
    - These are more task-specific but still transferable

Layer 5+: High-level features (specific objects, concepts)
    - These are task-specific and usually need retraining

Transfer Learning Strategy:
1. Take a pre-trained model (trained on ImageNet with 1M+ images)
2. Remove the final classification layer
3. Add new layers for your specific task
4. Train only the new layers (feature extraction) OR
5. Train the whole model with low learning rate (fine-tuning)
"""
print(how_it_works)

# ========== TRANSFER LEARNING IN CODE ==========
print("\n" + "=" * 60)
print("TRANSFER LEARNING IN CODE")
print("=" * 60)

try:
    import tensorflow as tf
    from tensorflow.keras.applications import VGG16
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
    from tensorflow.keras.models import Model
    
    print("\nLoading VGG16 pre-trained on ImageNet...")
    
    # Load VGG16 without the top classification layer
    base_model = VGG16(
        weights='imagenet',      # Use pre-trained ImageNet weights
        include_top=False,       # Remove the classifier layer
        input_shape=(224, 224, 3)
    )
    
    print(f"Base model loaded!")
    print(f"Number of layers: {len(base_model.layers)}")
    print(f"Total parameters: {base_model.count_params():,}")
    
    # Show the model structure
    print("\n--- VGG16 Architecture (without top) ---")
    for i, layer in enumerate(base_model.layers[:5]):  # Show first 5 layers
        print(f"Layer {i}: {layer.name} - Output shape: {layer.output_shape}")
    print("... (more layers)")
    
except ImportError:
    print("TensorFlow not installed. Install with: pip install tensorflow")
    print("\nExample code structure:")
    print("""
    from tensorflow.keras.applications import VGG16
    
    base_model = VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    """)

# ========== TYPES OF TRANSFER LEARNING ==========
print("\n" + "=" * 60)
print("TYPES OF TRANSFER LEARNING")
print("=" * 60)

types = """
1. FEATURE EXTRACTION (Most Common)
   - Freeze all pre-trained layers
   - Add new classifier layers on top
   - Train only the new layers
   - Best when: Little data, similar domain to pre-trained model

2. FINE-TUNING
   - Unfreeze some (or all) pre-trained layers
   - Train with very low learning rate
   - Best when: More data available, want to adapt features

3. DOMAIN ADAPTATION
   - Handle shift between source and target domains
   - More advanced techniques
   - Best when: Source and target domains differ significantly

Strategy Selection Guide:
┌─────────────────────────┬──────────────────────────┐
│ Your Data Amount        │ Recommended Strategy     │
├─────────────────────────┼──────────────────────────┤
│ Very Small (<1000)      │ Feature Extraction Only  │
│ Small (1000-10000)      │ Feature Extraction +     │
│                         │ Fine-tune last few layers│
│ Medium (10000-100000)   │ Fine-tune more layers    │
│ Large (>100000)         │ Fine-tune all or train   │
│                         │ from scratch             │
└─────────────────────────┴──────────────────────────┘
"""
print(types)

# ========== BUILDING A TRANSFER LEARNING MODEL ==========
print("\n" + "=" * 60)
print("BUILDING A TRANSFER LEARNING MODEL")
print("=" * 60)

try:
    # Step 1: Load base model
    base_model = VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # Step 2: Freeze base model layers
    base_model.trainable = False
    
    # Step 3: Add custom classification layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)  # Reduce dimensions
    x = Dense(256, activation='relu')(x)  # Hidden layer
    x = Dropout(0.5)(x)  # Prevent overfitting
    predictions = Dense(10, activation='softmax')(x)  # 10 classes
    
    # Step 4: Create the final model
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Step 5: Compile the model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Show model summary
    print("Transfer Learning Model Built Successfully!")
    print("\n--- Model Architecture ---")
    print(f"Base model layers: {len(base_model.layers)} (frozen)")
    print(f"Total model layers: {len(model.layers)}")
    
    # Count trainable vs non-trainable parameters
    trainable_params = sum([tf.size(w).numpy() for w in model.trainable_weights])
    non_trainable_params = sum([tf.size(w).numpy() for w in model.non_trainable_weights])
    
    print(f"\nTrainable parameters: {trainable_params:,}")
    print(f"Non-trainable parameters: {non_trainable_params:,}")
    print(f"Total parameters: {model.count_params():,}")
    
except Exception as e:
    print(f"Note: {e}")
    print("\nConceptual code structure:")
    print("""
    # Freeze base model
    base_model.trainable = False
    
    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    """)

# ========== WHEN TO USE TRANSFER LEARNING ==========
print("\n" + "=" * 60)
print("WHEN TO USE TRANSFER LEARNING")
print("=" * 60)

when_to_use = """
✅ USE Transfer Learning When:
   - You have limited training data
   - Your task is similar to what the model was trained on
   - You need faster development time
   - You lack computational resources
   - You want state-of-the-art performance quickly

❌ DON'T USE Transfer Learning When:
   - Your data is very different from pre-trained model's domain
   - You have massive amounts of data (millions of samples)
   - You need highly specialized features
   - The pre-trained model is much larger than needed

Common Use Cases:
• Medical imaging (X-rays, MRI scans)
• Satellite imagery analysis
• Product image classification
• Face recognition
• Document classification
• Style transfer
"""
print(when_to_use)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: DOG VS CAT CLASSIFIER")
print("=" * 60)

practical_example = """
# Complete Transfer Learning Pipeline

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1. Load pre-trained MobileNetV2 (lightweight, fast)
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# 2. Freeze base model
base_model.trainable = False

# 3. Build model
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(2, activation='softmax')  # 2 classes: dog, cat
])

# 4. Compile
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Prepare data with augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# 6. Train
model.fit(train_generator, epochs=10)

# 7. Save
model.save('cat_dog_classifier.keras')
"""
print(practical_example)

print("\n" + "=" * 60)
print("✅ Transfer Learning Basics - Complete!")
print("=" * 60)
