"""
Day 45 - Building Recommender Systems
=====================================
Learn: Hybrid approaches, Evaluation metrics, Cold start problem

Key Concepts:
- Hybrid recommenders combine collaborative and content-based filtering
- Evaluation metrics: RMSE, MAE, Precision, Recall, F1
- Cold start: Challenge of recommending for new users/items
- Cross-validation for robust evaluation
"""

import numpy as np
from collections import defaultdict

# ========== SAMPLE DATA ==========
print("=" * 60)
print("SETTING UP DATA FOR RECOMMENDER SYSTEM")
print("=" * 60)

# Movies with features
movies = {
    0: {"title": "The Matrix", "genres": ["Action", "Sci-Fi"], "year": 1999},
    1: {"title": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"], "year": 2010},
    2: {"title": "Titanic", "genres": ["Drama", "Romance"], "year": 1997},
    3: {"title": "The Notebook", "genres": ["Drama", "Romance"], "year": 2004},
    4: {"title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"], "year": 2014},
    5: {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"], "year": 2008},
    6: {"title": "Avengers", "genres": ["Action", "Adventure", "Sci-Fi"], "year": 2012},
    7: {"title": "Pride and Prejudice", "genres": ["Drama", "Romance"], "year": 2005},
}

# User ratings
ratings = {
    "Alice": {0: 5, 1: 4, 4: 5, 5: 4},
    "Bob": {0: 4, 1: 5, 5: 5, 6: 4},
    "Carol": {2: 5, 3: 5, 7: 4},
    "David": {0: 3, 2: 4, 3: 5, 4: 3},
    "Eve": {1: 4, 4: 5, 6: 4},
    "Frank": {2: 5, 3: 4, 7: 5},
}

print("Users and their ratings:")
for user, user_ratings in ratings.items():
    rated = [(movies[m]["title"], r) for m, r in user_ratings.items()]
    print(f"\n{user}:")
    for title, rating in rated:
        print(f"  - {title}: {rating} stars")

# ========== HELPER FUNCTIONS ==========
all_genres = set()
for movie in movies.values():
    all_genres.update(movie["genres"])
all_genres = sorted(list(all_genres))

def get_genre_vector(movie_genres):
    """Create binary genre vector."""
    return np.array([1 if g in movie_genres else 0 for g in all_genres])

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity."""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot_product / (norm1 * norm2)

# ========== COLLABORATIVE FILTERING COMPONENT ==========
print("\n" + "=" * 60)
print("COLLABORATIVE FILTERING COMPONENT")
print("=" * 60)

class CollaborativeFilter:
    def __init__(self, ratings, movies):
        self.ratings = ratings
        self.movies = movies
        self.users = list(ratings.keys())
        self.user_similarity = {}
        self._calculate_user_similarity()
    
    def _calculate_user_similarity(self):
        """Calculate similarity between all user pairs."""
        for user1 in self.users:
            self.user_similarity[user1] = {}
            for user2 in self.users:
                if user1 != user2:
                    self.user_similarity[user1][user2] = self._pearson_correlation(user1, user2)
    
    def _pearson_correlation(self, user1, user2):
        """Calculate Pearson correlation between two users."""
        common_items = set(self.ratings[user1].keys()) & set(self.ratings[user2].keys())
        if len(common_items) < 2:
            return 0
        
        ratings1 = [self.ratings[user1][i] for i in common_items]
        ratings2 = [self.ratings[user2][i] for i in common_items]
        
        mean1 = np.mean(ratings1)
        mean2 = np.mean(ratings2)
        
        numerator = sum((r1 - mean1) * (r2 - mean2) for r1, r2 in zip(ratings1, ratings2))
        denom1 = np.sqrt(sum((r - mean1) ** 2 for r in ratings1))
        denom2 = np.sqrt(sum((r - mean2) ** 2 for r in ratings2))
        
        if denom1 == 0 or denom2 == 0:
            return 0
        
        return numerator / (denom1 * denom2)
    
    def predict(self, user, item, k=3):
        """Predict rating for user-item pair."""
        if item in self.ratings.get(user, {}):
            return self.ratings[user][item]
        
        # Find k most similar users who rated this item
        similar_users = []
        for other_user in self.users:
            if other_user != user and item in self.ratings[other_user]:
                sim = self.user_similarity[user].get(other_user, 0)
                if sim > 0:
                    similar_users.append((other_user, sim))
        
        similar_users.sort(key=lambda x: x[1], reverse=True)
        top_k = similar_users[:k]
        
        if not top_k:
            # Return user's average rating
            if self.ratings.get(user):
                return np.mean(list(self.ratings[user].values()))
            return 3.0  # Default
        
        # Weighted average
        numerator = sum(sim * self.ratings[other][item] for other, sim in top_k)
        denominator = sum(sim for _, sim in top_k)
        
        return numerator / denominator if denominator > 0 else 3.0

cf = CollaborativeFilter(ratings, movies)
print("\nCollaborative Filtering predictions:")
print(f"Alice's predicted rating for Titanic: {cf.predict('Alice', 2):.2f}")
print(f"Bob's predicted rating for The Notebook: {cf.predict('Bob', 3):.2f}")

# ========== CONTENT-BASED COMPONENT ==========
print("\n" + "=" * 60)
print("CONTENT-BASED FILTERING COMPONENT")
print("=" * 60)

class ContentBasedFilter:
    def __init__(self, ratings, movies):
        self.ratings = ratings
        self.movies = movies
        self.movie_vectors = {m: get_genre_vector(movies[m]["genres"]) 
                             for m in movies}
        self.movie_similarity = {}
        self._calculate_movie_similarity()
    
    def _calculate_movie_similarity(self):
        """Calculate similarity between all movie pairs."""
        movie_ids = list(self.movies.keys())
        for m1 in movie_ids:
            self.movie_similarity[m1] = {}
            for m2 in movie_ids:
                if m1 != m2:
                    self.movie_similarity[m1][m2] = cosine_similarity(
                        self.movie_vectors[m1], self.movie_vectors[m2]
                    )
    
    def build_user_profile(self, user):
        """Build user preference profile from ratings."""
        if user not in self.ratings:
            return np.zeros(len(all_genres))
        
        profile = np.zeros(len(all_genres))
        for movie_id, rating in self.ratings[user].items():
            weight = (rating - 3) / 2  # Normalize to -1 to 1
            profile += weight * self.movie_vectors[movie_id]
        
        norm = np.linalg.norm(profile)
        if norm > 0:
            profile = profile / norm
        
        return profile
    
    def predict(self, user, item):
        """Predict rating based on content similarity."""
        if item in self.ratings.get(user, {}):
            return self.ratings[user][item]
        
        user_profile = self.build_user_profile(user)
        item_vector = self.movie_vectors[item]
        
        # Similarity between user profile and item
        similarity = cosine_similarity(user_profile, item_vector)
        
        # Convert similarity (-1 to 1) to rating (1 to 5)
        predicted_rating = 3 + (similarity * 2)
        return max(1, min(5, predicted_rating))

cb = ContentBasedFilter(ratings, movies)
print("\nContent-Based Filtering predictions:")
print(f"Alice's predicted rating for Titanic: {cb.predict('Alice', 2):.2f}")
print(f"Bob's predicted rating for The Notebook: {cb.predict('Bob', 3):.2f}")

# ========== HYBRID RECOMMENDER ==========
print("\n" + "=" * 60)
print("HYBRID RECOMMENDER SYSTEM")
print("=" * 60)

class HybridRecommender:
    def __init__(self, ratings, movies, cf_weight=0.6, cb_weight=0.4):
        self.ratings = ratings
        self.movies = movies
        self.cf = CollaborativeFilter(ratings, movies)
        self.cb = ContentBasedFilter(ratings, movies)
        self.cf_weight = cf_weight
        self.cb_weight = cb_weight
    
    def predict(self, user, item):
        """Predict rating using weighted combination."""
        cf_pred = self.cf.predict(user, item)
        cb_pred = self.cb.predict(user, item)
        
        return self.cf_weight * cf_pred + self.cb_weight * cb_pred
    
    def recommend(self, user, n=3):
        """Get top n recommendations for user."""
        user_rated = set(self.ratings.get(user, {}).keys())
        
        predictions = []
        for movie_id in self.movies:
            if movie_id not in user_rated:
                pred = self.predict(user, movie_id)
                predictions.append((movie_id, pred))
        
        predictions.sort(key=lambda x: x[1], reverse=True)
        return predictions[:n]

hybrid = HybridRecommender(ratings, movies)

print("\nHybrid Recommender predictions:")
print(f"Alice's predicted rating for Titanic: {hybrid.predict('Alice', 2):.2f}")
print(f"Bob's predicted rating for The Notebook: {hybrid.predict('Bob', 3):.2f}")

print("\nRecommendations for each user:")
for user in ratings:
    recs = hybrid.recommend(user, n=3)
    print(f"\n{user}:")
    for movie_id, score in recs:
        print(f"  - {movies[movie_id]['title']}: {score:.2f}")

# ========== EVALUATION METRICS ==========
print("\n" + "=" * 60)
print("EVALUATION METRICS")
print("=" * 60)

def calculate_rmse(predictions, actual):
    """Calculate Root Mean Square Error."""
    errors = [(pred - act) ** 2 for pred, act in zip(predictions, actual)]
    return np.sqrt(np.mean(errors))

def calculate_mae(predictions, actual):
    """Calculate Mean Absolute Error."""
    errors = [abs(pred - act) for pred, act in zip(predictions, actual)]
    return np.mean(errors)

def calculate_precision_recall(recommended, relevant, k):
    """Calculate Precision@K and Recall@K."""
    recommended_k = set(recommended[:k])
    relevant_set = set(relevant)
    
    hits = len(recommended_k & relevant_set)
    
    precision = hits / k if k > 0 else 0
    recall = hits / len(relevant_set) if relevant_set else 0
    
    return precision, recall

def calculate_f1(precision, recall):
    """Calculate F1 score."""
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

# Evaluate using leave-one-out
print("\nLeave-One-Out Evaluation:")

predictions_list = []
actual_list = []

for user in ratings:
    for movie_id, actual_rating in ratings[user].items():
        # Temporarily remove this rating
        temp_ratings = {u: dict(r) for u, r in ratings.items()}
        del temp_ratings[user][movie_id]
        
        # Create new recommender without this rating
        temp_hybrid = HybridRecommender(temp_ratings, movies)
        predicted = temp_hybrid.predict(user, movie_id)
        
        predictions_list.append(predicted)
        actual_list.append(actual_rating)

rmse = calculate_rmse(predictions_list, actual_list)
mae = calculate_mae(predictions_list, actual_list)

print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")

# Precision and Recall
print("\nPrecision and Recall (threshold = 4 stars):")
threshold = 4

for user in ratings:
    relevant = [m for m, r in ratings[user].items() if r >= threshold]
    
    # Get all predictions
    all_preds = []
    for movie_id in movies:
        pred = hybrid.predict(user, movie_id)
        all_preds.append((movie_id, pred))
    all_preds.sort(key=lambda x: x[1], reverse=True)
    recommended = [m for m, _ in all_preds]
    
    p5, r5 = calculate_precision_recall(recommended, relevant, k=5)
    f1 = calculate_f1(p5, r5)
    
    print(f"{user}: P@5={p5:.2f}, R@5={r5:.2f}, F1={f1:.2f}")

# ========== COLD START PROBLEM ==========
print("\n" + "=" * 60)
print("COLD START PROBLEM")
print("=" * 60)

print("""
Cold Start Problem:
- New User: No ratings to learn preferences
- New Item: No ratings from users

Solutions:
1. Ask for initial preferences/ratings
2. Use demographic data
3. Use content-based filtering for new items
4. Use popularity-based recommendations for new users
5. Hybrid approaches that balance CF and CB
""")

class ColdStartHandler:
    def __init__(self, ratings, movies):
        self.ratings = ratings
        self.movies = movies
        self.hybrid = HybridRecommender(ratings, movies)
    
    def get_popular_items(self, n=3):
        """Get most popular items (most rated or highest average)."""
        item_ratings = defaultdict(list)
        for user_ratings in self.ratings.values():
            for movie_id, rating in user_ratings.items():
                item_ratings[movie_id].append(rating)
        
        # Score by combination of count and average
        scores = []
        for movie_id, movie_ratings in item_ratings.items():
            avg = np.mean(movie_ratings)
            count = len(movie_ratings)
            score = avg * np.log(1 + count)  # Wilson lower bound-like
            scores.append((movie_id, score))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:n]
    
    def recommend_new_user(self, preferred_genres=None, n=3):
        """Recommend for new user with optional genre preferences."""
        if preferred_genres:
            # Content-based using preferred genres
            scores = []
            for movie_id, movie_data in self.movies.items():
                overlap = len(set(preferred_genres) & set(movie_data["genres"]))
                if overlap > 0:
                    scores.append((movie_id, overlap))
            scores.sort(key=lambda x: x[1], reverse=True)
            return scores[:n]
        else:
            # Return popular items
            return self.get_popular_items(n)
    
    def recommend_new_item(self, new_item_features, n_users=3):
        """Recommend new item to users based on content similarity."""
        new_vector = get_genre_vector(new_item_features["genres"])
        
        user_scores = []
        for user in self.ratings:
            profile = self.hybrid.cb.build_user_profile(user)
            sim = cosine_similarity(profile, new_vector)
            user_scores.append((user, sim))
        
        user_scores.sort(key=lambda x: x[1], reverse=True)
        return user_scores[:n_users]

handler = ColdStartHandler(ratings, movies)

print("\nPopular items:")
popular = handler.get_popular_items()
for movie_id, score in popular:
    print(f"  - {movies[movie_id]['title']}: Score = {score:.2f}")

print("\nRecommendations for new user who likes Sci-Fi and Action:")
new_user_recs = handler.recommend_new_user(preferred_genres=["Sci-Fi", "Action"])
for movie_id, score in new_user_recs:
    print(f"  - {movies[movie_id]['title']}: Score = {score}")

print("\nUsers to recommend new Romance/Drama movie to:")
new_movie = {"title": "New Romance", "genres": ["Romance", "Drama"], "year": 2024}
target_users = handler.recommend_new_item(new_movie)
for user, score in target_users:
    print(f"  - {user}: Similarity = {score:.2f}")

print("\n" + "=" * 60)
print("✅ Building Recommender Systems - Complete!")
print("=" * 60)
