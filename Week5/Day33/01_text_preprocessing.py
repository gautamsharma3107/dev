"""
Day 33 - Text Preprocessing
============================
Learn: Tokenization, padding, text normalization

Key Concepts:
- Text preprocessing is the first step in any NLP pipeline
- Tokenization breaks text into smaller units (words, sentences)
- Padding ensures all sequences have the same length for neural networks
- Normalization includes lowercasing, removing punctuation, stemming, lemmatization
"""

import re
import string

# ========== BASIC TEXT PREPROCESSING ==========
print("=" * 60)
print("BASIC TEXT PREPROCESSING")
print("=" * 60)

# Sample text
text = "Hello World! This is my first NLP tutorial. It's amazing!"

# 1. Lowercasing
text_lower = text.lower()
print(f"Original: {text}")
print(f"Lowercase: {text_lower}")

# 2. Remove punctuation
text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
print(f"No punctuation: {text_no_punct}")

# 3. Simple word splitting
words = text_lower.split()
print(f"Simple split: {words}")

# ========== NLTK TOKENIZATION ==========
print("\n" + "=" * 60)
print("NLTK TOKENIZATION")
print("=" * 60)

try:
    import nltk
    # Download required resources (run once)
    # nltk.download('punkt')
    # nltk.download('stopwords')
    # nltk.download('wordnet')
    
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer, WordNetLemmatizer
    
    # Word tokenization
    sample_text = "Hello world! This is NLP processing. It's very exciting."
    words = word_tokenize(sample_text)
    print(f"Word tokens: {words}")
    
    # Sentence tokenization
    sentences = sent_tokenize(sample_text)
    print(f"Sentence tokens: {sentences}")
    
    # Stopword removal
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words if w.lower() not in stop_words and w.isalpha()]
    print(f"After stopword removal: {filtered_words}")
    
    # Stemming (reduces words to their root form)
    stemmer = PorterStemmer()
    words_to_stem = ["running", "runs", "ran", "runner", "easily", "fairly"]
    stemmed = [stemmer.stem(w) for w in words_to_stem]
    print(f"Stemming: {list(zip(words_to_stem, stemmed))}")
    
    # Lemmatization (more accurate than stemming)
    lemmatizer = WordNetLemmatizer()
    words_to_lemmatize = ["running", "runs", "better", "geese", "feet"]
    lemmatized = [lemmatizer.lemmatize(w) for w in words_to_lemmatize]
    print(f"Lemmatization: {list(zip(words_to_lemmatize, lemmatized))}")
    
except ImportError:
    print("NLTK not installed. Run: pip install nltk")
    print("Then: python -m nltk.downloader punkt stopwords wordnet")

# ========== KERAS TEXT PREPROCESSING ==========
print("\n" + "=" * 60)
print("KERAS TEXT PREPROCESSING")
print("=" * 60)

try:
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    
    # Sample texts
    texts = [
        "I love machine learning",
        "Deep learning is amazing",
        "Natural language processing is fun",
        "I love NLP and AI",
        "This is great"
    ]
    
    # Create tokenizer
    tokenizer = Tokenizer(num_words=100)  # Keep top 100 words
    tokenizer.fit_on_texts(texts)
    
    # Get word index
    word_index = tokenizer.word_index
    print(f"Word index: {word_index}")
    
    # Convert texts to sequences
    sequences = tokenizer.texts_to_sequences(texts)
    print(f"\nOriginal texts: {texts}")
    print(f"Sequences: {sequences}")
    
    # Padding sequences (making them same length)
    max_length = 5
    padded = pad_sequences(sequences, maxlen=max_length, padding='post')
    print(f"\nPadded sequences (maxlen={max_length}):")
    for text, seq in zip(texts, padded):
        print(f"  '{text}' -> {seq}")
    
    # Pre-padding (default)
    padded_pre = pad_sequences(sequences, maxlen=max_length, padding='pre')
    print(f"\nPre-padded sequences:")
    for text, seq in zip(texts, padded_pre):
        print(f"  '{text}' -> {seq}")
    
    # Truncating long sequences
    long_text = ["I love machine learning and deep learning very much"]
    tokenizer.fit_on_texts(long_text)
    long_seq = tokenizer.texts_to_sequences(long_text)
    truncated = pad_sequences(long_seq, maxlen=5, truncating='post')
    print(f"\nTruncated sequence: {truncated}")

except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")

# ========== REGEX TEXT CLEANING ==========
print("\n" + "=" * 60)
print("REGEX TEXT CLEANING")
print("=" * 60)

def clean_text(text):
    """Clean text using regex patterns"""
    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove mentions (@username)
    text = re.sub(r'@\w+', '', text)
    # Remove hashtags
    text = re.sub(r'#\w+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Test cleaning
dirty_texts = [
    "Check out https://example.com #NLP @user123",
    "I love Python! 🐍 It's the best language 💯",
    "<html><body>HTML content here</body></html>",
    "Contact: test@email.com or call 123-456-7890"
]

print("Text cleaning examples:")
for text in dirty_texts:
    print(f"  Original: {text}")
    print(f"  Cleaned:  {clean_text(text)}\n")

# ========== FULL PREPROCESSING PIPELINE ==========
print("=" * 60)
print("FULL PREPROCESSING PIPELINE")
print("=" * 60)

def preprocess_text(text, remove_stopwords=True, lemmatize=True):
    """
    Complete text preprocessing pipeline
    """
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove URLs, mentions, hashtags
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    
    # 3. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # 4. Remove special characters but keep letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 5. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # 6. Tokenize
    try:
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        
        tokens = word_tokenize(text)
        
        # 7. Remove stopwords (optional)
        if remove_stopwords:
            stop_words = set(stopwords.words('english'))
            tokens = [t for t in tokens if t not in stop_words]
        
        # 8. Lemmatize (optional)
        if lemmatize:
            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(t) for t in tokens]
        
        return ' '.join(tokens)
    except ImportError:
        return text

# Test full pipeline
sample_tweets = [
    "I absolutely LOVE this product! 🎉 Best purchase ever! https://buy.now #happy @brand",
    "Terrible experience 😡 Never buying again! Support was awful @support #fail",
    "Just finished my first ML model! So excited to learn more about AI 🤖 #machinelearning"
]

print("\nFull preprocessing pipeline:")
for tweet in sample_tweets:
    print(f"Original: {tweet}")
    print(f"Processed: {preprocess_text(tweet)}\n")

# ========== PRACTICAL EXAMPLE ==========
print("=" * 60)
print("PRACTICAL EXAMPLE: Preparing Data for ML")
print("=" * 60)

try:
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    import numpy as np
    
    # Sample dataset (text and labels)
    data = [
        ("I love this movie, it was amazing!", 1),
        ("This is the worst product ever", 0),
        ("Great service and friendly staff", 1),
        ("Terrible experience, very disappointed", 0),
        ("Absolutely fantastic, highly recommend", 1),
        ("Waste of money, don't buy this", 0),
    ]
    
    # Separate texts and labels
    texts = [d[0] for d in data]
    labels = [d[1] for d in data]
    
    # Preprocess texts
    processed_texts = [preprocess_text(t) for t in texts]
    
    # Tokenize
    tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
    tokenizer.fit_on_texts(processed_texts)
    sequences = tokenizer.texts_to_sequences(processed_texts)
    
    # Pad sequences
    max_len = 10
    X = pad_sequences(sequences, maxlen=max_len, padding='post')
    y = np.array(labels)
    
    print("Data prepared for ML:")
    print(f"Vocabulary size: {len(tokenizer.word_index)}")
    print(f"X shape: {X.shape}")
    print(f"y shape: {y.shape}")
    print(f"\nSample processed data:")
    for i in range(min(3, len(texts))):
        print(f"  Text: {texts[i]}")
        print(f"  Processed: {processed_texts[i]}")
        print(f"  Sequence: {X[i]}")
        print(f"  Label: {y[i]}\n")

except ImportError as e:
    print(f"Import error: {e}")
    print("Install required packages with: pip install tensorflow numpy")

print("\n" + "=" * 60)
print("✅ Text Preprocessing - Complete!")
print("=" * 60)
