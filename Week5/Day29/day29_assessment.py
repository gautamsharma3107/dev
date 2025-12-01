"""
DAY 29 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 29 ASSESSMENT TEST - Neural Networks Fundamentals")
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
Q1. What is the main purpose of activation functions in neural networks?
a) To initialize weights
b) To introduce non-linearity
c) To reduce overfitting
d) To speed up training

Your answer: """)

print("""
Q2. Which activation function outputs values between 0 and 1?
a) ReLU
b) Tanh
c) Sigmoid
d) Leaky ReLU

Your answer: """)

print("""
Q3. What is the "dying ReLU" problem?
a) ReLU is computationally expensive
b) ReLU neurons can get stuck outputting 0 for all inputs
c) ReLU causes exploding gradients
d) ReLU cannot be differentiated

Your answer: """)

print("""
Q4. In backpropagation, what mathematical concept is used to compute gradients?
a) Matrix multiplication
b) The chain rule
c) Integration
d) Cross-validation

Your answer: """)

print("""
Q5. Which loss function is most appropriate for multi-class classification?
a) Mean Squared Error
b) Binary Cross-Entropy
c) Categorical Cross-Entropy
d) Mean Absolute Error

Your answer: """)

print("""
Q6. What is the typical default learning rate for the Adam optimizer?
a) 0.1
b) 0.01
c) 0.001
d) 0.0001

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Implement the ReLU activation function.
Complete the function below:
""")

import numpy as np

def relu(x):
    # Write your code here
    pass

# Test your implementation
test_values = np.array([-2, -1, 0, 1, 2])
# Expected output: [0, 0, 0, 1, 2]

print("""
Q8. (2 points) Calculate the output of a single neuron.
Given: inputs = [1, 2, 3], weights = [0.5, -0.3, 0.2], bias = 0.1
Calculate: output = sum(inputs * weights) + bias
""")

inputs = np.array([1, 2, 3])
weights = np.array([0.5, -0.3, 0.2])
bias = 0.1

# Write your code here to calculate output


print("""
Q9. (2 points) Implement one step of gradient descent.
Given: weight = 2.0, gradient = 0.5, learning_rate = 0.1
Calculate: new_weight = weight - learning_rate * gradient
""")

weight = 2.0
gradient = 0.5
learning_rate = 0.1

# Write your code here to calculate new_weight


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain why a single-layer perceptron cannot solve the XOR problem.
What is the minimum number of layers needed to solve XOR, and why?

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

Good luck! 🚀
""")

"""
ANSWER KEY (Don't look until you're done!)
============================================

Section A (MCQ):
Q1: b) To introduce non-linearity
    Without non-linearity, stacking layers would just be linear transformations

Q2: c) Sigmoid
    Sigmoid: f(x) = 1 / (1 + e^(-x)), outputs (0, 1)

Q3: b) ReLU neurons can get stuck outputting 0 for all inputs
    When weights become negative, ReLU outputs 0 and gradients are 0

Q4: b) The chain rule
    Backprop uses chain rule to compute gradients through composed functions

Q5: c) Categorical Cross-Entropy
    CCE is designed for multi-class classification with softmax output

Q6: c) 0.001
    Adam's default learning rate is typically 0.001

Section B (Coding):
Q7: 
def relu(x):
    return np.maximum(0, x)

Q8:
output = np.sum(inputs * weights) + bias
# = (1*0.5) + (2*-0.3) + (3*0.2) + 0.1
# = 0.5 - 0.6 + 0.6 + 0.1 = 0.6

Q9:
new_weight = weight - learning_rate * gradient
# = 2.0 - 0.1 * 0.5 = 1.95

Section C:
Q10: 
- A single-layer perceptron can only create linear decision boundaries
- XOR is not linearly separable (cannot draw a single line to separate classes)
- Minimum 2 layers (1 hidden + 1 output) are needed
- The hidden layer can learn intermediate representations that make the problem
  linearly separable for the output layer
- First layer separates (0,0) and (1,1) from (0,1) and (1,0)
- Second layer combines these to produce correct XOR output
"""
