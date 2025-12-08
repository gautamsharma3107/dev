"""
Day 33 - Word Embeddings
========================
Learn: Word embedding concepts and usage

Key Concepts:
- Word embeddings represent words as dense vectors
- Similar words have similar vector representations
- Pre-trained embeddings: Word2Vec, GloVe, FastText
- Embedding layer in neural networks learns task-specific embeddings
"""

import numpy as np

# ========== WHAT ARE WORD EMBEDDINGS? ==========
print("=" * 60)
print("WHAT ARE WORD EMBEDDINGS?")
print("=" * 60)

print("""
Word embeddings are a type of word representation that allows words 
with similar meaning to have similar vector representations.

Traditional one-hot encoding:
- "cat" = [1, 0, 0, 0, 0, ...]  (very sparse, high dimensional)
- "dog" = [0, 1, 0, 0, 0, ...]  (no relationship between words)

Word embeddings:
- "cat" = [0.2, -0.4, 0.7, 0.1, ...]  (dense, low dimensional)
- "dog" = [0.1, -0.3, 0.8, 0.2, ...]  (similar vectors for similar words!)

Key benefits:
1. Capture semantic relationships
2. Lower dimensionality (50-300 vs vocabulary size)
3. Pre-trained embeddings transfer knowledge
4. Enable arithmetic: king - man + woman ≈ queen
""")

# ========== SIMPLE EMBEDDING EXAMPLE ==========
print("\n" + "=" * 60)
print("SIMPLE EMBEDDING EXAMPLE")
print("=" * 60)

# Simulated simple embeddings (in reality, these are learned)
simple_embeddings = {
    "king": np.array([0.9, 0.7, 0.3]),
    "queen": np.array([0.8, 0.8, 0.3]),
    "man": np.array([0.9, 0.2, 0.5]),
    "woman": np.array([0.8, 0.3, 0.5]),
    "prince": np.array([0.85, 0.6, 0.35]),
    "princess": np.array([0.75, 0.65, 0.35]),
}

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

print("Cosine similarities:")
print(f"  king ↔ queen:  {cosine_similarity(simple_embeddings['king'], simple_embeddings['queen']):.4f}")
print(f"  king ↔ man:    {cosine_similarity(simple_embeddings['king'], simple_embeddings['man']):.4f}")
print(f"  king ↔ woman:  {cosine_similarity(simple_embeddings['king'], simple_embeddings['woman']):.4f}")
print(f"  man ↔ woman:   {cosine_similarity(simple_embeddings['man'], simple_embeddings['woman']):.4f}")

# Vector arithmetic: king - man + woman ≈ queen
result = simple_embeddings["king"] - simple_embeddings["man"] + simple_embeddings["woman"]
print(f"\nVector arithmetic: king - man + woman")
print(f"  Result vector: {result}")
print(f"  Queen vector:  {simple_embeddings['queen']}")
print(f"  Similarity to queen: {cosine_similarity(result, simple_embeddings['queen']):.4f}")

# ========== KERAS EMBEDDING LAYER ==========
print("\n" + "=" * 60)
print("KERAS EMBEDDING LAYER")
print("=" * 60)

try:
    from tensorflow.keras.layers import Embedding
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    
    # Sample vocabulary
    texts = ["I love machine learning", "Deep learning is amazing", "NLP is fun"]
    
    # Tokenize
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)
    vocab_size = len(tokenizer.word_index) + 1  # +1 for padding token
    
    print(f"Vocabulary size: {vocab_size}")
    print(f"Word index: {tokenizer.word_index}")
    
    # Create embedding layer
    embedding_dim = 8  # Each word represented as 8-dimensional vector
    
    model = Sequential([
        Embedding(input_dim=vocab_size, 
                  output_dim=embedding_dim, 
                  input_length=5,
                  name='embedding_layer')
    ])
    
    model.summary()
    
    # Process sample text
    sample_text = ["I love learning"]
    sequences = tokenizer.texts_to_sequences(sample_text)
    padded = pad_sequences(sequences, maxlen=5, padding='post')
    
    print(f"\nSample text: {sample_text}")
    print(f"Sequence: {padded}")
    
    # Get embeddings
    embeddings = model.predict(padded, verbose=0)
    print(f"Embedding shape: {embeddings.shape}")
    print(f"First word embedding: {embeddings[0][0]}")
    
except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")

# ========== USING EMBEDDING IN NLP MODEL ==========
print("\n" + "=" * 60)
print("USING EMBEDDING IN NLP MODEL")
print("=" * 60)

try:
    from tensorflow.keras.layers import Embedding, Dense, Flatten, LSTM
    from tensorflow.keras.models import Sequential
    
    # Example model with embedding for text classification
    vocab_size = 10000
    embedding_dim = 128
    max_length = 100
    
    # Simple model with Embedding + Dense
    model_simple = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ], name="simple_embedding_model")
    
    print("Simple Model (Embedding + Dense):")
    model_simple.summary()
    
    # Model with Embedding + LSTM
    model_lstm = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        LSTM(64),
        Dense(1, activation='sigmoid')
    ], name="lstm_embedding_model")
    
    print("\nLSTM Model (Embedding + LSTM):")
    model_lstm.summary()
    
except ImportError:
    print("TensorFlow not installed.")

# ========== PRE-TRAINED EMBEDDINGS CONCEPT ==========
print("\n" + "=" * 60)
print("PRE-TRAINED EMBEDDINGS CONCEPT")
print("=" * 60)

print("""
Popular Pre-trained Embeddings:

1. Word2Vec (Google, 2013)
   - Skip-gram and CBOW architectures
   - Trained on Google News (100 billion words)
   - 300 dimensions, 3 million words
   
2. GloVe (Stanford, 2014)
   - Global Vectors for Word Representation
   - Trained on Wikipedia + Gigaword
   - Available in 50, 100, 200, 300 dimensions
   
3. FastText (Facebook, 2016)
   - Handles out-of-vocabulary words
   - Uses subword information
   - Available for 157 languages

How to use pre-trained embeddings:

1. Download pre-trained vectors (e.g., GloVe)
2. Create embedding matrix for your vocabulary
3. Initialize Embedding layer with pre-trained weights
4. Optionally freeze or fine-tune
""")

# ========== LOADING PRE-TRAINED EMBEDDINGS (CONCEPT) ==========
print("\n" + "=" * 60)
print("LOADING PRE-TRAINED EMBEDDINGS (CODE EXAMPLE)")
print("=" * 60)

print("""
# Example code to load GloVe embeddings (you need to download the file first)
# Download from: https://nlp.stanford.edu/projects/glove/

def load_glove_embeddings(glove_file, word_index, embedding_dim=100):
    '''
    Load GloVe embeddings and create embedding matrix
    
    Args:
        glove_file: Path to GloVe file (e.g., 'glove.6B.100d.txt')
        word_index: Dictionary mapping words to indices
        embedding_dim: Dimension of embeddings
    
    Returns:
        embedding_matrix: NumPy array of shape (vocab_size, embedding_dim)
    '''
    # Load GloVe vectors
    embeddings_index = {}
    with open(glove_file, encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    
    print(f'Loaded {len(embeddings_index)} word vectors.')
    
    # Create embedding matrix
    vocab_size = len(word_index) + 1
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    
    for word, i in word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector
    
    return embedding_matrix

# Usage:
# embedding_matrix = load_glove_embeddings('glove.6B.100d.txt', tokenizer.word_index)
# 
# model = Sequential([
#     Embedding(vocab_size, 100, 
#               weights=[embedding_matrix],
#               input_length=max_len,
#               trainable=False),  # Freeze pre-trained weights
#     LSTM(64),
#     Dense(1, activation='sigmoid')
# ])
""")

# ========== VISUALIZING EMBEDDINGS ==========
print("\n" + "=" * 60)
print("VISUALIZING EMBEDDINGS (CONCEPT)")
print("=" * 60)

print("""
Embeddings can be visualized using dimensionality reduction:

1. PCA (Principal Component Analysis)
2. t-SNE (t-Distributed Stochastic Neighbor Embedding)

Example code:
-------------
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Get word vectors
words = ['king', 'queen', 'man', 'woman', 'prince', 'princess']
vectors = [embedding_model[word] for word in words]

# Reduce to 2D
tsne = TSNE(n_components=2, random_state=42)
vectors_2d = tsne.fit_transform(vectors)

# Plot
plt.figure(figsize=(10, 8))
for word, vec in zip(words, vectors_2d):
    plt.scatter(vec[0], vec[1])
    plt.annotate(word, (vec[0], vec[1]))
plt.title('Word Embeddings Visualization')
plt.show()
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Embedding for Sentiment Analysis")
print("=" * 60)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, Dense, GlobalAveragePooling1D, Dropout
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np
    
    # Sample data
    texts = [
        "This movie is fantastic and amazing",
        "I really enjoyed this product",
        "Great quality and fast shipping",
        "Terrible experience never again",
        "Worst purchase I have ever made",
        "Awful product do not buy",
        "Highly recommended excellent service",
        "Very disappointing poor quality"
    ]
    labels = [1, 1, 1, 0, 0, 0, 1, 0]  # 1 = positive, 0 = negative
    
    # Tokenize
    tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    
    # Pad sequences
    max_len = 10
    X = pad_sequences(sequences, maxlen=max_len, padding='post')
    y = np.array(labels)
    
    # Build model with embedding
    vocab_size = len(tokenizer.word_index) + 1
    embedding_dim = 16
    
    model = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_len),
        GlobalAveragePooling1D(),  # Average the embeddings
        Dense(16, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    print("Model Summary:")
    model.summary()
    
    print("\nTraining model...")
    history = model.fit(X, y, epochs=50, verbose=0)
    print(f"Final accuracy: {history.history['accuracy'][-1]:.4f}")
    
    # Test prediction
    test_texts = ["This is wonderful", "Terrible quality"]
    test_seq = tokenizer.texts_to_sequences(test_texts)
    test_pad = pad_sequences(test_seq, maxlen=max_len, padding='post')
    predictions = model.predict(test_pad, verbose=0)
    
    print("\nTest predictions:")
    for text, pred in zip(test_texts, predictions):
        sentiment = "Positive" if pred > 0.5 else "Negative"
        print(f"  '{text}' -> {sentiment} ({pred[0]:.4f})")

except ImportError as e:
    print(f"Import error: {e}")

print("\n" + "=" * 60)
print("✅ Word Embeddings - Complete!")
print("=" * 60)
