"""
EXERCISES: RNN/LSTM
===================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Understanding Sequence Data
# TODO: Convert text data to sequences suitable for RNN input

print("Exercise 1: Understanding Sequence Data")
print("-" * 40)

def text_to_sequences(texts, vocab=None):
    """
    Convert list of texts to sequences of integers
    Returns: sequences, vocabulary dictionary
    """
    # Your code here
    # 1. Build vocabulary if not provided
    # 2. Convert each word to its index
    pass

# Test
texts = ["I love NLP", "NLP is amazing", "I learn NLP"]
sequences, vocab = text_to_sequences(texts) if text_to_sequences(texts) else (None, None)
if sequences:
    print(f"Vocabulary: {vocab}")
    print(f"Sequences: {sequences}")


# Exercise 2: Manual Padding
# TODO: Implement padding function without using Keras

print("\n\nExercise 2: Manual Padding")
print("-" * 40)

def pad_sequences_manual(sequences, maxlen, padding='post', value=0):
    """
    Pad sequences to the same length
    
    Args:
        sequences: List of lists (integer sequences)
        maxlen: Maximum length
        padding: 'pre' or 'post'
        value: Padding value (default 0)
    
    Returns:
        Padded numpy array
    """
    # Your code here
    pass

# Test
test_seqs = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
padded = pad_sequences_manual(test_seqs, maxlen=5, padding='post')
print(f"Original: {test_seqs}")
print(f"Padded (post): {padded}")

padded_pre = pad_sequences_manual(test_seqs, maxlen=5, padding='pre')
print(f"Padded (pre): {padded_pre}")


# Exercise 3: Simple RNN Cell (Conceptual)
# TODO: Implement a single RNN cell forward pass

print("\n\nExercise 3: Simple RNN Cell Forward Pass")
print("-" * 40)

def rnn_cell_forward(x_t, h_prev, Wx, Wh, b):
    """
    Single RNN cell forward pass
    
    Args:
        x_t: Current input (shape: input_size)
        h_prev: Previous hidden state (shape: hidden_size)
        Wx: Input weights (shape: input_size x hidden_size)
        Wh: Hidden weights (shape: hidden_size x hidden_size)
        b: Bias (shape: hidden_size)
    
    Returns:
        h_next: Next hidden state
    """
    # Formula: h_t = tanh(Wx * x_t + Wh * h_prev + b)
    # Your code here
    pass

# Test
np.random.seed(42)
input_size, hidden_size = 3, 4
x_t = np.random.randn(input_size)
h_prev = np.zeros(hidden_size)
Wx = np.random.randn(input_size, hidden_size) * 0.01
Wh = np.random.randn(hidden_size, hidden_size) * 0.01
b = np.zeros(hidden_size)

h_next = rnn_cell_forward(x_t, h_prev, Wx, Wh, b)
if h_next is not None:
    print(f"Input: {x_t}")
    print(f"Previous hidden: {h_prev}")
    print(f"Next hidden: {h_next}")


# Exercise 4: Build Different RNN Architectures
# TODO: Create models with different RNN architectures

print("\n\nExercise 4: Build RNN Architectures")
print("-" * 40)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import (
        Embedding, SimpleRNN, LSTM, GRU, 
        Dense, Bidirectional
    )
    
    def build_simple_rnn(vocab_size=1000, embedding_dim=64, 
                         max_length=100, rnn_units=32):
        """Build SimpleRNN model"""
        # Your code here
        pass
    
    def build_stacked_lstm(vocab_size=1000, embedding_dim=64, 
                           max_length=100, lstm_units=[64, 32]):
        """Build stacked LSTM model"""
        # Your code here
        pass
    
    def build_bidirectional_gru(vocab_size=1000, embedding_dim=64, 
                                max_length=100, gru_units=32):
        """Build bidirectional GRU model"""
        # Your code here
        pass
    
    # Test models
    print("SimpleRNN model:")
    model1 = build_simple_rnn()
    if model1:
        model1.summary()
    
    print("\nStacked LSTM model:")
    model2 = build_stacked_lstm()
    if model2:
        model2.summary()
    
    print("\nBidirectional GRU model:")
    model3 = build_bidirectional_gru()
    if model3:
        model3.summary()

except ImportError:
    print("TensorFlow not installed")


# Exercise 5: Compare Model Parameters
# TODO: Calculate and compare the number of parameters in different models

print("\n\nExercise 5: Compare Model Parameters")
print("-" * 40)

def calculate_embedding_params(vocab_size, embedding_dim):
    """Calculate parameters in embedding layer"""
    # Your code here
    pass

def calculate_lstm_params(input_size, hidden_size):
    """
    Calculate parameters in LSTM layer
    LSTM has 4 gates, each with weights for input and hidden state
    """
    # Your code here
    pass

def calculate_gru_params(input_size, hidden_size):
    """
    Calculate parameters in GRU layer
    GRU has 3 gates
    """
    # Your code here
    pass

# Test
vocab_size = 10000
embedding_dim = 128
lstm_units = 64

print(f"Embedding params: {calculate_embedding_params(vocab_size, embedding_dim)}")
print(f"LSTM params (input={embedding_dim}, hidden={lstm_units}): "
      f"{calculate_lstm_params(embedding_dim, lstm_units)}")
print(f"GRU params (input={embedding_dim}, hidden={lstm_units}): "
      f"{calculate_gru_params(embedding_dim, lstm_units)}")
