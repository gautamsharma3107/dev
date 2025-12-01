"""
Day 27 Mini Project: Customer Segmentation
============================================
Build a complete customer segmentation system using:
- K-Means Clustering
- PCA for visualization
- Cross-validation for evaluation
- Hyperparameter tuning

This project combines all Day 27 concepts!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.pipeline import Pipeline

print("=" * 70)
print("CUSTOMER SEGMENTATION PROJECT")
print("=" * 70)

# ============================================================
# PART 1: Generate Customer Data
# ============================================================
print("\n" + "=" * 70)
print("PART 1: GENERATE CUSTOMER DATA")
print("=" * 70)

# Create synthetic customer data
np.random.seed(42)
n_customers = 500

# Features: Annual Income (K$), Spending Score (1-100), Age, Visits per Month
data = {
    'CustomerID': range(1, n_customers + 1),
    'Annual_Income': np.concatenate([
        np.random.normal(30, 10, 125),   # Low income
        np.random.normal(60, 15, 125),   # Medium income
        np.random.normal(100, 20, 125),  # High income
        np.random.normal(80, 15, 125)    # Upper-medium income
    ]),
    'Spending_Score': np.concatenate([
        np.random.normal(20, 10, 125),   # Low spenders
        np.random.normal(50, 15, 125),   # Medium spenders
        np.random.normal(80, 10, 125),   # High spenders
        np.random.normal(40, 15, 125)    # Conservative spenders
    ]),
    'Age': np.concatenate([
        np.random.normal(45, 10, 125),   # Older
        np.random.normal(35, 8, 125),    # Middle-aged
        np.random.normal(28, 5, 125),    # Young
        np.random.normal(50, 12, 125)    # Mature
    ]),
    'Visits_Per_Month': np.concatenate([
        np.random.normal(2, 1, 125),     # Infrequent
        np.random.normal(5, 2, 125),     # Regular
        np.random.normal(10, 3, 125),    # Frequent
        np.random.normal(3, 1.5, 125)    # Occasional
    ])
}

# Create DataFrame
df = pd.DataFrame(data)

# Clip values to realistic ranges
df['Annual_Income'] = df['Annual_Income'].clip(15, 150)
df['Spending_Score'] = df['Spending_Score'].clip(1, 100)
df['Age'] = df['Age'].clip(18, 70).astype(int)
df['Visits_Per_Month'] = df['Visits_Per_Month'].clip(1, 20)

print(f"Created dataset with {len(df)} customers")
print(f"\nFeatures: {list(df.columns[1:])}")
print(f"\nData Overview:")
print(df.describe().round(2))

# ============================================================
# PART 2: Data Preprocessing
# ============================================================
print("\n" + "=" * 70)
print("PART 2: DATA PREPROCESSING")
print("=" * 70)

# Select features for clustering
features = ['Annual_Income', 'Spending_Score', 'Age', 'Visits_Per_Month']
X = df[features].values

print(f"Feature matrix shape: {X.shape}")

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Data scaled using StandardScaler")
print(f"Scaled data mean: {X_scaled.mean(axis=0).round(4)}")
print(f"Scaled data std: {X_scaled.std(axis=0).round(4)}")

# ============================================================
# PART 3: Find Optimal Number of Clusters
# ============================================================
print("\n" + "=" * 70)
print("PART 3: FIND OPTIMAL NUMBER OF CLUSTERS")
print("=" * 70)

# Elbow method and Silhouette analysis
K_range = range(2, 11)
inertias = []
silhouette_scores = []

print("\nEvaluating K values from 2 to 10...")
print("-" * 50)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    inertias.append(kmeans.inertia_)
    sil_score = silhouette_score(X_scaled, labels)
    silhouette_scores.append(sil_score)
    print(f"K={k}: Inertia={kmeans.inertia_:.2f}, Silhouette={sil_score:.4f}")

# Find best K based on silhouette score
best_k = K_range[np.argmax(silhouette_scores)]
print(f"\nBest K based on Silhouette Score: {best_k}")

# Plot Elbow and Silhouette
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Elbow plot
axes[0].plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
axes[0].set_xlabel('Number of Clusters (K)', fontsize=12)
axes[0].set_ylabel('Inertia', fontsize=12)
axes[0].set_title('Elbow Method', fontsize=14)
axes[0].grid(True, alpha=0.3)

# Silhouette plot
axes[1].plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
axes[1].axvline(x=best_k, color='r', linestyle='--', label=f'Best K={best_k}')
axes[1].set_xlabel('Number of Clusters (K)', fontsize=12)
axes[1].set_ylabel('Silhouette Score', fontsize=12)
axes[1].set_title('Silhouette Analysis', fontsize=14)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('01_optimal_k_analysis.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 01_optimal_k_analysis.png")

# ============================================================
# PART 4: Perform K-Means Clustering
# ============================================================
print("\n" + "=" * 70)
print("PART 4: PERFORM K-MEANS CLUSTERING")
print("=" * 70)

# Use optimal K (or 4 for clear business interpretation)
optimal_k = 4  # Can also use best_k from silhouette analysis
print(f"Using K={optimal_k} for business interpretation")

# Final K-Means model
kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
cluster_labels = kmeans_final.fit_predict(X_scaled)

# Add labels to dataframe
df['Cluster'] = cluster_labels

print(f"\nCluster Distribution:")
print(df['Cluster'].value_counts().sort_index())

# Evaluation metrics
sil_final = silhouette_score(X_scaled, cluster_labels)
ch_score = calinski_harabasz_score(X_scaled, cluster_labels)
print(f"\nFinal Model Metrics:")
print(f"  Silhouette Score: {sil_final:.4f}")
print(f"  Calinski-Harabasz Score: {ch_score:.2f}")

# ============================================================
# PART 5: PCA for Visualization
# ============================================================
print("\n" + "=" * 70)
print("PART 5: PCA FOR VISUALIZATION")
print("=" * 70)

# Apply PCA for 2D visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"PCA Explained Variance:")
print(f"  PC1: {pca.explained_variance_ratio_[0]:.4f} ({pca.explained_variance_ratio_[0]*100:.1f}%)")
print(f"  PC2: {pca.explained_variance_ratio_[1]:.4f} ({pca.explained_variance_ratio_[1]*100:.1f}%)")
print(f"  Total: {sum(pca.explained_variance_ratio_):.4f} ({sum(pca.explained_variance_ratio_)*100:.1f}%)")

# Visualize clusters in PCA space
plt.figure(figsize=(12, 8))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
cluster_names = ['Segment A', 'Segment B', 'Segment C', 'Segment D']

for i in range(optimal_k):
    mask = cluster_labels == i
    plt.scatter(
        X_pca[mask, 0], X_pca[mask, 1],
        c=colors[i], label=cluster_names[i],
        s=100, alpha=0.7, edgecolors='white', linewidth=0.5
    )

# Plot cluster centers in PCA space
centers_pca = pca.transform(kmeans_final.cluster_centers_)
plt.scatter(
    centers_pca[:, 0], centers_pca[:, 1],
    c='black', marker='X', s=300, edgecolors='white',
    linewidth=2, label='Centroids'
)

plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)', fontsize=12)
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)', fontsize=12)
plt.title('Customer Segments in PCA Space', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('02_customer_segments_pca.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 02_customer_segments_pca.png")

# ============================================================
# PART 6: Segment Analysis
# ============================================================
print("\n" + "=" * 70)
print("PART 6: SEGMENT ANALYSIS")
print("=" * 70)

# Analyze each segment
segment_analysis = df.groupby('Cluster')[features].agg(['mean', 'std']).round(2)
print("\nSegment Statistics:")
print(segment_analysis)

# Create segment profiles
print("\n" + "=" * 70)
print("SEGMENT PROFILES")
print("=" * 70)

for i in range(optimal_k):
    segment_data = df[df['Cluster'] == i]
    print(f"\n📊 Segment {i} ({len(segment_data)} customers):")
    print(f"   Avg Annual Income: ${segment_data['Annual_Income'].mean():.1f}K")
    print(f"   Avg Spending Score: {segment_data['Spending_Score'].mean():.1f}")
    print(f"   Avg Age: {segment_data['Age'].mean():.1f} years")
    print(f"   Avg Visits/Month: {segment_data['Visits_Per_Month'].mean():.1f}")

# Create visual comparison of segments
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for idx, feature in enumerate(features):
    ax = axes[idx // 2, idx % 2]
    segment_means = [df[df['Cluster'] == i][feature].mean() for i in range(optimal_k)]
    bars = ax.bar(cluster_names, segment_means, color=colors)
    ax.set_ylabel(feature)
    ax.set_title(f'{feature} by Segment')
    ax.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, val in zip(bars, segment_means):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                f'{val:.1f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('03_segment_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("\nPlot saved: 03_segment_comparison.png")

# ============================================================
# PART 7: Business Recommendations
# ============================================================
print("\n" + "=" * 70)
print("PART 7: BUSINESS RECOMMENDATIONS")
print("=" * 70)

print("""
Based on the customer segmentation analysis:

🎯 MARKETING STRATEGIES BY SEGMENT:

Segment A (if low income, low spending):
   → Budget-friendly promotions
   → Loyalty programs for small purchases
   → Email campaigns with discount codes

Segment B (if medium income, medium spending):
   → Cross-selling opportunities
   → Bundle deals
   → Seasonal promotions

Segment C (if high income, high spending):
   → Premium product recommendations
   → VIP loyalty program
   → Exclusive early access to new products
   → Personalized concierge service

Segment D (if high income, low spending):
   → Targeted engagement campaigns
   → Product education content
   → Incentives to increase purchase frequency

📈 NEXT STEPS:
1. Validate segments with business stakeholders
2. A/B test marketing strategies per segment
3. Monitor segment migration over time
4. Refine model with additional customer data
""")

# ============================================================
# PART 8: Save Results
# ============================================================
print("\n" + "=" * 70)
print("PART 8: SAVE RESULTS")
print("=" * 70)

# Save segmented customer data
df.to_csv('customer_segments.csv', index=False)
print("Saved: customer_segments.csv")

# Summary statistics
summary = {
    'Total Customers': len(df),
    'Number of Segments': optimal_k,
    'Silhouette Score': round(sil_final, 4),
    'CH Score': round(ch_score, 2)
}

print("\n📊 PROJECT SUMMARY:")
print("-" * 40)
for key, value in summary.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 70)
print("✅ CUSTOMER SEGMENTATION PROJECT COMPLETE!")
print("=" * 70)
