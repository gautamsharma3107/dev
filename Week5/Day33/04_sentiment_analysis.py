"""
Day 33 - Sentiment Analysis Basics
==================================
Learn: Building sentiment analysis models

Key Concepts:
- Sentiment analysis classifies text as positive, negative, or neutral
- Common approaches: Lexicon-based, Machine Learning, Deep Learning
- Preprocessing is crucial for good results
- Evaluation metrics: accuracy, precision, recall, F1-score
"""

import numpy as np
import re
import string

# ========== WHAT IS SENTIMENT ANALYSIS? ==========
print("=" * 60)
print("WHAT IS SENTIMENT ANALYSIS?")
print("=" * 60)

print("""
Sentiment Analysis (Opinion Mining) determines the emotional tone
of text - is it positive, negative, or neutral?

Use Cases:
- Customer reviews analysis
- Social media monitoring
- Brand reputation management
- Market research
- Customer service prioritization

Types of Sentiment Analysis:
1. Binary: Positive vs Negative
2. Multi-class: Positive, Negative, Neutral
3. Fine-grained: Very Positive, Positive, Neutral, Negative, Very Negative
4. Aspect-based: Sentiment for specific aspects (price, quality, service)
5. Emotion detection: Happy, Sad, Angry, Fearful, etc.
""")

# ========== APPROACH 1: LEXICON-BASED ==========
print("\n" + "=" * 60)
print("APPROACH 1: LEXICON-BASED (Rule-Based)")
print("=" * 60)

# Simple lexicon-based sentiment analysis
positive_words = {
    'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
    'love', 'like', 'best', 'happy', 'awesome', 'perfect', 'recommend',
    'beautiful', 'enjoy', 'pleasant', 'satisfied', 'impressed', 'positive'
}

negative_words = {
    'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'poor',
    'disappointed', 'disappointing', 'waste', 'useless', 'broken',
    'angry', 'sad', 'frustrating', 'negative', 'never', 'avoid', 'fail'
}

def lexicon_sentiment(text):
    """Simple lexicon-based sentiment analysis"""
    words = text.lower().split()
    
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    
    score = positive_count - negative_count
    
    if score > 0:
        return "Positive", score
    elif score < 0:
        return "Negative", score
    else:
        return "Neutral", score

# Test lexicon-based
test_texts = [
    "This product is great and amazing! I love it!",
    "Terrible experience, worst purchase ever",
    "The product is okay, nothing special",
    "Good quality but disappointed with shipping"
]

print("Lexicon-based sentiment analysis:")
print("-" * 50)
for text in test_texts:
    sentiment, score = lexicon_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment} (score: {score})\n")

# ========== APPROACH 2: TEXTBLOB/VADER ==========
print("\n" + "=" * 60)
print("APPROACH 2: TEXTBLOB / VADER")
print("=" * 60)

print("""
TextBlob and VADER are popular libraries for quick sentiment analysis.

TextBlob:
- Returns polarity (-1 to 1) and subjectivity (0 to 1)
- Good for general text
- pip install textblob

VADER (Valence Aware Dictionary and sEntiment Reasoner):
- Specifically tuned for social media text
- Handles emojis, slang, capitalization
- Part of NLTK: nltk.download('vader_lexicon')

Example usage:
--------------
from textblob import TextBlob
blob = TextBlob("This movie is amazing!")
print(blob.sentiment)  # Sentiment(polarity=0.75, subjectivity=0.75)

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores("This movie is amazing!")
# {'neg': 0.0, 'neu': 0.423, 'pos': 0.577, 'compound': 0.6239}
""")

try:
    from textblob import TextBlob
    
    print("TextBlob sentiment analysis:")
    print("-" * 50)
    for text in test_texts:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        print(f"Text: {text}")
        print(f"Polarity: {polarity:.3f} -> {sentiment}\n")
        
except ImportError:
    print("TextBlob not installed. Run: pip install textblob")

# ========== APPROACH 3: MACHINE LEARNING ==========
print("\n" + "=" * 60)
print("APPROACH 3: MACHINE LEARNING (Scikit-learn)")
print("=" * 60)

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, accuracy_score
    
    # Sample training data
    texts = [
        "This product is amazing and works perfectly",
        "I absolutely love this, best purchase ever",
        "Great quality, highly recommend to everyone",
        "Excellent service and fast delivery",
        "The product exceeded my expectations",
        "Wonderful experience, will buy again",
        "Terrible product, complete waste of money",
        "Worst purchase I have ever made",
        "Very disappointing, does not work",
        "Poor quality, broke after one day",
        "Awful customer service, very rude",
        "Do not buy this, total garbage"
    ]
    labels = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]  # 1 = positive, 0 = negative
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.25, random_state=42
    )
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(max_features=1000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train Naive Bayes
    nb_model = MultinomialNB()
    nb_model.fit(X_train_tfidf, y_train)
    nb_pred = nb_model.predict(X_test_tfidf)
    
    print("Naive Bayes Results:")
    print(f"Accuracy: {accuracy_score(y_test, nb_pred):.2f}")
    
    # Train Logistic Regression
    lr_model = LogisticRegression()
    lr_model.fit(X_train_tfidf, y_train)
    lr_pred = lr_model.predict(X_test_tfidf)
    
    print(f"\nLogistic Regression Results:")
    print(f"Accuracy: {accuracy_score(y_test, lr_pred):.2f}")
    
    # Predict new text
    def predict_sentiment_ml(text, model, vectorizer):
        text_tfidf = vectorizer.transform([text])
        pred = model.predict(text_tfidf)[0]
        prob = model.predict_proba(text_tfidf)[0]
        return "Positive" if pred == 1 else "Negative", max(prob)
    
    print("\nNew predictions (Logistic Regression):")
    new_texts = ["This is wonderful!", "Terrible, don't buy"]
    for text in new_texts:
        sentiment, confidence = predict_sentiment_ml(text, lr_model, vectorizer)
        print(f"  '{text}' -> {sentiment} ({confidence:.2%} confidence)")

except ImportError as e:
    print(f"Import error: {e}")
    print("Install: pip install scikit-learn")

# ========== APPROACH 4: DEEP LEARNING ==========
print("\n" + "=" * 60)
print("APPROACH 4: DEEP LEARNING (Keras/TensorFlow)")
print("=" * 60)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.callbacks import EarlyStopping
    
    # Expanded training data
    train_texts = [
        # Positive
        "This product is amazing and works perfectly",
        "I absolutely love this best purchase ever",
        "Great quality highly recommend to everyone",
        "Excellent service and fast delivery",
        "The product exceeded my expectations",
        "Wonderful experience will buy again",
        "Fantastic product everyone should buy",
        "Very happy with my purchase",
        "Outstanding quality great value",
        "Perfect exactly what I needed",
        # Negative
        "Terrible product complete waste of money",
        "Worst purchase I have ever made",
        "Very disappointing does not work",
        "Poor quality broke after one day",
        "Awful customer service very rude",
        "Do not buy this total garbage",
        "Horrible experience never again",
        "Cheaply made falls apart quickly",
        "Regret buying this so bad",
        "Save your money this is junk"
    ]
    train_labels = [1]*10 + [0]*10
    
    # Preprocess
    tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
    tokenizer.fit_on_texts(train_texts)
    sequences = tokenizer.texts_to_sequences(train_texts)
    
    max_len = 15
    X = pad_sequences(sequences, maxlen=max_len, padding='post')
    y = np.array(train_labels)
    
    vocab_size = len(tokenizer.word_index) + 1
    
    # Build model
    model = Sequential([
        Embedding(vocab_size, 64, input_length=max_len),
        Bidirectional(LSTM(32, dropout=0.2)),
        Dense(16, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    print("Model Summary:")
    model.summary()
    
    # Train
    print("\nTraining...")
    history = model.fit(
        X, y,
        epochs=50,
        verbose=0,
        validation_split=0.2
    )
    
    print(f"Final training accuracy: {history.history['accuracy'][-1]:.4f}")
    print(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")
    
    # Predict function
    def predict_sentiment_dl(text, model, tokenizer, max_len):
        seq = tokenizer.texts_to_sequences([text])
        padded = pad_sequences(seq, maxlen=max_len, padding='post')
        pred = model.predict(padded, verbose=0)[0][0]
        return "Positive" if pred > 0.5 else "Negative", pred
    
    # Test predictions
    print("\nTest predictions:")
    test_texts = [
        "This is absolutely fantastic!",
        "Terrible product never buying again",
        "It was okay nothing special",
        "I love this so much!"
    ]
    
    for text in test_texts:
        sentiment, score = predict_sentiment_dl(text, model, tokenizer, max_len)
        print(f"  '{text}'")
        print(f"  -> {sentiment} ({score:.4f})\n")

except ImportError as e:
    print(f"Import error: {e}")
    print("Install: pip install tensorflow")

# ========== EVALUATION METRICS ==========
print("\n" + "=" * 60)
print("EVALUATION METRICS")
print("=" * 60)

print("""
Key metrics for sentiment analysis:

1. Accuracy: Overall correct predictions / Total predictions
   - Good when classes are balanced
   
2. Precision: True Positives / (True Positives + False Positives)
   - "Of all positive predictions, how many were correct?"
   
3. Recall: True Positives / (True Positives + False Negatives)
   - "Of all actual positives, how many did we catch?"
   
4. F1-Score: 2 * (Precision * Recall) / (Precision + Recall)
   - Harmonic mean of precision and recall
   - Good for imbalanced datasets

Confusion Matrix:
                    Predicted
                 Neg    |   Pos
        --------|-------|-------
Actual   Neg    |  TN   |   FP
         Pos    |  FN   |   TP

Example:
--------
from sklearn.metrics import classification_report, confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]

print(classification_report(y_true, y_pred, target_names=['Negative', 'Positive']))
print(confusion_matrix(y_true, y_pred))
""")

try:
    from sklearn.metrics import classification_report, confusion_matrix
    
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
    y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]
    
    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=['Negative', 'Positive']))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    
except ImportError:
    pass

# ========== BEST PRACTICES ==========
print("\n" + "=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("""
1. Data Preprocessing:
   - Clean text (remove URLs, special chars)
   - Handle negations ("not good" = negative)
   - Consider emojis for social media
   
2. Feature Engineering:
   - N-grams (bigrams capture "not good")
   - TF-IDF weights
   - Word embeddings
   
3. Handle Class Imbalance:
   - Oversampling (SMOTE)
   - Undersampling
   - Class weights
   
4. Model Selection:
   - Start simple (Naive Bayes)
   - Try multiple models
   - Consider pre-trained models (BERT)
   
5. Evaluation:
   - Use appropriate metrics
   - Cross-validation
   - Test on diverse data
   
6. Domain Adaptation:
   - Fine-tune for specific domain
   - Build domain-specific lexicons
   - Use domain-specific training data
""")

print("\n" + "=" * 60)
print("✅ Sentiment Analysis Basics - Complete!")
print("=" * 60)
