# Day 43 Quick Reference Cheat Sheet

## Installation
```bash
pip install opencv-python numpy matplotlib
```

## Basic Operations
```python
import cv2
import numpy as np

# Read image
img = cv2.imread('image.jpg')           # Color (BGR)
img_gray = cv2.imread('image.jpg', 0)   # Grayscale

# Display image
cv2.imshow('Window Name', img)
cv2.waitKey(0)              # Wait for key press
cv2.destroyAllWindows()     # Close all windows

# Write image
cv2.imwrite('output.jpg', img)

# Get image properties
height, width, channels = img.shape
print(f"Size: {width}x{height}, Channels: {channels}")
```

## Image Resizing
```python
# Resize to specific dimensions
resized = cv2.resize(img, (width, height))

# Resize by scale factor
resized = cv2.resize(img, None, fx=0.5, fy=0.5)

# Different interpolation methods
resized = cv2.resize(img, (400, 300), interpolation=cv2.INTER_LINEAR)
# INTER_NEAREST - fastest
# INTER_LINEAR - default, good for enlarging
# INTER_AREA - best for shrinking
# INTER_CUBIC - slow but better quality
```

## Color Conversions
```python
# BGR to RGB (for matplotlib)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Grayscale to BGR
bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
```

## Image Transformations
```python
# Rotate image
center = (width // 2, height // 2)
matrix = cv2.getRotationMatrix2D(center, angle=45, scale=1.0)
rotated = cv2.warpAffine(img, matrix, (width, height))

# Flip image
flipped_h = cv2.flip(img, 1)   # Horizontal
flipped_v = cv2.flip(img, 0)   # Vertical
flipped_both = cv2.flip(img, -1)  # Both

# Crop image
cropped = img[y1:y2, x1:x2]

# Translation
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, M, (width, height))
```

## Image Filtering
```python
# Blur (smoothing)
blur = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)

# Sharpen
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel)

# Custom kernel
kernel = np.ones((5, 5), np.float32) / 25
filtered = cv2.filter2D(img, -1, kernel)
```

## Edge Detection
```python
# Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Sobel edges
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

# Laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
```

## Thresholding
```python
# Simple threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Adaptive threshold
adaptive = cv2.adaptiveThreshold(gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2)

# Otsu's threshold
_, otsu = cv2.threshold(gray, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

## Contours
```python
# Find contours
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Contour area and perimeter
area = cv2.contourArea(contour)
perimeter = cv2.arcLength(contour, True)

# Bounding rectangle
x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
```

## Drawing Operations
```python
# Line
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 2)

# Rectangle
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 2)

# Circle
cv2.circle(img, (100, 100), 50, (0, 0, 255), -1)

# Text
cv2.putText(img, 'Text', (x, y),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```

## Face Detection (Haar Cascade)
```python
# Load cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
```

## Video Capture
```python
# From webcam
cap = cv2.VideoCapture(0)

# From file
cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Video Writing
```python
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)

out.release()
```

## Morphological Operations
```python
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Opening (erosion followed by dilation)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing (dilation followed by erosion)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```

## Histogram
```python
# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Equalize histogram (improve contrast)
equ = cv2.equalizeHist(gray)

# CLAHE (Adaptive histogram equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(gray)
```

## Template Matching
```python
template = cv2.imread('template.jpg', 0)
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw rectangle at match location
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
```

## Common YOLO Usage Pattern
```python
# Note: This is a conceptual pattern for YOLO
# Actual implementation requires model weights

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Detect objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True)
net.setInput(blob)
outputs = net.forward(output_layers)
```

---
**Keep this handy for quick reference!** 🚀
