"""
EXERCISES: Text Classification
==============================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Feature Extraction with TF-IDF
# TODO: Implement TF-IDF vectorization

print("Exercise 1: TF-IDF Feature Extraction")
print("-" * 40)

def calculate_tf(text):
    """
    Calculate Term Frequency for a text
    TF(t) = (Number of times term t appears) / (Total number of terms)
    """
    # Your code here
    pass

def calculate_idf(documents):
    """
    Calculate Inverse Document Frequency for all terms
    IDF(t) = log(Total documents / Documents containing term t)
    """
    # Your code here
    pass

def calculate_tfidf(texts):
    """
    Calculate TF-IDF matrix for a list of texts
    """
    # Your code here
    pass

# Test
texts = [
    "I love machine learning",
    "Machine learning is great",
    "Deep learning is part of machine learning"
]

tfidf = calculate_tfidf(texts)
if tfidf:
    print("TF-IDF Matrix:")
    print(tfidf)


# Exercise 2: Data Augmentation for Text
# TODO: Implement text augmentation techniques

print("\n\nExercise 2: Text Data Augmentation")
print("-" * 40)

import random

def augment_synonym_replacement(text, n=1):
    """
    Replace n words with synonyms
    Use simple synonym dictionary for demo
    """
    synonyms = {
        'good': ['great', 'excellent', 'wonderful'],
        'bad': ['terrible', 'awful', 'poor'],
        'love': ['adore', 'like', 'enjoy'],
        'hate': ['dislike', 'despise', 'detest'],
        'big': ['large', 'huge', 'enormous'],
        'small': ['tiny', 'little', 'mini']
    }
    # Your code here
    pass

def augment_random_deletion(text, p=0.1):
    """
    Randomly delete words with probability p
    """
    # Your code here
    pass

def augment_random_swap(text, n=1):
    """
    Randomly swap n pairs of words
    """
    # Your code here
    pass

# Test
original = "This is a good product and I love it"
print(f"Original: {original}")
print(f"Synonym replacement: {augment_synonym_replacement(original)}")
print(f"Random deletion: {augment_random_deletion(original)}")
print(f"Random swap: {augment_random_swap(original)}")


# Exercise 3: Cross-Validation for Text Classification
# TODO: Implement k-fold cross-validation

print("\n\nExercise 3: K-Fold Cross-Validation")
print("-" * 40)

def k_fold_split(data, labels, k=5):
    """
    Split data into k folds
    Returns: list of (train_indices, test_indices) tuples
    """
    # Your code here
    pass

def cross_validate(data, labels, model_fn, k=5):
    """
    Perform k-fold cross-validation
    model_fn: function that returns a trained model
    Returns: list of accuracies for each fold
    """
    # Your code here
    pass

# Test
data = list(range(100))
labels = [0]*50 + [1]*50
folds = k_fold_split(data, labels, k=5)
if folds:
    for i, (train_idx, test_idx) in enumerate(folds):
        print(f"Fold {i+1}: Train size={len(train_idx)}, Test size={len(test_idx)}")


# Exercise 4: Multi-Label Classification
# TODO: Build a model for multi-label text classification

print("\n\nExercise 4: Multi-Label Classification")
print("-" * 40)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
    
    def build_multilabel_model(vocab_size=5000, embedding_dim=64, 
                               max_length=100, num_labels=5):
        """
        Build a multi-label classification model
        - A text can have multiple labels simultaneously
        - Use sigmoid activation for each label independently
        - Use binary_crossentropy loss
        """
        # Your code here
        pass
    
    model = build_multilabel_model()
    if model:
        model.summary()

except ImportError:
    print("TensorFlow not installed")


# Exercise 5: Complete Text Classification Pipeline
# TODO: Build an end-to-end text classification system

print("\n\nExercise 5: Complete Classification Pipeline")
print("-" * 40)

class TextClassifier:
    """
    Complete text classification pipeline
    """
    
    def __init__(self, num_classes, max_vocab=5000, max_length=100):
        self.num_classes = num_classes
        self.max_vocab = max_vocab
        self.max_length = max_length
        self.tokenizer = None
        self.model = None
        self.label_encoder = None
    
    def preprocess(self, texts):
        """Preprocess and tokenize texts"""
        # Your code here
        pass
    
    def build_model(self, embedding_dim=64, lstm_units=32):
        """Build the classification model"""
        # Your code here
        pass
    
    def fit(self, texts, labels, epochs=10, validation_split=0.2):
        """Train the model"""
        # Your code here
        pass
    
    def predict(self, texts):
        """Make predictions"""
        # Your code here
        pass
    
    def evaluate(self, texts, labels):
        """Evaluate model performance"""
        # Your code here
        pass
    
    def save(self, path):
        """Save model and tokenizer"""
        # Your code here
        pass
    
    def load(self, path):
        """Load model and tokenizer"""
        # Your code here
        pass

# Test
train_texts = [
    "Technology news about smartphones",
    "Sports update on basketball",
    "New movie releases this week",
    "Stock market trends analysis",
    "Celebrity gossip and news"
]
train_labels = ["tech", "sports", "entertainment", "business", "entertainment"]

classifier = TextClassifier(num_classes=4)

print("TextClassifier initialized")
print("To use: classifier.fit(texts, labels)")
print("Then: classifier.predict(new_texts)")
