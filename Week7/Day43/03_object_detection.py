"""
Day 43 - Object Detection Overview (YOLO)
==========================================
Learn: Object detection concepts, YOLO architecture, OpenCV DNN

Key Concepts:
- Object detection vs classification
- YOLO (You Only Look Once) architecture
- Bounding boxes and confidence scores
- Non-Maximum Suppression (NMS)
- Using pre-trained models with OpenCV DNN
"""

import cv2
import numpy as np

# ========== OBJECT DETECTION FUNDAMENTALS ==========
print("=" * 60)
print("OBJECT DETECTION FUNDAMENTALS")
print("=" * 60)

print("""
Object Detection vs Image Classification:
-----------------------------------------

Image Classification:
- Input: Image
- Output: Single class label (e.g., "cat")
- Answers: "What is in this image?"

Object Detection:
- Input: Image
- Output: Multiple bounding boxes + class labels + confidence
- Answers: "What objects are where in this image?"

Object detection = Classification + Localization (for multiple objects)
""")

# ========== BOUNDING BOXES ==========
print("=" * 60)
print("BOUNDING BOXES")
print("=" * 60)

# Create a demo image
demo_img = np.ones((400, 600, 3), dtype=np.uint8) * 240

# Draw some "detected objects" with bounding boxes
detections = [
    {"box": (50, 50, 150, 200), "label": "Person", "confidence": 0.95},
    {"box": (200, 100, 120, 150), "label": "Dog", "confidence": 0.87},
    {"box": (400, 50, 150, 180), "label": "Car", "confidence": 0.92},
]

for det in detections:
    x, y, w, h = det["box"]
    label = det["label"]
    conf = det["confidence"]
    
    # Draw bounding box
    cv2.rectangle(demo_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Draw label with confidence
    text = f"{label}: {conf:.2f}"
    cv2.putText(demo_img, text, (x, y - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imwrite('/tmp/bounding_boxes_demo.jpg', demo_img)
print("Created bounding box demo at /tmp/bounding_boxes_demo.jpg")

print("""
Bounding Box Formats:
--------------------
1. (x, y, w, h) - top-left corner + width/height
2. (x1, y1, x2, y2) - top-left and bottom-right corners
3. (cx, cy, w, h) - center coordinates + width/height (YOLO uses this)

Converting between formats:
--------------------------
# (x, y, w, h) to (x1, y1, x2, y2)
x1, y1, x2, y2 = x, y, x + w, y + h

# (cx, cy, w, h) to (x, y, w, h)
x, y = cx - w/2, cy - h/2
""")

# ========== YOLO OVERVIEW ==========
print("\n" + "=" * 60)
print("YOLO (You Only Look Once) OVERVIEW")
print("=" * 60)

print("""
YOLO Architecture:
------------------
YOLO revolutionized object detection by treating it as a
regression problem rather than classification.

Key Ideas:
1. Single Neural Network: One forward pass detects all objects
2. Grid-based: Image divided into SxS grid cells
3. Each cell predicts:
   - B bounding boxes
   - Confidence scores
   - C class probabilities

YOLO Versions:
-------------
- YOLOv1 (2016): Original, fast but less accurate
- YOLOv2 (2017): Better accuracy, batch normalization
- YOLOv3 (2018): Multi-scale detection, better small objects
- YOLOv4 (2020): Many improvements, state-of-art
- YOLOv5 (2020): PyTorch-based, easier to use
- YOLOv8 (2023): Latest, best performance

Speed Comparison (rough estimates):
-----------------------------------
- YOLO: ~45 FPS on GPU
- Faster R-CNN: ~7 FPS on GPU
- SSD: ~22 FPS on GPU
""")

# ========== CONFIDENCE SCORES AND NMS ==========
print("=" * 60)
print("CONFIDENCE SCORES AND NON-MAXIMUM SUPPRESSION")
print("=" * 60)

print("""
Confidence Scores:
-----------------
Each detection has a confidence score (0-1) indicating
how certain the model is about:
1. Object presence in the box
2. Box accuracy (IOU with ground truth)
3. Class prediction

Typically filter detections with confidence < 0.5

Non-Maximum Suppression (NMS):
-----------------------------
Problem: Multiple overlapping boxes for same object
Solution: Keep only the best box, remove overlapping ones

Algorithm:
1. Sort boxes by confidence
2. Take the highest confidence box
3. Remove all boxes with high IOU overlap
4. Repeat until no boxes left

IOU (Intersection over Union):
------------------------------
IOU = Area of Overlap / Area of Union

IOU > 0.5 typically means same object
""")

# Implement IOU calculation
def calculate_iou(box1, box2):
    """
    Calculate Intersection over Union between two boxes.
    Boxes in format: (x1, y1, x2, y2)
    """
    # Determine intersection rectangle
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    # Calculate intersection area
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    
    # Calculate union area
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union = box1_area + box2_area - intersection
    
    return intersection / union if union > 0 else 0

# Demo IOU calculation
box1 = (100, 100, 200, 200)  # 100x100 box
box2 = (150, 100, 250, 200)  # 50% overlap horizontally

iou = calculate_iou(box1, box2)
print(f"\nIOU Example:")
print(f"Box 1: {box1}")
print(f"Box 2: {box2}")
print(f"IOU: {iou:.2f}")

# Implement NMS
def non_maximum_suppression(boxes, scores, iou_threshold=0.5):
    """
    Apply Non-Maximum Suppression.
    
    Args:
        boxes: List of (x1, y1, x2, y2) tuples
        scores: List of confidence scores
        iou_threshold: IOU threshold for suppression
    
    Returns:
        indices: Indices of boxes to keep
    """
    if len(boxes) == 0:
        return []
    
    # Sort by scores
    indices = np.argsort(scores)[::-1]
    keep = []
    
    while len(indices) > 0:
        # Keep the highest scoring box
        current = indices[0]
        keep.append(current)
        
        # Remove current from consideration
        indices = indices[1:]
        
        # Calculate IOUs with remaining boxes
        remaining = []
        for idx in indices:
            iou = calculate_iou(boxes[current], boxes[idx])
            if iou < iou_threshold:
                remaining.append(idx)
        
        indices = np.array(remaining)
    
    return keep

# Demo NMS
demo_boxes = [
    (100, 100, 200, 200),
    (110, 105, 210, 205),  # High overlap with first
    (300, 100, 400, 200),  # Different location
    (305, 105, 405, 205),  # High overlap with third
]
demo_scores = [0.9, 0.8, 0.95, 0.75]

kept_indices = non_maximum_suppression(demo_boxes, demo_scores, 0.5)
print(f"\nNMS Demo:")
print(f"Input boxes: {len(demo_boxes)}")
print(f"Kept indices: {kept_indices}")
print(f"Boxes after NMS: {len(kept_indices)}")

# ========== USING OPENCV DNN ==========
print("\n" + "=" * 60)
print("USING OPENCV DNN MODULE")
print("=" * 60)

print("""
OpenCV DNN Module:
-----------------
OpenCV can run pre-trained deep learning models for detection.

Supported Frameworks:
- Caffe (.prototxt + .caffemodel)
- TensorFlow (.pb or .pbtxt)
- Darknet/YOLO (.cfg + .weights)
- ONNX (.onnx)
- Torch (.t7)

Loading Models:
--------------
# YOLO/Darknet
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# TensorFlow
net = cv2.dnn.readNetFromTensorflow('frozen_model.pb')

# Caffe
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'model.caffemodel')

# ONNX
net = cv2.dnn.readNetFromONNX('model.onnx')
""")

# ========== YOLO DETECTION PATTERN ==========
print("=" * 60)
print("YOLO DETECTION PATTERN")
print("=" * 60)

# Note: This is a pattern/template - actual weights not included
yolo_detection_code = '''
# Complete YOLO Object Detection Pattern
# =====================================

import cv2
import numpy as np

# Configuration
CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
INPUT_WIDTH = 416
INPUT_HEIGHT = 416

# Load class names (COCO dataset has 80 classes)
def load_classes(filename):
    with open(filename, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    return classes

# Load YOLO model
def load_yolo(cfg_path, weights_path):
    net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
    
    # Use GPU if available
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    # For GPU: cv2.dnn.DNN_TARGET_CUDA
    
    return net

# Get output layer names
def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

# Detect objects
def detect_objects(image, net, output_layers, classes):
    height, width = image.shape[:2]
    
    # Create blob from image
    blob = cv2.dnn.blobFromImage(
        image, 
        scalefactor=1/255.0,  # Normalize to 0-1
        size=(INPUT_WIDTH, INPUT_HEIGHT),
        swapRB=True,  # BGR to RGB
        crop=False
    )
    
    # Set input and forward pass
    net.setInput(blob)
    outputs = net.forward(output_layers)
    
    # Process detections
    boxes = []
    confidences = []
    class_ids = []
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]  # Class probabilities
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > CONFIDENCE_THRESHOLD:
                # YOLO outputs center_x, center_y, w, h (normalized)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Convert to corner coordinates
                x = center_x - w // 2
                y = center_y - h // 2
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Apply NMS
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 
                                CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    
    return boxes, confidences, class_ids, indices

# Draw detections
def draw_detections(image, boxes, confidences, class_ids, indices, classes):
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    
    for i in indices:
        box = boxes[i]
        x, y, w, h = box
        label = classes[class_ids[i]]
        confidence = confidences[i]
        color = colors[class_ids[i]]
        
        # Draw box
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        
        # Draw label
        text = f"{label}: {confidence:.2f}"
        cv2.putText(image, text, (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return image

# Main function
def main():
    # Load model and classes
    classes = load_classes('coco.names')
    net = load_yolo('yolov3.cfg', 'yolov3.weights')
    output_layers = get_output_layers(net)
    
    # Load image
    image = cv2.imread('test_image.jpg')
    
    # Detect objects
    boxes, confidences, class_ids, indices = detect_objects(
        image, net, output_layers, classes)
    
    # Draw and save results
    result = draw_detections(image, boxes, confidences, 
                             class_ids, indices, classes)
    cv2.imwrite('detection_result.jpg', result)
    print(f"Detected {len(indices)} objects")

if __name__ == '__main__':
    main()
'''

print(yolo_detection_code)

# ========== ALTERNATIVE: USING SIMPLER DETECTORS ==========
print("\n" + "=" * 60)
print("SIMPLER OBJECT DETECTORS IN OPENCV")
print("=" * 60)

# HOG Person Detector (built into OpenCV)
print("\nHOG (Histogram of Oriented Gradients) Person Detector:")
print("-" * 50)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Create a demo image (in real use, load actual image)
person_demo = np.ones((400, 300, 3), dtype=np.uint8) * 200

print("""
# Using HOG Person Detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Detect people in image
boxes, weights = hog.detectMultiScale(
    image,
    winStride=(8, 8),
    padding=(4, 4),
    scale=1.05
)

# Draw bounding boxes
for (x, y, w, h) in boxes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
""")

# ========== COCO DATASET ==========
print("\n" + "=" * 60)
print("COCO DATASET CLASSES")
print("=" * 60)

coco_classes = [
    "person", "bicycle", "car", "motorcycle", "airplane",
    "bus", "train", "truck", "boat", "traffic light",
    "fire hydrant", "stop sign", "parking meter", "bench", "bird",
    "cat", "dog", "horse", "sheep", "cow",
    "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee",
    "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
    "wine glass", "cup", "fork", "knife", "spoon",
    "bowl", "banana", "apple", "sandwich", "orange",
    "broccoli", "carrot", "hot dog", "pizza", "donut",
    "cake", "chair", "couch", "potted plant", "bed",
    "dining table", "toilet", "tv", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven",
    "toaster", "sink", "refrigerator", "book", "clock",
    "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

print(f"COCO Dataset: {len(coco_classes)} classes")
print("\nSample classes:")
for i, cls in enumerate(coco_classes[:20]):
    print(f"  {i}: {cls}")
print("  ...")

# ========== MODEL DOWNLOADS ==========
print("\n" + "=" * 60)
print("WHERE TO GET YOLO WEIGHTS")
print("=" * 60)

print("""
YOLOv3 Files:
------------
1. Configuration: yolov3.cfg
   https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg

2. Weights: yolov3.weights (236 MB)
   https://pjreddie.com/media/files/yolov3.weights

3. Class Names: coco.names
   https://github.com/pjreddie/darknet/blob/master/data/coco.names

YOLOv3-tiny (faster, less accurate):
-----------------------------------
- yolov3-tiny.cfg
- yolov3-tiny.weights (33 MB)

Alternative: YOLOv5 with PyTorch
-------------------------------
pip install ultralytics

from ultralytics import YOLO
model = YOLO('yolov5s.pt')  # Auto-downloads
results = model('image.jpg')
""")

# ========== PERFORMANCE TIPS ==========
print("\n" + "=" * 60)
print("PERFORMANCE OPTIMIZATION TIPS")
print("=" * 60)

print("""
1. Use GPU Acceleration:
   net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
   net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

2. Use Smaller Input Size:
   - 416x416 is standard
   - 320x320 for faster inference
   - 608x608 for better accuracy

3. Use Tiny Models:
   - YOLOv3-tiny is 10x faster than YOLOv3
   - Good for real-time on CPU

4. Batch Processing:
   - Process multiple images at once
   - Improves GPU utilization

5. Model Optimization:
   - Convert to TensorRT for NVIDIA GPUs
   - Use ONNX Runtime for optimization
   - Quantize to INT8 for faster inference

6. Adjust Confidence Threshold:
   - Higher threshold = fewer detections, faster NMS
   - Balance accuracy vs speed
""")

print("\n" + "=" * 60)
print("✅ Object Detection Overview - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Object detection = classification + localization
2. YOLO: Fast, single-pass detection
3. Bounding boxes: (x, y, w, h) or (x1, y1, x2, y2)
4. IOU measures overlap between boxes
5. NMS removes duplicate detections
6. OpenCV DNN can run YOLO and other models
7. COCO dataset: 80 common object classes
8. Use GPU and smaller models for real-time

Next Steps:
-----------
1. Download YOLO weights and try detection
2. Experiment with different confidence thresholds
3. Try YOLOv5 with PyTorch for easier setup
4. Apply to your specific use case
""")
