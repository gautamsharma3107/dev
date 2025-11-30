"""
Day 23 - Correlation Heatmaps
==============================
Learn: Correlation analysis and visualization with heatmaps

Key Concepts:
- Correlation measures relationship between variables (-1 to 1)
- Heatmaps visualize correlation matrices
- Positive correlation: both increase together
- Negative correlation: one increases, other decreases
- No correlation: no linear relationship
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set style
sns.set_theme(style="white")

# ========== UNDERSTANDING CORRELATION ==========
print("=" * 50)
print("UNDERSTANDING CORRELATION")
print("=" * 50)

# Create correlated data
np.random.seed(42)
n = 200

# Generate variables with different correlations
x = np.random.randn(n)
y_positive = x + np.random.randn(n) * 0.3     # Strong positive correlation
y_negative = -x + np.random.randn(n) * 0.3    # Strong negative correlation
y_weak = x * 0.3 + np.random.randn(n)         # Weak positive correlation
y_none = np.random.randn(n)                    # No correlation

# Visualize correlation types
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].scatter(x, y_positive, alpha=0.6, c='steelblue')
axes[0, 0].set_title(f'Strong Positive (r = {np.corrcoef(x, y_positive)[0,1]:.2f})')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')

axes[0, 1].scatter(x, y_negative, alpha=0.6, c='coral')
axes[0, 1].set_title(f'Strong Negative (r = {np.corrcoef(x, y_negative)[0,1]:.2f})')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')

axes[1, 0].scatter(x, y_weak, alpha=0.6, c='green')
axes[1, 0].set_title(f'Weak Positive (r = {np.corrcoef(x, y_weak)[0,1]:.2f})')
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')

axes[1, 1].scatter(x, y_none, alpha=0.6, c='purple')
axes[1, 1].set_title(f'No Correlation (r = {np.corrcoef(x, y_none)[0,1]:.2f})')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')

plt.tight_layout()
plt.suptitle('Types of Correlation', y=1.02, fontsize=14)
plt.savefig('corr_01_types.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Correlation types saved as 'corr_01_types.png'")

# ========== CORRELATION MATRIX ==========
print("\n" + "=" * 50)
print("CORRELATION MATRIX")
print("=" * 50)

# Create a sample dataset
df = pd.DataFrame({
    'Height': np.random.normal(170, 10, 200),
    'Weight': np.random.normal(70, 12, 200),
    'Age': np.random.randint(20, 60, 200),
    'Income': np.random.normal(50000, 15000, 200),
    'Spending': np.random.normal(2000, 500, 200)
})

# Add correlations
df['Weight'] = df['Height'] * 0.5 + np.random.randn(200) * 5
df['Income'] = df['Age'] * 800 + np.random.randn(200) * 10000
df['Spending'] = df['Income'] * 0.04 + np.random.randn(200) * 300

print("Sample Dataset:")
print(df.head())

# Calculate correlation matrix
corr_matrix = df.corr()
print("\nCorrelation Matrix:")
print(corr_matrix.round(2))

# ========== BASIC HEATMAP ==========
print("\n" + "=" * 50)
print("BASIC HEATMAP")
print("=" * 50)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Basic Correlation Heatmap', fontsize=14)
plt.tight_layout()
plt.savefig('corr_02_basic_heatmap.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Basic heatmap saved as 'corr_02_basic_heatmap.png'")

# ========== CUSTOMIZED HEATMAP ==========
print("\n" + "=" * 50)
print("CUSTOMIZED HEATMAP")
print("=" * 50)

plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,              # Show values
    fmt='.2f',               # Format to 2 decimal places
    cmap='RdYlBu_r',         # Red-Yellow-Blue reversed colormap
    center=0,                # Center color at 0
    linewidths=0.5,          # Line between cells
    square=True,             # Square cells
    vmin=-1, vmax=1,         # Value range
    cbar_kws={'shrink': 0.8} # Colorbar size
)
plt.title('Customized Correlation Heatmap', fontsize=14)
plt.tight_layout()
plt.savefig('corr_03_custom_heatmap.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Customized heatmap saved as 'corr_03_custom_heatmap.png'")

# ========== TRIANGLE HEATMAP ==========
print("\n" + "=" * 50)
print("TRIANGLE HEATMAP (Remove Duplicate Info)")
print("=" * 50)

# Create mask for upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    mask=mask,               # Hide upper triangle
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    square=True
)
plt.title('Lower Triangle Correlation Heatmap', fontsize=14)
plt.tight_layout()
plt.savefig('corr_04_triangle_heatmap.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Triangle heatmap saved as 'corr_04_triangle_heatmap.png'")

# ========== DIFFERENT COLOR MAPS ==========
print("\n" + "=" * 50)
print("DIFFERENT COLOR MAPS")
print("=" * 50)

colormaps = ['coolwarm', 'RdYlGn', 'viridis', 'plasma', 'YlOrRd', 'BuPu']

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for ax, cmap in zip(axes, colormaps):
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap=cmap, 
                center=0, ax=ax, cbar=False)
    ax.set_title(f'Colormap: {cmap}')

plt.tight_layout()
plt.suptitle('Comparing Different Colormaps', y=1.02, fontsize=14)
plt.savefig('corr_05_colormaps.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Colormap comparison saved as 'corr_05_colormaps.png'")

# ========== CLUSTERED HEATMAP ==========
print("\n" + "=" * 50)
print("CLUSTERED HEATMAP")
print("=" * 50)

# Clustermap automatically clusters similar variables together
g = sns.clustermap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    figsize=(10, 10)
)
plt.suptitle('Clustered Correlation Heatmap', y=1.02, fontsize=14)
plt.savefig('corr_06_clustermap.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Clustermap saved as 'corr_06_clustermap.png'")

# ========== HEATMAP WITH SIGNIFICANCE ==========
print("\n" + "=" * 50)
print("CORRELATION WITH SIGNIFICANCE LEVELS")
print("=" * 50)

from scipy import stats

# Calculate p-values for correlations
def correlation_with_pvalues(df):
    corr = df.corr()
    pvals = pd.DataFrame(np.zeros_like(corr), columns=corr.columns, index=corr.index)
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            if i != j:
                _, pvals.iloc[i, j] = stats.pearsonr(df.iloc[:, i], df.iloc[:, j])
    return corr, pvals

corr, pvals = correlation_with_pvalues(df)

# Create annotation showing significance
def annotate_heatmap(corr, pvals):
    annot = np.empty_like(corr, dtype=str)
    for i in range(corr.shape[0]):
        for j in range(corr.shape[1]):
            p = pvals.iloc[i, j]
            r = corr.iloc[i, j]
            stars = ''
            if p < 0.001:
                stars = '***'
            elif p < 0.01:
                stars = '**'
            elif p < 0.05:
                stars = '*'
            annot[i, j] = f'{r:.2f}{stars}'
    return annot

annot = annotate_heatmap(corr, pvals)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=annot, fmt='', cmap='coolwarm', center=0, linewidths=0.5)
plt.title('Correlation Heatmap with Significance\n(* p<0.05, ** p<0.01, *** p<0.001)', fontsize=14)
plt.tight_layout()
plt.savefig('corr_07_significance.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Significance heatmap saved as 'corr_07_significance.png'")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE - House Price Correlation Analysis")
print("=" * 50)

# Create house price dataset
np.random.seed(42)
houses = pd.DataFrame({
    'Price': np.random.normal(300000, 100000, 300),
    'SquareFeet': np.random.normal(2000, 500, 300),
    'Bedrooms': np.random.randint(1, 6, 300),
    'Bathrooms': np.random.randint(1, 4, 300),
    'Age': np.random.randint(0, 50, 300),
    'Distance_City': np.random.uniform(1, 30, 300),
    'Crime_Rate': np.random.uniform(1, 10, 300)
})

# Add realistic correlations
houses['Price'] = (houses['SquareFeet'] * 100 + 
                   houses['Bedrooms'] * 20000 - 
                   houses['Age'] * 1000 - 
                   houses['Distance_City'] * 3000 -
                   houses['Crime_Rate'] * 10000 +
                   np.random.randn(300) * 30000)
houses['Bathrooms'] = (houses['Bedrooms'] * 0.5 + np.random.randn(300) * 0.5).clip(1, 4).astype(int)

print("House Price Dataset:")
print(houses.head())

# Calculate correlations
house_corr = houses.corr()

# Create comprehensive visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap
mask = np.triu(np.ones_like(house_corr, dtype=bool))
sns.heatmap(house_corr, mask=mask, annot=True, fmt='.2f', 
            cmap='RdYlGn', center=0, linewidths=0.5, ax=axes[0])
axes[0].set_title('House Price Correlation Matrix')

# Bar chart of correlations with Price
price_correlations = house_corr['Price'].drop('Price').sort_values()
colors = ['red' if x < 0 else 'green' for x in price_correlations]
price_correlations.plot(kind='barh', color=colors, ax=axes[1])
axes[1].set_title('Correlation with House Price')
axes[1].set_xlabel('Correlation Coefficient')
axes[1].axvline(x=0, color='black', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.savefig('corr_08_house_analysis.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ House price analysis saved as 'corr_08_house_analysis.png'")

# ========== INTERPRETATION GUIDE ==========
print("\n" + "=" * 50)
print("CORRELATION INTERPRETATION GUIDE")
print("=" * 50)

print("""
Correlation Coefficient (r) Interpretation:
-------------------------------------------
| Range          | Strength    | Interpretation                |
|----------------|-------------|-------------------------------|
| 0.9 to 1.0     | Very Strong | Almost perfect relationship   |
| 0.7 to 0.9     | Strong      | Clear relationship exists     |
| 0.5 to 0.7     | Moderate    | Noticeable relationship       |
| 0.3 to 0.5     | Weak        | Slight relationship           |
| 0.0 to 0.3     | Very Weak   | Negligible relationship       |
| -0.3 to 0.0    | Very Weak   | Negligible negative           |
| -0.5 to -0.3   | Weak        | Slight negative relationship  |
| -0.7 to -0.5   | Moderate    | Noticeable negative           |
| -0.9 to -0.7   | Strong      | Clear negative relationship   |
| -1.0 to -0.9   | Very Strong | Almost perfect negative       |

Important Notes:
----------------
1. Correlation does NOT imply causation!
2. Only measures LINEAR relationships
3. Sensitive to outliers
4. Check scatter plots for non-linear patterns
""")

print("\n" + "=" * 50)
print("✅ Correlation Heatmaps - Complete!")
print("=" * 50)
