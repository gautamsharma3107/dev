"""
EXERCISES: Text Preprocessing
=============================
Complete all 5 exercises below
"""

# Exercise 1: Basic Text Cleaning
# TODO: Write a function that:
# - Converts text to lowercase
# - Removes URLs
# - Removes mentions (@username)
# - Removes hashtags (#topic)
# - Removes extra whitespace

print("Exercise 1: Basic Text Cleaning")
print("-" * 40)

import re

def clean_social_text(text):
    """Clean social media text"""
    # Your code here
    pass

# Test your function
test_texts = [
    "Check out https://example.com #NLP @user123",
    "I LOVE this product!!! @company #best",
    "Visit www.test.com for more info #deals"
]

for text in test_texts:
    print(f"Original: {text}")
    print(f"Cleaned: {clean_social_text(text)}\n")


# Exercise 2: Stopword Removal
# TODO: Implement stopword removal without using NLTK
# Create your own list of common English stopwords

print("\n\nExercise 2: Stopword Removal")
print("-" * 40)

def remove_stopwords(text):
    """Remove common English stopwords from text"""
    # Your stopwords list
    stopwords = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                 'would', 'could', 'should', 'may', 'might', 'can', 'to', 'of',
                 'in', 'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
                 'through', 'during', 'before', 'after', 'above', 'below',
                 'this', 'that', 'these', 'those', 'it', 'its'}
    
    # Your code here
    pass

# Test
test_sentence = "The quick brown fox jumps over the lazy dog"
print(f"Original: {test_sentence}")
print(f"Without stopwords: {remove_stopwords(test_sentence)}")


# Exercise 3: Simple Stemming
# TODO: Implement a basic stemming function that removes common suffixes
# Handle: -ing, -ed, -ly, -tion, -ness

print("\n\nExercise 3: Simple Stemming")
print("-" * 40)

def simple_stem(word):
    """Remove common suffixes from a word"""
    # Your code here
    pass

# Test
words = ["running", "walked", "quickly", "education", "happiness", "playing"]
for word in words:
    print(f"{word} -> {simple_stem(word)}")


# Exercise 4: N-gram Generation
# TODO: Write a function that generates n-grams from text

print("\n\nExercise 4: N-gram Generation")
print("-" * 40)

def generate_ngrams(text, n):
    """Generate n-grams from text"""
    # Your code here
    pass

# Test
text = "I love natural language processing"
print(f"Text: {text}")
print(f"Unigrams: {generate_ngrams(text, 1)}")
print(f"Bigrams: {generate_ngrams(text, 2)}")
print(f"Trigrams: {generate_ngrams(text, 3)}")


# Exercise 5: Complete Preprocessing Pipeline
# TODO: Combine all preprocessing steps into one function

print("\n\nExercise 5: Complete Preprocessing Pipeline")
print("-" * 40)

def preprocess_pipeline(text, remove_stops=True, stem=True):
    """
    Complete text preprocessing pipeline:
    1. Lowercase
    2. Remove URLs, mentions, hashtags
    3. Remove punctuation
    4. Remove stopwords (if enabled)
    5. Stem words (if enabled)
    6. Remove extra whitespace
    """
    # Your code here
    pass

# Test
sample_texts = [
    "Check out @TechNews for the LATEST updates! https://news.com #technology",
    "The meeting was CANCELLED due to weather conditions!!! #update",
    "Running quickly through the forest was exhilarating!"
]

for text in sample_texts:
    print(f"Original: {text}")
    print(f"Processed: {preprocess_pipeline(text)}\n")
