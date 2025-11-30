"""
Day 33 - RNN/LSTM Overview
==========================
Learn: Simple RNN and LSTM architecture

Key Concepts:
- RNNs process sequential data by maintaining hidden state
- Vanilla RNNs suffer from vanishing gradient problem
- LSTMs solve this with gates (forget, input, output)
- GRUs are a simpler alternative to LSTMs
"""

import numpy as np

# ========== WHY SEQUENTIAL MODELS? ==========
print("=" * 60)
print("WHY SEQUENTIAL MODELS?")
print("=" * 60)

print("""
Traditional neural networks treat each input independently.
But for text, sequence matters!

Example:
- "The cat sat on the mat" - Normal sentence
- "mat the on sat cat The" - Same words, no meaning!

Sequential models (RNN, LSTM, GRU) process data step by step,
maintaining a "memory" of what came before.

Applications:
- Text classification (sentiment analysis)
- Language modeling (predicting next word)
- Machine translation
- Speech recognition
- Time series forecasting
""")

# ========== SIMPLE RNN CONCEPT ==========
print("\n" + "=" * 60)
print("SIMPLE RNN CONCEPT")
print("=" * 60)

print("""
RNN (Recurrent Neural Network) Architecture:

        ┌──────────────────────────────────────────┐
        │                                          │
        ▼                                          │
    ┌───────┐    ┌───────┐    ┌───────┐    ┌───────┐
    │ h(t-1)│───▶│  h(t) │───▶│ h(t+1)│───▶│ h(t+2)│
    └───────┘    └───────┘    └───────┘    └───────┘
        ▲            ▲            ▲            ▲
        │            │            │            │
    ┌───────┐    ┌───────┐    ┌───────┐    ┌───────┐
    │  x(t) │    │ x(t+1)│    │ x(t+2)│    │ x(t+3)│
    └───────┘    └───────┘    └───────┘    └───────┘
       "I"        "love"       "NLP"        "!"

For each time step t:
    h(t) = tanh(W_hh * h(t-1) + W_xh * x(t) + b)

h(t) = current hidden state (memory)
x(t) = current input
W_hh = hidden-to-hidden weights
W_xh = input-to-hidden weights

Problem: Vanishing gradients make RNNs bad at long sequences!
""")

# Simulate simple RNN forward pass
def simple_rnn_forward(inputs, hidden_size=4):
    """Simplified RNN forward pass"""
    np.random.seed(42)
    sequence_length = len(inputs)
    input_size = len(inputs[0])
    
    # Initialize weights
    W_xh = np.random.randn(input_size, hidden_size) * 0.01
    W_hh = np.random.randn(hidden_size, hidden_size) * 0.01
    b_h = np.zeros(hidden_size)
    
    # Initialize hidden state
    h = np.zeros(hidden_size)
    
    print("Simple RNN forward pass:")
    for t, x in enumerate(inputs):
        x = np.array(x)
        h = np.tanh(np.dot(x, W_xh) + np.dot(h, W_hh) + b_h)
        print(f"  Step {t}: input={x} -> hidden={np.round(h, 3)}")
    
    return h

# Demo
sample_inputs = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # 3 one-hot encoded words
final_hidden = simple_rnn_forward(sample_inputs)
print(f"Final hidden state: {np.round(final_hidden, 3)}")

# ========== LSTM CONCEPT ==========
print("\n" + "=" * 60)
print("LSTM CONCEPT")
print("=" * 60)

print("""
LSTM (Long Short-Term Memory) solves the vanishing gradient problem
using GATES to control information flow.

LSTM has two states:
- h(t): Hidden state (short-term memory)
- c(t): Cell state (long-term memory)

Three gates (values between 0-1):
1. Forget Gate (f): What to forget from cell state
2. Input Gate (i): What new info to add to cell state  
3. Output Gate (o): What to output from cell state

LSTM Equations:
---------------
f(t) = σ(W_f · [h(t-1), x(t)] + b_f)     # Forget gate
i(t) = σ(W_i · [h(t-1), x(t)] + b_i)     # Input gate
c̃(t) = tanh(W_c · [h(t-1), x(t)] + b_c)  # Candidate cell state
c(t) = f(t) * c(t-1) + i(t) * c̃(t)       # New cell state
o(t) = σ(W_o · [h(t-1), x(t)] + b_o)     # Output gate
h(t) = o(t) * tanh(c(t))                  # New hidden state

σ = sigmoid function (outputs 0-1)
* = element-wise multiplication

Visual:
-------
            ┌─────────────────────────────────────────────────┐
            │                   Cell State c(t)                │
            │    ┌──────┐                      ┌──────┐        │
  c(t-1)───▶│───▶│  ×   │──────────[+]────────▶│      │───────▶│c(t)
            │    └──────┘           ▲          └──────┘        │
            │        ▲              │                          │
            │        │              │                          │
            │    ┌──────┐       ┌──────┐                      │
            │    │forget│       │input │                      │
            │    │ gate │       │ gate │                      │
            │    └──────┘       └──────┘                      │
            │        ▲              ▲                          │
            └────────│──────────────│──────────────────────────┘
                     │              │
  h(t-1)────────────[concat]───────[concat]─────────▶h(t)
                     │              │
  x(t) ─────────────┘              └
""")

# ========== GRU CONCEPT ==========
print("\n" + "=" * 60)
print("GRU CONCEPT")
print("=" * 60)

print("""
GRU (Gated Recurrent Unit) is a simplified LSTM with fewer parameters.

GRU has only two gates:
1. Reset Gate (r): How much past info to forget
2. Update Gate (z): How much to update the state

GRU Equations:
--------------
z(t) = σ(W_z · [h(t-1), x(t)])            # Update gate
r(t) = σ(W_r · [h(t-1), x(t)])            # Reset gate
h̃(t) = tanh(W · [r(t) * h(t-1), x(t)])    # Candidate state
h(t) = (1 - z(t)) * h(t-1) + z(t) * h̃(t)  # New state

Comparison:
-----------
| Feature          | RNN   | LSTM  | GRU   |
|------------------|-------|-------|-------|
| Gates            | 0     | 3     | 2     |
| States           | 1     | 2     | 1     |
| Parameters       | Few   | Many  | Medium|
| Long sequences   | Poor  | Good  | Good  |
| Training speed   | Fast  | Slow  | Medium|
""")

# ========== KERAS IMPLEMENTATION ==========
print("\n" + "=" * 60)
print("KERAS IMPLEMENTATION")
print("=" * 60)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import (
        Embedding, SimpleRNN, LSTM, GRU, 
        Dense, Bidirectional, Dropout
    )
    
    vocab_size = 10000
    embedding_dim = 128
    max_length = 100
    
    # 1. Simple RNN model
    print("\n1. Simple RNN Model:")
    model_rnn = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        SimpleRNN(64),  # 64 hidden units
        Dense(1, activation='sigmoid')
    ], name="simple_rnn")
    model_rnn.summary()
    
    # 2. LSTM model
    print("\n2. LSTM Model:")
    model_lstm = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        LSTM(64, dropout=0.2),  # With dropout for regularization
        Dense(1, activation='sigmoid')
    ], name="lstm")
    model_lstm.summary()
    
    # 3. Stacked LSTM model
    print("\n3. Stacked LSTM Model:")
    model_stacked = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        LSTM(64, return_sequences=True),  # Return sequence for stacking
        LSTM(32),
        Dense(1, activation='sigmoid')
    ], name="stacked_lstm")
    model_stacked.summary()
    
    # 4. Bidirectional LSTM
    print("\n4. Bidirectional LSTM Model:")
    model_bilstm = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        Bidirectional(LSTM(64)),  # Processes sequence both directions
        Dense(1, activation='sigmoid')
    ], name="bidirectional_lstm")
    model_bilstm.summary()
    
    # 5. GRU model
    print("\n5. GRU Model:")
    model_gru = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        GRU(64, dropout=0.2),
        Dense(1, activation='sigmoid')
    ], name="gru")
    model_gru.summary()

except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")

# ========== RETURN SEQUENCES EXPLAINED ==========
print("\n" + "=" * 60)
print("RETURN SEQUENCES EXPLAINED")
print("=" * 60)

print("""
return_sequences parameter determines LSTM output shape:

return_sequences=False (default):
- Returns only the last hidden state
- Shape: (batch_size, units)
- Use for: Classification (final prediction)

return_sequences=True:
- Returns hidden state at each time step
- Shape: (batch_size, sequence_length, units)
- Use for: Stacking LSTMs, sequence-to-sequence tasks

Example:
--------
Input shape: (32, 100, 128)  # 32 samples, 100 timesteps, 128 features

LSTM(64, return_sequences=False) -> Output: (32, 64)
LSTM(64, return_sequences=True)  -> Output: (32, 100, 64)

Stacking LSTMs:
---------------
# First LSTM must return sequences for second LSTM to process
model.add(LSTM(64, return_sequences=True))   # -> (batch, 100, 64)
model.add(LSTM(32, return_sequences=False))  # -> (batch, 32)
model.add(Dense(1))
""")

# ========== PRACTICAL COMPARISON ==========
print("\n" + "=" * 60)
print("PRACTICAL COMPARISON")
print("=" * 60)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, GRU, Dense
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np
    import time
    
    # Sample data
    texts = [
        "This movie is fantastic and amazing",
        "I really enjoyed this product very much",
        "Great quality and excellent service",
        "Terrible experience never buying again",
        "Worst purchase I have ever made",
        "Awful product do not waste money",
        "Highly recommended loved it",
        "Very disappointing poor quality bad",
        "Excellent work very satisfied happy",
        "Horrible service rude staff angry"
    ] * 10  # Repeat for more data
    
    labels = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0] * 10
    
    # Preprocess
    tokenizer = Tokenizer(num_words=1000)
    tokenizer.fit_on_texts(texts)
    X = pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=20)
    y = np.array(labels)
    
    vocab_size = len(tokenizer.word_index) + 1
    
    def train_and_evaluate(model_type, layer_class):
        """Train a model and return accuracy and time"""
        model = Sequential([
            Embedding(vocab_size, 32, input_length=20),
            layer_class(32),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        start_time = time.time()
        history = model.fit(X, y, epochs=10, verbose=0)
        train_time = time.time() - start_time
        
        return history.history['accuracy'][-1], train_time
    
    print("\nComparing RNN architectures (10 epochs):")
    print("-" * 50)
    
    # Compare
    models = [
        ("SimpleRNN", SimpleRNN),
        ("LSTM", LSTM),
        ("GRU", GRU)
    ]
    
    for name, layer in models:
        acc, duration = train_and_evaluate(name, layer)
        print(f"{name:12} - Accuracy: {acc:.4f}, Time: {duration:.2f}s")

except ImportError as e:
    print(f"Import error: {e}")

# ========== WHEN TO USE WHAT ==========
print("\n" + "=" * 60)
print("WHEN TO USE WHAT?")
print("=" * 60)

print("""
Choosing the right architecture:

SimpleRNN:
✓ Short sequences (< 50 tokens)
✓ Quick prototyping
✓ Limited computational resources
✗ Long sequences (vanishing gradients)

LSTM:
✓ Long sequences
✓ Complex dependencies
✓ When accuracy is priority
✓ Language modeling, translation
✗ Limited resources (many parameters)

GRU:
✓ Good balance of speed and accuracy
✓ Fewer parameters than LSTM
✓ Faster training
✓ Similar performance to LSTM
✓ Good default choice

Bidirectional:
✓ Context from both directions matters
✓ Text classification
✓ Named entity recognition
✗ Real-time/streaming tasks

Stacked layers:
✓ Complex patterns
✓ Large datasets
✗ Small datasets (overfitting risk)

Modern alternatives:
- Transformer models (BERT, GPT) often outperform
- Consider using pre-trained models for best results
""")

print("\n" + "=" * 60)
print("✅ RNN/LSTM Overview - Complete!")
print("=" * 60)
