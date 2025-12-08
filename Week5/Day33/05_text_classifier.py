"""
Day 33 - Simple Text Classifier Project
========================================
Build: Complete text classification pipeline

This project demonstrates:
- Text preprocessing
- Tokenization and padding
- Embedding layer usage
- LSTM/GRU model building
- Training and evaluation
- Making predictions on new text
"""

import numpy as np
import re
import string

print("=" * 60)
print("SIMPLE TEXT CLASSIFIER PROJECT")
print("Day 33: NLP & Text Processing")
print("=" * 60)

# ========== STEP 1: IMPORT LIBRARIES ==========
print("\n" + "=" * 60)
print("STEP 1: IMPORTING LIBRARIES")
print("=" * 60)

try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import (
        Embedding, LSTM, Dense, Dropout, 
        Bidirectional, GlobalMaxPooling1D
    )
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.callbacks import EarlyStopping
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, confusion_matrix
    print("✓ All libraries imported successfully!")
    print(f"  TensorFlow version: {tf.__version__}")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Install required packages:")
    print("  pip install tensorflow scikit-learn numpy")
    raise SystemExit()

# ========== STEP 2: PREPARE DATASET ==========
print("\n" + "=" * 60)
print("STEP 2: PREPARING DATASET")
print("=" * 60)

# Sample dataset for text classification
# Categories: Tech, Sports, Entertainment
data = {
    'text': [
        # Technology
        "Apple announces new iPhone with advanced AI features",
        "Google releases new machine learning framework",
        "Microsoft unveils latest cloud computing services",
        "Tesla introduces autonomous driving technology",
        "Amazon launches new artificial intelligence assistant",
        "The new laptop has amazing processing power",
        "Python programming language gains popularity",
        "Cybersecurity threats increase with remote work",
        "New smartphone features revolutionary camera tech",
        "Software engineers are in high demand",
        "Cloud computing transforms business operations",
        "Data science bootcamps attract students",
        "Virtual reality headsets become more affordable",
        "Blockchain technology disrupts financial industry",
        "Tech companies invest in renewable energy",
        
        # Sports
        "Lakers win championship in thrilling final game",
        "Football team prepares for upcoming tournament",
        "Tennis star wins grand slam tournament",
        "Olympic athletes train for summer games",
        "Soccer world cup draws millions of viewers",
        "Basketball player scores career high points",
        "Golf tournament attracts top players",
        "Swimming champion breaks world record",
        "Baseball team signs star player",
        "Hockey playoffs begin this weekend",
        "Marathon runner completes historic race",
        "Cricket team wins series against rivals",
        "Rugby match ends in dramatic victory",
        "Volleyball team qualifies for nationals",
        "Boxing champion defends title successfully",
        
        # Entertainment
        "New blockbuster movie breaks box office records",
        "Famous singer releases highly anticipated album",
        "TV series finale draws record viewership",
        "Celebrity couple announces engagement",
        "Music festival lineup includes top artists",
        "Award show celebrates best performances",
        "Streaming platform releases original content",
        "Concert tour sells out within minutes",
        "Actor wins award for outstanding performance",
        "Director announces new film project",
        "Band reunites for world tour",
        "Comedy special receives rave reviews",
        "Documentary explores fascinating subject",
        "Dance show returns with new season",
        "Podcast becomes most downloaded show"
    ],
    'label': ['tech']*15 + ['sports']*15 + ['entertainment']*15
}

# Create label encoding
label_map = {'tech': 0, 'sports': 1, 'entertainment': 2}
label_names = ['Technology', 'Sports', 'Entertainment']

texts = data['text']
labels = [label_map[l] for l in data['label']]

print(f"✓ Dataset loaded: {len(texts)} samples")
print(f"  Classes: {list(label_map.keys())}")
print(f"  Class distribution: {dict(zip(label_map.keys(), [labels.count(i) for i in range(3)]))}")

# ========== STEP 3: TEXT PREPROCESSING ==========
print("\n" + "=" * 60)
print("STEP 3: TEXT PREPROCESSING")
print("=" * 60)

def preprocess_text(text):
    """Clean and preprocess text"""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Preprocess all texts
processed_texts = [preprocess_text(t) for t in texts]

print("✓ Text preprocessing complete")
print(f"\nExample:")
print(f"  Original:  {texts[0]}")
print(f"  Processed: {processed_texts[0]}")

# ========== STEP 4: TOKENIZATION AND PADDING ==========
print("\n" + "=" * 60)
print("STEP 4: TOKENIZATION AND PADDING")
print("=" * 60)

# Tokenizer parameters
VOCAB_SIZE = 5000
MAX_LENGTH = 20
OOV_TOKEN = "<OOV>"  # Out-of-vocabulary token

# Create and fit tokenizer
tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token=OOV_TOKEN)
tokenizer.fit_on_texts(processed_texts)

# Convert texts to sequences
sequences = tokenizer.texts_to_sequences(processed_texts)

# Pad sequences
X = pad_sequences(sequences, maxlen=MAX_LENGTH, padding='post', truncating='post')
y = np.array(labels)

print(f"✓ Tokenization complete")
print(f"  Vocabulary size: {len(tokenizer.word_index)} words")
print(f"  Max sequence length: {MAX_LENGTH}")
print(f"  X shape: {X.shape}")
print(f"  y shape: {y.shape}")

print(f"\nExample tokenization:")
print(f"  Text: '{processed_texts[0]}'")
print(f"  Sequence: {sequences[0]}")
print(f"  Padded: {X[0]}")

# ========== STEP 5: SPLIT DATA ==========
print("\n" + "=" * 60)
print("STEP 5: SPLITTING DATA")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"✓ Data split complete")
print(f"  Training samples: {len(X_train)}")
print(f"  Testing samples: {len(X_test)}")

# ========== STEP 6: BUILD MODEL ==========
print("\n" + "=" * 60)
print("STEP 6: BUILDING MODEL")
print("=" * 60)

# Model parameters
EMBEDDING_DIM = 64
LSTM_UNITS = 32

# Build the model
model = Sequential([
    # Embedding layer - converts word indices to dense vectors
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=EMBEDDING_DIM,
        input_length=MAX_LENGTH,
        name='embedding'
    ),
    
    # Bidirectional LSTM - processes sequence in both directions
    Bidirectional(LSTM(LSTM_UNITS, dropout=0.2), name='bilstm'),
    
    # Dense layer with dropout for regularization
    Dense(32, activation='relu', name='dense1'),
    Dropout(0.5, name='dropout'),
    
    # Output layer - 3 classes with softmax
    Dense(3, activation='softmax', name='output')
], name='text_classifier')

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("✓ Model built successfully")
model.summary()

# ========== STEP 7: TRAIN MODEL ==========
print("\n" + "=" * 60)
print("STEP 7: TRAINING MODEL")
print("=" * 60)

# Early stopping to prevent overfitting
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

# Train the model
print("Training started...")
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=8,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

print(f"\n✓ Training complete")
print(f"  Final training accuracy: {history.history['accuracy'][-1]:.4f}")
print(f"  Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")

# ========== STEP 8: EVALUATE MODEL ==========
print("\n" + "=" * 60)
print("STEP 8: EVALUATING MODEL")
print("=" * 60)

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.4f}")
print(f"Test Loss: {test_loss:.4f}")

# Get predictions
y_pred_proba = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_pred_proba, axis=1)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_names))

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ========== STEP 9: PREDICTION FUNCTION ==========
print("\n" + "=" * 60)
print("STEP 9: MAKING PREDICTIONS")
print("=" * 60)

def predict_category(text, model, tokenizer, max_length):
    """Predict category for new text"""
    # Preprocess
    processed = preprocess_text(text)
    
    # Tokenize and pad
    seq = tokenizer.texts_to_sequences([processed])
    padded = pad_sequences(seq, maxlen=max_length, padding='post')
    
    # Predict
    pred = model.predict(padded, verbose=0)[0]
    
    # Get predicted class and confidence
    predicted_class = np.argmax(pred)
    confidence = pred[predicted_class]
    
    return {
        'text': text,
        'category': label_names[predicted_class],
        'confidence': float(confidence),
        'probabilities': {name: float(p) for name, p in zip(label_names, pred)}
    }

# Test with new examples
new_texts = [
    "Python becomes most popular programming language",
    "Team wins championship trophy in final match",
    "New movie starring famous actor released today",
    "Scientists develop new quantum computing chip",
    "Tennis player wins tournament after epic match",
    "Music album breaks streaming records worldwide"
]

print("Predictions on new texts:")
print("-" * 60)

for text in new_texts:
    result = predict_category(text, model, tokenizer, MAX_LENGTH)
    print(f"\nText: '{result['text']}'")
    print(f"Category: {result['category']} ({result['confidence']:.2%} confidence)")
    print(f"All probabilities: {result['probabilities']}")

# ========== STEP 10: SAVE MODEL (OPTIONAL) ==========
print("\n" + "=" * 60)
print("STEP 10: SAVING MODEL (OPTIONAL)")
print("=" * 60)

print("""
To save your model for later use:

# Save model
model.save('text_classifier_model.h5')

# Save tokenizer
import pickle
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# Load model later
from tensorflow.keras.models import load_model
loaded_model = load_model('text_classifier_model.h5')

# Load tokenizer
with open('tokenizer.pkl', 'rb') as f:
    loaded_tokenizer = pickle.load(f)
""")

# ========== PROJECT COMPLETE ==========
print("\n" + "=" * 60)
print("✅ TEXT CLASSIFIER PROJECT COMPLETE!")
print("=" * 60)

print("""
What you learned:
1. Text preprocessing (cleaning, lowercasing)
2. Tokenization and sequence padding
3. Building LSTM-based text classifier
4. Training with early stopping
5. Evaluation metrics for classification
6. Making predictions on new text

Next steps to improve:
- Add more training data
- Try different architectures (CNN, Transformer)
- Use pre-trained embeddings (GloVe, Word2Vec)
- Fine-tune hyperparameters
- Add data augmentation
- Try transfer learning with BERT

Keep learning and building! 🚀
""")
