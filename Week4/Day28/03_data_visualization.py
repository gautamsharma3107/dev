"""
DATA VISUALIZATION - End-to-End ML Project
============================================
Day 28: Week 4 Mini-Project

Learn how to visualize data for exploratory data analysis (EDA).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

print("=" * 60)
print("DATA VISUALIZATION - ML Project Pipeline")
print("=" * 60)

# Create sample dataset
np.random.seed(42)
n_samples = 1000

data = {
    'square_feet': np.random.randint(500, 5000, n_samples),
    'bedrooms': np.random.randint(1, 7, n_samples),
    'bathrooms': np.random.randint(1, 5, n_samples),
    'age_years': np.random.randint(0, 100, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples).round(2),
    'garage_spaces': np.random.randint(0, 4, n_samples),
    'has_pool': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
    'neighborhood': np.random.choice(['A', 'B', 'C', 'D'], n_samples)
}

price = (
    data['square_feet'] * 100 +
    data['bedrooms'] * 15000 +
    data['bathrooms'] * 10000 -
    data['age_years'] * 500 +
    data['location_score'] * 5000 +
    data['garage_spaces'] * 8000 +
    data['has_pool'] * 20000 +
    np.random.normal(0, 20000, n_samples)
)
data['price'] = price.astype(int)

df = pd.DataFrame(data)
print("Dataset loaded for visualization!")
print(f"Shape: {df.shape}")

# ============================================================
# 1. Distribution Plots
# ============================================================

print("\n1. DISTRIBUTION PLOTS")
print("-" * 40)

# Histogram
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Distribution of Numerical Features', fontsize=14)

numerical_cols = ['square_feet', 'bedrooms', 'bathrooms', 
                  'age_years', 'location_score', 'price']

for idx, col in enumerate(numerical_cols):
    ax = axes[idx // 3, idx % 3]
    df[col].hist(bins=30, ax=ax, edgecolor='black', alpha=0.7)
    ax.set_title(f'Distribution of {col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('01_distributions.png', dpi=100, bbox_inches='tight')
plt.close()
print("Distribution plots saved to '01_distributions.png'")

# ============================================================
# 2. Box Plots (Outlier Detection)
# ============================================================

print("\n2. BOX PLOTS")
print("-" * 40)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Box Plots for Outlier Detection', fontsize=14)

for idx, col in enumerate(numerical_cols):
    ax = axes[idx // 3, idx % 3]
    df.boxplot(column=col, ax=ax)
    ax.set_title(f'Box Plot: {col}')

plt.tight_layout()
plt.savefig('02_boxplots.png', dpi=100, bbox_inches='tight')
plt.close()
print("Box plots saved to '02_boxplots.png'")

# ============================================================
# 3. Correlation Heatmap
# ============================================================

print("\n3. CORRELATION HEATMAP")
print("-" * 40)

# Calculate correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', linewidths=0.5, square=True)
plt.title('Correlation Heatmap', fontsize=14)
plt.tight_layout()
plt.savefig('03_correlation_heatmap.png', dpi=100, bbox_inches='tight')
plt.close()
print("Correlation heatmap saved to '03_correlation_heatmap.png'")

print("\nTop correlations with price:")
price_corr = correlation_matrix['price'].drop('price').sort_values(ascending=False)
print(price_corr)

# ============================================================
# 4. Scatter Plots
# ============================================================

print("\n4. SCATTER PLOTS")
print("-" * 40)

# Scatter plot: Price vs Square Feet
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Price vs Key Features', fontsize=14)

# Price vs Square Feet
axes[0, 0].scatter(df['square_feet'], df['price'], alpha=0.5, c='blue')
axes[0, 0].set_xlabel('Square Feet')
axes[0, 0].set_ylabel('Price')
axes[0, 0].set_title('Price vs Square Feet')

# Price vs Bedrooms
axes[0, 1].scatter(df['bedrooms'], df['price'], alpha=0.5, c='green')
axes[0, 1].set_xlabel('Bedrooms')
axes[0, 1].set_ylabel('Price')
axes[0, 1].set_title('Price vs Bedrooms')

# Price vs Age
axes[1, 0].scatter(df['age_years'], df['price'], alpha=0.5, c='red')
axes[1, 0].set_xlabel('Age (years)')
axes[1, 0].set_ylabel('Price')
axes[1, 0].set_title('Price vs Age')

# Price vs Location Score
axes[1, 1].scatter(df['location_score'], df['price'], alpha=0.5, c='purple')
axes[1, 1].set_xlabel('Location Score')
axes[1, 1].set_ylabel('Price')
axes[1, 1].set_title('Price vs Location Score')

plt.tight_layout()
plt.savefig('04_scatter_plots.png', dpi=100, bbox_inches='tight')
plt.close()
print("Scatter plots saved to '04_scatter_plots.png'")

# ============================================================
# 5. Categorical Analysis
# ============================================================

print("\n5. CATEGORICAL ANALYSIS")
print("-" * 40)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Categorical Feature Analysis', fontsize=14)

# Neighborhood distribution
df['neighborhood'].value_counts().plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Neighborhood Distribution')
axes[0].set_xlabel('Neighborhood')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=0)

# Price by Neighborhood
df.boxplot(column='price', by='neighborhood', ax=axes[1])
axes[1].set_title('Price by Neighborhood')
axes[1].set_xlabel('Neighborhood')
axes[1].set_ylabel('Price')
plt.suptitle('')  # Remove automatic title

# Pool distribution
df['has_pool'].value_counts().plot(kind='pie', ax=axes[2], autopct='%1.1f%%',
                                    labels=['No Pool', 'Has Pool'], colors=['lightcoral', 'lightgreen'])
axes[2].set_title('Pool Distribution')
axes[2].set_ylabel('')

plt.tight_layout()
plt.savefig('05_categorical_analysis.png', dpi=100, bbox_inches='tight')
plt.close()
print("Categorical analysis saved to '05_categorical_analysis.png'")

# ============================================================
# 6. Pair Plot
# ============================================================

print("\n6. PAIR PLOT")
print("-" * 40)

# Select subset of features for pair plot
selected_cols = ['square_feet', 'bedrooms', 'location_score', 'price']
pair_plot = sns.pairplot(df[selected_cols], diag_kind='hist', corner=True)
pair_plot.fig.suptitle('Pair Plot of Key Features', y=1.02)
plt.savefig('06_pair_plot.png', dpi=100, bbox_inches='tight')
plt.close()
print("Pair plot saved to '06_pair_plot.png'")

# ============================================================
# 7. Price Distribution Analysis
# ============================================================

print("\n7. PRICE DISTRIBUTION ANALYSIS")
print("-" * 40)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Price histogram with KDE
df['price'].plot(kind='hist', bins=30, ax=axes[0], alpha=0.7, 
                  edgecolor='black', density=True)
df['price'].plot(kind='kde', ax=axes[0], color='red', linewidth=2)
axes[0].set_title('Price Distribution with KDE')
axes[0].set_xlabel('Price')
axes[0].set_ylabel('Density')

# Log-transformed price
df['log_price'] = np.log(df['price'])
df['log_price'].plot(kind='hist', bins=30, ax=axes[1], alpha=0.7,
                      edgecolor='black', density=True, color='green')
df['log_price'].plot(kind='kde', ax=axes[1], color='red', linewidth=2)
axes[1].set_title('Log-Transformed Price Distribution')
axes[1].set_xlabel('Log(Price)')
axes[1].set_ylabel('Density')

plt.tight_layout()
plt.savefig('07_price_analysis.png', dpi=100, bbox_inches='tight')
plt.close()
print("Price analysis saved to '07_price_analysis.png'")

# ============================================================
# 8. Feature Importance Preview
# ============================================================

print("\n8. FEATURE RELATIONSHIPS")
print("-" * 40)

# Create grouped bar chart
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Average price by bedrooms
avg_price_by_bedrooms = df.groupby('bedrooms')['price'].mean()
avg_price_by_bedrooms.plot(kind='bar', ax=axes[0], color='steelblue', edgecolor='black')
axes[0].set_title('Average Price by Number of Bedrooms')
axes[0].set_xlabel('Bedrooms')
axes[0].set_ylabel('Average Price')
axes[0].tick_params(axis='x', rotation=0)

# Average price by has_pool
avg_price_by_pool = df.groupby('has_pool')['price'].mean()
avg_price_by_pool.plot(kind='bar', ax=axes[1], color=['coral', 'seagreen'], edgecolor='black')
axes[1].set_title('Average Price by Pool Availability')
axes[1].set_xlabel('Has Pool')
axes[1].set_ylabel('Average Price')
axes[1].set_xticklabels(['No', 'Yes'], rotation=0)

plt.tight_layout()
plt.savefig('08_feature_relationships.png', dpi=100, bbox_inches='tight')
plt.close()
print("Feature relationships saved to '08_feature_relationships.png'")

# ============================================================
# SUMMARY STATISTICS VISUALIZATION
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Visualizations Created:
1. Distribution plots for numerical features
2. Box plots for outlier detection
3. Correlation heatmap
4. Scatter plots for feature relationships
5. Categorical feature analysis
6. Pair plot for multivariate analysis
7. Price distribution analysis
8. Feature relationship bar charts

All plots saved as PNG files in the current directory.
""")

# ============================================================
# EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
1. Create additional visualizations:
   - Violin plots for price by neighborhood
   - Stacked bar chart for categorical features
   - 3D scatter plot with plotly

2. Analyze your visualizations:
   - What patterns do you see?
   - Are there any outliers?
   - Which features seem most correlated with price?

3. Create a dashboard-style visualization:
   - Combine multiple plots in one figure
   - Add proper titles and labels
   - Use consistent color schemes

4. Practice with a different dataset:
   - Load a new dataset
   - Create at least 5 different visualizations
   - Document your findings
""")

# ============================================================
# KEY TAKEAWAYS
# ============================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ Use histograms to understand distributions
✅ Use box plots to detect outliers
✅ Use correlation heatmaps to find relationships
✅ Use scatter plots to visualize feature relationships
✅ Use bar charts for categorical comparisons
✅ Always add proper titles and labels
✅ Choose appropriate color schemes
✅ Save visualizations for reports and documentation
""")
