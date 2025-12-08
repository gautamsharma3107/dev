"""
Day 43 - Mini Project 3: Shape Detector
========================================
Detect and classify geometric shapes in images
"""

import cv2
import numpy as np

class ShapeDetector:
    """
    Detect and classify geometric shapes using contour analysis.
    """
    
    def __init__(self):
        """Initialize the shape detector."""
        print("Shape Detector initialized")
    
    def detect_shapes(self, image):
        """
        Detect shapes in an image.
        
        Args:
            image: Input BGR image
        
        Returns:
            List of detected shapes with info
        """
        # Convert to grayscale and threshold
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        shapes = []
        for contour in contours:
            # Filter small contours
            if cv2.contourArea(contour) < 100:
                continue
            
            shape_info = self._classify_shape(contour)
            if shape_info:
                shapes.append(shape_info)
        
        return shapes
    
    def _classify_shape(self, contour):
        """
        Classify a single contour as a shape.
        
        Args:
            contour: Contour to classify
        
        Returns:
            Dictionary with shape info or None
        """
        # Approximate the contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        
        # Get bounding box
        x, y, w, h = cv2.boundingRect(approx)
        
        # Classify based on number of vertices
        vertices = len(approx)
        
        if vertices == 3:
            shape_name = "Triangle"
        elif vertices == 4:
            # Check if square or rectangle
            aspect_ratio = w / float(h)
            if 0.95 <= aspect_ratio <= 1.05:
                shape_name = "Square"
            else:
                shape_name = "Rectangle"
        elif vertices == 5:
            shape_name = "Pentagon"
        elif vertices == 6:
            shape_name = "Hexagon"
        elif vertices > 6:
            # Check if circle
            area = cv2.contourArea(contour)
            circularity = 4 * np.pi * area / (perimeter * perimeter)
            if circularity > 0.8:
                shape_name = "Circle"
            else:
                shape_name = f"Polygon ({vertices} sides)"
        else:
            shape_name = "Unknown"
        
        return {
            'name': shape_name,
            'vertices': vertices,
            'contour': contour,
            'bounding_box': (x, y, w, h),
            'center': (x + w // 2, y + h // 2),
            'area': cv2.contourArea(contour),
            'perimeter': perimeter
        }
    
    def draw_shapes(self, image, shapes, show_info=True):
        """
        Draw detected shapes on image.
        
        Args:
            image: Input image
            shapes: List of shape dictionaries
            show_info: Whether to show shape names
        
        Returns:
            Annotated image
        """
        output = image.copy()
        
        colors = {
            'Triangle': (0, 255, 0),
            'Square': (255, 0, 0),
            'Rectangle': (0, 0, 255),
            'Circle': (255, 255, 0),
            'Pentagon': (255, 0, 255),
            'Hexagon': (0, 255, 255),
        }
        
        for shape in shapes:
            name = shape['name']
            color = colors.get(name, (128, 128, 128))
            
            # Draw contour
            cv2.drawContours(output, [shape['contour']], -1, color, 2)
            
            # Draw label
            if show_info:
                cx, cy = shape['center']
                cv2.putText(output, name, (cx - 30, cy),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return output
    
    def get_shape_statistics(self, shapes):
        """
        Get statistics about detected shapes.
        
        Args:
            shapes: List of shape dictionaries
        
        Returns:
            Dictionary with statistics
        """
        stats = {
            'total': len(shapes),
            'by_type': {},
            'avg_area': 0,
            'largest': None,
            'smallest': None
        }
        
        if not shapes:
            return stats
        
        # Count by type
        for shape in shapes:
            name = shape['name']
            stats['by_type'][name] = stats['by_type'].get(name, 0) + 1
        
        # Calculate average area
        areas = [s['area'] for s in shapes]
        stats['avg_area'] = sum(areas) / len(areas)
        
        # Find largest and smallest
        stats['largest'] = max(shapes, key=lambda s: s['area'])
        stats['smallest'] = min(shapes, key=lambda s: s['area'])
        
        return stats


def create_test_image():
    """Create a test image with various shapes."""
    img = np.ones((500, 700, 3), dtype=np.uint8) * 240
    
    # Triangle
    pts = np.array([[100, 150], [50, 250], [150, 250]], np.int32)
    cv2.fillPoly(img, [pts], (0, 200, 0))
    
    # Square
    cv2.rectangle(img, (200, 150), (300, 250), (200, 0, 0), -1)
    
    # Rectangle
    cv2.rectangle(img, (350, 130), (500, 270), (0, 0, 200), -1)
    
    # Circle
    cv2.circle(img, (600, 200), 70, (200, 200, 0), -1)
    
    # Pentagon
    pts = np.array([
        [100, 350], [50, 400], [75, 460], [125, 460], [150, 400]
    ], np.int32)
    cv2.fillPoly(img, [pts], (200, 0, 200))
    
    # Hexagon
    pts = np.array([
        [250, 330], [220, 380], [250, 430],
        [310, 430], [340, 380], [310, 330]
    ], np.int32)
    cv2.fillPoly(img, [pts], (0, 200, 200))
    
    return img


# Demo
if __name__ == "__main__":
    print("=" * 60)
    print("SHAPE DETECTOR DEMO")
    print("=" * 60)
    
    # Create test image
    test_img = create_test_image()
    
    # Initialize detector
    detector = ShapeDetector()
    
    # Detect shapes
    shapes = detector.detect_shapes(test_img)
    
    # Draw results
    result = detector.draw_shapes(test_img, shapes)
    
    # Get statistics
    stats = detector.get_shape_statistics(shapes)
    
    print(f"\nDetected {stats['total']} shapes:")
    for shape_type, count in stats['by_type'].items():
        print(f"  - {shape_type}: {count}")
    
    print(f"\nAverage area: {stats['avg_area']:.0f} pixels")
    if stats['largest']:
        print(f"Largest: {stats['largest']['name']} ({stats['largest']['area']:.0f} px)")
    if stats['smallest']:
        print(f"Smallest: {stats['smallest']['name']} ({stats['smallest']['area']:.0f} px)")
    
    # Save results
    cv2.imwrite('/tmp/shapes_original.jpg', test_img)
    cv2.imwrite('/tmp/shapes_detected.jpg', result)
    
    print("\nOutput files:")
    print("  - /tmp/shapes_original.jpg")
    print("  - /tmp/shapes_detected.jpg")
    print("\n✓ Shape Detector demo complete!")
