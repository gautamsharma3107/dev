"""
Day 32 - Fine-Tuning Pre-trained Models
=======================================
Learn: How to fine-tune pre-trained models for better performance

Key Concepts:
- Fine-tuning unfreezes some layers for training
- Use low learning rates to avoid destroying pre-trained weights
- Gradual unfreezing prevents catastrophic forgetting
"""

# ========== WHAT IS FINE-TUNING? ==========
print("=" * 60)
print("WHAT IS FINE-TUNING?")
print("=" * 60)

intro = """
Fine-tuning is a transfer learning technique where we:
1. Start with pre-trained weights
2. Unfreeze some (or all) layers
3. Train with a very low learning rate

This allows the model to adapt its learned features to your
specific dataset while preserving general knowledge.

Feature Extraction vs Fine-Tuning:
┌─────────────────────┬─────────────────────────┐
│ Feature Extraction  │ Fine-Tuning             │
├─────────────────────┼─────────────────────────┤
│ Freeze ALL layers   │ Unfreeze SOME layers    │
│ Train only new head │ Train unfrozen + head   │
│ Fast training       │ Slower training         │
│ Less risk overfitting│ More risk overfitting  │
│ Best for small data │ Better for more data    │
└─────────────────────┴─────────────────────────┘
"""
print(intro)

# ========== FINE-TUNING STRATEGIES ==========
print("\n" + "=" * 60)
print("FINE-TUNING STRATEGIES")
print("=" * 60)

strategies = """
Three main approaches to fine-tuning:

1. FEATURE EXTRACTION ONLY (No fine-tuning)
   - Freeze entire base model
   - Only train the new classification head
   - Best for: Very small datasets, similar domains
   
2. FINE-TUNE TOP LAYERS
   - Freeze early layers (low-level features)
   - Unfreeze and train later layers
   - Best for: Medium datasets, somewhat different domain

3. FINE-TUNE ALL LAYERS
   - Unfreeze entire model
   - Train everything with very low learning rate
   - Best for: Large datasets, different domain

Which layers to fine-tune?
• Early layers: Learn generic features (edges, colors)
  → Usually keep frozen
• Later layers: Learn task-specific features
  → Unfreeze these for fine-tuning
"""
print(strategies)

# ========== TWO-PHASE TRAINING APPROACH ==========
print("\n" + "=" * 60)
print("TWO-PHASE TRAINING APPROACH")
print("=" * 60)

two_phase = """
Recommended approach for best results:

PHASE 1: Feature Extraction
├── Freeze entire base model
├── Train only the new classification head
├── Use normal learning rate (e.g., 0.001)
├── Train until convergence (5-10 epochs)
└── Goal: Learn good classifier weights

PHASE 2: Fine-Tuning
├── Unfreeze top layers of base model
├── Use very low learning rate (e.g., 0.00001)
├── Train for a few more epochs
└── Goal: Adapt features to your data

Why two phases?
• Phase 1 learns a good classifier first
• Phase 2 can then fine-tune without random gradient noise
• Prevents destroying pre-trained weights early in training
"""
print(two_phase)

# ========== IMPLEMENTATION ==========
print("\n" + "=" * 60)
print("FINE-TUNING IMPLEMENTATION")
print("=" * 60)

try:
    import tensorflow as tf
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
    from tensorflow.keras.models import Model
    from tensorflow.keras.optimizers import Adam
    
    # Load base model
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    print(f"Base model: MobileNetV2")
    print(f"Total layers: {len(base_model.layers)}")
    
    # ===== PHASE 1: Feature Extraction =====
    print("\n--- PHASE 1: Feature Extraction ---")
    
    # Freeze all layers
    base_model.trainable = False
    
    # Add classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    outputs = Dense(10, activation='softmax')(x)  # 10 classes
    
    model = Model(inputs=base_model.input, outputs=outputs)
    
    # Compile with normal learning rate
    model.compile(
        optimizer=Adam(learning_rate=1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    trainable_phase1 = sum([tf.size(w).numpy() for w in model.trainable_weights])
    print(f"Trainable parameters: {trainable_phase1:,}")
    print(f"Learning rate: 0.001")
    print("Ready for Phase 1 training!")
    
    # ===== PHASE 2: Fine-Tuning =====
    print("\n--- PHASE 2: Fine-Tuning ---")
    
    # Unfreeze base model
    base_model.trainable = True
    
    # Freeze early layers, unfreeze later layers
    fine_tune_at = 100  # Unfreeze layers after this index
    
    for layer in base_model.layers[:fine_tune_at]:
        layer.trainable = False
    
    # Recompile with lower learning rate
    model.compile(
        optimizer=Adam(learning_rate=1e-5),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    trainable_phase2 = sum([tf.size(w).numpy() for w in model.trainable_weights])
    print(f"Frozen layers: {fine_tune_at}")
    print(f"Unfrozen layers: {len(base_model.layers) - fine_tune_at}")
    print(f"Trainable parameters: {trainable_phase2:,}")
    print(f"Learning rate: 0.00001 (10x lower)")
    print("Ready for Phase 2 training!")
    
except ImportError:
    print("TensorFlow not installed. Install with: pip install tensorflow")

# ========== VIEWING LAYER STRUCTURE ==========
print("\n" + "=" * 60)
print("VIEWING AND MODIFYING LAYERS")
print("=" * 60)

try:
    # Show layer structure
    print("\nMobileNetV2 layer structure (first 20 and last 10):")
    print("-" * 50)
    
    for i, layer in enumerate(base_model.layers[:10]):
        status = "🔓" if layer.trainable else "🔒"
        print(f"{i:3d}. {status} {layer.name[:30]:<30}")
    
    print("... (more layers)")
    
    for i, layer in enumerate(base_model.layers[-10:], start=len(base_model.layers)-10):
        status = "🔓" if layer.trainable else "🔒"
        print(f"{i:3d}. {status} {layer.name[:30]:<30}")
    
    print("\n🔒 = Frozen (not trainable)")
    print("🔓 = Unfrozen (trainable)")
    
except Exception as e:
    print(f"Note: {e}")

# ========== LEARNING RATE IMPORTANCE ==========
print("\n" + "=" * 60)
print("LEARNING RATE FOR FINE-TUNING")
print("=" * 60)

learning_rate_info = """
Learning rate is CRITICAL for fine-tuning!

Too high learning rate → Destroys pre-trained weights
Too low learning rate → Learning is too slow

Recommended learning rates:
┌───────────────────────┬──────────────────┐
│ Phase                 │ Learning Rate    │
├───────────────────────┼──────────────────┤
│ Feature extraction    │ 1e-3 to 1e-4     │
│ Fine-tuning           │ 1e-5 to 1e-6     │
└───────────────────────┴──────────────────┘

Learning Rate Scheduling:
• Start with slightly higher rate
• Reduce as training progresses
• Use ReduceLROnPlateau callback

Example:
```python
from tensorflow.keras.callbacks import ReduceLROnPlateau

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.2,        # Reduce by 5x
    patience=2,        # Wait 2 epochs
    min_lr=1e-7        # Minimum learning rate
)
```
"""
print(learning_rate_info)

# ========== COMPLETE FINE-TUNING EXAMPLE ==========
print("\n" + "=" * 60)
print("COMPLETE FINE-TUNING EXAMPLE")
print("=" * 60)

complete_example = """
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# 1. Load pre-trained model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# 2. Add classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
outputs = Dense(num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=outputs)

# ===== PHASE 1: Feature Extraction =====
base_model.trainable = False

model.compile(
    optimizer=Adam(learning_rate=1e-3),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ReduceLROnPlateau(factor=0.2, patience=2)
]

# Train Phase 1
history1 = model.fit(
    train_data,
    epochs=10,
    validation_data=val_data,
    callbacks=callbacks
)

# ===== PHASE 2: Fine-Tuning =====
base_model.trainable = True

# Freeze early layers
for layer in base_model.layers[:-50]:
    layer.trainable = False

# Lower learning rate
model.compile(
    optimizer=Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train Phase 2
history2 = model.fit(
    train_data,
    epochs=10,
    validation_data=val_data,
    callbacks=callbacks
)

# Save fine-tuned model
model.save('fine_tuned_model.keras')
"""
print(complete_example)

# ========== FINE-TUNING TIPS ==========
print("\n" + "=" * 60)
print("FINE-TUNING TIPS AND BEST PRACTICES")
print("=" * 60)

tips = """
✅ DO:
• Start with feature extraction, then fine-tune
• Use very low learning rate for fine-tuning (10-100x lower)
• Use BatchNormalization carefully (keep in inference mode)
• Monitor validation loss to detect overfitting
• Use early stopping and model checkpointing
• Unfreeze layers gradually from top to bottom

❌ DON'T:
• Fine-tune with high learning rate
• Fine-tune all layers with very small dataset
• Skip the feature extraction phase
• Forget to recompile after unfreezing layers
• Ignore BatchNorm layer behavior

BatchNormalization Warning:
When fine-tuning, BatchNorm layers should typically stay frozen
to prevent them from updating their statistics:

```python
# Option 1: Keep base model frozen when unfreezing
for layer in base_model.layers:
    if isinstance(layer, tf.keras.layers.BatchNormalization):
        layer.trainable = False
```

Regularization:
• Use Dropout in classification head
• Consider L2 regularization for dense layers
• Data augmentation helps prevent overfitting
"""
print(tips)

# ========== MONITORING TRAINING ==========
print("\n" + "=" * 60)
print("MONITORING FINE-TUNING PROGRESS")
print("=" * 60)

monitoring = """
Key metrics to watch during fine-tuning:

1. Training vs Validation Loss
   • Should decrease together
   • Large gap = overfitting
   
2. Training vs Validation Accuracy
   • Should increase together
   • Val accuracy plateaus first

3. Learning Rate
   • Should decrease over time
   • Use ReduceLROnPlateau

Callbacks for monitoring:

```python
callbacks = [
    # Stop if no improvement
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    
    # Save best model
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras',
        monitor='val_accuracy',
        save_best_only=True
    ),
    
    # Reduce learning rate
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.2,
        patience=3,
        min_lr=1e-7
    ),
    
    # Log to TensorBoard
    tf.keras.callbacks.TensorBoard(
        log_dir='./logs'
    )
]
```
"""
print(monitoring)

print("\n" + "=" * 60)
print("✅ Fine-Tuning - Complete!")
print("=" * 60)
