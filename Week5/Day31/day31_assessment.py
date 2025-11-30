"""
DAY 31 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 31 ASSESSMENT TEST - Deep Learning for Images: CNNs")
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
Q1. What is the typical shape of a grayscale image for CNN input in Keras?
a) (batch, height, width)
b) (batch, height, width, 1)
c) (batch, 1, height, width)
d) (height, width, batch)

Your answer: """)

print("""
Q2. What does a 2x2 Max Pooling layer do?
a) Increases the spatial dimensions by 2
b) Adds 2 rows and columns of padding
c) Reduces spatial dimensions by taking maximum value in each 2x2 window
d) Multiplies all values by 2

Your answer: """)

print("""
Q3. In Conv2D(32, (3, 3)), what does 32 represent?
a) The kernel size
b) The number of filters
c) The stride
d) The padding size

Your answer: """)

print("""
Q4. What is the purpose of normalizing image pixel values to [0, 1]?
a) To make the images look better
b) To reduce file size
c) To help neural networks train more effectively
d) To convert images to grayscale

Your answer: """)

print("""
Q5. Which activation function is commonly used in the output layer 
    for a 10-class image classification problem?
a) ReLU
b) Sigmoid
c) Softmax
d) Tanh

Your answer: """)

print("""
Q6. If the input to a Conv2D layer is (28, 28, 1) and we use 
    Conv2D(32, (3, 3), padding='valid'), what is the output shape?
a) (28, 28, 32)
b) (26, 26, 32)
c) (30, 30, 32)
d) (28, 28, 1)

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Complete the code to preprocess MNIST data for a CNN:

from tensorflow.keras.datasets import mnist

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# TODO: Reshape x_train to add channel dimension
# x_train shape should be (60000, 28, 28, 1)
x_train = ______________________________

# TODO: Normalize x_train to range [0, 1]
x_train = ______________________________
""")

# Write your code here:
# x_train = x_train.reshape(-1, 28, 28, 1)
# x_train = x_train.astype('float32') / 255.0


print("""
Q8. (2 points) Build a simple CNN with the following architecture:
    - Conv2D: 32 filters, 3x3 kernel, ReLU, input_shape=(28, 28, 1)
    - MaxPooling2D: 2x2
    - Flatten
    - Dense: 10 neurons, softmax

Write the complete model using Sequential:
""")

# Write your code here:
# model = Sequential([
#     Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
#     MaxPooling2D((2, 2)),
#     Flatten(),
#     Dense(10, activation='softmax')
# ])


print("""
Q9. (2 points) Write code to compile a model with:
    - Optimizer: adam
    - Loss: sparse categorical crossentropy
    - Metrics: accuracy
    
Then train for 5 epochs with batch_size=32 and validation_split=0.1
""")

# Write your code here:
# model.compile(
#     optimizer='adam',
#     loss='sparse_categorical_crossentropy',
#     metrics=['accuracy']
# )
# history = model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)


# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the purpose of convolutional layers in a CNN.
Why are they better than fully connected layers for image processing?
Give at least two advantages.

Your answer:
""")

# Write your explanation here as comments:
# Convolutional layers:
# 1. Parameter Efficiency: Use weight sharing, so fewer parameters than dense layers
# 2. Translation Invariance: Detect features regardless of position in image
# 3. Spatial Hierarchy: Learn low-level to high-level features progressively
# 4. Local Connectivity: Each neuron only looks at a small region


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
Q1: b) (batch, height, width, 1) - Keras uses channels_last format
Q2: c) Reduces spatial dimensions by taking maximum value in each 2x2 window
Q3: b) The number of filters
Q4: c) To help neural networks train more effectively
Q5: c) Softmax - outputs probability distribution over classes
Q6: b) (26, 26, 32) - valid padding reduces size by (kernel_size - 1)

Section B (Coding):

Q7: Preprocessing MNIST
x_train = x_train.reshape(-1, 28, 28, 1)  # Add channel dimension
x_train = x_train.astype('float32') / 255.0  # Normalize

Q8: Building CNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(10, activation='softmax')
])

Q9: Compile and Train
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
history = model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

Section C:

Q10: Purpose of Convolutional Layers
1. PARAMETER EFFICIENCY: Conv layers use weight sharing. A 3x3 filter with 32 
   output channels on a 28x28 image has far fewer parameters than a fully 
   connected layer would have.
   
2. TRANSLATION INVARIANCE: The same filter slides over the entire image, so 
   features can be detected regardless of their position in the image.
   
3. SPATIAL HIERARCHY: Conv layers learn features progressively - early layers 
   detect edges, later layers detect complex patterns and objects.
   
4. LOCAL CONNECTIVITY: Each neuron only looks at a small receptive field 
   (local region), which is more appropriate for image data where nearby 
   pixels are more related than distant ones.
"""
