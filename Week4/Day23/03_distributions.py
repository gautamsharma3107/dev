"""
Day 23 - Plotting Distributions
================================
Learn: Various ways to visualize data distributions

Key Concepts:
- Histograms show frequency distribution
- KDE (Kernel Density Estimation) for smooth density curves
- Box plots show quartiles and outliers
- Violin plots combine box plots with KDE
- QQ plots check normality
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats

# Set style
sns.set_theme(style="whitegrid")

# ========== GENERATING SAMPLE DATA ==========
print("=" * 50)
print("GENERATING SAMPLE DISTRIBUTIONS")
print("=" * 50)

np.random.seed(42)

# Different distributions
normal_data = np.random.normal(loc=50, scale=10, size=1000)
skewed_data = np.random.exponential(scale=20, size=1000)
bimodal_data = np.concatenate([
    np.random.normal(30, 5, 500),
    np.random.normal(70, 5, 500)
])
uniform_data = np.random.uniform(0, 100, 1000)

print("Generated 4 different distributions:")
print("1. Normal Distribution (mean=50, std=10)")
print("2. Skewed Distribution (exponential)")
print("3. Bimodal Distribution (two peaks)")
print("4. Uniform Distribution (0-100)")

# ========== HISTOGRAMS ==========
print("\n" + "=" * 50)
print("HISTOGRAMS")
print("=" * 50)

# Basic histogram
plt.figure(figsize=(10, 6))
plt.hist(normal_data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
plt.title('Basic Histogram - Normal Distribution', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.axvline(np.mean(normal_data), color='red', linestyle='--', label=f'Mean: {np.mean(normal_data):.2f}')
plt.legend()
plt.savefig('dist_01_histogram.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Basic histogram saved as 'dist_01_histogram.png'")

# Compare different distributions
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].hist(normal_data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Normal Distribution')
axes[0, 0].axvline(np.mean(normal_data), color='red', linestyle='--')

axes[0, 1].hist(skewed_data, bins=30, color='coral', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Skewed Distribution (Exponential)')
axes[0, 1].axvline(np.mean(skewed_data), color='red', linestyle='--')

axes[1, 0].hist(bimodal_data, bins=30, color='green', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Bimodal Distribution')
axes[1, 0].axvline(np.mean(bimodal_data), color='red', linestyle='--')

axes[1, 1].hist(uniform_data, bins=30, color='purple', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Uniform Distribution')
axes[1, 1].axvline(np.mean(uniform_data), color='red', linestyle='--')

plt.tight_layout()
plt.suptitle('Comparing Different Distributions (Red line = Mean)', y=1.02, fontsize=14)
plt.savefig('dist_02_compare.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Distribution comparison saved as 'dist_02_compare.png'")

# ========== KDE PLOTS ==========
print("\n" + "=" * 50)
print("KDE PLOTS (Kernel Density Estimation)")
print("=" * 50)

# Basic KDE
plt.figure(figsize=(10, 6))
sns.kdeplot(normal_data, fill=True, color='steelblue', alpha=0.5)
plt.title('KDE Plot - Smooth Density Estimation', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.savefig('dist_03_kde.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ KDE plot saved as 'dist_03_kde.png'")

# Histogram with KDE overlay
plt.figure(figsize=(10, 6))
sns.histplot(normal_data, bins=30, kde=True, color='steelblue', alpha=0.5)
plt.title('Histogram with KDE Overlay', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig('dist_04_hist_kde.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Histogram with KDE saved as 'dist_04_hist_kde.png'")

# Multiple KDE comparison
plt.figure(figsize=(10, 6))
sns.kdeplot(normal_data, fill=True, label='Normal', alpha=0.5)
sns.kdeplot(skewed_data, fill=True, label='Skewed', alpha=0.5)
sns.kdeplot(bimodal_data, fill=True, label='Bimodal', alpha=0.5)
plt.title('Comparing Distributions with KDE', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend()
plt.savefig('dist_05_kde_compare.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ KDE comparison saved as 'dist_05_kde_compare.png'")

# ========== BOX PLOTS ==========
print("\n" + "=" * 50)
print("BOX PLOTS")
print("=" * 50)

# Create DataFrame for easier plotting
df = pd.DataFrame({
    'Normal': normal_data,
    'Skewed': skewed_data[:1000],
    'Bimodal': bimodal_data,
    'Uniform': uniform_data
})

# Basic box plot
plt.figure(figsize=(10, 6))
df.boxplot()
plt.title('Box Plots - Distribution Summary', fontsize=14)
plt.ylabel('Value', fontsize=12)
plt.savefig('dist_06_boxplot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Box plots saved as 'dist_06_boxplot.png'")

# Seaborn box plot with customization
plt.figure(figsize=(10, 6))
df_melted = df.melt(var_name='Distribution', value_name='Value')
sns.boxplot(x='Distribution', y='Value', data=df_melted, palette='Set2')
plt.title('Seaborn Box Plots - Enhanced Styling', fontsize=14)
plt.savefig('dist_07_boxplot_seaborn.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Seaborn box plots saved as 'dist_07_boxplot_seaborn.png'")

# Box plot anatomy explanation
plt.figure(figsize=(12, 6))
ax = sns.boxplot(x=[1]*100, y=normal_data[:100], width=0.3, color='steelblue')

# Add annotations
plt.annotate('Median (Q2)', xy=(0, np.median(normal_data[:100])), 
             xytext=(0.5, np.median(normal_data[:100])),
             fontsize=10, arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate('Q3 (75th percentile)', xy=(0, np.percentile(normal_data[:100], 75)), 
             xytext=(0.5, np.percentile(normal_data[:100], 75) + 5),
             fontsize=10, arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate('Q1 (25th percentile)', xy=(0, np.percentile(normal_data[:100], 25)), 
             xytext=(0.5, np.percentile(normal_data[:100], 25) - 5),
             fontsize=10, arrowprops=dict(arrowstyle='->', color='red'))

plt.title('Box Plot Anatomy', fontsize=14)
plt.xlim(-0.5, 1.5)
plt.xticks([])
plt.ylabel('Value', fontsize=12)
plt.savefig('dist_08_boxplot_anatomy.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Box plot anatomy saved as 'dist_08_boxplot_anatomy.png'")

# ========== VIOLIN PLOTS ==========
print("\n" + "=" * 50)
print("VIOLIN PLOTS")
print("=" * 50)

# Basic violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, palette='Set3')
plt.title('Violin Plots - Distribution Shape', fontsize=14)
plt.ylabel('Value', fontsize=12)
plt.savefig('dist_09_violin.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Violin plots saved as 'dist_09_violin.png'")

# Split violin plot (compare two groups)
np.random.seed(42)
compare_df = pd.DataFrame({
    'value': np.concatenate([normal_data[:500], normal_data[:500] + 10]),
    'distribution': ['Group A']*500 + ['Group B']*500,
    'category': np.tile(['Cat 1', 'Cat 2', 'Cat 3', 'Cat 4', 'Cat 5'], 200)
})

plt.figure(figsize=(12, 6))
sns.violinplot(x='category', y='value', hue='distribution', data=compare_df, 
               split=True, palette='muted')
plt.title('Split Violin Plot - Group Comparison', fontsize=14)
plt.ylabel('Value', fontsize=12)
plt.legend(title='Group')
plt.savefig('dist_10_violin_split.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Split violin plot saved as 'dist_10_violin_split.png'")

# ========== QQ PLOTS ==========
print("\n" + "=" * 50)
print("QQ PLOTS - Checking Normality")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# QQ plot for normal data
stats.probplot(normal_data, dist="norm", plot=axes[0, 0])
axes[0, 0].set_title('QQ Plot - Normal Data (Should be linear)')

# QQ plot for skewed data
stats.probplot(skewed_data, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('QQ Plot - Skewed Data (Deviates from line)')

# QQ plot for bimodal data
stats.probplot(bimodal_data, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('QQ Plot - Bimodal Data')

# QQ plot for uniform data
stats.probplot(uniform_data, dist="norm", plot=axes[1, 1])
axes[1, 1].set_title('QQ Plot - Uniform Data')

plt.tight_layout()
plt.suptitle('QQ Plots for Normality Check', y=1.02, fontsize=14)
plt.savefig('dist_11_qqplots.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ QQ plots saved as 'dist_11_qqplots.png'")

# ========== DISTRIBUTION STATISTICS ==========
print("\n" + "=" * 50)
print("DISTRIBUTION STATISTICS")
print("=" * 50)

def print_stats(data, name):
    print(f"\n{name}:")
    print(f"  Mean: {np.mean(data):.2f}")
    print(f"  Median: {np.median(data):.2f}")
    print(f"  Std Dev: {np.std(data):.2f}")
    print(f"  Skewness: {stats.skew(data):.2f}")
    print(f"  Kurtosis: {stats.kurtosis(data):.2f}")

print_stats(normal_data, "Normal Distribution")
print_stats(skewed_data, "Skewed Distribution")
print_stats(bimodal_data, "Bimodal Distribution")
print_stats(uniform_data, "Uniform Distribution")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE - Student Grades Analysis")
print("=" * 50)

# Generate student grades data
np.random.seed(42)
grades_data = pd.DataFrame({
    'Math': np.random.normal(75, 12, 200).clip(0, 100),
    'Science': np.random.normal(72, 15, 200).clip(0, 100),
    'English': np.random.normal(78, 10, 200).clip(0, 100),
    'History': np.random.normal(68, 18, 200).clip(0, 100)
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Overlapping histograms
for subject in grades_data.columns:
    axes[0, 0].hist(grades_data[subject], bins=20, alpha=0.5, label=subject)
axes[0, 0].set_title('Grade Distributions by Subject')
axes[0, 0].set_xlabel('Grade')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()

# Plot 2: KDE comparison
for subject in grades_data.columns:
    sns.kdeplot(grades_data[subject], fill=True, alpha=0.3, label=subject, ax=axes[0, 1])
axes[0, 1].set_title('Grade Density Comparison')
axes[0, 1].set_xlabel('Grade')
axes[0, 1].legend()

# Plot 3: Box plots
grades_melted = grades_data.melt(var_name='Subject', value_name='Grade')
sns.boxplot(x='Subject', y='Grade', data=grades_melted, palette='Set2', ax=axes[1, 0])
axes[1, 0].set_title('Grade Distribution Summary')
axes[1, 0].axhline(y=70, color='red', linestyle='--', label='Passing Grade')
axes[1, 0].legend()

# Plot 4: Violin plots
sns.violinplot(x='Subject', y='Grade', data=grades_melted, palette='muted', ax=axes[1, 1])
axes[1, 1].set_title('Grade Distribution Shape')
axes[1, 1].axhline(y=70, color='red', linestyle='--')

plt.tight_layout()
plt.suptitle('Student Grades Analysis', y=1.02, fontsize=14)
plt.savefig('dist_12_grades_analysis.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Student grades analysis saved as 'dist_12_grades_analysis.png'")

print("\n" + "=" * 50)
print("✅ Plotting Distributions - Complete!")
print("=" * 50)
