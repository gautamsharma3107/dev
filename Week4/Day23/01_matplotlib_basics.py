"""
Day 23 - Matplotlib Basics
===========================
Learn: Line plots, Scatter plots, Bar charts, Histograms

Key Concepts:
- Matplotlib is the foundation library for Python visualization
- plt.plot() for line charts
- plt.scatter() for scatter plots
- plt.bar() for bar charts
- plt.hist() for histograms
"""

import matplotlib.pyplot as plt
import numpy as np

# ========== LINE PLOTS ==========
print("=" * 50)
print("LINE PLOTS")
print("=" * 50)

# Simple line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linewidth=2, label='sin(x)')
plt.title('Simple Line Plot - Sine Wave', fontsize=14)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('01_line_plot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Line plot saved as '01_line_plot.png'")

# Multiple lines on same plot
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label='sin(x)', color='blue', linestyle='-')
plt.plot(x, np.cos(x), label='cos(x)', color='red', linestyle='--')
plt.plot(x, np.tan(x), label='tan(x)', color='green', linestyle=':')
plt.title('Multiple Line Plot - Trigonometric Functions', fontsize=14)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.ylim(-2, 2)  # Limit y-axis for better visualization
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('02_multiple_lines.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Multiple lines plot saved as '02_multiple_lines.png'")

# ========== SCATTER PLOTS ==========
print("\n" + "=" * 50)
print("SCATTER PLOTS")
print("=" * 50)

# Simple scatter plot
np.random.seed(42)
x = np.random.randn(100)
y = x + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='blue', alpha=0.6, edgecolors='black', s=50)
plt.title('Simple Scatter Plot', fontsize=14)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('03_scatter_plot.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Scatter plot saved as '03_scatter_plot.png'")

# Scatter plot with color and size variation
colors = np.random.rand(100)
sizes = np.random.rand(100) * 500

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(scatter, label='Color Scale')
plt.title('Scatter Plot with Color and Size Variation', fontsize=14)
plt.xlabel('X values', fontsize=12)
plt.ylabel('Y values', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('04_scatter_colors.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Colored scatter plot saved as '04_scatter_colors.png'")

# ========== BAR CHARTS ==========
print("\n" + "=" * 50)
print("BAR CHARTS")
print("=" * 50)

# Simple bar chart
categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
values = [85, 78, 72, 65, 58]

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['#3776ab', '#f7df1e', '#b07219', '#00599C', '#00ADD8'])
plt.title('Programming Language Popularity', fontsize=14)
plt.xlabel('Languages', fontsize=12)
plt.ylabel('Popularity Score', fontsize=12)

# Add value labels on bars
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(value), ha='center', fontsize=10)

plt.savefig('05_bar_chart.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Bar chart saved as '05_bar_chart.png'")

# Horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(categories, values, color=['#3776ab', '#f7df1e', '#b07219', '#00599C', '#00ADD8'])
plt.title('Programming Language Popularity (Horizontal)', fontsize=14)
plt.xlabel('Popularity Score', fontsize=12)
plt.ylabel('Languages', fontsize=12)
plt.savefig('06_horizontal_bar.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Horizontal bar chart saved as '06_horizontal_bar.png'")

# Grouped bar chart
x_pos = np.arange(len(categories))
width = 0.35
values_2023 = [85, 78, 72, 65, 58]
values_2024 = [88, 82, 70, 62, 65]

plt.figure(figsize=(12, 6))
plt.bar(x_pos - width/2, values_2023, width, label='2023', color='steelblue')
plt.bar(x_pos + width/2, values_2024, width, label='2024', color='coral')
plt.xticks(x_pos, categories)
plt.title('Language Popularity Comparison 2023 vs 2024', fontsize=14)
plt.xlabel('Languages', fontsize=12)
plt.ylabel('Popularity Score', fontsize=12)
plt.legend()
plt.savefig('07_grouped_bar.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Grouped bar chart saved as '07_grouped_bar.png'")

# ========== HISTOGRAMS ==========
print("\n" + "=" * 50)
print("HISTOGRAMS")
print("=" * 50)

# Simple histogram
np.random.seed(42)
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='steelblue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Normal Distribution', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.savefig('08_histogram.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Histogram saved as '08_histogram.png'")

# Histogram with multiple datasets
data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2

plt.figure(figsize=(10, 6))
plt.hist(data1, bins=30, alpha=0.5, label='Dataset 1', color='blue')
plt.hist(data2, bins=30, alpha=0.5, label='Dataset 2', color='red')
plt.title('Overlapping Histograms', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.savefig('09_overlapping_hist.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Overlapping histograms saved as '09_overlapping_hist.png'")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE - Sales Dashboard")
print("=" * 50)

# Create a 2x2 subplot dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Line chart - Monthly sales
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 135, 142, 138, 155, 168]
axes[0, 0].plot(months, sales, marker='o', color='green', linewidth=2)
axes[0, 0].set_title('Monthly Sales Trend')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales ($K)')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Bar chart - Product sales
products = ['A', 'B', 'C', 'D', 'E']
product_sales = [45, 62, 38, 55, 48]
axes[0, 1].bar(products, product_sales, color='coral')
axes[0, 1].set_title('Product-wise Sales')
axes[0, 1].set_xlabel('Product')
axes[0, 1].set_ylabel('Sales ($K)')

# Plot 3: Scatter - Customer spend vs visits
visits = np.random.randint(1, 20, 50)
spend = visits * 15 + np.random.randn(50) * 30
axes[1, 0].scatter(visits, spend, c='purple', alpha=0.6)
axes[1, 0].set_title('Customer Spend vs Visits')
axes[1, 0].set_xlabel('Number of Visits')
axes[1, 0].set_ylabel('Total Spend ($)')

# Plot 4: Histogram - Transaction amounts
transactions = np.random.exponential(50, 500)
axes[1, 1].hist(transactions, bins=25, color='teal', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Transaction Amount Distribution')
axes[1, 1].set_xlabel('Amount ($)')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('10_sales_dashboard.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Sales dashboard saved as '10_sales_dashboard.png'")

print("\n" + "=" * 50)
print("✅ Matplotlib Basics - Complete!")
print("=" * 50)
