"""
Day 45 - Collaborative Filtering
================================
Learn: User-based CF, Item-based CF, Matrix Factorization

Key Concepts:
- Collaborative filtering recommends items based on user behavior patterns
- User-based CF: Find similar users and recommend what they liked
- Item-based CF: Find similar items to what user already liked
- Matrix factorization: Decompose user-item matrix into latent factors
"""

import numpy as np
from collections import defaultdict

# ========== USER-ITEM RATINGS MATRIX ==========
print("=" * 60)
print("USER-ITEM RATINGS MATRIX")
print("=" * 60)

# Sample ratings: rows=users, columns=movies
# 0 means no rating
ratings = np.array([
    [5, 3, 0, 1, 4],  # User 0
    [4, 0, 0, 1, 5],  # User 1
    [1, 1, 0, 5, 4],  # User 2
    [0, 1, 5, 4, 0],  # User 3
    [5, 4, 1, 0, 4],  # User 4
])

movies = ["The Matrix", "Inception", "Titanic", "The Notebook", "Interstellar"]
users = ["Alice", "Bob", "Carol", "David", "Eve"]

print("Ratings Matrix (0 = not rated):")
print(f"Movies: {movies}")
print(f"Users: {users}")
print(ratings)

# ========== USER-BASED COLLABORATIVE FILTERING ==========
print("\n" + "=" * 60)
print("USER-BASED COLLABORATIVE FILTERING")
print("=" * 60)

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    # Only consider items rated by both users
    mask = (vec1 != 0) & (vec2 != 0)
    if not np.any(mask):
        return 0
    
    v1 = vec1[mask]
    v2 = vec2[mask]
    
    dot_product = np.dot(v1, v2)
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    
    if norm1 == 0 or norm2 == 0:
        return 0
    
    return dot_product / (norm1 * norm2)

def pearson_correlation(vec1, vec2):
    """Calculate Pearson correlation between two vectors."""
    mask = (vec1 != 0) & (vec2 != 0)
    if np.sum(mask) < 2:
        return 0
    
    v1 = vec1[mask]
    v2 = vec2[mask]
    
    mean1 = np.mean(v1)
    mean2 = np.mean(v2)
    
    numerator = np.sum((v1 - mean1) * (v2 - mean2))
    denominator = np.sqrt(np.sum((v1 - mean1)**2) * np.sum((v2 - mean2)**2))
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

print("\nCalculating User Similarities (Cosine):")
user_similarities = np.zeros((len(users), len(users)))

for i in range(len(users)):
    for j in range(len(users)):
        user_similarities[i][j] = cosine_similarity(ratings[i], ratings[j])

print("User Similarity Matrix:")
for i, user in enumerate(users):
    print(f"{user}: {np.round(user_similarities[i], 3)}")

def predict_user_based(user_idx, item_idx, k=2):
    """Predict rating using user-based CF."""
    if ratings[user_idx][item_idx] != 0:
        return ratings[user_idx][item_idx]
    
    # Get similarities with all other users
    similarities = user_similarities[user_idx].copy()
    similarities[user_idx] = 0  # Exclude self
    
    # Get top k similar users who rated this item
    rated_users = [(i, similarities[i]) for i in range(len(users)) 
                   if ratings[i][item_idx] != 0 and i != user_idx]
    rated_users.sort(key=lambda x: x[1], reverse=True)
    top_k = rated_users[:k]
    
    if not top_k:
        return 0
    
    # Weighted average
    numerator = sum(sim * ratings[user_i][item_idx] for user_i, sim in top_k)
    denominator = sum(abs(sim) for _, sim in top_k)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

print("\nUser-Based CF Predictions:")
print(f"Predicting Bob's rating for Inception (Movie 1):")
prediction = predict_user_based(1, 1)
print(f"Predicted rating: {prediction:.2f}")

print(f"\nPredicting Carol's rating for Inception (Movie 1):")
prediction = predict_user_based(2, 1)
print(f"Predicted rating: {prediction:.2f}")

# ========== ITEM-BASED COLLABORATIVE FILTERING ==========
print("\n" + "=" * 60)
print("ITEM-BASED COLLABORATIVE FILTERING")
print("=" * 60)

print("\nCalculating Item Similarities:")
item_similarities = np.zeros((len(movies), len(movies)))

for i in range(len(movies)):
    for j in range(len(movies)):
        # Get column vectors for items
        item_similarities[i][j] = cosine_similarity(ratings[:, i], ratings[:, j])

print("Item Similarity Matrix:")
for i, movie in enumerate(movies):
    print(f"{movie}: {np.round(item_similarities[i], 3)}")

def predict_item_based(user_idx, item_idx, k=2):
    """Predict rating using item-based CF."""
    if ratings[user_idx][item_idx] != 0:
        return ratings[user_idx][item_idx]
    
    # Get similarities with all other items
    similarities = item_similarities[item_idx].copy()
    similarities[item_idx] = 0  # Exclude self
    
    # Get top k similar items that user has rated
    rated_items = [(i, similarities[i]) for i in range(len(movies)) 
                   if ratings[user_idx][i] != 0 and i != item_idx]
    rated_items.sort(key=lambda x: x[1], reverse=True)
    top_k = rated_items[:k]
    
    if not top_k:
        return 0
    
    # Weighted average
    numerator = sum(sim * ratings[user_idx][item_i] for item_i, sim in top_k)
    denominator = sum(abs(sim) for _, sim in top_k)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

print("\nItem-Based CF Predictions:")
print(f"Predicting Bob's rating for Inception (Movie 1):")
prediction = predict_item_based(1, 1)
print(f"Predicted rating: {prediction:.2f}")

# ========== SIMPLE MATRIX FACTORIZATION ==========
print("\n" + "=" * 60)
print("MATRIX FACTORIZATION (SIMPLIFIED)")
print("=" * 60)

def matrix_factorization(R, K, steps=1000, alpha=0.002, beta=0.02):
    """
    Perform matrix factorization using gradient descent.
    R: user-item rating matrix
    K: number of latent factors
    alpha: learning rate
    beta: regularization parameter
    """
    num_users, num_items = R.shape
    
    # Initialize user and item latent factor matrices
    P = np.random.rand(num_users, K)  # User latent factors
    Q = np.random.rand(num_items, K)  # Item latent factors
    
    # Convert to list of training samples
    samples = [
        (i, j, R[i][j])
        for i in range(num_users)
        for j in range(num_items)
        if R[i][j] > 0
    ]
    
    # Training
    for step in range(steps):
        np.random.shuffle(samples)
        for i, j, r in samples:
            # Calculate prediction and error
            prediction = np.dot(P[i, :], Q[j, :])
            error = r - prediction
            
            # Update P and Q
            P[i, :] += alpha * (2 * error * Q[j, :] - beta * P[i, :])
            Q[j, :] += alpha * (2 * error * P[i, :] - beta * Q[j, :])
    
    return P, Q

print("\nTraining Matrix Factorization model...")
P, Q = matrix_factorization(ratings, K=2, steps=5000)

# Predict all ratings
predicted_ratings = np.dot(P, Q.T)
print("\nPredicted Ratings Matrix:")
print(np.round(predicted_ratings, 2))

print("\nOriginal vs Predicted for known ratings:")
for i in range(len(users)):
    for j in range(len(movies)):
        if ratings[i][j] > 0:
            print(f"{users[i]} - {movies[j]}: Actual={ratings[i][j]}, "
                  f"Predicted={predicted_ratings[i][j]:.2f}")

# ========== RECOMMENDATIONS ==========
print("\n" + "=" * 60)
print("GENERATING RECOMMENDATIONS")
print("=" * 60)

def get_recommendations(user_idx, predicted_matrix, n=3):
    """Get top n recommendations for a user."""
    user_ratings = predicted_matrix[user_idx]
    original_ratings = ratings[user_idx]
    
    # Only consider unrated items
    recommendations = []
    for i, (pred, orig) in enumerate(zip(user_ratings, original_ratings)):
        if orig == 0:  # Not rated
            recommendations.append((i, pred))
    
    # Sort by predicted rating
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations[:n]

print("\nTop Recommendations for each user:")
for i, user in enumerate(users):
    recs = get_recommendations(i, predicted_ratings)
    print(f"\n{user}'s recommendations:")
    for movie_idx, pred_rating in recs:
        print(f"  - {movies[movie_idx]}: Predicted rating = {pred_rating:.2f}")

# ========== EVALUATION METRICS ==========
print("\n" + "=" * 60)
print("EVALUATION METRICS")
print("=" * 60)

def rmse(actual, predicted):
    """Calculate Root Mean Square Error."""
    mask = actual > 0
    return np.sqrt(np.mean((actual[mask] - predicted[mask]) ** 2))

def mae(actual, predicted):
    """Calculate Mean Absolute Error."""
    mask = actual > 0
    return np.mean(np.abs(actual[mask] - predicted[mask]))

rmse_value = rmse(ratings, predicted_ratings)
mae_value = mae(ratings, predicted_ratings)

print(f"RMSE (Root Mean Square Error): {rmse_value:.4f}")
print(f"MAE (Mean Absolute Error): {mae_value:.4f}")
print("\nLower values indicate better predictions!")

print("\n" + "=" * 60)
print("✅ Collaborative Filtering - Complete!")
print("=" * 60)
