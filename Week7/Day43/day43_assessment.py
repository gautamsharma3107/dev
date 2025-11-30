"""
DAY 43 ASSESSMENT TEST
======================
Total: 14 points
Pass: 10+ points (70%)
Time: 15 minutes
"""

print("=" * 60)
print("DAY 43 ASSESSMENT - Advanced Computer Vision")
print("=" * 60)
print("Total Points: 14 | Passing Score: 10 (70%)")
print("=" * 60)

# ============================================================
# SECTION A: Multiple Choice Questions (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION A: Multiple Choice (6 points)")
print("=" * 60)

print("""
Q1. What color format does OpenCV use by default?
a) RGB
b) BGR
c) HSV
d) CMYK

Your answer: """)

print("""
Q2. Which function is used to detect faces using Haar cascades?
a) detectFaces()
b) findContours()
c) detectMultiScale()
d) cascadeDetect()

Your answer: """)

print("""
Q3. What does IOU stand for in object detection?
a) Input Output Unit
b) Intersection Over Union
c) Image Object Utility
d) Intelligent Object Understanding

Your answer: """)

print("""
Q4. What is the purpose of Non-Maximum Suppression (NMS)?
a) Increase image brightness
b) Remove duplicate overlapping bounding boxes
c) Sharpen images
d) Detect edges

Your answer: """)

print("""
Q5. Which edge detection method is most commonly used?
a) Sobel only
b) Laplacian only
c) Canny
d) Roberts

Your answer: """)

print("""
Q6. What does the scaleFactor parameter in detectMultiScale() do?
a) Scales the output bounding boxes
b) Determines how much image size is reduced at each scale
c) Adjusts the color intensity
d) Sets the minimum face size

Your answer: """)

# ============================================================
# SECTION B: Coding Challenges (6 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION B: Coding Challenges (6 points)")
print("=" * 60)

print("""
Q7. (2 points) Write code to:
    1. Create a 400x400 black image
    2. Draw a green rectangle from (50,50) to (150,150)
    3. Draw a red circle at center (300,300) with radius 50
""")

# Write your code here:
import cv2
import numpy as np

# Your solution:




print("""
Q8. (2 points) Write a function that takes an image and returns
    the number of faces detected using Haar cascades.
    Use appropriate scaleFactor and minNeighbors values.
""")

# Write your code here:

# def count_faces(image):
#     # Your code here
#     pass




print("""
Q9. (2 points) Write code to apply Canny edge detection to a 
    grayscale image with threshold values of 100 and 200.
    Also apply Gaussian blur (5x5) before edge detection.
""")

# Write your code here:

# def detect_edges(gray_image):
#     # Your code here
#     pass




# ============================================================
# SECTION C: Conceptual Question (2 points)
# ============================================================

print("\n" + "=" * 60)
print("SECTION C: Conceptual Question (2 points)")
print("=" * 60)

print("""
Q10. (2 points) Explain the difference between:
     - Haar cascade face detection
     - DNN-based face detection
     
     Which one would you choose for a production application and why?

Your answer:
""")

# Write your explanation here as comments:
# 




print("\n" + "=" * 60)
print("TEST COMPLETE!")
print("=" * 60)

"""
ANSWER KEY
==========

Section A:
Q1: b) BGR
Q2: c) detectMultiScale()
Q3: b) Intersection Over Union
Q4: b) Remove duplicate overlapping bounding boxes
Q5: c) Canny
Q6: b) Determines how much image size is reduced at each scale

Section B:
Q7:
import cv2
import numpy as np

# Create black image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw green rectangle (BGR format, so green is (0, 255, 0))
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), -1)

# Draw red circle (BGR format, so red is (0, 0, 255))
cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)


Q8:
def count_faces(image):
    # Load cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    return len(faces)


Q9:
def detect_edges(gray_image):
    # Apply Gaussian blur first to reduce noise
    blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)
    
    return edges


Section C:
Q10:
Haar Cascade Face Detection:
- Uses Haar-like features (edge, line, center features)
- Fast, works well on CPU
- Less accurate, especially for:
  * Faces at different angles
  * Partially occluded faces
  * Poor lighting conditions
- Pre-trained, easy to use

DNN-based Face Detection:
- Uses deep neural networks (typically SSD + ResNet)
- More accurate in various conditions
- Better handles:
  * Different face angles
  * Occlusions
  * Lighting variations
- Can be slower on CPU, faster with GPU
- More robust and reliable

For Production:
I would choose DNN-based detection because:
1. More accurate = fewer false positives/negatives
2. Handles real-world conditions better
3. More consistent results across different images
4. Can leverage GPU acceleration
5. Better for user-facing applications where reliability matters

However, Haar cascades are still useful for:
- Resource-constrained devices
- Quick prototyping
- Simple use cases with controlled conditions
"""
