"""
MINI PROJECT 3: Customer Segmentation (Unsupervised Learning)
==============================================================
Day 28: Week 4 Mini-Project

Complete end-to-end ML project for customer segmentation using clustering.
This project demonstrates unsupervised learning techniques.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("MINI PROJECT: CUSTOMER SEGMENTATION")
print("=" * 70)

# ============================================================
# STEP 1: DATA GENERATION/LOADING
# ============================================================

print("\n" + "=" * 50)
print("STEP 1: DATA GENERATION")
print("=" * 50)

# Generate synthetic customer dataset
np.random.seed(42)
n_samples = 1500

# Generate different customer segments
# Segment 1: High-value frequent shoppers
n1 = 400
seg1 = {
    'annual_income': np.random.normal(85000, 15000, n1),
    'spending_score': np.random.normal(75, 10, n1),
    'age': np.random.normal(35, 8, n1),
    'purchase_frequency': np.random.normal(25, 5, n1),
    'avg_purchase_value': np.random.normal(150, 30, n1),
    'years_customer': np.random.normal(5, 2, n1),
    'online_purchases_pct': np.random.normal(60, 15, n1)
}

# Segment 2: Budget-conscious customers
n2 = 400
seg2 = {
    'annual_income': np.random.normal(35000, 8000, n2),
    'spending_score': np.random.normal(30, 10, n2),
    'age': np.random.normal(45, 12, n2),
    'purchase_frequency': np.random.normal(10, 3, n2),
    'avg_purchase_value': np.random.normal(50, 15, n2),
    'years_customer': np.random.normal(3, 1.5, n2),
    'online_purchases_pct': np.random.normal(30, 10, n2)
}

# Segment 3: Young professionals
n3 = 350
seg3 = {
    'annual_income': np.random.normal(55000, 12000, n3),
    'spending_score': np.random.normal(55, 15, n3),
    'age': np.random.normal(28, 5, n3),
    'purchase_frequency': np.random.normal(15, 4, n3),
    'avg_purchase_value': np.random.normal(80, 25, n3),
    'years_customer': np.random.normal(2, 1, n3),
    'online_purchases_pct': np.random.normal(80, 10, n3)
}

# Segment 4: Premium occasional buyers
n4 = 350
seg4 = {
    'annual_income': np.random.normal(100000, 20000, n4),
    'spending_score': np.random.normal(50, 15, n4),
    'age': np.random.normal(50, 10, n4),
    'purchase_frequency': np.random.normal(8, 3, n4),
    'avg_purchase_value': np.random.normal(250, 50, n4),
    'years_customer': np.random.normal(7, 3, n4),
    'online_purchases_pct': np.random.normal(40, 15, n4)
}

# Combine all segments
data = {}
for key in seg1.keys():
    data[key] = np.concatenate([seg1[key], seg2[key], seg3[key], seg4[key]])

# Create DataFrame
df = pd.DataFrame(data)

# Clean up values
df['annual_income'] = df['annual_income'].clip(20000, 150000).astype(int)
df['spending_score'] = df['spending_score'].clip(1, 100).astype(int)
df['age'] = df['age'].clip(18, 70).astype(int)
df['purchase_frequency'] = df['purchase_frequency'].clip(1, 50).astype(int)
df['avg_purchase_value'] = df['avg_purchase_value'].clip(10, 500).round(2)
df['years_customer'] = df['years_customer'].clip(0.5, 15).round(1)
df['online_purchases_pct'] = df['online_purchases_pct'].clip(0, 100).round(1)

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Add customer ID
df.insert(0, 'customer_id', range(1, len(df) + 1))

print(f"Dataset created with {len(df)} customers")
print(f"\nFeatures: {list(df.columns)}")

# ============================================================
# STEP 2: EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("STEP 2: EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Basic statistics
print("\n📊 Dataset Statistics:")
print(df.describe())

# Feature distributions
print("\n📈 Feature Ranges:")
for col in df.columns[1:]:  # Skip customer_id
    print(f"   {col}: {df[col].min():.1f} - {df[col].max():.1f}")

# ============================================================
# STEP 3: DATA VISUALIZATION
# ============================================================

print("\n" + "=" * 50)
print("STEP 3: DATA VISUALIZATION")
print("=" * 50)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Customer Data - Exploratory Analysis', fontsize=14)

# Feature distributions
features_to_plot = ['annual_income', 'spending_score', 'age', 
                    'purchase_frequency', 'avg_purchase_value', 'online_purchases_pct']

for idx, feature in enumerate(features_to_plot):
    ax = axes[idx // 3, idx % 3]
    df[feature].hist(bins=30, ax=ax, edgecolor='black', alpha=0.7, color='steelblue')
    ax.set_title(f'Distribution of {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('customer_segmentation_distributions.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Distribution plots saved")

# Scatter plot: Income vs Spending Score
plt.figure(figsize=(10, 6))
plt.scatter(df['annual_income'], df['spending_score'], alpha=0.5, c='blue')
plt.xlabel('Annual Income ($)')
plt.ylabel('Spending Score')
plt.title('Annual Income vs Spending Score')
plt.tight_layout()
plt.savefig('customer_income_vs_spending.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Income vs Spending plot saved")

# ============================================================
# STEP 4: DATA PREPROCESSING
# ============================================================

print("\n" + "=" * 50)
print("STEP 4: DATA PREPROCESSING")
print("=" * 50)

# Select features for clustering
feature_columns = ['annual_income', 'spending_score', 'age', 'purchase_frequency',
                   'avg_purchase_value', 'years_customer', 'online_purchases_pct']

X = df[feature_columns]

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"Features selected: {feature_columns}")
print(f"Data shape: {X_scaled.shape}")
print("✓ Features scaled using StandardScaler")

# ============================================================
# STEP 5: FINDING OPTIMAL K
# ============================================================

print("\n" + "=" * 50)
print("STEP 5: FINDING OPTIMAL NUMBER OF CLUSTERS")
print("=" * 50)

# Elbow Method
inertias = []
silhouette_scores = []
K_range = range(2, 11)

print("\nTesting different values of K...")
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    print(f"   K={k}: Inertia={kmeans.inertia_:.0f}, Silhouette={silhouette_scores[-1]:.4f}")

# Plot Elbow and Silhouette
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Elbow plot
axes[0].plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
axes[0].set_xlabel('Number of Clusters (K)')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')
axes[0].grid(True, alpha=0.3)

# Silhouette plot
axes[1].plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
axes[1].set_xlabel('Number of Clusters (K)')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Analysis')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('customer_optimal_k.png', dpi=100, bbox_inches='tight')
plt.close()
print("\n✓ Elbow and Silhouette plots saved")

# Choose optimal K
optimal_k = 4
print(f"\n🎯 Optimal number of clusters: {optimal_k}")

# ============================================================
# STEP 6: K-MEANS CLUSTERING
# ============================================================

print("\n" + "=" * 50)
print("STEP 6: K-MEANS CLUSTERING")
print("=" * 50)

# Final model
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataframe
df['cluster'] = clusters

print(f"\n📊 Cluster Distribution:")
cluster_counts = df['cluster'].value_counts().sort_index()
for cluster, count in cluster_counts.items():
    print(f"   Cluster {cluster}: {count} customers ({count/len(df)*100:.1f}%)")

# Final silhouette score
final_silhouette = silhouette_score(X_scaled, clusters)
print(f"\n📈 Final Silhouette Score: {final_silhouette:.4f}")

# ============================================================
# STEP 7: CLUSTER ANALYSIS
# ============================================================

print("\n" + "=" * 50)
print("STEP 7: CLUSTER ANALYSIS")
print("=" * 50)

# Cluster profiles
print("\n📋 Cluster Profiles (Mean Values):")
cluster_profiles = df.groupby('cluster')[feature_columns].mean()
print(cluster_profiles.round(2))

# Cluster descriptions
cluster_names = {
    0: 'Premium Loyalists',
    1: 'Budget Conscious',
    2: 'Young Digital Natives',
    3: 'Occasional High Spenders'
}

# Determine cluster characteristics
print("\n🏷️ Cluster Characteristics:")
for cluster_id in range(optimal_k):
    cluster_data = df[df['cluster'] == cluster_id]
    print(f"\n   Cluster {cluster_id}:")
    print(f"   - Avg Income: ${cluster_data['annual_income'].mean():,.0f}")
    print(f"   - Avg Spending Score: {cluster_data['spending_score'].mean():.0f}")
    print(f"   - Avg Age: {cluster_data['age'].mean():.0f}")
    print(f"   - Avg Purchase Frequency: {cluster_data['purchase_frequency'].mean():.0f}/year")
    print(f"   - Online Shopping %: {cluster_data['online_purchases_pct'].mean():.0f}%")

# ============================================================
# STEP 8: VISUALIZATION OF CLUSTERS
# ============================================================

print("\n" + "=" * 50)
print("STEP 8: CLUSTER VISUALIZATION")
print("=" * 50)

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"PCA explained variance: {pca.explained_variance_ratio_.sum()*100:.1f}%")

# Plot clusters in PCA space
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# PCA visualization
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96E6A1']
for cluster in range(optimal_k):
    mask = clusters == cluster
    axes[0].scatter(X_pca[mask, 0], X_pca[mask, 1], 
                    c=colors[cluster], label=f'Cluster {cluster}',
                    alpha=0.6, s=50)

axes[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                c='black', marker='X', s=200, label='Centroids')
axes[0].set_xlabel('PCA Component 1')
axes[0].set_ylabel('PCA Component 2')
axes[0].set_title('Customer Segments (PCA View)')
axes[0].legend()

# Income vs Spending Score by Cluster
for cluster in range(optimal_k):
    mask = df['cluster'] == cluster
    axes[1].scatter(df.loc[mask, 'annual_income'], df.loc[mask, 'spending_score'],
                    c=colors[cluster], label=f'Cluster {cluster}', alpha=0.6, s=50)

axes[1].set_xlabel('Annual Income ($)')
axes[1].set_ylabel('Spending Score')
axes[1].set_title('Customer Segments by Income & Spending')
axes[1].legend()

plt.tight_layout()
plt.savefig('customer_clusters_visualization.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Cluster visualizations saved")

# Cluster comparison heatmap
plt.figure(figsize=(12, 6))
cluster_profiles_normalized = (cluster_profiles - cluster_profiles.mean()) / cluster_profiles.std()
sns.heatmap(cluster_profiles_normalized.T, annot=True, cmap='RdYlGn', center=0,
            fmt='.2f', xticklabels=[f'Cluster {i}' for i in range(optimal_k)])
plt.title('Cluster Profiles (Standardized)')
plt.tight_layout()
plt.savefig('customer_cluster_heatmap.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Cluster heatmap saved")

# ============================================================
# STEP 9: SAVE MODEL
# ============================================================

print("\n" + "=" * 50)
print("STEP 9: SAVE MODEL")
print("=" * 50)

joblib.dump(kmeans, 'customer_segmentation_model.pkl')
joblib.dump(scaler, 'customer_segmentation_scaler.pkl')
joblib.dump(pca, 'customer_segmentation_pca.pkl')

print("✓ K-Means model saved to 'customer_segmentation_model.pkl'")
print("✓ Scaler saved to 'customer_segmentation_scaler.pkl'")
print("✓ PCA saved to 'customer_segmentation_pca.pkl'")

# Save customer segments
df.to_csv('customer_segments.csv', index=False)
print("✓ Customer segments saved to 'customer_segments.csv'")

# ============================================================
# STEP 10: PREDICTION FUNCTION
# ============================================================

print("\n" + "=" * 50)
print("STEP 10: SEGMENT NEW CUSTOMERS")
print("=" * 50)

def segment_customer(customer_data):
    """
    Predict segment for a new customer.
    """
    input_df = pd.DataFrame([customer_data])[feature_columns]
    input_scaled = scaler.transform(input_df)
    cluster = kmeans.predict(input_scaled)[0]
    return cluster

# Example segmentation
print("\n👥 Sample Customer Segmentation:")

new_customers = [
    {
        'annual_income': 90000, 'spending_score': 80, 'age': 32,
        'purchase_frequency': 28, 'avg_purchase_value': 160,
        'years_customer': 6, 'online_purchases_pct': 55
    },
    {
        'annual_income': 30000, 'spending_score': 25, 'age': 50,
        'purchase_frequency': 8, 'avg_purchase_value': 45,
        'years_customer': 2, 'online_purchases_pct': 25
    },
    {
        'annual_income': 50000, 'spending_score': 60, 'age': 25,
        'purchase_frequency': 18, 'avg_purchase_value': 90,
        'years_customer': 1, 'online_purchases_pct': 85
    },
]

for i, customer in enumerate(new_customers, 1):
    segment = segment_customer(customer)
    print(f"\n   Customer {i}:")
    print(f"   - Income: ${customer['annual_income']:,}")
    print(f"   - Spending Score: {customer['spending_score']}")
    print(f"   - Age: {customer['age']}")
    print(f"   🎯 Assigned Segment: Cluster {segment}")

# ============================================================
# PROJECT SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print(f"""
✅ Dataset: {len(df)} customers
✅ Features: {len(feature_columns)}
✅ Optimal Clusters: {optimal_k}
✅ Silhouette Score: {final_silhouette:.4f}
✅ Model saved and ready for deployment

Files Created:
- customer_segmentation_distributions.png
- customer_income_vs_spending.png
- customer_optimal_k.png
- customer_clusters_visualization.png
- customer_cluster_heatmap.png
- customer_segments.csv
- customer_segmentation_model.pkl
- customer_segmentation_scaler.pkl
- customer_segmentation_pca.pkl

Business Applications:
1. Targeted Marketing - Customize campaigns for each segment
2. Product Recommendations - Tailor offerings to segment preferences
3. Customer Retention - Identify at-risk segments
4. Pricing Strategy - Optimize pricing for each segment
5. Resource Allocation - Focus on high-value segments

Key Insights:
- 4 distinct customer segments identified
- Clear separation based on income and spending behavior
- Age and online shopping patterns vary by segment
- Actionable segments for marketing strategies
""")

print("=" * 70)
print("PROJECT COMPLETE! 🎉")
print("=" * 70)
