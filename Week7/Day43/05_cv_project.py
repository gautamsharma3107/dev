"""
Day 43 - CV Project: Building a Computer Vision Feature
========================================================
Learn: Practical CV application combining learned concepts

Project: Smart Image Analyzer
- Detects faces and draws info
- Applies image enhancements
- Detects edges and shapes
- Creates annotated output

This project combines:
- Face detection
- Image processing
- Drawing operations
- File handling
"""

import cv2
import numpy as np
from datetime import datetime

# ========== PROJECT: SMART IMAGE ANALYZER ==========
print("=" * 60)
print("PROJECT: SMART IMAGE ANALYZER")
print("=" * 60)

class SmartImageAnalyzer:
    """
    A comprehensive image analysis tool that combines
    multiple computer vision techniques.
    """
    
    def __init__(self):
        """Initialize the analyzer with required cascades."""
        # Load face cascade
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Load eye cascade
        self.eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        # Analysis results
        self.results = {}
        
        print("✓ Smart Image Analyzer initialized")
    
    def analyze(self, image):
        """
        Perform comprehensive analysis on an image.
        
        Args:
            image: Input image (BGR format)
        
        Returns:
            dict: Analysis results
        """
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'dimensions': {},
            'faces': [],
            'color_info': {},
            'quality_score': 0
        }
        
        # Basic info
        h, w, c = image.shape
        self.results['dimensions'] = {
            'height': h,
            'width': w,
            'channels': c,
            'total_pixels': h * w
        }
        
        # Face detection
        self._detect_faces(image)
        
        # Color analysis
        self._analyze_colors(image)
        
        # Quality assessment
        self._assess_quality(image)
        
        return self.results
    
    def _detect_faces(self, image):
        """Detect faces and eyes in the image."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            face_info = {
                'location': {'x': int(x), 'y': int(y), 
                            'width': int(w), 'height': int(h)},
                'eyes_detected': 0,
                'face_area_percent': (w * h) / (image.shape[0] * image.shape[1]) * 100
            }
            
            # Detect eyes within face ROI
            roi_gray = gray[y:y+h, x:x+w]
            eyes = self.eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
            face_info['eyes_detected'] = len(eyes)
            
            self.results['faces'].append(face_info)
    
    def _analyze_colors(self, image):
        """Analyze color distribution."""
        # Split channels
        b, g, r = cv2.split(image)
        
        self.results['color_info'] = {
            'mean_blue': float(np.mean(b)),
            'mean_green': float(np.mean(g)),
            'mean_red': float(np.mean(r)),
            'brightness': float(np.mean(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))),
            'dominant_channel': ['Blue', 'Green', 'Red'][
                np.argmax([np.mean(b), np.mean(g), np.mean(r)])]
        }
    
    def _assess_quality(self, image):
        """Assess image quality based on various metrics."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Sharpness (using Laplacian variance)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # Contrast (standard deviation)
        contrast = np.std(gray)
        
        # Brightness
        brightness = np.mean(gray)
        
        # Calculate quality score (0-100)
        sharpness_score = min(laplacian_var / 10, 40)  # Max 40 points
        contrast_score = min(contrast / 2, 30)  # Max 30 points
        brightness_score = 30 - abs(brightness - 127) / 4.23  # Max 30 points
        
        self.results['quality_score'] = max(0, min(100, 
            sharpness_score + contrast_score + brightness_score))
        
        self.results['quality_details'] = {
            'sharpness': float(laplacian_var),
            'contrast': float(contrast),
            'brightness': float(brightness)
        }
    
    def create_annotated_image(self, image):
        """
        Create an annotated version of the image.
        
        Args:
            image: Input image
        
        Returns:
            Annotated image
        """
        output = image.copy()
        
        # Draw faces
        for face in self.results.get('faces', []):
            loc = face['location']
            x, y, w, h = loc['x'], loc['y'], loc['width'], loc['height']
            
            # Face rectangle
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Face info
            info = f"Eyes: {face['eyes_detected']}"
            cv2.putText(output, info, (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        # Add summary overlay
        overlay = output.copy()
        cv2.rectangle(overlay, (10, 10), (250, 120), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, output, 0.3, 0, output)
        
        # Add text
        y_offset = 30
        texts = [
            f"Faces: {len(self.results.get('faces', []))}",
            f"Quality: {self.results.get('quality_score', 0):.1f}/100",
            f"Brightness: {self.results.get('color_info', {}).get('brightness', 0):.1f}",
            f"Size: {self.results['dimensions']['width']}x{self.results['dimensions']['height']}"
        ]
        
        for text in texts:
            cv2.putText(output, text, (20, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            y_offset += 22
        
        return output
    
    def enhance_image(self, image, brightness=0, contrast=1.0, sharpen=False):
        """
        Enhance the image with various adjustments.
        
        Args:
            image: Input image
            brightness: Brightness adjustment (-100 to 100)
            contrast: Contrast multiplier (0.5 to 2.0)
            sharpen: Whether to apply sharpening
        
        Returns:
            Enhanced image
        """
        output = image.copy()
        
        # Adjust brightness and contrast
        output = cv2.convertScaleAbs(output, alpha=contrast, beta=brightness)
        
        # Apply sharpening
        if sharpen:
            kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
            output = cv2.filter2D(output, -1, kernel)
        
        return output
    
    def detect_edges(self, image, method='canny'):
        """
        Detect edges in the image.
        
        Args:
            image: Input image
            method: 'canny', 'sobel', or 'laplacian'
        
        Returns:
            Edge image
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        if method == 'canny':
            edges = cv2.Canny(gray, 100, 200)
        elif method == 'sobel':
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            edges = np.uint8(np.abs(cv2.magnitude(sobel_x, sobel_y)))
        elif method == 'laplacian':
            edges = np.uint8(np.abs(cv2.Laplacian(gray, cv2.CV_64F)))
        else:
            edges = gray
        
        return edges
    
    def create_collage(self, image):
        """
        Create a collage showing various analysis views.
        
        Args:
            image: Input image
        
        Returns:
            Collage image
        """
        # Resize all to same size
        h, w = 200, 300
        
        # Original (resized)
        original = cv2.resize(image, (w, h))
        
        # Grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (w, h))
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        
        # Edges
        edges = self.detect_edges(image)
        edges = cv2.resize(edges, (w, h))
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        # Annotated
        annotated = self.create_annotated_image(image)
        annotated = cv2.resize(annotated, (w, h))
        
        # Create 2x2 grid
        top_row = np.hstack([original, annotated])
        bottom_row = np.hstack([gray_bgr, edges_bgr])
        collage = np.vstack([top_row, bottom_row])
        
        # Add labels
        labels = [
            ((10, 20), "Original"),
            ((w + 10, 20), "Annotated"),
            ((10, h + 20), "Grayscale"),
            ((w + 10, h + 20), "Edges")
        ]
        
        for pos, text in labels:
            cv2.putText(collage, text, pos,
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        return collage
    
    def get_report(self):
        """Generate a text report of the analysis."""
        report = []
        report.append("=" * 50)
        report.append("IMAGE ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"Analysis Time: {self.results.get('timestamp', 'N/A')}")
        report.append("")
        
        # Dimensions
        dims = self.results.get('dimensions', {})
        report.append("DIMENSIONS:")
        report.append(f"  Size: {dims.get('width', 0)} x {dims.get('height', 0)}")
        report.append(f"  Total Pixels: {dims.get('total_pixels', 0):,}")
        report.append("")
        
        # Faces
        faces = self.results.get('faces', [])
        report.append(f"FACE DETECTION: {len(faces)} face(s) found")
        for i, face in enumerate(faces, 1):
            loc = face['location']
            report.append(f"  Face {i}:")
            report.append(f"    Position: ({loc['x']}, {loc['y']})")
            report.append(f"    Size: {loc['width']}x{loc['height']}")
            report.append(f"    Eyes Detected: {face['eyes_detected']}")
            report.append(f"    Area: {face['face_area_percent']:.2f}% of image")
        report.append("")
        
        # Color info
        colors = self.results.get('color_info', {})
        report.append("COLOR ANALYSIS:")
        report.append(f"  Dominant Channel: {colors.get('dominant_channel', 'N/A')}")
        report.append(f"  Average Brightness: {colors.get('brightness', 0):.1f}")
        report.append(f"  RGB Means: R={colors.get('mean_red', 0):.1f}, "
                     f"G={colors.get('mean_green', 0):.1f}, "
                     f"B={colors.get('mean_blue', 0):.1f}")
        report.append("")
        
        # Quality
        quality = self.results.get('quality_details', {})
        report.append("QUALITY ASSESSMENT:")
        report.append(f"  Overall Score: {self.results.get('quality_score', 0):.1f}/100")
        report.append(f"  Sharpness: {quality.get('sharpness', 0):.2f}")
        report.append(f"  Contrast: {quality.get('contrast', 0):.2f}")
        report.append("")
        report.append("=" * 50)
        
        return "\n".join(report)


# ========== DEMO: USING THE ANALYZER ==========
print("\n" + "=" * 60)
print("DEMO: USING THE SMART IMAGE ANALYZER")
print("=" * 60)

# Create a sample image for demonstration
def create_demo_image():
    """Create a demo image with various features."""
    img = np.ones((400, 600, 3), dtype=np.uint8) * 200
    
    # Add a gradient background
    for i in range(600):
        img[:, i] = [200 - i//10, 180 + i//15, 150 + i//10]
    
    # Add some shapes
    cv2.rectangle(img, (50, 50), (200, 200), (255, 100, 100), -1)
    cv2.circle(img, (450, 150), 80, (100, 255, 100), -1)
    cv2.ellipse(img, (150, 320), (80, 40), 0, 0, 360, (100, 100, 255), -1)
    
    # Add some noise for texture
    noise = np.random.randint(-20, 20, img.shape, dtype=np.int16)
    img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    # Add text
    cv2.putText(img, "Demo Image", (220, 380),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 50), 2)
    
    return img

# Create demo image
demo_img = create_demo_image()
cv2.imwrite('/tmp/demo_project_input.jpg', demo_img)

# Initialize analyzer
analyzer = SmartImageAnalyzer()

# Analyze the image
results = analyzer.analyze(demo_img)

# Print report
print(analyzer.get_report())

# Create annotated version
annotated = analyzer.create_annotated_image(demo_img)
cv2.imwrite('/tmp/demo_project_annotated.jpg', annotated)

# Create collage
collage = analyzer.create_collage(demo_img)
cv2.imwrite('/tmp/demo_project_collage.jpg', collage)

# Create enhanced version
enhanced = analyzer.enhance_image(demo_img, brightness=20, contrast=1.2, sharpen=True)
cv2.imwrite('/tmp/demo_project_enhanced.jpg', enhanced)

print("\nOutput files saved:")
print("  - /tmp/demo_project_input.jpg")
print("  - /tmp/demo_project_annotated.jpg")
print("  - /tmp/demo_project_collage.jpg")
print("  - /tmp/demo_project_enhanced.jpg")

# ========== ADDITIONAL PROJECT IDEAS ==========
print("\n" + "=" * 60)
print("ADDITIONAL PROJECT IDEAS")
print("=" * 60)

print("""
1. MOTION DETECTOR
   ----------------
   - Compare consecutive video frames
   - Detect and highlight moving objects
   - Send alerts on motion detection
   - Great for security applications

2. DOCUMENT SCANNER
   -----------------
   - Detect document edges
   - Apply perspective transform
   - Enhance for readability
   - OCR integration (pytesseract)

3. COLOR PALETTE EXTRACTOR
   -----------------------
   - Extract dominant colors from images
   - K-means clustering on pixels
   - Generate color schemes
   - Useful for design tools

4. AUGMENTED REALITY FILTER
   ------------------------
   - Detect face landmarks
   - Overlay virtual objects
   - Real-time processing
   - Instagram-style filters

5. LICENSE PLATE DETECTOR
   ----------------------
   - Detect license plates
   - Extract text regions
   - Apply OCR
   - Vehicle tracking system

6. HAND GESTURE RECOGNITION
   ------------------------
   - Detect hand contours
   - Count fingers
   - Recognize gestures
   - Control applications

7. OBJECT TRACKING
   ----------------
   - Select object to track
   - Track across video frames
   - Multiple tracker types
   - Sports analysis, surveillance

8. BARCODE/QR CODE READER
   ----------------------
   - Detect barcodes
   - Decode information
   - pyzbar library integration
   - Inventory management
""")

# ========== WEBCAM PROJECT TEMPLATE ==========
print("\n" + "=" * 60)
print("WEBCAM PROJECT TEMPLATE")
print("=" * 60)

webcam_template = '''
# Real-time Image Analysis with Webcam
# =====================================

import cv2
import numpy as np
from datetime import datetime

class WebcamAnalyzer:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Set resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    def process_frame(self, frame):
        """Process a single frame."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Face detection
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Add info overlay
        cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, datetime.now().strftime("%H:%M:%S"), (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        return frame
    
    def run(self):
        """Main loop."""
        print("Press 'q' to quit, 's' to save screenshot")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Process frame
            processed = self.process_frame(frame)
            
            # Display
            cv2.imshow('Webcam Analyzer', processed)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, processed)
                print(f"Saved: {filename}")
        
        self.cleanup()
    
    def cleanup(self):
        """Release resources."""
        self.cap.release()
        cv2.destroyAllWindows()

# Run the analyzer
if __name__ == '__main__':
    analyzer = WebcamAnalyzer()
    analyzer.run()
'''

print(webcam_template)

print("\n" + "=" * 60)
print("✅ CV Project - Complete!")
print("=" * 60)

print("""
Summary:
--------
1. Built a comprehensive SmartImageAnalyzer class
2. Combines face detection, color analysis, quality assessment
3. Creates annotated images and analysis reports
4. Generates image collages for comparison
5. Includes enhancement features

Skills Applied:
--------------
- Face detection (Haar cascades)
- Image processing (filters, edge detection)
- Drawing operations (rectangles, text)
- Color space analysis
- Image quality assessment
- Code organization (OOP)

Next Steps:
----------
1. Try with real images
2. Add more analysis features
3. Build a GUI with tkinter or PyQt
4. Create a web interface with Flask
5. Add machine learning features
""")
