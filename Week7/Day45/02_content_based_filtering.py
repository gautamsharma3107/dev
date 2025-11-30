"""
Day 45 - Content-Based Filtering
================================
Learn: Feature extraction, TF-IDF, Cosine similarity

Key Concepts:
- Content-based filtering recommends items similar to what user liked
- Uses item features/attributes instead of user behavior
- TF-IDF: Term Frequency-Inverse Document Frequency for text
- Cosine similarity measures angle between feature vectors
"""

import numpy as np
from collections import Counter
import re

# ========== MOVIE DATASET ==========
print("=" * 60)
print("MOVIE DATASET FOR CONTENT-BASED FILTERING")
print("=" * 60)

# Movie database with features
movies = [
    {
        "id": 0,
        "title": "The Matrix",
        "genres": ["Action", "Sci-Fi"],
        "director": "Wachowski",
        "description": "A computer hacker learns about the true nature of reality and his role in the war against its controllers.",
        "year": 1999
    },
    {
        "id": 1,
        "title": "Inception",
        "genres": ["Action", "Sci-Fi", "Thriller"],
        "director": "Nolan",
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the task of planting an idea.",
        "year": 2010
    },
    {
        "id": 2,
        "title": "Titanic",
        "genres": ["Drama", "Romance"],
        "director": "Cameron",
        "description": "A seventeen-year-old aristocrat falls in love with a poor artist aboard the luxurious Titanic.",
        "year": 1997
    },
    {
        "id": 3,
        "title": "The Notebook",
        "genres": ["Drama", "Romance"],
        "director": "Cassavetes",
        "description": "A poor young man falls in love with a rich young woman, giving her a sense of freedom.",
        "year": 2004
    },
    {
        "id": 4,
        "title": "Interstellar",
        "genres": ["Adventure", "Drama", "Sci-Fi"],
        "director": "Nolan",
        "description": "A team of explorers travel through a wormhole in space to ensure humanity's survival.",
        "year": 2014
    },
    {
        "id": 5,
        "title": "The Dark Knight",
        "genres": ["Action", "Crime", "Drama"],
        "director": "Nolan",
        "description": "Batman raises the stakes in his war on crime fighting the menacing Joker.",
        "year": 2008
    },
    {
        "id": 6,
        "title": "Avengers",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "director": "Whedon",
        "description": "Earth's mightiest heroes must come together to stop an alien invasion.",
        "year": 2012
    },
    {
        "id": 7,
        "title": "Pride and Prejudice",
        "genres": ["Drama", "Romance"],
        "director": "Wright",
        "description": "A spirited young woman and a proud man overcome their prejudices.",
        "year": 2005
    }
]

print("Movies in database:")
for movie in movies:
    print(f"  {movie['id']}. {movie['title']} ({movie['year']}) - {', '.join(movie['genres'])}")

# ========== FEATURE EXTRACTION ==========
print("\n" + "=" * 60)
print("FEATURE EXTRACTION")
print("=" * 60)

# Get all unique genres
all_genres = set()
for movie in movies:
    all_genres.update(movie["genres"])
all_genres = sorted(list(all_genres))
print(f"\nAll genres: {all_genres}")

def get_genre_vector(movie_genres):
    """Create binary vector for genres."""
    return [1 if genre in movie_genres else 0 for genre in all_genres]

# Create genre vectors
genre_vectors = []
print("\nGenre Vectors:")
for movie in movies:
    vector = get_genre_vector(movie["genres"])
    genre_vectors.append(vector)
    print(f"{movie['title']}: {vector}")

genre_vectors = np.array(genre_vectors)

# ========== COSINE SIMILARITY ==========
print("\n" + "=" * 60)
print("COSINE SIMILARITY")
print("=" * 60)

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0
    
    return dot_product / (norm1 * norm2)

# Calculate similarity matrix
print("\nCalculating movie similarity based on genres...")
n_movies = len(movies)
similarity_matrix = np.zeros((n_movies, n_movies))

for i in range(n_movies):
    for j in range(n_movies):
        similarity_matrix[i][j] = cosine_similarity(genre_vectors[i], genre_vectors[j])

print("\nSimilarity Matrix:")
print("      ", end="")
for m in movies:
    print(f"{m['title'][:8]:>10}", end="")
print()

for i, movie in enumerate(movies):
    print(f"{movie['title'][:6]:>6}", end="")
    for j in range(n_movies):
        print(f"{similarity_matrix[i][j]:>10.2f}", end="")
    print()

# ========== TF-IDF FOR TEXT ==========
print("\n" + "=" * 60)
print("TF-IDF (Term Frequency-Inverse Document Frequency)")
print("=" * 60)

def preprocess_text(text):
    """Clean and tokenize text."""
    # Convert to lowercase and split
    words = re.findall(r'\b[a-z]+\b', text.lower())
    # Remove common stop words
    stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
                  'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be',
                  'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
                  'will', 'would', 'could', 'should', 'may', 'might', 'must',
                  'through', 'his', 'her', 'their', 'who', 'against', 'about'}
    return [w for w in words if w not in stop_words]

def calculate_tf(document):
    """Calculate term frequency."""
    word_count = Counter(document)
    total_words = len(document)
    return {word: count / total_words for word, count in word_count.items()}

def calculate_idf(documents):
    """Calculate inverse document frequency."""
    n_docs = len(documents)
    all_words = set()
    for doc in documents:
        all_words.update(doc)
    
    idf = {}
    for word in all_words:
        doc_count = sum(1 for doc in documents if word in doc)
        idf[word] = np.log(n_docs / (1 + doc_count)) + 1
    return idf

def calculate_tfidf(documents):
    """Calculate TF-IDF vectors for documents."""
    # Preprocess all documents
    processed_docs = [preprocess_text(doc) for doc in documents]
    
    # Calculate IDF
    idf = calculate_idf(processed_docs)
    
    # Get vocabulary
    vocabulary = sorted(list(idf.keys()))
    
    # Calculate TF-IDF for each document
    tfidf_vectors = []
    for doc in processed_docs:
        tf = calculate_tf(doc)
        vector = [tf.get(word, 0) * idf[word] for word in vocabulary]
        tfidf_vectors.append(vector)
    
    return np.array(tfidf_vectors), vocabulary

# Get descriptions
descriptions = [movie["description"] for movie in movies]

print("\nCalculating TF-IDF vectors from movie descriptions...")
tfidf_vectors, vocabulary = calculate_tfidf(descriptions)

print(f"\nVocabulary size: {len(vocabulary)}")
print(f"Sample vocabulary: {vocabulary[:10]}...")

# Calculate similarity based on descriptions
print("\nCalculating similarity based on descriptions...")
desc_similarity = np.zeros((n_movies, n_movies))

for i in range(n_movies):
    for j in range(n_movies):
        desc_similarity[i][j] = cosine_similarity(tfidf_vectors[i], tfidf_vectors[j])

print("\nTop 3 similar movies for each movie (by description):")
for i, movie in enumerate(movies):
    similarities = [(j, desc_similarity[i][j]) for j in range(n_movies) if i != j]
    similarities.sort(key=lambda x: x[1], reverse=True)
    print(f"\n{movie['title']}:")
    for j, sim in similarities[:3]:
        print(f"  - {movies[j]['title']}: {sim:.3f}")

# ========== COMBINED CONTENT FEATURES ==========
print("\n" + "=" * 60)
print("COMBINED CONTENT FEATURES")
print("=" * 60)

def create_combined_features(movie):
    """Create combined feature string for a movie."""
    features = []
    features.extend(movie["genres"])
    features.append(movie["director"])
    features.extend(preprocess_text(movie["description"]))
    return " ".join(features)

combined_features = [create_combined_features(m) for m in movies]
print("\nCombined features example:")
print(f"{movies[0]['title']}: {combined_features[0][:100]}...")

# Calculate TF-IDF on combined features
combined_tfidf, combined_vocab = calculate_tfidf(combined_features)

# Calculate combined similarity
combined_similarity = np.zeros((n_movies, n_movies))
for i in range(n_movies):
    for j in range(n_movies):
        combined_similarity[i][j] = cosine_similarity(combined_tfidf[i], combined_tfidf[j])

print("\nTop 3 similar movies for each movie (combined features):")
for i, movie in enumerate(movies):
    similarities = [(j, combined_similarity[i][j]) for j in range(n_movies) if i != j]
    similarities.sort(key=lambda x: x[1], reverse=True)
    print(f"\n{movie['title']}:")
    for j, sim in similarities[:3]:
        print(f"  - {movies[j]['title']}: {sim:.3f}")

# ========== CONTENT-BASED RECOMMENDATIONS ==========
print("\n" + "=" * 60)
print("CONTENT-BASED RECOMMENDATIONS")
print("=" * 60)

def get_content_recommendations(user_liked_movies, n=3):
    """
    Get recommendations based on movies user has liked.
    user_liked_movies: list of movie indices user has liked
    """
    # Calculate average similarity to liked movies
    avg_similarity = np.zeros(n_movies)
    
    for i in range(n_movies):
        if i not in user_liked_movies:
            # Average similarity to all liked movies
            avg_similarity[i] = np.mean([combined_similarity[i][j] 
                                         for j in user_liked_movies])
    
    # Get top n recommendations
    recommendations = [(i, avg_similarity[i]) for i in range(n_movies) 
                      if i not in user_liked_movies]
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations[:n]

# Example: User likes The Matrix and Inception
user_likes = [0, 1]  # The Matrix, Inception
print(f"\nUser liked: {[movies[i]['title'] for i in user_likes]}")
print("\nRecommendations:")

recs = get_content_recommendations(user_likes)
for movie_idx, score in recs:
    print(f"  - {movies[movie_idx]['title']}: Score = {score:.3f}")

# Example: User likes Romance movies
user_likes = [2, 3]  # Titanic, The Notebook
print(f"\nUser liked: {[movies[i]['title'] for i in user_likes]}")
print("\nRecommendations:")

recs = get_content_recommendations(user_likes)
for movie_idx, score in recs:
    print(f"  - {movies[movie_idx]['title']}: Score = {score:.3f}")

# ========== USER PROFILE BASED ==========
print("\n" + "=" * 60)
print("USER PROFILE-BASED RECOMMENDATIONS")
print("=" * 60)

def build_user_profile(user_ratings):
    """
    Build user profile based on rated items.
    user_ratings: dict of {movie_idx: rating}
    """
    # Weight features by user ratings
    profile = np.zeros(len(combined_vocab))
    
    for movie_idx, rating in user_ratings.items():
        # Normalize rating to 0-1 scale
        weight = (rating - 1) / 4  # Assuming 1-5 scale
        profile += weight * combined_tfidf[movie_idx]
    
    # Normalize profile
    norm = np.linalg.norm(profile)
    if norm > 0:
        profile = profile / norm
    
    return profile

def recommend_from_profile(user_profile, rated_movies, n=3):
    """Recommend movies based on user profile."""
    scores = []
    
    for i in range(n_movies):
        if i not in rated_movies:
            score = cosine_similarity(user_profile, combined_tfidf[i])
            scores.append((i, score))
    
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:n]

# Example user ratings
user_ratings = {
    0: 5,  # The Matrix: 5 stars
    1: 4,  # Inception: 4 stars
    5: 5,  # The Dark Knight: 5 stars
}

print("\nUser ratings:")
for movie_idx, rating in user_ratings.items():
    print(f"  - {movies[movie_idx]['title']}: {rating} stars")

user_profile = build_user_profile(user_ratings)
recommendations = recommend_from_profile(user_profile, set(user_ratings.keys()))

print("\nPersonalized recommendations:")
for movie_idx, score in recommendations:
    print(f"  - {movies[movie_idx]['title']}: Score = {score:.3f}")

print("\n" + "=" * 60)
print("✅ Content-Based Filtering - Complete!")
print("=" * 60)
