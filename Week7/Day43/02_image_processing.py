"""
Day 43 - Image Processing Techniques
=====================================
Learn: Resize, rotate, filters, edge detection, thresholding

Key Concepts:
- Image transformations (resize, rotate, flip)
- Filtering and smoothing
- Edge detection (Canny, Sobel)
- Thresholding techniques
- Morphological operations
"""

import cv2
import numpy as np

# ========== RESIZING IMAGES ==========
print("=" * 60)
print("RESIZING IMAGES")
print("=" * 60)

# Create a sample image
original = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.rectangle(original, (100, 100), (500, 300), (0, 255, 0), -1)
cv2.circle(original, (300, 200), 80, (255, 0, 0), -1)

print(f"Original size: {original.shape}")

# Resize to specific dimensions
resized_specific = cv2.resize(original, (300, 200))
print(f"Resized to 300x200: {resized_specific.shape}")

# Resize by scale factor
resized_half = cv2.resize(original, None, fx=0.5, fy=0.5)
print(f"Resized to 50%: {resized_half.shape}")

resized_double = cv2.resize(original, None, fx=2, fy=2)
print(f"Resized to 200%: {resized_double.shape}")

# Different interpolation methods
print("\nInterpolation methods:")
methods = [
    (cv2.INTER_NEAREST, "INTER_NEAREST - Fastest, pixelated"),
    (cv2.INTER_LINEAR, "INTER_LINEAR - Default, good balance"),
    (cv2.INTER_AREA, "INTER_AREA - Best for shrinking"),
    (cv2.INTER_CUBIC, "INTER_CUBIC - Better quality, slower"),
    (cv2.INTER_LANCZOS4, "INTER_LANCZOS4 - Highest quality, slowest"),
]

for method, description in methods:
    resized = cv2.resize(original, (300, 200), interpolation=method)
    print(f"  {description}")

# ========== ROTATING IMAGES ==========
print("\n" + "=" * 60)
print("ROTATING IMAGES")
print("=" * 60)

# Create a sample image with text for rotation demo
img_to_rotate = np.ones((300, 400, 3), dtype=np.uint8) * 200
cv2.putText(img_to_rotate, 'ROTATE ME', (80, 160), 
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

height, width = img_to_rotate.shape[:2]
center = (width // 2, height // 2)

# Rotate using rotation matrix
angle = 45  # degrees
scale = 1.0  # no scaling

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_45 = cv2.warpAffine(img_to_rotate, rotation_matrix, (width, height))
print(f"Rotated 45 degrees")

# Rotate with border handling
rotated_border = cv2.warpAffine(
    img_to_rotate, rotation_matrix, (width, height),
    borderMode=cv2.BORDER_CONSTANT,
    borderValue=(255, 255, 255)  # White border
)
print("Rotated with white border")

# Simple rotations (90, 180, 270 degrees)
rotated_90_cw = cv2.rotate(img_to_rotate, cv2.ROTATE_90_CLOCKWISE)
rotated_90_ccw = cv2.rotate(img_to_rotate, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_180 = cv2.rotate(img_to_rotate, cv2.ROTATE_180)

print("Simple rotations: 90° CW, 90° CCW, 180°")

# ========== FLIPPING IMAGES ==========
print("\n" + "=" * 60)
print("FLIPPING IMAGES")
print("=" * 60)

# Flip horizontally (mirror)
flipped_h = cv2.flip(img_to_rotate, 1)
print("Flipped horizontally (flipCode=1)")

# Flip vertically
flipped_v = cv2.flip(img_to_rotate, 0)
print("Flipped vertically (flipCode=0)")

# Flip both
flipped_both = cv2.flip(img_to_rotate, -1)
print("Flipped both ways (flipCode=-1)")

# ========== IMAGE FILTERING (SMOOTHING) ==========
print("\n" + "=" * 60)
print("IMAGE FILTERING (SMOOTHING)")
print("=" * 60)

# Create a noisy image
noise_img = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)

# Average blur
blur_avg = cv2.blur(noise_img, (5, 5))
print("Applied average blur (5x5 kernel)")

# Gaussian blur - most commonly used
blur_gaussian = cv2.GaussianBlur(noise_img, (5, 5), 0)
print("Applied Gaussian blur (5x5 kernel)")

# Median blur - great for salt & pepper noise
blur_median = cv2.medianBlur(noise_img, 5)
print("Applied median blur (kernel size 5)")

# Bilateral filter - preserves edges while smoothing
blur_bilateral = cv2.bilateralFilter(noise_img, 9, 75, 75)
print("Applied bilateral filter (edge-preserving)")

# Compare kernel sizes
print("\nDifferent kernel sizes:")
for k in [3, 5, 7, 11, 15]:
    blurred = cv2.GaussianBlur(noise_img, (k, k), 0)
    print(f"  Kernel {k}x{k}: More blur, slower")

# ========== SHARPENING ==========
print("\n" + "=" * 60)
print("SHARPENING")
print("=" * 60)

# Create a sample image
sharp_demo = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.putText(sharp_demo, 'SHARP', (50, 170), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (200, 200, 200), 3)

# Sharpen using kernel
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(sharp_demo, -1, sharpen_kernel)
print("Applied sharpening kernel")

# Another sharpening kernel (stronger)
sharpen_strong = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])
sharpened_strong = cv2.filter2D(sharp_demo, -1, sharpen_strong)
print("Applied stronger sharpening kernel")

# ========== EDGE DETECTION ==========
print("\n" + "=" * 60)
print("EDGE DETECTION")
print("=" * 60)

# Create a sample image with shapes
edge_demo = np.zeros((300, 400), dtype=np.uint8)
cv2.rectangle(edge_demo, (50, 50), (150, 150), 255, -1)
cv2.circle(edge_demo, (250, 100), 60, 255, -1)
cv2.rectangle(edge_demo, (200, 180), (350, 280), 200, -1)

# Canny edge detection - most popular
edges_canny = cv2.Canny(edge_demo, 100, 200)
print("Canny edge detection:")
print("  - threshold1 (100): Lower threshold for edge linking")
print("  - threshold2 (200): Upper threshold for strong edges")

# Sobel edge detection
sobel_x = cv2.Sobel(edge_demo, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(edge_demo, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
print("\nSobel edge detection:")
print("  - sobel_x: Detects vertical edges")
print("  - sobel_y: Detects horizontal edges")

# Laplacian edge detection
laplacian = cv2.Laplacian(edge_demo, cv2.CV_64F)
print("\nLaplacian edge detection: Detects all edges")

# Save edge detection results
cv2.imwrite('/tmp/edges_canny.jpg', edges_canny)
cv2.imwrite('/tmp/edges_sobel.jpg', np.uint8(np.abs(sobel_combined)))
print("\nSaved edge detection results to /tmp/")

# ========== THRESHOLDING ==========
print("\n" + "=" * 60)
print("THRESHOLDING")
print("=" * 60)

# Create a gradient image for thresholding demo
gradient = np.zeros((200, 300), dtype=np.uint8)
for i in range(300):
    gradient[:, i] = int(i * 255 / 300)

# Simple (global) thresholding
_, thresh_binary = cv2.threshold(gradient, 127, 255, cv2.THRESH_BINARY)
_, thresh_binary_inv = cv2.threshold(gradient, 127, 255, cv2.THRESH_BINARY_INV)
_, thresh_trunc = cv2.threshold(gradient, 127, 255, cv2.THRESH_TRUNC)
_, thresh_tozero = cv2.threshold(gradient, 127, 255, cv2.THRESH_TOZERO)
_, thresh_tozero_inv = cv2.threshold(gradient, 127, 255, cv2.THRESH_TOZERO_INV)

print("Thresholding types:")
print("  THRESH_BINARY: pixel > thresh ? max : 0")
print("  THRESH_BINARY_INV: pixel > thresh ? 0 : max")
print("  THRESH_TRUNC: pixel > thresh ? thresh : pixel")
print("  THRESH_TOZERO: pixel > thresh ? pixel : 0")
print("  THRESH_TOZERO_INV: pixel > thresh ? 0 : pixel")

# Otsu's thresholding - automatic threshold selection
_, thresh_otsu = cv2.threshold(gradient, 0, 255, 
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("\nOtsu's method: Automatically finds optimal threshold")

# Adaptive thresholding - for varying lighting
# Create an image with varying brightness
varying = np.zeros((200, 300), dtype=np.uint8)
varying[:, :150] = gradient[:, :150] // 2  # Darker left half
varying[:, 150:] = gradient[:, 150:]

adaptive_mean = cv2.adaptiveThreshold(
    varying, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_gaussian = cv2.adaptiveThreshold(
    varying, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

print("\nAdaptive thresholding:")
print("  ADAPTIVE_THRESH_MEAN_C: Uses mean of neighborhood")
print("  ADAPTIVE_THRESH_GAUSSIAN_C: Uses Gaussian-weighted sum")

# ========== MORPHOLOGICAL OPERATIONS ==========
print("\n" + "=" * 60)
print("MORPHOLOGICAL OPERATIONS")
print("=" * 60)

# Create an image with noise
morph_demo = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(morph_demo, (50, 50), (150, 150), 255, -1)
# Add some noise
noise_points = np.random.randint(0, 200, (20, 2))
for pt in noise_points:
    morph_demo[pt[0], pt[1]] = 255

# Create structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Erosion - shrinks white regions
erosion = cv2.erode(morph_demo, kernel, iterations=1)
print("Erosion: Shrinks white regions, removes small noise")

# Dilation - expands white regions
dilation = cv2.dilate(morph_demo, kernel, iterations=1)
print("Dilation: Expands white regions, fills small holes")

# Opening - erosion followed by dilation
# Good for removing small bright spots (noise)
opening = cv2.morphologyEx(morph_demo, cv2.MORPH_OPEN, kernel)
print("Opening: Removes small bright spots")

# Closing - dilation followed by erosion
# Good for filling small dark holes
closing = cv2.morphologyEx(morph_demo, cv2.MORPH_CLOSE, kernel)
print("Closing: Fills small dark holes")

# Morphological gradient - difference between dilation and erosion
gradient_morph = cv2.morphologyEx(morph_demo, cv2.MORPH_GRADIENT, kernel)
print("Gradient: Shows edges (dilation - erosion)")

# Top hat - difference between input and opening
tophat = cv2.morphologyEx(morph_demo, cv2.MORPH_TOPHAT, kernel)
print("Top Hat: Shows small bright spots")

# Black hat - difference between closing and input
blackhat = cv2.morphologyEx(morph_demo, cv2.MORPH_BLACKHAT, kernel)
print("Black Hat: Shows small dark holes")

# Different kernel shapes
print("\nStructuring element shapes:")
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

print("  MORPH_RECT: Rectangular")
print("  MORPH_ELLIPSE: Elliptical")
print("  MORPH_CROSS: Cross-shaped")

# ========== CONTOURS ==========
print("\n" + "=" * 60)
print("CONTOURS")
print("=" * 60)

# Create an image with shapes
contour_demo = np.zeros((300, 400), dtype=np.uint8)
cv2.rectangle(contour_demo, (50, 50), (150, 150), 255, -1)
cv2.circle(contour_demo, (250, 100), 60, 255, -1)
cv2.ellipse(contour_demo, (300, 220), (60, 30), 0, 0, 360, 255, -1)

# Find contours
contours, hierarchy = cv2.findContours(
    contour_demo, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f"Found {len(contours)} contours")

# Draw contours on color image
contour_output = cv2.cvtColor(contour_demo, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_output, contours, -1, (0, 255, 0), 2)

# Analyze each contour
print("\nContour analysis:")
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    x, y, w, h = cv2.boundingRect(contour)
    
    print(f"\nContour {i + 1}:")
    print(f"  Area: {area:.0f} pixels")
    print(f"  Perimeter: {perimeter:.2f} pixels")
    print(f"  Bounding box: ({x}, {y}), {w}x{h}")

# Save contour result
cv2.imwrite('/tmp/contours.jpg', contour_output)
print("\nSaved contour visualization to /tmp/contours.jpg")

# ========== HISTOGRAM OPERATIONS ==========
print("\n" + "=" * 60)
print("HISTOGRAM OPERATIONS")
print("=" * 60)

# Create an image with varying brightness
hist_demo = np.zeros((200, 300), dtype=np.uint8)
hist_demo[:100, :] = 50   # Dark top
hist_demo[100:, :] = 200  # Bright bottom

# Calculate histogram
hist = cv2.calcHist([hist_demo], [0], None, [256], [0, 256])
print(f"Histogram shape: {hist.shape}")

# Histogram equalization - improve contrast
equalized = cv2.equalizeHist(hist_demo)
print("Applied histogram equalization")

# CLAHE - Contrast Limited Adaptive Histogram Equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_result = clahe.apply(hist_demo)
print("Applied CLAHE (adaptive histogram equalization)")

# ========== PRACTICAL EXAMPLE ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: IMAGE ENHANCEMENT PIPELINE")
print("=" * 60)

# Create a simulated "dirty" image
dirty_img = np.random.randint(100, 150, (300, 400), dtype=np.uint8)
cv2.rectangle(dirty_img, (100, 80), (300, 220), 180, -1)
cv2.putText(dirty_img, 'TEXT', (130, 170), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, 50, 3)

# Add noise
noise = np.random.randint(-30, 30, dirty_img.shape, dtype=np.int16)
dirty_img = np.clip(dirty_img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

print("Enhancement pipeline:")

# Step 1: Denoise
step1 = cv2.GaussianBlur(dirty_img, (3, 3), 0)
print("  1. Applied Gaussian blur to reduce noise")

# Step 2: Enhance contrast
step2 = cv2.equalizeHist(step1)
print("  2. Applied histogram equalization")

# Step 3: Sharpen
sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
step3 = cv2.filter2D(step2, -1, sharpen)
print("  3. Applied sharpening filter")

# Step 4: Threshold for clear text
_, step4 = cv2.threshold(step3, 127, 255, cv2.THRESH_BINARY)
print("  4. Applied binary threshold")

# Save results
cv2.imwrite('/tmp/enhancement_original.jpg', dirty_img)
cv2.imwrite('/tmp/enhancement_final.jpg', step4)
print("\nSaved enhancement results to /tmp/")

print("\n" + "=" * 60)
print("✅ Image Processing Techniques - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Resize: cv2.resize() with different interpolation methods
2. Rotate: cv2.getRotationMatrix2D() + cv2.warpAffine()
3. Flip: cv2.flip() with flipCode (0, 1, -1)
4. Blur: Gaussian, median, bilateral filters
5. Edge detection: Canny, Sobel, Laplacian
6. Thresholding: Global, Otsu's, Adaptive
7. Morphology: Erosion, dilation, opening, closing
8. Contours: Find, draw, analyze shapes
9. Histogram: Calculate, equalize, CLAHE
""")
