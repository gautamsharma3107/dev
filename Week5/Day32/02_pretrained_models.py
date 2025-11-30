"""
Day 32 - Pre-trained Models
===========================
Learn: Popular pre-trained models and how to use them

Key Concepts:
- ImageNet pre-trained models available in Keras
- Each model has different size/accuracy trade-offs
- Proper preprocessing is essential for each model
"""

# ========== POPULAR PRE-TRAINED MODELS ==========
print("=" * 60)
print("POPULAR PRE-TRAINED MODELS")
print("=" * 60)

models_overview = """
Keras provides many pre-trained models from the ImageNet competition.
All models were trained on 1.2 million images across 1000 categories.

┌───────────────┬────────────┬────────────┬─────────────────────────┐
│ Model         │ Parameters │ Top-5 Acc  │ Best Use Case           │
├───────────────┼────────────┼────────────┼─────────────────────────┤
│ VGG16         │ 138M       │ 92.7%      │ Good baseline           │
│ VGG19         │ 144M       │ 93.0%      │ Slightly better VGG     │
│ ResNet50      │ 25M        │ 92.1%      │ General purpose         │
│ ResNet101     │ 45M        │ 93.5%      │ Higher accuracy         │
│ InceptionV3   │ 24M        │ 93.7%      │ Good accuracy/size      │
│ Xception      │ 23M        │ 94.5%      │ Depthwise separable     │
│ MobileNetV2   │ 3.4M       │ 90.1%      │ Mobile/Edge devices     │
│ EfficientNetB0│ 5.3M       │ 93.3%      │ Best efficiency         │
│ EfficientNetB7│ 66M        │ 96.9%      │ Best accuracy           │
└───────────────┴────────────┴────────────┴─────────────────────────┘

Model Selection Guide:
• Limited compute: MobileNetV2 or EfficientNetB0
• Balance accuracy/speed: ResNet50 or InceptionV3
• Maximum accuracy: EfficientNetB7 or ResNet101
• Learning purposes: VGG16 (simple architecture)
"""
print(models_overview)

# ========== LOADING PRE-TRAINED MODELS ==========
print("\n" + "=" * 60)
print("LOADING PRE-TRAINED MODELS")
print("=" * 60)

try:
    import tensorflow as tf
    from tensorflow.keras import applications
    
    print("\nAvailable pre-trained models in Keras:")
    
    # VGG16
    print("\n1. VGG16 - Classic deep CNN")
    vgg16 = applications.VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    print(f"   Layers: {len(vgg16.layers)}, Params: {vgg16.count_params():,}")
    
    # ResNet50
    print("\n2. ResNet50 - Skip connections, residual learning")
    resnet50 = applications.ResNet50(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    print(f"   Layers: {len(resnet50.layers)}, Params: {resnet50.count_params():,}")
    
    # MobileNetV2
    print("\n3. MobileNetV2 - Lightweight, mobile-friendly")
    mobilenet = applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    print(f"   Layers: {len(mobilenet.layers)}, Params: {mobilenet.count_params():,}")
    
    # InceptionV3
    print("\n4. InceptionV3 - Multi-scale feature extraction")
    inception = applications.InceptionV3(
        weights='imagenet',
        include_top=False,
        input_shape=(299, 299, 3)  # Note: different input size!
    )
    print(f"   Layers: {len(inception.layers)}, Params: {inception.count_params():,}")
    
except ImportError:
    print("TensorFlow not installed. Install with: pip install tensorflow")

# ========== MODEL INPUT REQUIREMENTS ==========
print("\n" + "=" * 60)
print("MODEL INPUT REQUIREMENTS")
print("=" * 60)

input_requirements = """
Different models require different input sizes and preprocessing:

┌───────────────┬─────────────┬──────────────────────────────┐
│ Model         │ Input Size  │ Preprocessing                │
├───────────────┼─────────────┼──────────────────────────────┤
│ VGG16/19      │ 224 x 224   │ BGR, subtract ImageNet mean  │
│ ResNet50/101  │ 224 x 224   │ caffe preprocessing          │
│ InceptionV3   │ 299 x 299   │ Scale to [-1, 1]             │
│ Xception      │ 299 x 299   │ Scale to [-1, 1]             │
│ MobileNetV2   │ 224 x 224   │ Scale to [-1, 1]             │
│ EfficientNet  │ 224-600     │ Model-specific               │
└───────────────┴─────────────┴──────────────────────────────┘

IMPORTANT: Use the correct preprocessing for each model!
"""
print(input_requirements)

# ========== PREPROCESSING EXAMPLES ==========
print("\n" + "=" * 60)
print("PREPROCESSING EXAMPLES")
print("=" * 60)

try:
    from tensorflow.keras.applications import vgg16, resnet50, mobilenet_v2, inception_v3
    import numpy as np
    
    # Create a sample image (random for demonstration)
    sample_image = np.random.rand(1, 224, 224, 3) * 255
    sample_image_inception = np.random.rand(1, 299, 299, 3) * 255
    
    print("\nPreprocessing sample image for different models:")
    
    # VGG16 preprocessing
    vgg_processed = vgg16.preprocess_input(sample_image.copy())
    print(f"\nVGG16 preprocessed - Range: [{vgg_processed.min():.1f}, {vgg_processed.max():.1f}]")
    
    # ResNet50 preprocessing
    resnet_processed = resnet50.preprocess_input(sample_image.copy())
    print(f"ResNet50 preprocessed - Range: [{resnet_processed.min():.1f}, {resnet_processed.max():.1f}]")
    
    # MobileNetV2 preprocessing
    mobilenet_processed = mobilenet_v2.preprocess_input(sample_image.copy())
    print(f"MobileNetV2 preprocessed - Range: [{mobilenet_processed.min():.2f}, {mobilenet_processed.max():.2f}]")
    
    # InceptionV3 preprocessing
    inception_processed = inception_v3.preprocess_input(sample_image_inception.copy())
    print(f"InceptionV3 preprocessed - Range: [{inception_processed.min():.2f}, {inception_processed.max():.2f}]")
    
except Exception as e:
    print(f"Note: {e}")

# ========== FEATURE EXTRACTION WITH PRE-TRAINED MODELS ==========
print("\n" + "=" * 60)
print("FEATURE EXTRACTION WITH PRE-TRAINED MODELS")
print("=" * 60)

try:
    # Using MobileNetV2 for feature extraction
    print("\nUsing MobileNetV2 for feature extraction:")
    
    # Load model
    base_model = applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # Create a random sample image
    sample = np.random.rand(1, 224, 224, 3)
    sample = mobilenet_v2.preprocess_input(sample * 255)
    
    # Extract features
    features = base_model.predict(sample, verbose=0)
    print(f"Input shape: {sample.shape}")
    print(f"Output features shape: {features.shape}")
    print(f"Feature dimensions: {np.prod(features.shape[1:])}")
    
    # With Global Average Pooling
    from tensorflow.keras.layers import GlobalAveragePooling2D
    from tensorflow.keras.models import Model
    
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    feature_extractor = Model(inputs=base_model.input, outputs=x)
    
    features_pooled = feature_extractor.predict(sample, verbose=0)
    print(f"\nWith GlobalAveragePooling:")
    print(f"Pooled features shape: {features_pooled.shape}")
    
except Exception as e:
    print(f"Note: {e}")

# ========== USING MODELS FOR CLASSIFICATION ==========
print("\n" + "=" * 60)
print("USING PRE-TRAINED MODELS FOR CLASSIFICATION")
print("=" * 60)

try:
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
    
    # Load model WITH top (classifier)
    print("\nLoading MobileNetV2 with classifier (1000 ImageNet classes)...")
    model = MobileNetV2(weights='imagenet', include_top=True)
    
    # Create a sample image (in practice, load a real image)
    sample = np.random.rand(224, 224, 3) * 255
    sample = np.expand_dims(sample, axis=0)
    sample = preprocess_input(sample)
    
    # Make prediction
    predictions = model.predict(sample, verbose=0)
    print(f"Prediction shape: {predictions.shape}")
    print(f"Sum of probabilities: {predictions.sum():.4f}")
    
    # Decode predictions
    decoded = decode_predictions(predictions, top=3)[0]
    print("\nTop 3 predictions (for random image):")
    for i, (imagenet_id, label, score) in enumerate(decoded):
        print(f"  {i+1}. {label}: {score:.4f}")
    
    print("\nNote: Random image gives random predictions!")
    
except Exception as e:
    print(f"Note: {e}")

# ========== CUSTOM CLASSIFICATION HEAD ==========
print("\n" + "=" * 60)
print("ADDING CUSTOM CLASSIFICATION HEAD")
print("=" * 60)

try:
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
    from tensorflow.keras.models import Model
    
    # Load base model without top
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # Freeze base model
    base_model.trainable = False
    
    # Add custom classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.3)(x)
    outputs = Dense(5, activation='softmax')(x)  # 5 custom classes
    
    # Create final model
    model = Model(inputs=base_model.input, outputs=outputs)
    
    # Compile
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Custom classification model created!")
    print(f"\nArchitecture:")
    print(f"  Base model: MobileNetV2 (frozen)")
    print(f"  GlobalAveragePooling2D")
    print(f"  Dense(512, relu)")
    print(f"  Dropout(0.5)")
    print(f"  Dense(256, relu)")
    print(f"  Dropout(0.3)")
    print(f"  Dense(5, softmax) - 5 custom classes")
    
    # Show trainable parameters
    trainable_count = sum([tf.size(w).numpy() for w in model.trainable_weights])
    total_count = model.count_params()
    
    print(f"\nParameters:")
    print(f"  Trainable: {trainable_count:,}")
    print(f"  Non-trainable: {total_count - trainable_count:,}")
    print(f"  Total: {total_count:,}")
    
except Exception as e:
    print(f"Note: {e}")

# ========== CHOOSING THE RIGHT MODEL ==========
print("\n" + "=" * 60)
print("CHOOSING THE RIGHT MODEL")
print("=" * 60)

choosing_guide = """
Decision Flowchart:

1. What's your deployment target?
   ├── Mobile/Edge device → MobileNetV2 or EfficientNetB0
   ├── Cloud/Server → ResNet50 or EfficientNetB4
   └── Research/Best accuracy → EfficientNetB7

2. How much training data do you have?
   ├── < 1000 samples → Smaller models (MobileNetV2)
   ├── 1000-10000 samples → Medium models (ResNet50)
   └── > 10000 samples → Larger models OK

3. What's your inference time budget?
   ├── < 10ms → MobileNetV2, EfficientNetB0
   ├── 10-50ms → ResNet50, InceptionV3
   └── > 50ms OK → Larger models

4. Learning or production?
   ├── Learning → VGG16 (simple architecture)
   └── Production → EfficientNet (best efficiency)

My Recommendations:
• Start with: MobileNetV2 (good balance, fast)
• Default choice: ResNet50 (reliable, well-studied)
• Best accuracy: EfficientNetB4 or higher
• Mobile deployment: MobileNetV2 or EfficientNetB0
"""
print(choosing_guide)

print("\n" + "=" * 60)
print("✅ Pre-trained Models - Complete!")
print("=" * 60)
