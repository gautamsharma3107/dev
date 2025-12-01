"""
Day 23 - Seaborn for Better Visuals
====================================
Learn: Seaborn library for statistical visualizations

Key Concepts:
- Seaborn is built on Matplotlib and provides better default aesthetics
- Great for statistical visualizations
- Easy to create complex visualizations with less code
- Built-in themes and color palettes
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set Seaborn style
sns.set_theme(style="whitegrid")

# ========== SEABORN SETUP AND STYLES ==========
print("=" * 50)
print("SEABORN SETUP AND STYLES")
print("=" * 50)

# Create sample data
np.random.seed(42)
df = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C', 'D'], 200),
    'value1': np.random.randn(200) * 10 + 50,
    'value2': np.random.randn(200) * 15 + 60,
    'count': np.random.randint(10, 100, 200)
})

print("Sample DataFrame:")
print(df.head())
print(f"\nShape: {df.shape}")

# ========== SEABORN THEMES ==========
print("\n" + "=" * 50)
print("SEABORN THEMES")
print("=" * 50)

# Different themes demonstration
themes = ['whitegrid', 'darkgrid', 'white', 'dark', 'ticks']

fig, axes = plt.subplots(1, 5, figsize=(20, 4))
for ax, theme in zip(axes, themes):
    sns.set_theme(style=theme)
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x))
    ax.set_title(f'Theme: {theme}')

plt.tight_layout()
plt.savefig('seaborn_01_themes.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Themes comparison saved as 'seaborn_01_themes.png'")

# Reset to whitegrid for rest of examples
sns.set_theme(style="whitegrid")

# ========== CATEGORICAL PLOTS ==========
print("\n" + "=" * 50)
print("CATEGORICAL PLOTS")
print("=" * 50)

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='value1', data=df, palette='Set2')
plt.title('Bar Plot - Average Value by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Average Value', fontsize=12)
plt.savefig('seaborn_02_barplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Bar plot saved as 'seaborn_02_barplot.png'")

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='value1', data=df, palette='husl')
plt.title('Box Plot - Distribution by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.savefig('seaborn_03_boxplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Box plot saved as 'seaborn_03_boxplot.png'")

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='category', y='value1', data=df, palette='muted')
plt.title('Violin Plot - Distribution Shape by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.savefig('seaborn_04_violinplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Violin plot saved as 'seaborn_04_violinplot.png'")

# Swarm plot (shows all data points)
plt.figure(figsize=(10, 6))
sample_df = df.sample(50)  # Use smaller sample for visibility
sns.swarmplot(x='category', y='value1', data=sample_df, palette='dark')
plt.title('Swarm Plot - Individual Points by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.savefig('seaborn_05_swarmplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Swarm plot saved as 'seaborn_05_swarmplot.png'")

# ========== RELATIONSHIP PLOTS ==========
print("\n" + "=" * 50)
print("RELATIONSHIP PLOTS")
print("=" * 50)

# Scatter plot with hue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='value1', y='value2', hue='category', data=df, palette='deep', s=100)
plt.title('Scatter Plot with Categories', fontsize=14)
plt.xlabel('Value 1', fontsize=12)
plt.ylabel('Value 2', fontsize=12)
plt.legend(title='Category')
plt.savefig('seaborn_06_scatterplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Scatter plot saved as 'seaborn_06_scatterplot.png'")

# Line plot
# Create time series data
dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
ts_data = pd.DataFrame({
    'date': np.tile(dates, 2),
    'value': np.concatenate([
        np.cumsum(np.random.randn(30)) + 50,
        np.cumsum(np.random.randn(30)) + 45
    ]),
    'group': np.repeat(['Group A', 'Group B'], 30)
})

plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='value', hue='group', data=ts_data, marker='o', markersize=4)
plt.title('Line Plot - Time Series Comparison', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('seaborn_07_lineplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Line plot saved as 'seaborn_07_lineplot.png'")

# Regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='value1', y='value2', data=df, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Regression Plot - Linear Relationship', fontsize=14)
plt.xlabel('Value 1', fontsize=12)
plt.ylabel('Value 2', fontsize=12)
plt.savefig('seaborn_08_regplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Regression plot saved as 'seaborn_08_regplot.png'")

# ========== FACET GRIDS ==========
print("\n" + "=" * 50)
print("FACET GRIDS - Multiple Plots")
print("=" * 50)

# FacetGrid for categorical comparison
g = sns.FacetGrid(df, col='category', col_wrap=2, height=4)
g.map(plt.hist, 'value1', bins=20, color='steelblue', edgecolor='black')
g.fig.suptitle('Distribution of Values by Category', y=1.02, fontsize=14)
plt.tight_layout()
plt.savefig('seaborn_09_facetgrid.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ FacetGrid saved as 'seaborn_09_facetgrid.png'")

# Pair plot for multiple variables
sample_df = df[['value1', 'value2', 'count', 'category']].sample(100)
g = sns.pairplot(sample_df, hue='category', palette='husl', diag_kind='kde')
g.fig.suptitle('Pair Plot - Variable Relationships', y=1.02, fontsize=14)
plt.savefig('seaborn_10_pairplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Pair plot saved as 'seaborn_10_pairplot.png'")

# ========== COLOR PALETTES ==========
print("\n" + "=" * 50)
print("COLOR PALETTES")
print("=" * 50)

palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for ax, palette in zip(axes, palettes):
    colors = sns.color_palette(palette, 6)
    for i, color in enumerate(colors):
        ax.bar(i, 1, color=color, width=0.8)
    ax.set_title(f"Palette: {palette}")
    ax.set_xticks([])
    ax.set_yticks([])

plt.suptitle('Seaborn Color Palettes', fontsize=14)
plt.tight_layout()
plt.savefig('seaborn_11_palettes.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Color palettes saved as 'seaborn_11_palettes.png'")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE - Customer Analysis Dashboard")
print("=" * 50)

# Create customer data
np.random.seed(42)
customers = pd.DataFrame({
    'age': np.random.randint(18, 70, 200),
    'income': np.random.normal(50000, 20000, 200),
    'spending_score': np.random.randint(1, 100, 200),
    'segment': np.random.choice(['Budget', 'Standard', 'Premium'], 200),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 200)
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Distribution of spending scores by segment
sns.boxplot(x='segment', y='spending_score', data=customers, palette='Set2', ax=axes[0, 0])
axes[0, 0].set_title('Spending Score by Customer Segment')

# Plot 2: Age vs Income scatter by segment
sns.scatterplot(x='age', y='income', hue='segment', data=customers, palette='deep', ax=axes[0, 1])
axes[0, 1].set_title('Age vs Income by Segment')

# Plot 3: Customer count by region and segment
customer_counts = customers.groupby(['region', 'segment']).size().unstack()
customer_counts.plot(kind='bar', ax=axes[1, 0], colormap='Set2')
axes[1, 0].set_title('Customer Distribution by Region and Segment')
axes[1, 0].legend(title='Segment')
axes[1, 0].tick_params(axis='x', rotation=0)

# Plot 4: Income distribution by region
sns.violinplot(x='region', y='income', data=customers, palette='muted', ax=axes[1, 1])
axes[1, 1].set_title('Income Distribution by Region')

plt.tight_layout()
plt.savefig('seaborn_12_dashboard.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Customer analysis dashboard saved as 'seaborn_12_dashboard.png'")

print("\n" + "=" * 50)
print("✅ Seaborn for Better Visuals - Complete!")
print("=" * 50)
