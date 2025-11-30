"""
Day 35 - Model Training Pipeline
=================================
Learn: Complete training pipeline for CNN image classification

Key Concepts:
- Loading and preprocessing datasets
- Data augmentation for better generalization
- Training with validation
- Monitoring training progress
- Saving trained models
"""

import numpy as np
import os

# TensorFlow import with fallback
try:
    import tensorflow as tf
    from tensorflow import keras
    from keras import layers
    from keras.preprocessing.image import ImageDataGenerator
    TF_AVAILABLE = True
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    TF_AVAILABLE = False
    print("TensorFlow not installed. Install with: pip install tensorflow")

# ========== LOADING CIFAR-10 DATASET ==========
print("=" * 60)
print("LOADING CIFAR-10 DATASET")
print("=" * 60)

print("""
CIFAR-10 Dataset:
- 60,000 32x32 color images
- 10 classes: airplane, automobile, bird, cat, deer, 
              dog, frog, horse, ship, truck
- 50,000 training + 10,000 test images
- 6,000 images per class
""")

# Class names for CIFAR-10
CIFAR10_CLASSES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

if TF_AVAILABLE:
    # Load CIFAR-10
    print("\nLoading CIFAR-10 dataset...")
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
    
    print(f"Training data shape: {x_train.shape}")
    print(f"Training labels shape: {y_train.shape}")
    print(f"Test data shape: {x_test.shape}")
    print(f"Test labels shape: {y_test.shape}")
    
    # Display sample images info
    print(f"\nImage dimensions: {x_train[0].shape}")
    print(f"Pixel value range: {x_train.min()} - {x_train.max()}")
    
else:
    print("\nDataset loading skipped (TensorFlow not available)")
    print("CIFAR-10 shapes would be:")
    print("- Training: (50000, 32, 32, 3)")
    print("- Test: (10000, 32, 32, 3)")

# ========== DATA PREPROCESSING ==========
print("\n" + "=" * 60)
print("DATA PREPROCESSING")
print("=" * 60)

print("""
Preprocessing Steps:
1. Normalize pixel values to [0, 1]
2. Split training data for validation
3. (Optional) One-hot encode labels
""")

if TF_AVAILABLE:
    # Normalize pixel values
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    print(f"After normalization: {x_train.min():.2f} - {x_train.max():.2f}")
    
    # Create validation split
    val_split = 0.1
    val_size = int(len(x_train) * val_split)
    
    x_val = x_train[:val_size]
    y_val = y_train[:val_size]
    x_train = x_train[val_size:]
    y_train = y_train[val_size:]
    
    print(f"\nAfter validation split:")
    print(f"Training samples: {len(x_train)}")
    print(f"Validation samples: {len(x_val)}")
    print(f"Test samples: {len(x_test)}")

# ========== DATA AUGMENTATION ==========
print("\n" + "=" * 60)
print("DATA AUGMENTATION")
print("=" * 60)

print("""
Data Augmentation Techniques:
- Rotation: Rotate images randomly
- Width/Height Shift: Move images
- Horizontal Flip: Mirror images
- Zoom: Slight zoom in/out
- Shear: Slant transformation

Benefits:
- Increases effective dataset size
- Reduces overfitting
- Improves model generalization
""")

if TF_AVAILABLE:
    # Create data augmentation generator
    datagen = ImageDataGenerator(
        rotation_range=15,          # Random rotation up to 15 degrees
        width_shift_range=0.1,      # Horizontal shift up to 10%
        height_shift_range=0.1,     # Vertical shift up to 10%
        horizontal_flip=True,       # Random horizontal flip
        zoom_range=0.1,             # Random zoom up to 10%
        fill_mode='nearest'         # Fill missing pixels
    )
    
    print("Data augmentation generator created!")
    print("\nAugmentation settings:")
    print("- Rotation: ±15°")
    print("- Shift: ±10%")
    print("- Horizontal flip: Yes")
    print("- Zoom: ±10%")

# ========== BUILD THE MODEL ==========
print("\n" + "=" * 60)
print("BUILD THE MODEL")
print("=" * 60)

if TF_AVAILABLE:
    def create_cnn_model():
        """Create a CNN model for CIFAR-10"""
        model = keras.Sequential([
            # Block 1
            layers.Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)),
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
            layers.Dense(10, activation='softmax')
        ])
        
        return model
    
    # Create and compile model
    model = create_cnn_model()
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Model created and compiled!")
    print(f"Total parameters: {model.count_params():,}")

# ========== TRAINING CALLBACKS ==========
print("\n" + "=" * 60)
print("TRAINING CALLBACKS")
print("=" * 60)

print("""
Useful Callbacks:
1. EarlyStopping: Stop when no improvement
2. ModelCheckpoint: Save best model
3. ReduceLROnPlateau: Reduce learning rate when stuck
4. TensorBoard: Visualize training
""")

if TF_AVAILABLE:
    # Create callbacks
    callbacks = [
        # Stop training if validation loss doesn't improve
        keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True,
            verbose=1
        ),
        
        # Save the best model
        keras.callbacks.ModelCheckpoint(
            'best_model.keras',
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        ),
        
        # Reduce learning rate when stuck
        keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=3,
            min_lr=1e-6,
            verbose=1
        )
    ]
    
    print("Callbacks configured:")
    print("- EarlyStopping (patience=5)")
    print("- ModelCheckpoint (save best)")
    print("- ReduceLROnPlateau (factor=0.5)")

# ========== TRAINING THE MODEL ==========
print("\n" + "=" * 60)
print("TRAINING THE MODEL")
print("=" * 60)

print("""
Training Configuration:
- Epochs: 20 (with early stopping)
- Batch size: 64
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy
""")

if TF_AVAILABLE:
    # Training parameters
    EPOCHS = 3  # Reduced for demonstration
    BATCH_SIZE = 64
    
    print(f"\nStarting training for {EPOCHS} epochs (demo mode)...")
    print("(Increase EPOCHS to 20+ for better accuracy)\n")
    
    # Train with data augmentation
    history = model.fit(
        datagen.flow(x_train, y_train, batch_size=BATCH_SIZE),
        epochs=EPOCHS,
        validation_data=(x_val, y_val),
        callbacks=callbacks,
        verbose=1
    )
    
    print("\n✅ Training complete!")

# ========== TRAINING HISTORY ANALYSIS ==========
print("\n" + "=" * 60)
print("TRAINING HISTORY ANALYSIS")
print("=" * 60)

if TF_AVAILABLE:
    # Print training history
    print("\nTraining History:")
    for epoch in range(len(history.history['loss'])):
        print(f"Epoch {epoch+1}:")
        print(f"  Loss: {history.history['loss'][epoch]:.4f}")
        print(f"  Accuracy: {history.history['accuracy'][epoch]:.4f}")
        print(f"  Val Loss: {history.history['val_loss'][epoch]:.4f}")
        print(f"  Val Accuracy: {history.history['val_accuracy'][epoch]:.4f}")
    
    # Plot training history (text-based)
    print("\nAccuracy Progress:")
    for i, acc in enumerate(history.history['accuracy']):
        bar = "█" * int(acc * 50)
        print(f"Epoch {i+1}: {bar} {acc:.2%}")

# ========== MODEL EVALUATION ==========
print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

if TF_AVAILABLE:
    # Evaluate on test set
    print("\nEvaluating on test set...")
    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    
    print(f"\nTest Results:")
    print(f"Loss: {test_loss:.4f}")
    print(f"Accuracy: {test_accuracy:.4f} ({test_accuracy:.2%})")
    
    # Make predictions on sample
    print("\nSample Predictions:")
    predictions = model.predict(x_test[:5], verbose=0)
    
    for i in range(5):
        pred_class = np.argmax(predictions[i])
        true_class = y_test[i][0]
        confidence = predictions[i][pred_class]
        
        status = "✅" if pred_class == true_class else "❌"
        print(f"{status} Image {i+1}: Predicted={CIFAR10_CLASSES[pred_class]} "
              f"({confidence:.2%}), Actual={CIFAR10_CLASSES[true_class]}")

# ========== SAVING THE MODEL ==========
print("\n" + "=" * 60)
print("SAVING THE MODEL")
print("=" * 60)

print("""
Model Saving Options:
1. Full model (architecture + weights + optimizer)
   model.save('model.keras')
   
2. Weights only
   model.save_weights('weights.h5')
   
3. TensorFlow SavedModel format
   model.save('saved_model/')
""")

if TF_AVAILABLE:
    # Save the model
    model_path = 'cifar10_cnn_model.keras'
    model.save(model_path)
    print(f"\n✅ Model saved to '{model_path}'")
    
    # Check file size
    if os.path.exists(model_path):
        size_mb = os.path.getsize(model_path) / (1024 * 1024)
        print(f"Model file size: {size_mb:.2f} MB")
    
    # Demonstrate loading
    print("\nLoading model back...")
    loaded_model = keras.models.load_model(model_path)
    print("✅ Model loaded successfully!")
    
    # Verify loaded model
    loaded_loss, loaded_acc = loaded_model.evaluate(x_test[:100], y_test[:100], verbose=0)
    print(f"Loaded model accuracy (100 samples): {loaded_acc:.2%}")
    
    # Cleanup
    if os.path.exists(model_path):
        os.remove(model_path)
    if os.path.exists('best_model.keras'):
        os.remove('best_model.keras')
    print("\n✅ Cleaned up model files")

# ========== TRAINING TIPS ==========
print("\n" + "=" * 60)
print("TRAINING TIPS")
print("=" * 60)

print("""
Tips for Better Training:

1. LEARNING RATE:
   - Start with 0.001 (Adam default)
   - Use ReduceLROnPlateau callback
   - Try learning rate schedules

2. BATCH SIZE:
   - Larger = faster but needs more memory
   - Typical values: 32, 64, 128
   - Smaller can help generalization

3. EPOCHS:
   - Use early stopping
   - Monitor validation loss
   - 20-50 epochs typically enough

4. DATA AUGMENTATION:
   - Always use for image data
   - Don't augment validation/test data
   - Experiment with different transforms

5. REGULARIZATION:
   - Dropout (0.25-0.5 typically)
   - L2 regularization on Dense layers
   - Batch normalization

6. ARCHITECTURE:
   - Start simple, add complexity
   - Use proven architectures (VGG, ResNet)
   - Transfer learning often better
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Training Pipeline Checklist:
✅ Load and preprocess data
✅ Normalize pixel values to [0, 1]
✅ Create validation split
✅ Apply data augmentation
✅ Build and compile model
✅ Configure callbacks
✅ Train with validation monitoring
✅ Evaluate on test set
✅ Save the trained model

Next: Use the model for inference!
""")

print("\n" + "=" * 60)
print("✅ Model Training Pipeline - Complete!")
print("=" * 60)
