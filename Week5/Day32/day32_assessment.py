"""
DAY 32 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes

Answer all questions. Good luck!
"""

print("=" * 60)
print("DAY 32 ASSESSMENT TEST - Transfer Learning")
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
Q1. What is Transfer Learning?
a) Training a model from scratch
b) Reusing a model trained on one task for another task
c) Transferring data between computers
d) A type of reinforcement learning

Your answer: """)

print("""
Q2. When using a pre-trained model, what does 'include_top=False' mean?
a) Include all layers of the model
b) Only include the first layer
c) Remove the classification head layer
d) Flip the model upside down

Your answer: """)

print("""
Q3. What learning rate should you use when fine-tuning a pre-trained model?
a) Very high (0.1)
b) High (0.01)
c) Normal (0.001)
d) Very low (0.00001)

Your answer: """)

print("""
Q4. What is the main purpose of data augmentation?
a) To speed up training
b) To increase effective training data and reduce overfitting
c) To decrease model accuracy
d) To convert images to text

Your answer: """)

print("""
Q5. Which pre-trained model is best for mobile/edge deployment?
a) VGG16 (138M parameters)
b) ResNet101 (45M parameters)
c) MobileNetV2 (3.4M parameters)
d) EfficientNetB7 (66M parameters)

Your answer: """)

print("""
Q6. In the two-phase transfer learning approach, what happens in Phase 1?
a) Fine-tune all layers
b) Freeze all base model layers and train only new classifier
c) Train from scratch
d) Delete the pre-trained weights

Your answer: """)

# ============================================================
# SECTION B: Short Coding Challenges (6 points)
# 2 points each
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Complete the code to load a pre-trained MobileNetV2 
    without the classification layer for 224x224 RGB images.

from tensorflow.keras.applications import MobileNetV2

base_model = MobileNetV2(
    ________________,  # Use ImageNet weights
    ________________,  # Remove top layer
    ________________   # Input shape
)
""")

# Write your code here:




print("""
Q8. (2 points) Write code to freeze all layers of a base model
    and then create a simple classification head with 5 classes.

# base_model is already loaded

# Step 1: Freeze base model
___________________________

# Step 2: Add classification head
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
outputs = ___________________________  # 5 classes with softmax

model = Model(inputs=base_model.input, outputs=outputs)
""")

# Write your code here:




print("""
Q9. (2 points) Create a data augmentation pipeline using Keras 
    preprocessing layers that includes:
    - Horizontal flip
    - Random rotation (10%)
    - Random zoom (20%)

import tensorflow as tf
from tensorflow.keras import layers

data_augmentation = tf.keras.Sequential([
    ________________,
    ________________,
    ________________
])
""")

# Write your code here:




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain why we use a very low learning rate when 
     fine-tuning a pre-trained model. What could happen if we use 
     a high learning rate?

Your answer:
""")

# Write your explanation here as comments:
# 
# 
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
Q1: b) Reusing a model trained on one task for another task
Q2: c) Remove the classification head layer
Q3: d) Very low (0.00001)
Q4: b) To increase effective training data and reduce overfitting
Q5: c) MobileNetV2 (3.4M parameters)
Q6: b) Freeze all base model layers and train only new classifier

Section B (Coding):

Q7:
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

Q8:
# Freeze base model
base_model.trainable = False

# Output layer with 5 classes
outputs = Dense(5, activation='softmax')(x)

Q9:
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.2)
])

Section C:

Q10: 
We use a very low learning rate when fine-tuning because:
1. Pre-trained weights have already learned useful features
2. A high learning rate would make large weight updates
3. This would destroy the pre-trained knowledge
4. We want to make small adjustments to adapt features

If we use a high learning rate:
- Pre-trained weights would be overwritten
- Model would essentially train from scratch
- We'd lose the benefit of transfer learning
- Training would be unstable and may not converge
- This is called "catastrophic forgetting"

The low learning rate allows:
- Small, gradual adjustments
- Preservation of learned features
- Adaptation to new task without forgetting
"""
