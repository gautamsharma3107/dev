"""
EXERCISES: Sentiment Analysis
=============================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Simple Lexicon-Based Sentiment
# TODO: Implement a lexicon-based sentiment analyzer with scoring

print("Exercise 1: Lexicon-Based Sentiment")
print("-" * 40)

# Extended sentiment lexicons with scores
positive_lexicon = {
    'excellent': 3, 'amazing': 3, 'wonderful': 3, 'fantastic': 3,
    'great': 2, 'good': 2, 'nice': 2, 'lovely': 2,
    'like': 1, 'enjoy': 1, 'happy': 1, 'pleased': 1,
    'love': 3, 'best': 3, 'perfect': 3, 'awesome': 3
}

negative_lexicon = {
    'terrible': -3, 'horrible': -3, 'awful': -3, 'worst': -3,
    'bad': -2, 'poor': -2, 'disappointing': -2, 'useless': -2,
    'hate': -3, 'dislike': -1, 'boring': -1, 'annoying': -1,
    'waste': -2, 'broken': -2, 'fail': -2, 'angry': -2
}

def analyze_sentiment_lexicon(text):
    """
    Analyze sentiment using lexicons
    Returns: sentiment label, total score, word scores
    """
    # Your code here
    pass

# Test
test_texts = [
    "This is an excellent product, I love it!",
    "Terrible experience, the worst service ever",
    "It was okay, nothing special",
    "Great quality but disappointing delivery"
]

for text in test_texts:
    result = analyze_sentiment_lexicon(text)
    if result:
        print(f"Text: {text}")
        print(f"Result: {result}\n")


# Exercise 2: Handle Negation
# TODO: Improve sentiment analysis to handle negation words

print("\n\nExercise 2: Handle Negation")
print("-" * 40)

negation_words = {'not', 'no', 'never', "don't", "doesn't", "didn't", 
                  "won't", "wouldn't", "couldn't", "shouldn't", "isn't",
                  "aren't", "wasn't", "weren't"}

def analyze_with_negation(text):
    """
    Analyze sentiment considering negation words
    Negation should flip the sentiment of following words
    """
    # Your code here
    pass

# Test
negation_texts = [
    "This is not good",
    "I don't like this product",
    "The service was not bad at all",
    "I would never recommend this"
]

for text in negation_texts:
    result = analyze_with_negation(text)
    if result:
        print(f"Text: {text}")
        print(f"Result: {result}\n")


# Exercise 3: Multi-class Sentiment
# TODO: Build a model for 3-class sentiment (positive, neutral, negative)

print("\n\nExercise 3: Multi-class Sentiment")
print("-" * 40)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
    
    def build_multiclass_sentiment_model(vocab_size=5000, embedding_dim=64, 
                                         max_length=100, num_classes=3):
        """
        Build a multi-class sentiment classification model
        Output should use softmax activation for 3 classes
        """
        # Your code here
        pass
    
    model = build_multiclass_sentiment_model()
    if model:
        model.summary()

except ImportError:
    print("TensorFlow not installed")


# Exercise 4: Evaluation Metrics
# TODO: Implement functions to calculate precision, recall, and F1 score

print("\n\nExercise 4: Evaluation Metrics")
print("-" * 40)

def calculate_precision(y_true, y_pred, positive_class=1):
    """Calculate precision: TP / (TP + FP)"""
    # Your code here
    pass

def calculate_recall(y_true, y_pred, positive_class=1):
    """Calculate recall: TP / (TP + FN)"""
    # Your code here
    pass

def calculate_f1(precision, recall):
    """Calculate F1 score: 2 * (precision * recall) / (precision + recall)"""
    # Your code here
    pass

# Test
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]

precision = calculate_precision(y_true, y_pred)
recall = calculate_recall(y_true, y_pred)
f1 = calculate_f1(precision, recall) if precision and recall else None

print(f"y_true: {y_true}")
print(f"y_pred: {y_pred}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")


# Exercise 5: Complete Sentiment Pipeline
# TODO: Build a complete sentiment analysis pipeline

print("\n\nExercise 5: Complete Sentiment Pipeline")
print("-" * 40)

class SentimentAnalyzer:
    """
    Complete sentiment analysis pipeline
    """
    
    def __init__(self, model_type='lexicon'):
        """Initialize with model type: 'lexicon' or 'ml'"""
        self.model_type = model_type
        self.model = None
        self.tokenizer = None
        # Your initialization code here
    
    def preprocess(self, text):
        """Preprocess text for analysis"""
        # Your code here
        pass
    
    def train(self, texts, labels):
        """Train the model (for ML approach)"""
        # Your code here
        pass
    
    def predict(self, text):
        """Predict sentiment for a single text"""
        # Your code here
        pass
    
    def predict_batch(self, texts):
        """Predict sentiment for multiple texts"""
        # Your code here
        pass
    
    def evaluate(self, texts, labels):
        """Evaluate model performance"""
        # Your code here
        pass

# Test
analyzer = SentimentAnalyzer(model_type='lexicon')

test_texts = [
    "This product is amazing!",
    "Terrible quality, waste of money",
    "It's okay, nothing special"
]

for text in test_texts:
    result = analyzer.predict(text)
    if result:
        print(f"'{text}' -> {result}")
