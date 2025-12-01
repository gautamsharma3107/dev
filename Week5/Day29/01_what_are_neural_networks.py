"""
Day 29 - What Are Neural Networks?
===================================
Learn: The fundamentals of neural networks and why they work

Key Concepts:
- Neural networks are computing systems inspired by biological brains
- They learn patterns from data through training
- They are the foundation of modern AI and deep learning
"""

import numpy as np

# ========== INTRODUCTION ==========
print("=" * 60)
print("WHAT ARE NEURAL NETWORKS?")
print("=" * 60)

print("""
🧠 DEFINITION:
A Neural Network is a series of algorithms that attempt to recognize 
underlying relationships in a set of data through a process that mimics 
the way the human brain operates.

KEY IDEA:
Just like your brain uses neurons connected by synapses, artificial 
neural networks use nodes (artificial neurons) connected by weights.
""")

# ========== WHY NEURAL NETWORKS? ==========
print("\n" + "=" * 60)
print("WHY DO WE USE NEURAL NETWORKS?")
print("=" * 60)

print("""
Traditional Programming vs Neural Networks:

TRADITIONAL PROGRAMMING:
    Input + Rules → Output
    (You write the rules manually)

NEURAL NETWORKS:
    Input + Output → Rules (learned)
    (Network learns the rules from data)

Example: Image Recognition
    Traditional: Write rules for every pixel pattern (impossible!)
    Neural Net: Show many examples, let it learn patterns
""")

# ========== BASIC STRUCTURE ==========
print("\n" + "=" * 60)
print("BASIC STRUCTURE OF A NEURAL NETWORK")
print("=" * 60)

print("""
                    Neural Network Architecture
                    
    INPUT LAYER         HIDDEN LAYER(S)         OUTPUT LAYER
    
    ○ ─────────────►    ○ ─────────────►        ○
       Feature 1           Neuron 1                Prediction 1
    
    ○ ─────────────►    ○ ─────────────►        ○
       Feature 2           Neuron 2                Prediction 2
    
    ○ ─────────────►    ○ ─────────────►
       Feature 3           Neuron 3
    
    (Raw Data)         (Processing)            (Results)

LAYER TYPES:
1. INPUT LAYER:  Receives the raw data (features)
2. HIDDEN LAYERS: Process and transform the data  
3. OUTPUT LAYER: Produces the final prediction
""")

# ========== HOW IT WORKS ==========
print("\n" + "=" * 60)
print("HOW NEURAL NETWORKS LEARN")
print("=" * 60)

print("""
THE LEARNING PROCESS:

Step 1: FORWARD PROPAGATION
    - Input data flows through the network
    - Each neuron processes inputs and produces output
    - Final layer makes a prediction

Step 2: CALCULATE LOSS
    - Compare prediction to actual value
    - Loss = How wrong was the prediction?

Step 3: BACKWARD PROPAGATION
    - Calculate how much each weight contributed to error
    - Use calculus (chain rule) to find gradients

Step 4: UPDATE WEIGHTS
    - Adjust weights to reduce the error
    - Weights that caused more error change more

Step 5: REPEAT
    - Do this thousands of times with different data
    - Network gradually improves
""")

# ========== SIMPLE ANALOGY ==========
print("\n" + "=" * 60)
print("SIMPLE ANALOGY: LEARNING TO RECOGNIZE CATS")
print("=" * 60)

print("""
Imagine teaching a child to recognize cats:

1. Show picture → Child guesses "Dog!" (FORWARD PASS)
2. You say "No, it's a cat" (CALCULATE LOSS)
3. Child thinks about what they got wrong (BACKWARD PASS)
4. Child adjusts their understanding (UPDATE WEIGHTS)
5. Repeat with more pictures (ITERATE)

After many examples, child learns to recognize cats!

Neural networks work the same way - they adjust internal 
parameters (weights) based on feedback (loss) until they 
can make accurate predictions.
""")

# ========== PRACTICAL EXAMPLE: SIMPLE PERCEPTRON ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: SIMPLE PERCEPTRON")
print("=" * 60)

# A perceptron is the simplest neural network - just one neuron!
# Let's implement one to understand the basics

def simple_perceptron(x1, x2, w1, w2, bias):
    """
    A simple perceptron with two inputs
    """
    # Weighted sum
    z = x1 * w1 + x2 * w2 + bias
    
    # Activation (step function)
    output = 1 if z > 0 else 0
    
    return output

# Example: OR gate with a perceptron
print("\nOR Gate with Perceptron:")
print("-" * 40)

# Weights learned through training (we'll just use pre-trained values)
w1, w2, bias = 1.0, 1.0, -0.5

# Test all inputs
test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]

print(f"Weights: w1={w1}, w2={w2}, bias={bias}")
print()

for x1, x2 in test_cases:
    output = simple_perceptron(x1, x2, w1, w2, bias)
    expected = x1 or x2
    print(f"Input: ({x1}, {x2}) → Output: {output} | Expected OR: {expected}")

# ========== TYPES OF NEURAL NETWORKS ==========
print("\n" + "=" * 60)
print("TYPES OF NEURAL NETWORKS")
print("=" * 60)

print("""
1. FEEDFORWARD NEURAL NETWORKS (FNN)
   - Simplest type
   - Information flows in one direction
   - Good for: Classification, Regression

2. CONVOLUTIONAL NEURAL NETWORKS (CNN)
   - Specialized for images
   - Uses filters to detect patterns
   - Good for: Image recognition, Object detection

3. RECURRENT NEURAL NETWORKS (RNN)
   - Has memory of previous inputs
   - Good for: Sequences, Time series, Text

4. LONG SHORT-TERM MEMORY (LSTM)
   - Advanced RNN with better memory
   - Good for: Long sequences, Language modeling

5. TRANSFORMER
   - Modern architecture using attention
   - Good for: NLP, Language models (GPT, BERT)
""")

# ========== APPLICATIONS ==========
print("\n" + "=" * 60)
print("REAL-WORLD APPLICATIONS")
print("=" * 60)

print("""
🖼️  IMAGE RECOGNITION
    - Face recognition
    - Medical image analysis
    - Self-driving cars

💬  NATURAL LANGUAGE PROCESSING
    - ChatGPT, Claude, etc.
    - Translation
    - Sentiment analysis

🎮  GAMES AND ROBOTICS
    - AlphaGo
    - Game playing AI
    - Robot control

💰  FINANCE
    - Fraud detection
    - Stock prediction
    - Risk assessment

🏥  HEALTHCARE
    - Disease diagnosis
    - Drug discovery
    - Personalized treatment
""")

# ========== KEY TERMINOLOGY ==========
print("\n" + "=" * 60)
print("KEY TERMINOLOGY")
print("=" * 60)

print("""
NEURON/NODE:    Basic unit that receives inputs and produces output
WEIGHT:         Learnable parameter that scales input importance
BIAS:           Learnable offset added to weighted sum
ACTIVATION:     Function that introduces non-linearity
LAYER:          Collection of neurons at the same depth
LOSS/COST:      Measure of how wrong predictions are
GRADIENT:       Direction and magnitude to adjust weights
EPOCH:          One complete pass through training data
BATCH:          Subset of training data used in one step
LEARNING RATE:  How much weights change in each update
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✅ Neural networks learn from data, not from explicit rules
✅ They consist of layers of connected neurons
✅ Each neuron: output = activation(weights · inputs + bias)
✅ Learning happens through: Forward → Loss → Backward → Update
✅ Different architectures for different problems (CNN, RNN, etc.)
✅ They power most modern AI applications
""")

print("\n" + "=" * 60)
print("✅ What Are Neural Networks - Complete!")
print("=" * 60)
