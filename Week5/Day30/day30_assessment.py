"""
DAY 30 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Topics Covered:
- TensorFlow/Keras Setup
- Tensors and Operations
- Building Neural Networks
- Training and Evaluation

Answer all questions. Good luck!
"""

print("=" * 70)
print("DAY 30 ASSESSMENT TEST - TensorFlow/Keras Setup")
print("=" * 70)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 70)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# 1 point each
# ============================================================

print("\n" + "=" * 70)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 70)

print("""
Q1. What is a tensor in TensorFlow?
a) A Python list
b) A multi-dimensional array optimized for computation
c) A database
d) A type of neural network

Your answer: """)

print("""
Q2. Which activation function is recommended for the OUTPUT layer of a binary classification model?
a) ReLU
b) Softmax
c) Sigmoid
d) Tanh

Your answer: """)

print("""
Q3. What does the 'input_shape' parameter specify in the first layer?
a) The number of neurons
b) The shape of input data
c) The batch size
d) The learning rate

Your answer: """)

print("""
Q4. Which of the following is NOT a valid TensorFlow tensor creation method?
a) tf.constant([1, 2, 3])
b) tf.zeros((3, 3))
c) tf.create([1, 2, 3])
d) tf.ones((2, 2))

Your answer: """)

print("""
Q5. What happens during the backward pass (backpropagation)?
a) Predictions are made
b) Loss is calculated
c) Gradients are computed and weights are updated
d) Data is loaded

Your answer: """)

print("""
Q6. Which loss function should be used for multi-class classification with integer labels?
a) binary_crossentropy
b) sparse_categorical_crossentropy
c) mse
d) mae

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 70)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 70)

print("""
Q7. (2 points) Write code to create a 3x4 tensor filled with the value 5.
""")

# Write your code here:
import tensorflow as tf

# Your tensor creation code:




print("""
Q8. (2 points) Write code to create and compile a Sequential model for binary classification.
Requirements:
- Input: 10 features
- Hidden layer: 32 neurons with ReLU
- Output: 1 neuron with sigmoid
- Use Adam optimizer and binary_crossentropy loss
""")

# Write your code here:
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Your model code:




print("""
Q9. (2 points) Given a trained model and test data, write code to:
1. Evaluate the model on test data
2. Make predictions and convert probabilities to class labels (threshold 0.5)
""")

# Write your code here:
# Assume: model (trained), X_test, y_test are already defined

# Your evaluation and prediction code:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 70)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 70)

print("""
Q10. (2 points) Explain the difference between model.fit() training parameters:
- epochs
- batch_size
How do they affect training?

Your answer:
""")

# Write your explanation here as comments:
#
#
#


# ============================================================
# TEST COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("TEST COMPLETE!")
print("=" * 70)
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
============================================================
ANSWER KEY (Don't look until you're done!)
============================================================

Section A (MCQ):
Q1: b) A multi-dimensional array optimized for computation
Q2: c) Sigmoid
Q3: b) The shape of input data
Q4: c) tf.create([1, 2, 3]) (this function doesn't exist)
Q5: c) Gradients are computed and weights are updated
Q6: b) sparse_categorical_crossentropy

Section B (Coding):

Q7: Create tensor filled with 5
    tensor = tf.fill((3, 4), 5)
    # or (more idiomatic TensorFlow)
    tensor = tf.ones((3, 4)) * 5

Q8: Binary classification model
    model = Sequential([
        Dense(32, activation='relu', input_shape=(10,)),
        Dense(1, activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

Q9: Evaluation and prediction
    # Evaluate
    loss, accuracy = model.evaluate(X_test, y_test)
    
    # Predict and convert to classes
    predictions = model.predict(X_test)
    classes = (predictions > 0.5).astype(int)

Section C:

Q10: Explanation
    - epochs: Number of times the entire training dataset is passed through 
      the network. More epochs = more learning opportunities, but risk of 
      overfitting.
    
    - batch_size: Number of samples processed before updating weights. 
      Smaller batches = more frequent updates, more noise in training.
      Larger batches = more stable but may generalize worse.
    
    Example: 1000 samples, batch_size=100, epochs=5
    = 10 batches per epoch × 5 epochs = 50 weight updates total

============================================================
SCORING:
Section A: 6 points (1 each)
Section B: 6 points (2 each)
Section C: 2 points
Total: 14 points
Pass: 10+ points (70%)
============================================================
"""
