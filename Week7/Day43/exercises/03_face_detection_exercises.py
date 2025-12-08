"""
Day 43 - Face Detection Exercises
==================================
Practice face and eye detection with Haar cascades
"""

import cv2
import numpy as np

# ============================================================
# EXERCISE 1: Basic Face Detection
# ============================================================
print("Exercise 1: Basic Face Detection")
print("-" * 40)

"""
Task:
1. Load the frontal face cascade classifier
2. Create a function detect_faces(image) that:
   - Converts image to grayscale
   - Detects faces with scaleFactor=1.3, minNeighbors=5
   - Returns list of (x, y, w, h) tuples
3. Test with a sample image
"""

# Your solution:




# ============================================================
# EXERCISE 2: Face and Eye Detection
# ============================================================
print("\nExercise 2: Face and Eye Detection")
print("-" * 40)

"""
Task:
1. Load face and eye cascade classifiers
2. Create a function that:
   - Detects faces
   - For each face, detects eyes within face ROI
   - Draws green rectangle for face
   - Draws blue rectangles for eyes
3. Return annotated image
"""

# Your solution:




# ============================================================
# EXERCISE 3: Parameter Tuning
# ============================================================
print("\nExercise 3: Parameter Tuning")
print("-" * 40)

"""
Task:
Create a function compare_detection_params(image) that:
1. Runs face detection with different parameter combinations:
   - scaleFactor: [1.1, 1.2, 1.3]
   - minNeighbors: [3, 5, 7]
2. Returns a dictionary with results showing:
   - Parameters used
   - Number of faces detected
3. Help identify best parameters for the image
"""

# Your solution:




# ============================================================
# EXERCISE 4: Face Counter
# ============================================================
print("\nExercise 4: Face Counter")
print("-" * 40)

"""
Task:
Create a FaceCounter class with:
1. __init__: Load cascade classifier
2. count(image_path): Return number of faces
3. count_batch(image_paths): Return dict {path: count}
4. get_statistics(image_paths): Return min, max, avg faces
"""

# Your solution:




# ============================================================
# EXERCISE 5: Face Extraction
# ============================================================
print("\nExercise 5: Face Extraction")
print("-" * 40)

"""
Task:
Create a function extract_faces(image, padding=20) that:
1. Detects all faces in the image
2. Extracts each face with the specified padding
3. Resizes all faces to 100x100
4. Returns list of face images
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
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def detect_faces(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5)
        return faces.tolist() if len(faces) > 0 else []
    
    # Test
    test_img = np.ones((300, 300, 3), dtype=np.uint8) * 200
    result = detect_faces(test_img)
    print(f"\n✓ Exercise 1: detect_faces function created")
    print(f"  Test result (empty image): {len(result)} faces")
    return detect_faces

solution1()

# Solution 2
def solution2():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    def detect_faces_and_eyes(image):
        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = output[y:y+h, x:x+w]
            
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
        
        return output
    
    print("✓ Exercise 2: detect_faces_and_eyes function created")
    return detect_faces_and_eyes

solution2()

# Solution 3
def solution3():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def compare_detection_params(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        results = []
        
        for sf in [1.1, 1.2, 1.3]:
            for mn in [3, 5, 7]:
                faces = face_cascade.detectMultiScale(gray, sf, mn)
                results.append({
                    'scaleFactor': sf,
                    'minNeighbors': mn,
                    'faces_detected': len(faces)
                })
        
        return results
    
    # Test
    test_img = np.ones((300, 300, 3), dtype=np.uint8) * 200
    results = compare_detection_params(test_img)
    print("✓ Exercise 3: compare_detection_params function created")
    print("  Sample output:")
    for r in results[:3]:
        print(f"    {r}")
    return compare_detection_params

solution3()

# Solution 4
def solution4():
    class FaceCounter:
        def __init__(self):
            self.cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        def count(self, image_path):
            img = cv2.imread(image_path)
            if img is None:
                return -1
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.cascade.detectMultiScale(gray, 1.1, 5)
            return len(faces)
        
        def count_batch(self, image_paths):
            return {path: self.count(path) for path in image_paths}
        
        def get_statistics(self, image_paths):
            counts = [self.count(p) for p in image_paths]
            counts = [c for c in counts if c >= 0]
            if not counts:
                return {'min': 0, 'max': 0, 'avg': 0}
            return {
                'min': min(counts),
                'max': max(counts),
                'avg': sum(counts) / len(counts)
            }
    
    print("✓ Exercise 4: FaceCounter class created")
    counter = FaceCounter()
    print(f"  Methods: count(), count_batch(), get_statistics()")
    return FaceCounter

solution4()

# Solution 5
def solution5():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def extract_faces(image, padding=20):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        
        extracted = []
        h, w = image.shape[:2]
        
        for (x, y, fw, fh) in faces:
            x1 = max(0, x - padding)
            y1 = max(0, y - padding)
            x2 = min(w, x + fw + padding)
            y2 = min(h, y + fh + padding)
            
            face_crop = image[y1:y2, x1:x2]
            face_resized = cv2.resize(face_crop, (100, 100))
            extracted.append(face_resized)
        
        return extracted
    
    print("✓ Exercise 5: extract_faces function created")
    return extract_faces

solution5()

print("\n✓ All exercises completed!")
