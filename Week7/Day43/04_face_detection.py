"""
Day 43 - Face Detection Basics
===============================
Learn: Haar cascades, face detection, eye detection

Key Concepts:
- Haar cascade classifiers
- Pre-trained face detection models
- Real-time face detection
- Face and eye detection combined
- Alternative: DNN-based face detection
"""

import cv2
import numpy as np

# ========== HAAR CASCADE CLASSIFIERS ==========
print("=" * 60)
print("HAAR CASCADE CLASSIFIERS")
print("=" * 60)

print("""
What are Haar Cascades?
----------------------
Haar cascades are machine learning-based classifiers trained
to detect objects (like faces) using Haar-like features.

How they work:
1. Extract Haar features (edge, line, center features)
2. Use AdaBoost to select important features
3. Cascade classifiers for fast rejection
4. Sliding window approach

Pre-trained Cascades in OpenCV:
------------------------------
OpenCV comes with pre-trained cascades for:
- Frontal face detection
- Profile face detection
- Eye detection
- Smile detection
- Full body detection
- Upper body detection
- And more...

Location:
cv2.data.haarcascades + 'cascade_filename.xml'
""")

# List available cascades
print("\nAvailable Haar Cascades:")
cascades = [
    "haarcascade_frontalface_default.xml",
    "haarcascade_frontalface_alt.xml",
    "haarcascade_frontalface_alt2.xml",
    "haarcascade_profileface.xml",
    "haarcascade_eye.xml",
    "haarcascade_eye_tree_eyeglasses.xml",
    "haarcascade_smile.xml",
    "haarcascade_fullbody.xml",
    "haarcascade_upperbody.xml",
]
for cascade in cascades:
    print(f"  - {cascade}")

# ========== LOADING HAAR CASCADES ==========
print("\n" + "=" * 60)
print("LOADING HAAR CASCADES")
print("=" * 60)

# Load face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load eye cascade
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

# Check if loaded successfully
if face_cascade.empty():
    print("Error: Could not load face cascade!")
else:
    print("✓ Face cascade loaded successfully")

if eye_cascade.empty():
    print("Error: Could not load eye cascade!")
else:
    print("✓ Eye cascade loaded successfully")

# ========== BASIC FACE DETECTION ==========
print("\n" + "=" * 60)
print("BASIC FACE DETECTION")
print("=" * 60)

# Create a synthetic "face-like" image for demo
# In practice, use real images
demo_image = np.ones((400, 400, 3), dtype=np.uint8) * 200

# Draw face-like shape (won't be detected, just for demo)
cv2.ellipse(demo_image, (200, 200), (80, 100), 0, 0, 360, (150, 130, 120), -1)
cv2.circle(demo_image, (170, 180), 15, (255, 255, 255), -1)  # Left eye
cv2.circle(demo_image, (230, 180), 15, (255, 255, 255), -1)  # Right eye
cv2.circle(demo_image, (170, 180), 8, (50, 50, 50), -1)  # Left pupil
cv2.circle(demo_image, (230, 180), 8, (50, 50, 50), -1)  # Right pupil
cv2.ellipse(demo_image, (200, 250), (30, 15), 0, 0, 180, (150, 100, 100), -1)  # Mouth

cv2.imwrite('/tmp/demo_face.jpg', demo_image)
print("Created demo image at /tmp/demo_face.jpg")

print("""
Face Detection Code Pattern:
---------------------------
# Load cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read image
img = cv2.imread('photo.jpg')

# Convert to grayscale (required for Haar cascades)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,    # Image pyramid scale
    minNeighbors=5,     # Min neighbors to confirm detection
    minSize=(30, 30)    # Min face size
)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

print(f"Found {len(faces)} faces")
""")

# ========== DETECTION PARAMETERS ==========
print("\n" + "=" * 60)
print("UNDERSTANDING detectMultiScale PARAMETERS")
print("=" * 60)

print("""
detectMultiScale Parameters:
---------------------------

1. scaleFactor (default: 1.1)
   - How much to reduce image size at each scale
   - Smaller = more accurate but slower
   - Values: 1.01 to 1.4
   - Typical: 1.1 to 1.3

2. minNeighbors (default: 3)
   - Min number of neighbors to keep a detection
   - Higher = fewer false positives, may miss faces
   - Lower = more detections, more false positives
   - Typical: 3 to 6

3. minSize (default: varies)
   - Minimum object size to detect
   - Tuple: (width, height)
   - Example: (30, 30) for faces

4. maxSize (default: varies)
   - Maximum object size to detect
   - Tuple: (width, height)
   
5. flags (deprecated in newer versions)
   - Used to be for optimization
   - cv2.CASCADE_SCALE_IMAGE (default)
""")

# Demonstrate parameter effects
print("\nParameter Comparison (conceptual):")
print("-" * 40)

params = [
    {"scaleFactor": 1.1, "minNeighbors": 3, "desc": "Fast, more false positives"},
    {"scaleFactor": 1.1, "minNeighbors": 5, "desc": "Balanced"},
    {"scaleFactor": 1.1, "minNeighbors": 8, "desc": "Strict, may miss faces"},
    {"scaleFactor": 1.05, "minNeighbors": 5, "desc": "Accurate but slow"},
    {"scaleFactor": 1.3, "minNeighbors": 5, "desc": "Fast but less accurate"},
]

for p in params:
    print(f"scaleFactor={p['scaleFactor']}, minNeighbors={p['minNeighbors']}")
    print(f"  → {p['desc']}")

# ========== FACE AND EYE DETECTION ==========
print("\n" + "=" * 60)
print("FACE AND EYE DETECTION COMBINED")
print("=" * 60)

def detect_faces_and_eyes(image):
    """
    Detect faces and eyes in an image.
    
    Returns:
        image with drawn rectangles
    """
    # Make a copy
    output = image.copy()
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw face rectangle (green)
        cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Region of Interest for eyes (within face)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = output[y:y+h, x:x+w]
        
        # Detect eyes within face region
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        
        for (ex, ey, ew, eh) in eyes:
            # Draw eye rectangle (blue)
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
    
    return output, len(faces)

print("""
Face + Eye Detection Pattern:
----------------------------
1. Detect faces in full image
2. For each face:
   a. Extract Region of Interest (ROI)
   b. Detect eyes only within face ROI
   c. Draw rectangles
   
This is more efficient and accurate than searching
the entire image for eyes.
""")

# Create and save example
result_img, num_faces = detect_faces_and_eyes(demo_image)
cv2.imwrite('/tmp/face_eye_detection.jpg', result_img)
print(f"\nSaved face/eye detection demo to /tmp/face_eye_detection.jpg")

# ========== REAL-TIME FACE DETECTION ==========
print("\n" + "=" * 60)
print("REAL-TIME FACE DETECTION (WEBCAM)")
print("=" * 60)

real_time_code = '''
# Real-time Face Detection with Webcam
# =====================================

import cv2

# Load cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

# Set resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Draw rectangles and info
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Face', (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Show FPS
    cv2.putText(frame, f'Faces: {len(faces)}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    # Display
    cv2.imshow('Face Detection', frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
'''

print(real_time_code)

# ========== DNN-BASED FACE DETECTION ==========
print("\n" + "=" * 60)
print("DNN-BASED FACE DETECTION (MORE ACCURATE)")
print("=" * 60)

print("""
Why DNN over Haar Cascades?
--------------------------
- More accurate, especially for different angles
- Better with occlusions
- More robust to lighting changes
- Can detect faces Haar cascades miss

Pre-trained DNN Models:
----------------------
1. Caffe model (deploy.prototxt + model.caffemodel)
2. TensorFlow model (model.pb)
3. OpenCV's own model (res10_300x300_ssd_iter_140000.caffemodel)

OpenCV's DNN Face Detector:
--------------------------
- Based on SSD (Single Shot Detector) with ResNet backbone
- Trained on WIDER FACE dataset
- Works well on various face sizes and angles
""")

dnn_face_code = '''
# DNN-based Face Detection
# ========================

import cv2
import numpy as np

# Download these files:
# - deploy.prototxt from OpenCV face detection model
# - res10_300x300_ssd_iter_140000.caffemodel

# Load model
model_file = "res10_300x300_ssd_iter_140000.caffemodel"
config_file = "deploy.prototxt"
net = cv2.dnn.readNetFromCaffe(config_file, model_file)

def detect_faces_dnn(image, confidence_threshold=0.5):
    """
    Detect faces using DNN model.
    
    Args:
        image: Input image
        confidence_threshold: Min confidence to accept detection
    
    Returns:
        List of (x, y, w, h, confidence) tuples
    """
    h, w = image.shape[:2]
    
    # Create blob from image
    blob = cv2.dnn.blobFromImage(
        image, 
        scalefactor=1.0,
        size=(300, 300),
        mean=(104.0, 177.0, 123.0),  # Mean subtraction values
        swapRB=False,
        crop=False
    )
    
    # Set input and forward pass
    net.setInput(blob)
    detections = net.forward()
    
    faces = []
    
    # Process detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        if confidence > confidence_threshold:
            # Get bounding box coordinates
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            x1, y1, x2, y2 = box.astype(int)
            
            faces.append((x1, y1, x2-x1, y2-y1, confidence))
    
    return faces

# Usage
image = cv2.imread('photo.jpg')
faces = detect_faces_dnn(image)

for (x, y, w, h, conf) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(image, f'{conf:.2f}', (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
'''

print(dnn_face_code)

# ========== SMILE DETECTION ==========
print("\n" + "=" * 60)
print("SMILE DETECTION")
print("=" * 60)

# Load smile cascade
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml')

smile_code = '''
# Smile Detection (within detected face)
# ======================================

# Load cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml')

def detect_smiles(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw face rectangle
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # ROI for smile (lower half of face)
        roi_gray = gray[y+int(h/2):y+h, x:x+w]
        roi_color = image[y+int(h/2):y+h, x:x+w]
        
        # Detect smiles with stricter parameters
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.8,
            minNeighbors=20,
            minSize=(25, 25)
        )
        
        if len(smiles) > 0:
            cv2.putText(image, 'Smiling! :)', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
    
    return image
'''

print(smile_code)

# ========== FACE DETECTION OPTIMIZATION ==========
print("\n" + "=" * 60)
print("OPTIMIZATION TIPS")
print("=" * 60)

print("""
Performance Optimization:
------------------------

1. Process Smaller Images
   - Resize input before detection
   - Scale detection coordinates back
   
   small = cv2.resize(img, None, fx=0.5, fy=0.5)
   faces = face_cascade.detectMultiScale(small)
   faces = [(x*2, y*2, w*2, h*2) for (x, y, w, h) in faces]

2. Use Larger Scale Factor
   - scaleFactor=1.3 instead of 1.1
   - Fewer scales to search

3. Increase minSize
   - Skip tiny faces if not needed
   - minSize=(100, 100) for close faces

4. Skip Frames (for video)
   - Detect every 2-3 frames
   - Track between detections

5. Use Threading
   - Separate threads for capture and detection
   - Or use multiprocessing

6. Consider DNN Method
   - More accurate with similar speed
   - Better GPU utilization

7. ROI-based Detection
   - If face location is predictable
   - Only search relevant image regions
""")

# ========== PRACTICAL EXAMPLE: FACE COUNTER ==========
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE: FACE COUNTER")
print("=" * 60)

def count_faces_in_image(image_path):
    """
    Count the number of faces in an image.
    
    Args:
        image_path: Path to image file
    
    Returns:
        Number of faces detected
    """
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        return -1
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    return len(faces)

# Demo with our created image
face_count = count_faces_in_image('/tmp/demo_face.jpg')
print(f"Faces detected in demo image: {face_count}")
print("(Demo image is synthetic, real photos work better)")

# ========== SAVING DETECTED FACES ==========
print("\n" + "=" * 60)
print("SAVING DETECTED FACES (CROPPING)")
print("=" * 60)

save_faces_code = '''
# Extract and Save Detected Faces
# ================================

def extract_faces(image_path, output_dir):
    """
    Extract all detected faces from an image.
    
    Args:
        image_path: Path to input image
        output_dir: Directory to save face crops
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for i, (x, y, w, h) in enumerate(faces):
        # Add padding (optional)
        padding = 20
        x1 = max(0, x - padding)
        y1 = max(0, y - padding)
        x2 = min(img.shape[1], x + w + padding)
        y2 = min(img.shape[0], y + h + padding)
        
        # Crop face
        face_crop = img[y1:y2, x1:x2]
        
        # Save
        output_path = f"{output_dir}/face_{i+1}.jpg"
        cv2.imwrite(output_path, face_crop)
        print(f"Saved: {output_path}")
    
    return len(faces)

# Usage
num_faces = extract_faces('group_photo.jpg', 'extracted_faces')
print(f"Extracted {num_faces} faces")
'''

print(save_faces_code)

print("\n" + "=" * 60)
print("✅ Face Detection Basics - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Haar cascades: Fast, classic face detection
2. detectMultiScale: scaleFactor and minNeighbors are key
3. Eye/smile detection: Use face ROI for efficiency
4. DNN method: More accurate, handles more cases
5. Real-time: Use larger scale, skip frames
6. Extract faces: Crop and save for further processing

Applications:
------------
- Photo organization
- Security systems
- Attendance systems
- Emotion detection
- Face recognition preprocessing
- Snapchat-style filters

Next Steps:
----------
1. Try with real photos
2. Experiment with webcam detection
3. Combine with face recognition (face_recognition library)
4. Add face landmarks (dlib or MediaPipe)
""")
