"""
DAY 33 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 33 ASSESSMENT TEST - Intro to NLP & Text Processing")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What is the main purpose of tokenization in NLP?
a) To convert text to uppercase
b) To break text into smaller units (words, sentences)
c) To translate text to another language
d) To compress text data

Your answer: """)

print("""
Q2. What is the purpose of padding sequences in NLP?
a) To add extra words to short texts
b) To make all sequences the same length for neural networks
c) To improve text readability
d) To encrypt the text

Your answer: """)

print("""
Q3. Which of the following is NOT a common word embedding?
a) Word2Vec
b) GloVe
c) FastText
d) TF-IDF

Your answer: """)

print("""
Q4. What problem does LSTM solve that vanilla RNN struggles with?
a) Overfitting
b) Vanishing gradient problem
c) Data augmentation
d) Feature extraction

Your answer: """)

print("""
Q5. In an LSTM, what does the forget gate do?
a) Forgets the input data
b) Decides what information to discard from cell state
c) Outputs the final prediction
d) Creates new memory cells

Your answer: """)

print("""
Q6. What is sentiment analysis?
a) Detecting spam emails
b) Translating text between languages
c) Determining the emotional tone of text
d) Correcting grammar mistakes

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Complete the code to tokenize and pad text using Keras:

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

texts = ["I love NLP", "Deep learning is fun", "Text classification"]

# TODO: Create tokenizer with 100 words max
tokenizer = ______________________
tokenizer.fit_on_texts(texts)

# TODO: Convert texts to sequences
sequences = ______________________

# TODO: Pad sequences to length 5
padded = ______________________

print(padded)
""")

# Write your code here:


print("""
Q8. (2 points) Write code to create a simple LSTM model for binary classification:

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# TODO: Build model with:
# - Embedding layer (vocab_size=5000, embedding_dim=64, input_length=100)
# - LSTM layer with 32 units
# - Dense output layer with sigmoid activation

model = Sequential([
    # Your layers here
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
""")

# Write your code here:


print("""
Q9. (2 points) Complete the text preprocessing function:

import re
import string

def preprocess_text(text):
    '''
    Preprocess text by:
    1. Converting to lowercase
    2. Removing punctuation
    3. Removing extra whitespace
    '''
    # TODO: Convert to lowercase
    text = ______________________
    
    # TODO: Remove punctuation
    text = ______________________
    
    # TODO: Remove extra whitespace and strip
    text = ______________________
    
    return text

# Test
print(preprocess_text("Hello, WORLD!   How are   you?"))
# Expected: "hello world how are you"
""")

# Write your code here:


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between word embeddings and one-hot encoding.
Why are word embeddings preferred for NLP tasks?

Your answer:
""")

# Write your explanation here as comments:
# 


# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) To break text into smaller units (words, sentences)
Q2: b) To make all sequences the same length for neural networks
Q3: d) TF-IDF (it's a vectorization technique, not an embedding)
Q4: b) Vanishing gradient problem
Q5: b) Decides what information to discard from cell state
Q6: c) Determining the emotional tone of text

Section B (Coding):

Q7:
tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=5, padding='post')

Q8:
model = Sequential([
    Embedding(input_dim=5000, output_dim=64, input_length=100),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

Q9:
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\\s+', ' ', text).strip()
    return text

Section C:
Q10: 
One-hot encoding:
- Represents each word as a sparse vector with a single 1
- Vector dimension equals vocabulary size (very large)
- No semantic relationship between words
- "cat" and "dog" are equally different as "cat" and "car"

Word embeddings:
- Dense, low-dimensional vectors (50-300 dimensions)
- Similar words have similar vectors
- Capture semantic relationships
- Enable vector arithmetic (king - man + woman ≈ queen)
- Pre-trained embeddings transfer knowledge from large corpora

Word embeddings are preferred because they:
1. Are more memory efficient
2. Capture semantic meaning
3. Generalize better to new data
4. Enable transfer learning
"""
