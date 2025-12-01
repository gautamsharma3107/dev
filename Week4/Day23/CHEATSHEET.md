# Day 23 Quick Reference Cheat Sheet

## Matplotlib Basics
```python
import matplotlib.pyplot as plt
import numpy as np

# Basic plot structure
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)
ax.set_title("Title")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
plt.show()

# Line Plot
plt.plot(x, y, color='blue', linestyle='-', marker='o', label='Data')
plt.legend()

# Scatter Plot
plt.scatter(x, y, c='red', s=50, alpha=0.5)

# Bar Plot
plt.bar(categories, values, color='green')
plt.barh(categories, values)  # Horizontal

# Histogram
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
```

## Seaborn for Better Visuals
```python
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")
sns.set_palette("husl")

# Distribution plots
sns.histplot(data, kde=True)
sns.kdeplot(data, shade=True)

# Categorical plots
sns.barplot(x='category', y='value', data=df)
sns.boxplot(x='category', y='value', data=df)
sns.violinplot(x='category', y='value', data=df)

# Relationship plots
sns.scatterplot(x='x', y='y', hue='category', data=df)
sns.lineplot(x='x', y='y', data=df)

# Regression plot
sns.regplot(x='x', y='y', data=df)
sns.lmplot(x='x', y='y', hue='category', data=df)
```

## Plotting Distributions
```python
# Histogram with KDE
sns.histplot(data, kde=True, bins=30)

# KDE plot only
sns.kdeplot(data, fill=True)

# Box plot
sns.boxplot(x=data)

# Violin plot
sns.violinplot(x=data)

# QQ plot
from scipy import stats
stats.probplot(data, dist="norm", plot=plt)
```

## Correlation Heatmaps
```python
# Calculate correlation matrix
corr_matrix = df.corr()

# Basic heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Customized heatmap
sns.heatmap(
    corr_matrix,
    annot=True,          # Show values
    fmt='.2f',           # Format values
    cmap='RdYlBu_r',     # Color map
    center=0,            # Center color at 0
    linewidths=0.5,      # Line between cells
    square=True,         # Square cells
    vmin=-1, vmax=1      # Value range
)

# Mask upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm')
```

## Chart Customization
```python
# Figure and subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y)

# Colors
plt.plot(x, y, color='#FF5733')     # Hex color
plt.plot(x, y, color='red')          # Named color
plt.plot(x, y, color=(0.1, 0.2, 0.5)) # RGB tuple

# Line styles
linestyles = ['-', '--', '-.', ':']  # solid, dashed, dashdot, dotted

# Markers
markers = ['o', 's', '^', 'D', 'v', '*', 'p', 'h']

# Annotations
plt.annotate('Peak', xy=(x_point, y_point),
             xytext=(x_offset, y_offset),
             arrowprops=dict(arrowstyle='->'))

# Grid and styling
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save figure
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

## Common Color Palettes
```python
# Seaborn palettes
'deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'

# Matplotlib colormaps
'viridis', 'plasma', 'inferno', 'magma'  # Sequential
'coolwarm', 'RdYlBu', 'seismic'          # Diverging
'Set1', 'Set2', 'Set3', 'tab10'          # Categorical
```

## Quick Patterns
```python
# Multiple plots in one figure
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, data in zip(axes, [data1, data2, data3]):
    ax.hist(data)
plt.tight_layout()

# Save all plots
plt.savefig('all_plots.png', dpi=300)

# Clear and close
plt.clf()  # Clear current figure
plt.close('all')  # Close all figures
```

---
**Keep this handy for quick reference!** 📊🚀
