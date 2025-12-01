"""
EXERCISES: Word Embeddings
==========================
Complete all 5 exercises below
"""

import numpy as np

# Exercise 1: Cosine Similarity
# TODO: Implement cosine similarity function to compare vectors

print("Exercise 1: Cosine Similarity")
print("-" * 40)

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    # Your code here
    pass

# Test with sample vectors
vec_a = np.array([1, 2, 3, 4])
vec_b = np.array([1, 2, 3, 5])
vec_c = np.array([-1, -2, -3, -4])

print(f"Similarity(a, b): {cosine_similarity(vec_a, vec_b)}")  # Should be close to 1
print(f"Similarity(a, c): {cosine_similarity(vec_a, vec_c)}")  # Should be -1


# Exercise 2: Find Most Similar Word
# TODO: Given a word and a dictionary of embeddings, find the most similar word

print("\n\nExercise 2: Find Most Similar Word")
print("-" * 40)

# Sample embeddings
embeddings = {
    'king': np.array([0.9, 0.7, 0.3, 0.5]),
    'queen': np.array([0.8, 0.8, 0.3, 0.5]),
    'man': np.array([0.9, 0.2, 0.5, 0.3]),
    'woman': np.array([0.8, 0.3, 0.5, 0.3]),
    'prince': np.array([0.85, 0.6, 0.35, 0.4]),
    'princess': np.array([0.75, 0.65, 0.35, 0.4]),
    'boy': np.array([0.85, 0.15, 0.6, 0.2]),
    'girl': np.array([0.75, 0.2, 0.6, 0.2]),
}

def find_most_similar(word, embeddings, top_n=3):
    """Find the top_n most similar words to the given word"""
    # Your code here
    pass

# Test
print(f"Most similar to 'king': {find_most_similar('king', embeddings)}")
print(f"Most similar to 'woman': {find_most_similar('woman', embeddings)}")


# Exercise 3: Word Analogy
# TODO: Implement word analogy: a is to b as c is to ?
# Example: king is to queen as man is to ? (answer: woman)

print("\n\nExercise 3: Word Analogy")
print("-" * 40)

def word_analogy(a, b, c, embeddings):
    """
    Find word d such that: a is to b as c is to d
    d = b - a + c
    """
    # Your code here
    pass

# Test
print(f"king is to queen as man is to: {word_analogy('king', 'queen', 'man', embeddings)}")
print(f"man is to woman as boy is to: {word_analogy('man', 'woman', 'boy', embeddings)}")


# Exercise 4: Keras Embedding Layer
# TODO: Create a model with embedding layer and examine the embeddings

print("\n\nExercise 4: Keras Embedding Layer")
print("-" * 40)

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, Flatten, Dense
    
    # TODO: Create a model with:
    # - Embedding layer (vocab_size=100, embedding_dim=16, input_length=10)
    # - Flatten layer
    # - Dense layer with 1 unit and sigmoid activation
    
    def create_embedding_model():
        """Create a model with embedding layer"""
        # Your code here
        pass
    
    model = create_embedding_model()
    if model:
        model.summary()
    
except ImportError:
    print("TensorFlow not installed")


# Exercise 5: Visualize Embeddings (Conceptual)
# TODO: Write code to reduce embedding dimensions and prepare for visualization

print("\n\nExercise 5: Prepare Embeddings for Visualization")
print("-" * 40)

def prepare_embeddings_for_visualization(embeddings_dict):
    """
    Prepare embeddings for 2D visualization:
    1. Extract words and vectors
    2. Apply dimensionality reduction (use numpy for simple projection)
    Return: words list, 2D coordinates
    """
    # Your code here
    # Hint: For simplicity, just take first 2 dimensions
    # In real applications, use PCA or t-SNE
    pass

# Test
words, coords = prepare_embeddings_for_visualization(embeddings) if prepare_embeddings_for_visualization(embeddings) else (None, None)
if words and coords is not None:
    print("Embedding positions (first 2 dimensions):")
    for word, coord in zip(words, coords):
        print(f"  {word}: ({coord[0]:.2f}, {coord[1]:.2f})")
