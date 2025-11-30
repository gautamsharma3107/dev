"""
Day 43 - OpenCV Basics
======================
Learn: Installation, reading/writing images, basic operations

Key Concepts:
- OpenCV is the most popular computer vision library
- Images are represented as NumPy arrays
- OpenCV uses BGR color format (not RGB!)
- Basic operations: read, write, display, resize
"""

import cv2
import numpy as np

# ========== INSTALLATION CHECK ==========
print("=" * 60)
print("OPENCV INSTALLATION CHECK")
print("=" * 60)

print(f"OpenCV Version: {cv2.__version__}")
print(f"NumPy Version: {np.__version__}")

# ========== CREATING IMAGES FROM SCRATCH ==========
print("\n" + "=" * 60)
print("CREATING IMAGES FROM SCRATCH")
print("=" * 60)

# Create a black image (all zeros)
black_img = np.zeros((300, 400, 3), dtype=np.uint8)
print(f"Black image shape: {black_img.shape}")
print(f"Black image dtype: {black_img.dtype}")

# Create a white image (all 255)
white_img = np.ones((300, 400, 3), dtype=np.uint8) * 255
print(f"White image shape: {white_img.shape}")

# Create a colored image (BGR format!)
# Blue image
blue_img = np.zeros((300, 400, 3), dtype=np.uint8)
blue_img[:] = (255, 0, 0)  # BGR: Blue=255, Green=0, Red=0

# Green image
green_img = np.zeros((300, 400, 3), dtype=np.uint8)
green_img[:] = (0, 255, 0)  # BGR: Blue=0, Green=255, Red=0

# Red image
red_img = np.zeros((300, 400, 3), dtype=np.uint8)
red_img[:] = (0, 0, 255)  # BGR: Blue=0, Green=0, Red=255

print("\nCreated blue, green, and red images")
print("Remember: OpenCV uses BGR, not RGB!")

# ========== IMAGE PROPERTIES ==========
print("\n" + "=" * 60)
print("IMAGE PROPERTIES")
print("=" * 60)

# Create a sample image
sample_img = np.zeros((480, 640, 3), dtype=np.uint8)

# Get shape (height, width, channels)
height, width, channels = sample_img.shape
print(f"Height: {height}")
print(f"Width: {width}")
print(f"Channels: {channels}")

# Get size (total number of pixels * channels)
size = sample_img.size
print(f"Total size: {size}")

# Get data type
dtype = sample_img.dtype
print(f"Data type: {dtype}")

# ========== READING IMAGES (DEMONSTRATION) ==========
print("\n" + "=" * 60)
print("READING IMAGES (DEMONSTRATION)")
print("=" * 60)

print("""
# To read an image from file:
img = cv2.imread('path/to/image.jpg')

# Read as grayscale:
gray_img = cv2.imread('path/to/image.jpg', cv2.IMREAD_GRAYSCALE)
# or
gray_img = cv2.imread('path/to/image.jpg', 0)

# Read with alpha channel (transparency):
img_alpha = cv2.imread('path/to/image.png', cv2.IMREAD_UNCHANGED)

# Check if image loaded successfully:
if img is None:
    print("Error: Could not load image")
""")

# ========== WRITING IMAGES ==========
print("\n" + "=" * 60)
print("WRITING IMAGES")
print("=" * 60)

# Save the created images
cv2.imwrite('/tmp/blue_image.jpg', blue_img)
cv2.imwrite('/tmp/green_image.png', green_img)
cv2.imwrite('/tmp/red_image.bmp', red_img)

print("Saved images:")
print("  - /tmp/blue_image.jpg")
print("  - /tmp/green_image.png")
print("  - /tmp/red_image.bmp")

# ========== DISPLAYING IMAGES ==========
print("\n" + "=" * 60)
print("DISPLAYING IMAGES (DEMONSTRATION)")
print("=" * 60)

print("""
# Display image in a window:
cv2.imshow('Window Name', img)
cv2.waitKey(0)  # Wait indefinitely for key press
cv2.destroyAllWindows()

# Wait for specific time (in milliseconds):
cv2.waitKey(5000)  # Wait 5 seconds

# Display multiple images:
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Note: cv2.imshow() may not work in some environments
# (e.g., headless servers, Jupyter notebooks)
# Use matplotlib instead:

import matplotlib.pyplot as plt

# Convert BGR to RGB for matplotlib
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.title('My Image')
plt.axis('off')
plt.show()
""")

# ========== COLOR SPACE CONVERSIONS ==========
print("\n" + "=" * 60)
print("COLOR SPACE CONVERSIONS")
print("=" * 60)

# Create a sample color image
color_img = np.zeros((100, 100, 3), dtype=np.uint8)
color_img[:50, :50] = (255, 0, 0)   # Blue square
color_img[:50, 50:] = (0, 255, 0)   # Green square
color_img[50:, :50] = (0, 0, 255)   # Red square
color_img[50:, 50:] = (255, 255, 0) # Cyan square

# BGR to RGB
rgb_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
print("Converted BGR to RGB")

# BGR to Grayscale
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
print(f"Grayscale shape: {gray_img.shape} (no channel dimension)")

# BGR to HSV (Hue, Saturation, Value)
hsv_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
print("Converted BGR to HSV")

# List available color conversions
print("\nCommon color conversions:")
conversions = [
    "COLOR_BGR2RGB", "COLOR_RGB2BGR",
    "COLOR_BGR2GRAY", "COLOR_GRAY2BGR",
    "COLOR_BGR2HSV", "COLOR_HSV2BGR",
    "COLOR_BGR2LAB", "COLOR_LAB2BGR",
]
for conv in conversions:
    print(f"  cv2.{conv}")

# ========== BASIC IMAGE MANIPULATIONS ==========
print("\n" + "=" * 60)
print("BASIC IMAGE MANIPULATIONS")
print("=" * 60)

# Create a test image
img = np.zeros((200, 300, 3), dtype=np.uint8)
img[50:150, 100:200] = (0, 255, 255)  # Yellow rectangle

# Accessing pixel values
pixel = img[100, 150]  # Get pixel at (row=100, col=150)
print(f"Pixel at (100, 150): {pixel}")

# Modify pixel
img[100, 150] = (255, 255, 255)  # Set to white
print("Modified pixel at (100, 150) to white")

# Access region of interest (ROI)
roi = img[50:100, 100:150]  # Get top-left quarter of yellow rect
print(f"ROI shape: {roi.shape}")

# Copy ROI to another location
img[150:200, 200:250] = roi
print("Copied ROI to new location")

# ========== SPLITTING AND MERGING CHANNELS ==========
print("\n" + "=" * 60)
print("SPLITTING AND MERGING CHANNELS")
print("=" * 60)

# Create a colorful image
colorful = np.zeros((100, 100, 3), dtype=np.uint8)
colorful[:, :, 0] = np.linspace(0, 255, 100, dtype=np.uint8)  # Blue gradient
colorful[:, :, 1] = 128  # Constant green
colorful[:, :, 2] = np.linspace(255, 0, 100, dtype=np.uint8)  # Red gradient (reverse)

# Split into channels
b, g, r = cv2.split(colorful)
print(f"Blue channel shape: {b.shape}")
print(f"Green channel shape: {g.shape}")
print(f"Red channel shape: {r.shape}")

# Merge channels back
merged = cv2.merge([b, g, r])
print(f"Merged image shape: {merged.shape}")

# Swap channels (make BGR -> RGB without cvtColor)
swapped = cv2.merge([r, g, b])
print("Swapped channels (BGR to RGB)")

# ========== ARITHMETIC OPERATIONS ==========
print("\n" + "=" * 60)
print("ARITHMETIC OPERATIONS")
print("=" * 60)

# Create two images
img1 = np.ones((100, 100, 3), dtype=np.uint8) * 100
img2 = np.ones((100, 100, 3), dtype=np.uint8) * 150

# Add images
added = cv2.add(img1, img2)
print(f"Added: min={added.min()}, max={added.max()}")
# Note: cv2.add saturates at 255

# NumPy addition (wraps around at 256)
np_added = img1 + img2
print(f"NumPy add: min={np_added.min()}, max={np_added.max()}")

# Subtract images
subtracted = cv2.subtract(img2, img1)
print(f"Subtracted: {subtracted[0, 0]}")

# Weighted addition (blending)
alpha = 0.7
beta = 0.3
gamma = 0  # Scalar added to each sum
blended = cv2.addWeighted(img1, alpha, img2, beta, gamma)
print("Blended two images with weights 0.7 and 0.3")

# ========== BITWISE OPERATIONS ==========
print("\n" + "=" * 60)
print("BITWISE OPERATIONS")
print("=" * 60)

# Create shapes for bitwise operations
rect = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(rect, (30, 30), (170, 170), 255, -1)

circle = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(circle, (100, 100), 80, 255, -1)

# Bitwise operations
and_result = cv2.bitwise_and(rect, circle)
or_result = cv2.bitwise_or(rect, circle)
xor_result = cv2.bitwise_xor(rect, circle)
not_result = cv2.bitwise_not(rect)

print("Performed bitwise AND, OR, XOR, NOT operations")
print("Use bitwise operations for masking and combining shapes")

# Save results
cv2.imwrite('/tmp/bitwise_and.jpg', and_result)
cv2.imwrite('/tmp/bitwise_or.jpg', or_result)
cv2.imwrite('/tmp/bitwise_xor.jpg', xor_result)
print("Saved bitwise operation results to /tmp/")

# ========== PRACTICAL EXAMPLE: CREATE A LOGO ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: CREATE A SIMPLE LOGO")
print("=" * 60)

# Create a blank image
logo = np.zeros((200, 400, 3), dtype=np.uint8)

# Draw background
logo[:] = (50, 50, 50)  # Dark gray

# Draw a circle
cv2.circle(logo, (100, 100), 60, (0, 165, 255), -1)  # Orange circle

# Draw text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(logo, 'OpenCV', (180, 110), font, 1.5, (255, 255, 255), 2)

# Draw a line
cv2.line(logo, (180, 130), (380, 130), (0, 165, 255), 2)

# Save the logo
cv2.imwrite('/tmp/opencv_logo.jpg', logo)
print("Created and saved logo to /tmp/opencv_logo.jpg")

print("\n" + "=" * 60)
print("✅ OpenCV Basics - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. OpenCV uses BGR color format (not RGB!)
2. Images are NumPy arrays with shape (height, width, channels)
3. Use cv2.imread() to read, cv2.imwrite() to save
4. cv2.cvtColor() for color space conversions
5. Arithmetic operations: add, subtract, addWeighted
6. Bitwise operations: and, or, xor, not
7. Always check if image loaded successfully (is not None)
""")
