"""
Day 24 - What is Machine Learning?
===================================
Learn: ML fundamentals, applications, and key concepts

Key Concepts:
- Machine Learning is about learning patterns from data
- Models learn to make predictions without explicit programming
- ML is everywhere: recommendations, spam filters, voice assistants
"""

# ========== WHAT IS MACHINE LEARNING? ==========
print("=" * 60)
print("WHAT IS MACHINE LEARNING?")
print("=" * 60)

intro = """
Machine Learning (ML) is a subset of Artificial Intelligence (AI) that 
enables computers to learn from data and make decisions without being 
explicitly programmed for every scenario.

Traditional Programming:
    Rules + Data → Output
    
Machine Learning:
    Data + Output → Rules (Model)
"""
print(intro)

# ========== WHY MACHINE LEARNING? ==========
print("\n" + "=" * 60)
print("WHY MACHINE LEARNING?")
print("=" * 60)

why_ml = """
Machine Learning excels when:
1. Complex patterns exist in data that are hard to program manually
2. Rules change over time (spam detection, fraud detection)
3. Personalization is needed (recommendations)
4. Scale is too large for manual rules (image recognition)

Real-world examples:
- Email spam filtering
- Netflix/YouTube recommendations
- Voice assistants (Siri, Alexa)
- Self-driving cars
- Medical diagnosis
- Stock market prediction
"""
print(why_ml)

# ========== KEY TERMINOLOGY ==========
print("\n" + "=" * 60)
print("KEY TERMINOLOGY")
print("=" * 60)

terminology = """
Features (X): Input variables used to make predictions
  - Example: Age, Income, Education level
  
Target (y): Output variable we want to predict
  - Example: Will customer buy product? (Yes/No)
  
Model: Algorithm that learns patterns from data
  - Example: Linear Regression, Decision Tree, Neural Network
  
Training: Process of learning patterns from data
  - Model sees examples and adjusts its parameters
  
Inference/Prediction: Using trained model on new data
  - Model applies learned patterns to make predictions
  
Dataset: Collection of data used for training and testing
  - Usually split into training set and test set
"""
print(terminology)

# ========== SIMPLE ML ANALOGY ==========
print("\n" + "=" * 60)
print("SIMPLE ML ANALOGY: Learning to Recognize Fruits")
print("=" * 60)

analogy = """
Imagine teaching a child to recognize apples vs oranges:

1. TRAINING PHASE:
   - Show many examples of apples and oranges
   - Point out features: color, shape, texture
   - Child learns patterns: "Red/green, round = Apple"
   
2. TESTING PHASE:
   - Show a new fruit the child hasn't seen
   - Child uses learned patterns to classify it
   - "It's red and round, so it's probably an Apple!"

This is exactly what ML does with data!
"""
print(analogy)

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: Simple Data")
print("=" * 60)

import numpy as np

# Sample data: Hours studied vs Exam passed
print("\nExample: Predicting if a student will pass based on hours studied")
print("-" * 60)

# Features (X) - Hours studied
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Target (y) - Passed exam (0 = No, 1 = Yes)
passed_exam = np.array([0, 0, 0, 1, 1, 1, 1, 1])

print("Hours Studied (Features X):", hours_studied)
print("Passed Exam (Target y):    ", passed_exam)
print("\nPattern: Students who study more tend to pass!")
print("A model would learn: 'If hours >= 4, likely to pass'")

# ========== TYPES OF ML AT A GLANCE ==========
print("\n" + "=" * 60)
print("TYPES OF MACHINE LEARNING")
print("=" * 60)

types = """
1. SUPERVISED LEARNING
   - Has labeled data (we know the answers)
   - Classification: Predict categories (spam/not spam)
   - Regression: Predict numbers (house price)
   
2. UNSUPERVISED LEARNING  
   - No labels (we don't know the answers)
   - Clustering: Group similar items (customer segments)
   - Dimensionality Reduction: Simplify data (PCA)
   
3. REINFORCEMENT LEARNING
   - Agent learns through trial and error
   - Receives rewards/penalties for actions
   - Example: Game AI, Robot navigation

Today we'll focus on SUPERVISED LEARNING!
"""
print(types)

# ========== ML WORKFLOW PREVIEW ==========
print("\n" + "=" * 60)
print("ML WORKFLOW PREVIEW")
print("=" * 60)

workflow = """
The typical ML workflow:

1. Collect Data
   └─> Gather relevant data for your problem

2. Explore & Clean Data
   └─> Understand patterns, handle missing values

3. Prepare Features
   └─> Select, transform, and scale features

4. Split Data
   └─> Training set (learn) + Test set (evaluate)

5. Train Model
   └─> Choose algorithm and fit to training data

6. Evaluate Model
   └─> Check performance on test data

7. Tune & Improve
   └─> Adjust parameters for better results

8. Deploy & Monitor
   └─> Put model into production

We'll cover steps 3-6 today!
"""
print(workflow)

# ========== WHEN TO USE ML ==========
print("\n" + "=" * 60)
print("WHEN TO USE ML?")
print("=" * 60)

when_ml = """
✅ USE ML when:
   - Pattern is too complex to program manually
   - Data is available in sufficient quantity
   - Pattern exists in the data
   - Cost of errors is acceptable
   
❌ DON'T USE ML when:
   - Simple rules can solve the problem
   - Not enough data available
   - Complete accuracy is required
   - Decisions need to be fully explainable
   - No pattern exists in data
"""
print(when_ml)

print("\n" + "=" * 60)
print("✅ What is Machine Learning - Complete!")
print("=" * 60)
