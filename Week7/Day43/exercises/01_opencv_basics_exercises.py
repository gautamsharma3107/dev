"""
Day 43 - OpenCV Basics Exercises
================================
Practice fundamental OpenCV operations
"""

import cv2
import numpy as np

# ============================================================
# EXERCISE 1: Create a Colorful Pattern
# ============================================================
print("Exercise 1: Create a Colorful Pattern")
print("-" * 40)

"""
Task: Create a 400x400 image with the following pattern:
- Top-left quadrant: Blue
- Top-right quadrant: Green
- Bottom-left quadrant: Red
- Bottom-right quadrant: Yellow

Save as 'colorful_pattern.jpg'
"""

# Your solution:
# img = np.zeros((400, 400, 3), dtype=np.uint8)
# ... complete the exercise




# ============================================================
# EXERCISE 2: Draw Shapes
# ============================================================
print("\nExercise 2: Draw Shapes")
print("-" * 40)

"""
Task: On a white 500x500 image:
1. Draw a blue circle at center with radius 100
2. Draw a green rectangle from (50,50) to (200,150)
3. Draw a red line from (0,0) to (500,500)
4. Add text "OpenCV Shapes" at position (150, 450)

Save as 'shapes.jpg'
"""

# Your solution:




# ============================================================
# EXERCISE 3: Color Space Exploration
# ============================================================
print("\nExercise 3: Color Space Exploration")
print("-" * 40)

"""
Task: Create a 300x300 image with a horizontal rainbow gradient
(approximate: red -> orange -> yellow -> green -> blue -> purple)

Hint: Use HSV color space where H (hue) varies from 0 to 180
"""

# Your solution:




# ============================================================
# EXERCISE 4: Image Manipulation
# ============================================================
print("\nExercise 4: Image Manipulation")
print("-" * 40)

"""
Task: Create an image and perform these operations:
1. Create a 200x200 blue square on black background
2. Copy the blue square to create a 2x2 grid
3. Result should be a 400x400 image with 4 blue squares

Save as 'blue_grid.jpg'
"""

# Your solution:




# ============================================================
# EXERCISE 5: Channel Manipulation
# ============================================================
print("\nExercise 5: Channel Manipulation")
print("-" * 40)

"""
Task: Create three 100x100 images:
1. An image showing only the blue channel (full blue, no green/red)
2. An image showing only the green channel
3. An image showing only the red channel

Stack them horizontally into a single image.
Save as 'rgb_channels.jpg'
"""

# Your solution:




# ============================================================
# SOLUTIONS
# ============================================================
print("\n" + "=" * 60)
print("SOLUTIONS (scroll down after attempting)")
print("=" * 60)

# Solution 1
img1 = np.zeros((400, 400, 3), dtype=np.uint8)
img1[0:200, 0:200] = (255, 0, 0)      # Top-left: Blue
img1[0:200, 200:400] = (0, 255, 0)    # Top-right: Green
img1[200:400, 0:200] = (0, 0, 255)    # Bottom-left: Red
img1[200:400, 200:400] = (0, 255, 255) # Bottom-right: Yellow
cv2.imwrite('/tmp/colorful_pattern.jpg', img1)
print("\n✓ Exercise 1: Saved colorful_pattern.jpg")

# Solution 2
img2 = np.ones((500, 500, 3), dtype=np.uint8) * 255
cv2.circle(img2, (250, 250), 100, (255, 0, 0), -1)
cv2.rectangle(img2, (50, 50), (200, 150), (0, 255, 0), -1)
cv2.line(img2, (0, 0), (500, 500), (0, 0, 255), 2)
cv2.putText(img2, "OpenCV Shapes", (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.imwrite('/tmp/shapes.jpg', img2)
print("✓ Exercise 2: Saved shapes.jpg")

# Solution 3
img3 = np.zeros((300, 300, 3), dtype=np.uint8)
for i in range(300):
    hue = int(i * 180 / 300)  # 0 to 180
    img3[:, i] = [hue, 255, 255]  # HSV
img3 = cv2.cvtColor(img3, cv2.COLOR_HSV2BGR)
cv2.imwrite('/tmp/rainbow.jpg', img3)
print("✓ Exercise 3: Saved rainbow.jpg")

# Solution 4
square = np.zeros((200, 200, 3), dtype=np.uint8)
square[:, :] = (255, 0, 0)  # Blue
img4 = np.zeros((400, 400, 3), dtype=np.uint8)
img4[0:200, 0:200] = square
img4[0:200, 200:400] = square
img4[200:400, 0:200] = square
img4[200:400, 200:400] = square
cv2.imwrite('/tmp/blue_grid.jpg', img4)
print("✓ Exercise 4: Saved blue_grid.jpg")

# Solution 5
blue_only = np.zeros((100, 100, 3), dtype=np.uint8)
blue_only[:, :, 0] = 255

green_only = np.zeros((100, 100, 3), dtype=np.uint8)
green_only[:, :, 1] = 255

red_only = np.zeros((100, 100, 3), dtype=np.uint8)
red_only[:, :, 2] = 255

img5 = np.hstack([blue_only, green_only, red_only])
cv2.imwrite('/tmp/rgb_channels.jpg', img5)
print("✓ Exercise 5: Saved rgb_channels.jpg")

print("\n✓ All exercises completed!")
print("Check /tmp/ directory for output images")
