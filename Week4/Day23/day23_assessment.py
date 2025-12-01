"""
DAY 23 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 23 ASSESSMENT TEST - Data Visualization Essentials")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. Which Matplotlib function is used to create a scatter plot?
a) plt.line()
b) plt.scatter()
c) plt.points()
d) plt.draw()

Your answer: """)

print("""
Q2. What does the 'alpha' parameter control in a plot?
a) The color of the plot
b) The size of markers
c) The transparency of elements
d) The line width

Your answer: """)

print("""
Q3. Which Seaborn function is best for showing the distribution shape and quartiles?
a) sns.barplot()
b) sns.violinplot()
c) sns.scatterplot()
d) sns.lineplot()

Your answer: """)

print("""
Q4. A correlation coefficient of -0.85 indicates:
a) Strong positive relationship
b) Weak positive relationship
c) Strong negative relationship
d) No relationship

Your answer: """)

print("""
Q5. Which parameter in sns.heatmap() is used to display the correlation values?
a) show_values=True
b) annot=True
c) display=True
d) values=True

Your answer: """)

print("""
Q6. What does plt.tight_layout() do?
a) Makes the figure smaller
b) Automatically adjusts subplot parameters to fit the figure
c) Increases the resolution
d) Adds a border to the plot

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to create a line plot with:
- X values from 0 to 10 (use np.linspace with 100 points)
- Y values as sin(x)
- Blue color, dashed line, linewidth of 2
- Title: "Sine Wave"
- Include grid
""")

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Write your code here:




print("""
Q8. (2 points) Write code to create a histogram with KDE overlay:
- Generate 500 random normal values (mean=50, std=10)
- Use 25 bins
- Show KDE curve
- Set title: "Distribution of Values"
""")

# Write your code here:




print("""
Q9. (2 points) Write code to create a correlation heatmap:
- Create a DataFrame with 3 columns: 'A', 'B', 'C' (100 random values each)
- Calculate the correlation matrix
- Create a heatmap with annotations and 'coolwarm' colormap
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain when you would use:
1. A box plot vs a violin plot
2. A scatter plot vs a line plot

What information does each visualization provide?

Your answer:
""")

# Write your explanation here as comments:
# 




# ============================================================
# ANSWER KEY (For self-checking)
# ============================================================

print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)
print("""
When done, check your answers with your professor.
You need at least 10 points to pass!

Remember:
- Review topics you got wrong
- Practice more on weak areas
- Ask questions if confused

Good luck! 📊🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) plt.scatter()
Q2: c) The transparency of elements
Q3: b) sns.violinplot()
Q4: c) Strong negative relationship
Q5: b) annot=True
Q6: b) Automatically adjusts subplot parameters to fit the figure

Section B (Coding):
Q7: Line plot with sine wave
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', linestyle='--', linewidth=2)
plt.title('Sine Wave')
plt.grid(True)
plt.show()
```

Q8: Histogram with KDE
```python
data = np.random.normal(50, 10, 500)
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=25, kde=True)
plt.title('Distribution of Values')
plt.show()
```

Q9: Correlation heatmap
```python
df = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100),
    'C': np.random.randn(100)
})
corr_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()
```

Section C:
Q10: 
Box plot vs Violin plot:
- Box plot: Shows 5-number summary (min, Q1, median, Q3, max) and outliers
- Violin plot: Shows the same + the full distribution shape (density)
- Use violin when distribution shape matters (bimodal, skewed)
- Use box plot for simpler comparison of medians and quartiles

Scatter plot vs Line plot:
- Scatter plot: Shows individual data points, relationships between two variables
- Line plot: Shows trends over time or continuous data
- Use scatter for correlation analysis, discrete observations
- Use line for time series, continuous functions

"""
