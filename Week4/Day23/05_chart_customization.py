"""
Day 23 - Chart Customization
==============================
Learn: Styling, colors, annotations, and advanced customization

Key Concepts:
- Figure and axes customization
- Color schemes and palettes
- Annotations and labels
- Legends and titles
- Saving high-quality figures
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# ========== FIGURE AND SUBPLOT LAYOUT ==========
print("=" * 50)
print("FIGURE AND SUBPLOT LAYOUT")
print("=" * 50)

# Different subplot arrangements
fig = plt.figure(figsize=(14, 10))

# 2x2 grid
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax1.set_title('Subplot 1 (2x2)')

ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter([1, 2, 3], [3, 1, 2])
ax2.set_title('Subplot 2 (2x2)')

ax3 = fig.add_subplot(2, 2, 3)
ax3.bar(['A', 'B', 'C'], [3, 2, 5])
ax3.set_title('Subplot 3 (2x2)')

ax4 = fig.add_subplot(2, 2, 4)
ax4.hist(np.random.randn(100), bins=15)
ax4.set_title('Subplot 4 (2x2)')

plt.tight_layout()
plt.savefig('custom_01_subplots.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Subplots layout saved as 'custom_01_subplots.png'")

# Advanced layout with GridSpec
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])  # Top row, all columns
ax1.plot(np.sin(np.linspace(0, 4*np.pi, 100)))
ax1.set_title('Full Width Top')

ax2 = fig.add_subplot(gs[1, :2])  # Middle row, first 2 columns
ax2.bar(['A', 'B', 'C', 'D'], [4, 7, 3, 8])
ax2.set_title('2/3 Width Middle')

ax3 = fig.add_subplot(gs[1, 2])  # Middle row, last column
ax3.pie([30, 40, 30], labels=['X', 'Y', 'Z'], autopct='%1.1f%%')
ax3.set_title('Pie Chart')

ax4 = fig.add_subplot(gs[2, 0])  # Bottom row, first column
ax4.scatter(np.random.rand(20), np.random.rand(20))
ax4.set_title('Scatter')

ax5 = fig.add_subplot(gs[2, 1:])  # Bottom row, last 2 columns
ax5.hist(np.random.randn(500), bins=30)
ax5.set_title('Histogram')

plt.tight_layout()
plt.savefig('custom_02_gridspec.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ GridSpec layout saved as 'custom_02_gridspec.png'")

# ========== COLOR CUSTOMIZATION ==========
print("\n" + "=" * 50)
print("COLOR CUSTOMIZATION")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Named colors
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), color='red', label='red')
axes[0, 0].plot(x, np.cos(x), color='blue', label='blue')
axes[0, 0].plot(x, np.sin(x+1), color='green', label='green')
axes[0, 0].set_title('Named Colors')
axes[0, 0].legend()

# Hex colors
axes[0, 1].plot(x, np.sin(x), color='#FF5733', label='#FF5733')
axes[0, 1].plot(x, np.cos(x), color='#33FF57', label='#33FF57')
axes[0, 1].plot(x, np.sin(x+1), color='#3357FF', label='#3357FF')
axes[0, 1].set_title('Hex Colors')
axes[0, 1].legend()

# RGB tuples
axes[1, 0].plot(x, np.sin(x), color=(0.9, 0.3, 0.3), label='(0.9, 0.3, 0.3)')
axes[1, 0].plot(x, np.cos(x), color=(0.3, 0.9, 0.3), label='(0.3, 0.9, 0.3)')
axes[1, 0].plot(x, np.sin(x+1), color=(0.3, 0.3, 0.9), label='(0.3, 0.3, 0.9)')
axes[1, 0].set_title('RGB Tuple Colors')
axes[1, 0].legend()

# Color with transparency
for i in range(10):
    axes[1, 1].plot(x, np.sin(x + i*0.3), alpha=0.1 + i*0.09, color='blue')
axes[1, 1].set_title('Colors with Transparency (alpha)')

plt.tight_layout()
plt.savefig('custom_03_colors.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Color customization saved as 'custom_03_colors.png'")

# ========== LINE STYLES AND MARKERS ==========
print("\n" + "=" * 50)
print("LINE STYLES AND MARKERS")
print("=" * 50)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Line styles
x = np.linspace(0, 10, 50)
linestyles = ['-', '--', '-.', ':']
labels = ['solid', 'dashed', 'dashdot', 'dotted']

for i, (ls, label) in enumerate(zip(linestyles, labels)):
    axes[0].plot(x, np.sin(x + i), linestyle=ls, linewidth=2, label=label)
axes[0].set_title('Line Styles')
axes[0].legend()

# Markers
markers = ['o', 's', '^', 'D', 'v', '*', 'p', 'h']
marker_names = ['circle', 'square', 'triangle_up', 'diamond', 
                'triangle_down', 'star', 'pentagon', 'hexagon']

for i, (m, name) in enumerate(zip(markers, marker_names)):
    axes[1].plot(x[::5], np.sin(x[::5] + i*0.5), marker=m, 
                 linestyle='-', markersize=8, label=name)
axes[1].set_title('Marker Styles')
axes[1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('custom_04_linestyles.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Line styles saved as 'custom_04_linestyles.png'")

# ========== ANNOTATIONS AND LABELS ==========
print("\n" + "=" * 50)
print("ANNOTATIONS AND LABELS")
print("=" * 50)

# Create data with a peak
x = np.linspace(0, 10, 100)
y = np.sin(x) * np.exp(-0.1 * x)
peak_idx = np.argmax(y)
peak_x, peak_y = x[peak_idx], y[peak_idx]

plt.figure(figsize=(12, 7))
plt.plot(x, y, linewidth=2, color='steelblue')

# Annotate peak
plt.annotate(f'Peak: ({peak_x:.2f}, {peak_y:.2f})',
             xy=(peak_x, peak_y),
             xytext=(peak_x + 2, peak_y + 0.2),
             fontsize=12,
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

# Add text annotations
plt.text(7, 0.3, 'Damped Sine Wave', fontsize=14, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Add horizontal and vertical lines
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
plt.axvline(x=peak_x, color='red', linestyle=':', alpha=0.5)

# Add shaded region
plt.fill_between(x, y, where=(x > 2) & (x < 5), alpha=0.3, color='green')
plt.text(3.5, -0.2, 'Region of Interest', ha='center')

plt.title('Chart with Annotations', fontsize=14)
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('custom_05_annotations.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Annotations saved as 'custom_05_annotations.png'")

# ========== LEGEND CUSTOMIZATION ==========
print("\n" + "=" * 50)
print("LEGEND CUSTOMIZATION")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

x = np.linspace(0, 10, 100)

# Default legend
axes[0, 0].plot(x, np.sin(x), label='sin(x)')
axes[0, 0].plot(x, np.cos(x), label='cos(x)')
axes[0, 0].legend()
axes[0, 0].set_title('Default Legend')

# Legend outside plot
axes[0, 1].plot(x, np.sin(x), label='sin(x)')
axes[0, 1].plot(x, np.cos(x), label='cos(x)')
axes[0, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
axes[0, 1].set_title('Legend Outside')

# Legend with custom style
axes[1, 0].plot(x, np.sin(x), label='sin(x)')
axes[1, 0].plot(x, np.cos(x), label='cos(x)')
axes[1, 0].legend(loc='lower right', 
                   frameon=True, 
                   facecolor='lightgray',
                   edgecolor='black',
                   fontsize=10,
                   title='Functions')
axes[1, 0].set_title('Styled Legend')

# Multiple column legend
for i in range(6):
    axes[1, 1].plot(x, np.sin(x + i*0.5), label=f'sin(x+{i*0.5:.1f})')
axes[1, 1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)
axes[1, 1].set_title('Multi-Column Legend')

plt.tight_layout()
plt.savefig('custom_06_legends.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Legend customization saved as 'custom_06_legends.png'")

# ========== AXIS CUSTOMIZATION ==========
print("\n" + "=" * 50)
print("AXIS CUSTOMIZATION")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Axis limits
axes[0, 0].plot(x, y)
axes[0, 0].set_xlim(2, 8)
axes[0, 0].set_ylim(-0.5, 1)
axes[0, 0].set_title('Custom Axis Limits')

# Log scale
axes[0, 1].plot(np.arange(1, 100), np.arange(1, 100)**2)
axes[0, 1].set_yscale('log')
axes[0, 1].set_title('Log Scale Y-Axis')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y (log scale)')

# Custom ticks
axes[1, 0].plot(x, y)
axes[1, 0].set_xticks([0, np.pi, 2*np.pi, 3*np.pi])
axes[1, 0].set_xticklabels(['0', 'π', '2π', '3π'])
axes[1, 0].set_title('Custom Tick Labels')

# Twin axes
ax_twin = axes[1, 1].twinx()
axes[1, 1].plot(x, np.sin(x), 'b-', label='sin(x)')
ax_twin.plot(x, np.exp(-x/5), 'r--', label='exp(-x/5)')
axes[1, 1].set_ylabel('sin(x)', color='blue')
ax_twin.set_ylabel('exp(-x/5)', color='red')
axes[1, 1].set_title('Twin Axes (Two Y-Axes)')
axes[1, 1].tick_params(axis='y', labelcolor='blue')
ax_twin.tick_params(axis='y', labelcolor='red')

plt.tight_layout()
plt.savefig('custom_07_axes.png', dpi=100, bbox_inches='tight')
plt.show()
print("✅ Axis customization saved as 'custom_07_axes.png'")

# ========== SAVING FIGURES ==========
print("\n" + "=" * 50)
print("SAVING FIGURES")
print("=" * 50)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(np.sin(np.linspace(0, 4*np.pi, 200)), linewidth=2)
ax.set_title('High Quality Export Example')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.grid(True, alpha=0.3)

# Save in different formats
plt.savefig('custom_08_high_dpi.png', dpi=300, bbox_inches='tight')
plt.savefig('custom_08_figure.pdf', format='pdf', bbox_inches='tight')
# plt.savefig('custom_08_figure.svg', format='svg', bbox_inches='tight')
plt.show()

print("""
✅ Figures saved:
   - custom_08_high_dpi.png (300 DPI - high quality)
   - custom_08_figure.pdf (vector format)
   
Saving Tips:
- Use dpi=300 for print quality
- Use bbox_inches='tight' to avoid cropping
- PDF/SVG are vector formats (infinite zoom)
- PNG for web, PDF/SVG for publications
""")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE - Publication-Quality Figure")
print("=" * 50)

# Create publication-quality figure
plt.style.use('seaborn-v0_8-whitegrid')

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Sample data
np.random.seed(42)
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 32, 58]
x_data = np.linspace(0, 10, 100)

# Plot 1: Bar chart with value labels
bars = axes[0, 0].bar(categories, values, color=['#3498db', '#e74c3c', '#2ecc71', '#9b59b6'])
axes[0, 0].set_title('Sales by Category', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Revenue ($K)')
for bar, val in zip(bars, values):
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'${val}K', ha='center', fontsize=10)

# Plot 2: Line chart with confidence interval
y_mean = np.sin(x_data) + 0.5
y_std = 0.2
axes[0, 1].plot(x_data, y_mean, color='#3498db', linewidth=2, label='Mean')
axes[0, 1].fill_between(x_data, y_mean - y_std, y_mean + y_std, 
                         alpha=0.3, color='#3498db', label='±1 std')
axes[0, 1].set_title('Trend with Confidence Interval', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Time (s)')
axes[0, 1].set_ylabel('Value')
axes[0, 1].legend()

# Plot 3: Scatter with regression line
x_scatter = np.random.randn(50) * 2 + 5
y_scatter = x_scatter * 1.5 + np.random.randn(50) * 2
axes[1, 0].scatter(x_scatter, y_scatter, alpha=0.7, c='#e74c3c', edgecolors='black')
z = np.polyfit(x_scatter, y_scatter, 1)
p = np.poly1d(z)
x_line = np.linspace(x_scatter.min(), x_scatter.max(), 100)
axes[1, 0].plot(x_line, p(x_line), '--', color='#2c3e50', linewidth=2, label=f'y = {z[0]:.2f}x + {z[1]:.2f}')
axes[1, 0].set_title('Correlation Analysis', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Variable X')
axes[1, 0].set_ylabel('Variable Y')
axes[1, 0].legend()

# Plot 4: Pie chart
sizes = [35, 30, 20, 15]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
explode = (0.05, 0, 0, 0)
axes[1, 1].pie(sizes, explode=explode, labels=categories, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=90)
axes[1, 1].set_title('Market Share Distribution', fontsize=12, fontweight='bold')

# Add overall title
fig.suptitle('Quarterly Business Report', fontsize=14, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('custom_09_publication.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ Publication-quality figure saved as 'custom_09_publication.png'")

print("\n" + "=" * 50)
print("✅ Chart Customization - Complete!")
print("=" * 50)
