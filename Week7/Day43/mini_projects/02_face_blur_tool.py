"""
Day 43 - Mini Project 2: Face Blur Tool
========================================
Automatically detect and blur faces for privacy
"""

import cv2
import numpy as np

class FaceBlurTool:
    """
    Automatically detect and blur faces in images/video.
    Useful for privacy protection.
    """
    
    def __init__(self):
        """Initialize face detection cascade."""
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        print("Face Blur Tool initialized")
    
    def detect_faces(self, image):
        """
        Detect faces in an image.
        
        Args:
            image: Input BGR image
        
        Returns:
            List of (x, y, w, h) tuples
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return faces
    
    def blur_region(self, image, x, y, w, h, blur_type='gaussian', intensity=51):
        """
        Blur a specific region of the image.
        
        Args:
            image: Input image (modified in-place)
            x, y, w, h: Region coordinates
            blur_type: 'gaussian', 'pixelate', or 'black'
            intensity: Blur intensity (odd number for gaussian)
        
        Returns:
            Modified image
        """
        roi = image[y:y+h, x:x+w]
        
        if blur_type == 'gaussian':
            # Ensure intensity is odd
            intensity = intensity if intensity % 2 == 1 else intensity + 1
            blurred = cv2.GaussianBlur(roi, (intensity, intensity), 0)
        
        elif blur_type == 'pixelate':
            # Pixelate by downscaling and upscaling
            factor = max(1, int(intensity / 10))
            small = cv2.resize(roi, (max(1, w // factor), max(1, h // factor)))
            blurred = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
        
        elif blur_type == 'black':
            # Black rectangle
            blurred = np.zeros_like(roi)
        
        else:
            blurred = roi
        
        image[y:y+h, x:x+w] = blurred
        return image
    
    def blur_faces(self, image, blur_type='gaussian', intensity=51, padding=0):
        """
        Detect and blur all faces in an image.
        
        Args:
            image: Input BGR image
            blur_type: Type of blur ('gaussian', 'pixelate', 'black')
            intensity: Blur intensity
            padding: Extra padding around face
        
        Returns:
            Image with blurred faces, number of faces found
        """
        output = image.copy()
        faces = self.detect_faces(image)
        
        h, w = image.shape[:2]
        
        for (fx, fy, fw, fh) in faces:
            # Add padding
            x1 = max(0, fx - padding)
            y1 = max(0, fy - padding)
            x2 = min(w, fx + fw + padding)
            y2 = min(h, fy + fh + padding)
            
            output = self.blur_region(output, x1, y1, x2-x1, y2-y1, blur_type, intensity)
        
        return output, len(faces)
    
    def blur_faces_except(self, image, keep_indices, blur_type='gaussian', intensity=51):
        """
        Blur all faces except specified ones.
        
        Args:
            image: Input BGR image
            keep_indices: List of face indices to NOT blur
            blur_type: Type of blur
            intensity: Blur intensity
        
        Returns:
            Image with selected faces blurred
        """
        output = image.copy()
        faces = self.detect_faces(image)
        
        for i, (x, y, w, h) in enumerate(faces):
            if i not in keep_indices:
                output = self.blur_region(output, x, y, w, h, blur_type, intensity)
        
        return output
    
    def create_comparison(self, original, blurred):
        """
        Create side-by-side comparison.
        
        Args:
            original: Original image
            blurred: Image with blurred faces
        
        Returns:
            Comparison image
        """
        h = min(original.shape[0], 400)
        aspect = original.shape[1] / original.shape[0]
        w = int(h * aspect)
        
        orig_small = cv2.resize(original, (w, h))
        blur_small = cv2.resize(blurred, (w, h))
        
        cv2.putText(orig_small, "Original", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(blur_small, "Privacy Protected", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return np.hstack([orig_small, blur_small])
    
    def process_video_frame(self, frame, blur_type='gaussian', intensity=31):
        """
        Process a single video frame.
        
        Args:
            frame: Video frame
            blur_type: Type of blur
            intensity: Blur intensity
        
        Returns:
            Processed frame with blurred faces
        """
        output, num_faces = self.blur_faces(frame, blur_type, intensity)
        
        # Add face count indicator
        cv2.putText(output, f"Faces: {num_faces}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return output


# Demo
if __name__ == "__main__":
    print("=" * 60)
    print("FACE BLUR TOOL DEMO")
    print("=" * 60)
    
    # Create sample image with face-like shapes
    sample = np.ones((400, 600, 3), dtype=np.uint8) * 200
    
    # Add face-like oval shapes (these won't be detected as faces, 
    # but demonstrates the blur functionality)
    cv2.ellipse(sample, (150, 200), (60, 80), 0, 0, 360, (150, 130, 120), -1)
    cv2.ellipse(sample, (450, 200), (60, 80), 0, 0, 360, (140, 120, 110), -1)
    
    # Add "eyes" and "mouth"
    for cx in [150, 450]:
        cv2.circle(sample, (cx-20, 180), 10, (255, 255, 255), -1)
        cv2.circle(sample, (cx+20, 180), 10, (255, 255, 255), -1)
        cv2.ellipse(sample, (cx, 230), (20, 10), 0, 0, 180, (100, 80, 80), -1)
    
    cv2.putText(sample, "Face Blur Demo", (200, 380),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 50), 2)
    
    # Initialize tool
    tool = FaceBlurTool()
    
    # Apply different blur types
    blurred_gaussian, n1 = tool.blur_faces(sample, 'gaussian', 51)
    blurred_pixelate, n2 = tool.blur_faces(sample, 'pixelate', 30)
    blurred_black, n3 = tool.blur_faces(sample, 'black')
    
    # Create comparison
    comparison = tool.create_comparison(sample, blurred_gaussian)
    
    # Save results
    cv2.imwrite('/tmp/face_blur_original.jpg', sample)
    cv2.imwrite('/tmp/face_blur_gaussian.jpg', blurred_gaussian)
    cv2.imwrite('/tmp/face_blur_pixelate.jpg', blurred_pixelate)
    cv2.imwrite('/tmp/face_blur_black.jpg', blurred_black)
    cv2.imwrite('/tmp/face_blur_comparison.jpg', comparison)
    
    print(f"\nFaces detected: {n1}")
    print("\nOutput files:")
    print("  - /tmp/face_blur_original.jpg")
    print("  - /tmp/face_blur_gaussian.jpg")
    print("  - /tmp/face_blur_pixelate.jpg")
    print("  - /tmp/face_blur_black.jpg")
    print("  - /tmp/face_blur_comparison.jpg")
    print("\n✓ Face Blur Tool demo complete!")
    
    print("\n" + "=" * 60)
    print("WEBCAM VERSION (code template)")
    print("=" * 60)
    
    webcam_code = '''
# Real-time Face Blur with Webcam
# ================================

tool = FaceBlurTool()
cap = cv2.VideoCapture(0)

print("Press 'g' for Gaussian, 'p' for Pixelate, 'b' for Black, 'q' to quit")

blur_type = 'gaussian'

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    processed = tool.process_video_frame(frame, blur_type)
    cv2.imshow('Face Blur', processed)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        blur_type = 'gaussian'
    elif key == ord('p'):
        blur_type = 'pixelate'
    elif key == ord('b'):
        blur_type = 'black'

cap.release()
cv2.destroyAllWindows()
'''
    print(webcam_code)
