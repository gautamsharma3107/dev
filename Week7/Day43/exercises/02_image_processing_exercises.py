"""
Day 43 - Image Processing Exercises
====================================
Practice image processing techniques
"""

import cv2
import numpy as np

# ============================================================
# EXERCISE 1: Resize and Transform
# ============================================================
print("Exercise 1: Resize and Transform")
print("-" * 40)

"""
Task: 
1. Create a 400x600 image with text "TRANSFORM"
2. Create 4 versions:
   a) Resized to 50% (200x300)
   b) Rotated 45 degrees
   c) Flipped horizontally
   d) Flipped vertically
3. Stack all 4 into a 2x2 grid and save
"""

# Your solution:




# ============================================================
# EXERCISE 2: Apply Filters
# ============================================================
print("\nExercise 2: Apply Filters")
print("-" * 40)

"""
Task:
1. Create a noisy image (use np.random)
2. Apply these filters:
   a) Gaussian blur (7x7)
   b) Median blur (kernel 7)
   c) Bilateral filter
3. Create a comparison showing original + 3 filtered versions
"""

# Your solution:




# ============================================================
# EXERCISE 3: Edge Detection Comparison
# ============================================================
print("\nExercise 3: Edge Detection Comparison")
print("-" * 40)

"""
Task:
1. Create an image with various shapes (circle, rectangle, triangle)
2. Apply:
   a) Canny edge detection
   b) Sobel (combine X and Y)
   c) Laplacian
3. Create a side-by-side comparison
"""

# Your solution:




# ============================================================
# EXERCISE 4: Thresholding Techniques
# ============================================================
print("\nExercise 4: Thresholding Techniques")
print("-" * 40)

"""
Task:
1. Create a gradient image (0 to 255 horizontally)
2. Apply these thresholding methods:
   a) Simple binary (threshold 127)
   b) Otsu's method
   c) Adaptive mean
   d) Adaptive Gaussian
3. Create comparison showing all results
"""

# Your solution:




# ============================================================
# EXERCISE 5: Morphological Operations
# ============================================================
print("\nExercise 5: Morphological Operations")
print("-" * 40)

"""
Task:
1. Create a binary image with text "MORPH"
2. Apply with 5x5 kernel:
   a) Erosion (2 iterations)
   b) Dilation (2 iterations)
   c) Opening
   d) Closing
3. Show comparison of all operations
"""

# Your solution:




# ============================================================
# SOLUTIONS
# ============================================================
print("\n" + "=" * 60)
print("SOLUTIONS (scroll down after attempting)")
print("=" * 60)

# Solution 1
def solution1():
    # Create original
    img = np.ones((400, 600, 3), dtype=np.uint8) * 200
    cv2.putText(img, "TRANSFORM", (80, 220), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    
    # Resized
    resized = cv2.resize(img, (300, 200))
    
    # Rotated
    center = (img.shape[1]//2, img.shape[0]//2)
    matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))
    rotated = cv2.resize(rotated, (300, 200))
    
    # Flipped
    flipped_h = cv2.flip(img, 1)
    flipped_h = cv2.resize(flipped_h, (300, 200))
    
    flipped_v = cv2.flip(img, 0)
    flipped_v = cv2.resize(flipped_v, (300, 200))
    
    # Grid
    top = np.hstack([resized, rotated])
    bottom = np.hstack([flipped_h, flipped_v])
    result = np.vstack([top, bottom])
    
    cv2.imwrite('/tmp/exercise_transforms.jpg', result)
    print("\n✓ Exercise 1: Saved exercise_transforms.jpg")

solution1()

# Solution 2
def solution2():
    # Create noisy image
    noisy = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
    
    # Apply filters
    gaussian = cv2.GaussianBlur(noisy, (7, 7), 0)
    median = cv2.medianBlur(noisy, 7)
    bilateral = cv2.bilateralFilter(noisy, 9, 75, 75)
    
    # Resize for comparison
    h, w = 150, 150
    noisy_s = cv2.resize(noisy, (w, h))
    gaussian_s = cv2.resize(gaussian, (w, h))
    median_s = cv2.resize(median, (w, h))
    bilateral_s = cv2.resize(bilateral, (w, h))
    
    # Create comparison
    result = np.hstack([noisy_s, gaussian_s, median_s, bilateral_s])
    
    cv2.imwrite('/tmp/exercise_filters.jpg', result)
    print("✓ Exercise 2: Saved exercise_filters.jpg")

solution2()

# Solution 3
def solution3():
    # Create image with shapes
    img = np.zeros((300, 300), dtype=np.uint8)
    cv2.circle(img, (75, 75), 50, 255, -1)
    cv2.rectangle(img, (150, 50), (250, 150), 255, -1)
    pts = np.array([[150, 250], [100, 280], [200, 280]], np.int32)
    cv2.fillPoly(img, [pts], 255)
    
    # Edge detection
    canny = cv2.Canny(img, 100, 200)
    
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.uint8(np.abs(cv2.magnitude(sobel_x, sobel_y)))
    
    laplacian = np.uint8(np.abs(cv2.Laplacian(img, cv2.CV_64F)))
    
    # Comparison
    result = np.hstack([img, canny, sobel, laplacian])
    
    cv2.imwrite('/tmp/exercise_edges.jpg', result)
    print("✓ Exercise 3: Saved exercise_edges.jpg")

solution3()

# Solution 4
def solution4():
    # Create gradient
    gradient = np.zeros((200, 300), dtype=np.uint8)
    for i in range(300):
        gradient[:, i] = int(i * 255 / 300)
    
    # Thresholding
    _, binary = cv2.threshold(gradient, 127, 255, cv2.THRESH_BINARY)
    _, otsu = cv2.threshold(gradient, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    adapt_mean = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 11, 2)
    adapt_gauss = cv2.adaptiveThreshold(gradient, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)
    
    # Resize for comparison
    h, w = 100, 150
    images = [cv2.resize(x, (w, h)) for x in [gradient, binary, otsu, adapt_mean, adapt_gauss]]
    result = np.hstack(images)
    
    cv2.imwrite('/tmp/exercise_threshold.jpg', result)
    print("✓ Exercise 4: Saved exercise_threshold.jpg")

solution4()

# Solution 5
def solution5():
    # Create text image
    img = np.zeros((150, 300), dtype=np.uint8)
    cv2.putText(img, "MORPH", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, 3)
    
    kernel = np.ones((5, 5), np.uint8)
    
    # Operations
    erosion = cv2.erode(img, kernel, iterations=2)
    dilation = cv2.dilate(img, kernel, iterations=2)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    # Grid
    top = np.hstack([img, erosion, dilation])
    bottom = np.hstack([img, opening, closing])
    result = np.vstack([top, bottom])
    
    cv2.imwrite('/tmp/exercise_morph.jpg', result)
    print("✓ Exercise 5: Saved exercise_morph.jpg")

solution5()

print("\n✓ All exercises completed!")
print("Check /tmp/ directory for output images")
