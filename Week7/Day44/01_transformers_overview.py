"""
Day 44 - Transformers Architecture Overview
============================================
Learn: Transformers basics, self-attention, architecture components

Key Concepts:
- Transformers revolutionized NLP in 2017
- Self-attention mechanism allows models to weigh word importance
- Encoder-decoder architecture for sequence-to-sequence tasks
- Pre-training on massive datasets enables transfer learning
"""

# ========== INTRODUCTION TO TRANSFORMERS ==========
print("=" * 60)
print("INTRODUCTION TO TRANSFORMERS")
print("=" * 60)

introduction = """
Transformers are a type of neural network architecture introduced in the paper 
"Attention Is All You Need" (2017) by Vaswani et al.

Key innovations:
1. Self-Attention Mechanism: Allows the model to weigh the importance of 
   different parts of the input when processing each element.
2. Parallelization: Unlike RNNs, transformers process all positions simultaneously.
3. Long-Range Dependencies: Can capture relationships between distant words.

Why Transformers Matter:
- Foundation of ChatGPT, BERT, GPT-4, and most modern LLMs
- State-of-the-art performance on virtually all NLP tasks
- Enable transfer learning with pre-trained models
"""

print(introduction)

# ========== SELF-ATTENTION CONCEPT ==========
print("\n" + "=" * 60)
print("SELF-ATTENTION MECHANISM")
print("=" * 60)

import numpy as np

def simple_attention_demo():
    """
    Simplified demonstration of attention mechanism.
    In real transformers, this is more complex with Q, K, V matrices.
    """
    # Example sentence (represented as simple vectors)
    sentence = ["The", "cat", "sat", "on", "the", "mat"]
    
    # Simulated attention scores (how much each word attends to others)
    # Higher scores = more attention
    attention_scores = np.array([
        [0.1, 0.3, 0.2, 0.1, 0.1, 0.2],  # "The" attends to...
        [0.2, 0.4, 0.2, 0.1, 0.05, 0.05],  # "cat" attends to...
        [0.1, 0.3, 0.3, 0.15, 0.05, 0.1],  # "sat" attends to...
        [0.1, 0.2, 0.2, 0.2, 0.1, 0.2],   # "on" attends to...
        [0.15, 0.2, 0.15, 0.2, 0.15, 0.15],  # "the" attends to...
        [0.1, 0.2, 0.2, 0.2, 0.1, 0.2],   # "mat" attends to...
    ])
    
    print("Sentence:", sentence)
    print("\nAttention visualization:")
    print("(Each row shows how much attention a word pays to other words)")
    print()
    
    # Print header
    print(f"{'':>10}", end="")
    for word in sentence:
        print(f"{word:>8}", end="")
    print()
    
    # Print attention matrix
    for i, word in enumerate(sentence):
        print(f"{word:>10}", end="")
        for j, score in enumerate(attention_scores[i]):
            print(f"{score:>8.2f}", end="")
        print()
    
    return attention_scores

attention = simple_attention_demo()

# ========== TRANSFORMER ARCHITECTURE COMPONENTS ==========
print("\n" + "=" * 60)
print("TRANSFORMER ARCHITECTURE COMPONENTS")
print("=" * 60)

architecture_explanation = """
A Transformer consists of:

1. INPUT EMBEDDING
   - Converts tokens (words/subwords) to dense vectors
   - Usually 512 or 768 dimensions

2. POSITIONAL ENCODING
   - Adds position information since transformers have no inherent order
   - Uses sin/cos functions or learned embeddings

3. ENCODER (for understanding)
   - Multi-Head Self-Attention: Multiple attention patterns in parallel
   - Feed-Forward Network: Dense layers with non-linearity
   - Layer Normalization: Stabilizes training
   - Residual Connections: Helps gradient flow

4. DECODER (for generation)
   - Masked Multi-Head Self-Attention: Can only see previous tokens
   - Cross-Attention: Attends to encoder outputs
   - Feed-Forward Network
   
5. OUTPUT LAYER
   - Linear layer + Softmax for token probabilities

Model Types:
- Encoder-only (BERT): Good for understanding/classification
- Decoder-only (GPT): Good for generation
- Encoder-Decoder (T5, BART): Good for translation/summarization
"""

print(architecture_explanation)

# ========== SIMPLIFIED POSITIONAL ENCODING ==========
print("\n" + "=" * 60)
print("POSITIONAL ENCODING DEMO")
print("=" * 60)

def positional_encoding(seq_length, d_model):
    """
    Generate positional encoding matrix.
    Uses sin for even indices and cos for odd indices.
    """
    position = np.arange(seq_length)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    
    pe = np.zeros((seq_length, d_model))
    pe[:, 0::2] = np.sin(position * div_term)
    pe[:, 1::2] = np.cos(position * div_term)
    
    return pe

# Generate positional encoding for a sequence of 10 positions, 8 dimensions
seq_len = 10
d_model = 8
pe = positional_encoding(seq_len, d_model)

print(f"Positional Encoding Matrix ({seq_len} positions, {d_model} dimensions):")
print(f"Shape: {pe.shape}")
print("\nFirst 5 positions (first 4 dimensions):")
print(pe[:5, :4].round(3))

# ========== ATTENTION SCORE CALCULATION ==========
print("\n" + "=" * 60)
print("ATTENTION SCORE CALCULATION")
print("=" * 60)

def scaled_dot_product_attention(Q, K, V):
    """
    Compute scaled dot-product attention.
    
    Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) * V
    
    Args:
        Q: Query matrix (seq_len, d_k)
        K: Key matrix (seq_len, d_k)
        V: Value matrix (seq_len, d_v)
    
    Returns:
        Attention output and attention weights
    """
    d_k = K.shape[-1]
    
    # Compute attention scores
    scores = np.matmul(Q, K.T) / np.sqrt(d_k)
    
    # Apply softmax
    attention_weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
    
    # Multiply by values
    output = np.matmul(attention_weights, V)
    
    return output, attention_weights

# Simple example with 3 tokens, 4 dimensions
np.random.seed(42)
Q = np.random.randn(3, 4)  # 3 tokens, 4 dimensions
K = np.random.randn(3, 4)
V = np.random.randn(3, 4)

output, weights = scaled_dot_product_attention(Q, K, V)

print("Query (Q) shape:", Q.shape)
print("Key (K) shape:", K.shape)
print("Value (V) shape:", V.shape)
print("\nAttention Weights:")
print(weights.round(3))
print("\nAttention Output shape:", output.shape)

# ========== MULTI-HEAD ATTENTION CONCEPT ==========
print("\n" + "=" * 60)
print("MULTI-HEAD ATTENTION")
print("=" * 60)

multi_head_explanation = """
Multi-Head Attention:
- Instead of one attention, use multiple attention "heads"
- Each head learns different types of relationships
- Outputs are concatenated and projected

Example with 8 heads:
- Head 1: May focus on subject-verb relationships
- Head 2: May focus on adjective-noun relationships
- Head 3: May capture positional patterns
- ...and so on

Formula:
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) * W_O

where head_i = Attention(Q*W_Q_i, K*W_K_i, V*W_V_i)

Benefits:
- Captures different types of relationships
- More expressive power
- Better generalization
"""

print(multi_head_explanation)

# ========== TRANSFORMER TRAINING OVERVIEW ==========
print("\n" + "=" * 60)
print("HOW TRANSFORMERS ARE TRAINED")
print("=" * 60)

training_explanation = """
Pre-training Objectives:

1. MASKED LANGUAGE MODELING (BERT-style)
   - Randomly mask 15% of tokens
   - Model predicts masked tokens
   - Example: "The [MASK] sat on the mat" → predict "cat"

2. NEXT SENTENCE PREDICTION (BERT)
   - Given two sentences, predict if B follows A
   - Helps understand sentence relationships

3. CAUSAL LANGUAGE MODELING (GPT-style)
   - Predict the next token given previous tokens
   - Example: "The cat sat on the" → predict "mat"

4. DENOISING (T5, BART)
   - Corrupt text in various ways
   - Model reconstructs original text

Fine-tuning:
- Take pre-trained model
- Add task-specific head
- Train on smaller labeled dataset
- Transfer learning enables amazing performance!
"""

print(training_explanation)

# ========== PRACTICAL EXAMPLE: TOKENIZATION ==========
print("\n" + "=" * 60)
print("TOKENIZATION IN TRANSFORMERS")
print("=" * 60)

tokenization_explanation = """
Transformers use subword tokenization:

Methods:
1. BPE (Byte Pair Encoding) - GPT models
2. WordPiece - BERT
3. SentencePiece - Universal, language-agnostic

Example:
"unhappiness" → ["un", "##happiness"] (WordPiece)
"unhappiness" → ["un", "happi", "ness"] (BPE variant)

Benefits:
- Handles rare words by breaking into subwords
- Reduces vocabulary size
- No out-of-vocabulary (OOV) issues
"""

print(tokenization_explanation)

# Simple tokenization demo
def simple_tokenize(text, vocab=None):
    """Simple word-level tokenization demo."""
    tokens = text.lower().split()
    return tokens

text = "Transformers have revolutionized natural language processing"
tokens = simple_tokenize(text)
print(f"\nSimple tokenization:")
print(f"Text: '{text}'")
print(f"Tokens: {tokens}")
print(f"Number of tokens: {len(tokens)}")

# ========== KEY TRANSFORMER MODELS ==========
print("\n" + "=" * 60)
print("KEY TRANSFORMER MODELS")
print("=" * 60)

models_overview = """
1. BERT (2018) - Google
   - Bidirectional encoder
   - Great for classification, Q&A, NER
   - 110M-340M parameters

2. GPT-2/GPT-3/GPT-4 (2019-2023) - OpenAI
   - Decoder-only, autoregressive
   - Excellent text generation
   - GPT-3: 175B parameters

3. T5 (2020) - Google
   - Text-to-text framework
   - Versatile for any NLP task
   - Encoder-decoder

4. RoBERTa (2019) - Facebook
   - Improved BERT training
   - Better performance

5. ALBERT (2019) - Google
   - Efficient BERT variant
   - Parameter sharing

6. DistilBERT - Hugging Face
   - 40% smaller, 60% faster
   - 97% BERT performance

7. LLaMA/LLaMA 2 (2023) - Meta
   - Open-source large language models
   - Efficient and powerful
"""

print(models_overview)

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

summary = """
✅ Transformers use self-attention to process sequences
✅ Attention allows models to focus on relevant parts of input
✅ Positional encodings provide sequence order information
✅ Multi-head attention captures different relationship types
✅ Pre-training + fine-tuning enables powerful transfer learning
✅ Different architectures for different tasks (encoder/decoder)
✅ Subword tokenization handles vocabulary efficiently

Next Steps:
- Learn about BERT and GPT specifics
- Practice with Hugging Face transformers library
- Fine-tune pre-trained models for your tasks
"""

print(summary)

print("\n" + "=" * 60)
print("✅ Transformers Overview - Complete!")
print("=" * 60)
