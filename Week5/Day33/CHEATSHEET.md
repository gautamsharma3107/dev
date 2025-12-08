# Day 33 Quick Reference Cheat Sheet

## Text Preprocessing
```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Tokenization
text = "Hello world! This is NLP."
words = word_tokenize(text)        # ['Hello', 'world', '!', 'This', 'is', 'NLP', '.']
sentences = sent_tokenize(text)    # ['Hello world!', 'This is NLP.']

# Lowercasing
text_lower = text.lower()

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered = [w for w in words if w.lower() not in stop_words]

# Stemming (reduces to root form)
stemmer = PorterStemmer()
stemmer.stem("running")  # "run"

# Lemmatization (meaningful root form)
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("running", pos='v')  # "run"
```

## Keras Text Preprocessing
```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Tokenization
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Padding
padded = pad_sequences(sequences, 
                       maxlen=100, 
                       padding='post',      # 'pre' or 'post'
                       truncating='post')   # 'pre' or 'post'

# Word index
word_index = tokenizer.word_index  # {'the': 1, 'a': 2, ...}
```

## Word Embeddings
```python
from tensorflow.keras.layers import Embedding

# Embedding layer
embedding = Embedding(input_dim=vocab_size,   # Size of vocabulary
                      output_dim=128,          # Embedding dimension
                      input_length=max_len)    # Length of input sequences

# Pre-trained embeddings (GloVe)
embedding_matrix = np.zeros((vocab_size, embedding_dim))
for word, i in word_index.items():
    if word in glove_vectors:
        embedding_matrix[i] = glove_vectors[word]

# Use pre-trained weights
embedding = Embedding(vocab_size, embedding_dim,
                      weights=[embedding_matrix],
                      trainable=False)
```

## RNN/LSTM Overview
```python
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Bidirectional

# Simple RNN
model.add(SimpleRNN(units=64, return_sequences=False))

# LSTM (better for long sequences)
model.add(LSTM(units=64, return_sequences=True))   # For stacking
model.add(LSTM(units=32, return_sequences=False))  # Final LSTM

# Bidirectional LSTM
model.add(Bidirectional(LSTM(64)))

# GRU (lighter alternative to LSTM)
model.add(GRU(units=64))
```

## Sentiment Analysis Model
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Dropout

model = Sequential([
    Embedding(vocab_size, 128, input_length=max_len),
    LSTM(64, dropout=0.2),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # Binary: positive/negative
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# For multi-class sentiment
model.add(Dense(num_classes, activation='softmax'))
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

## Text Classification Pipeline
```python
# 1. Load and preprocess data
texts = df['text'].values
labels = df['label'].values

# 2. Tokenize and pad
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)
X = pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=200)

# 3. Encode labels
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# 4. Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 5. Build and train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# 6. Predict
def predict_text(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=200)
    pred = model.predict(padded)
    return encoder.inverse_transform([pred.argmax()])[0]
```

## Common NLP Tasks
```python
# Named Entity Recognition (using spaCy)
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Apple is looking at buying U.K. startup")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Part-of-Speech Tagging (using NLTK)
from nltk import pos_tag
tokens = word_tokenize("The quick brown fox")
tagged = pos_tag(tokens)  # [('The', 'DT'), ('quick', 'JJ'), ...]

# Text Similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
```

## Common Parameters
| Parameter | Description | Common Values |
|-----------|-------------|---------------|
| `vocab_size` | Vocabulary size | 5000-50000 |
| `embedding_dim` | Embedding dimension | 50, 100, 200, 300 |
| `max_len` | Max sequence length | 100-500 |
| `lstm_units` | LSTM hidden units | 32, 64, 128 |
| `dropout` | Dropout rate | 0.2-0.5 |

## Evaluation Metrics
```python
from sklearn.metrics import classification_report, confusion_matrix

# Get predictions
y_pred = (model.predict(X_test) > 0.5).astype(int)

# Classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
print(confusion_matrix(y_test, y_pred))
```

---
**Keep this handy for quick reference!** 🚀
