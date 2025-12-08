"""
Day 43 - Mini Project 1: Automatic Photo Enhancer
=================================================
Automatically enhance photos using various CV techniques
"""

import cv2
import numpy as np

class PhotoEnhancer:
    """
    Automatic photo enhancement tool using OpenCV.
    Applies various techniques to improve image quality.
    """
    
    def __init__(self):
        """Initialize the photo enhancer."""
        print("Photo Enhancer initialized")
    
    def auto_enhance(self, image):
        """
        Apply automatic enhancements to an image.
        
        Args:
            image: Input BGR image
        
        Returns:
            Enhanced BGR image
        """
        # Convert to LAB for better processing
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Apply CLAHE to L channel (lightness)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l_enhanced = clahe.apply(l)
        
        # Merge channels
        enhanced_lab = cv2.merge([l_enhanced, a, b])
        enhanced = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        
        return enhanced
    
    def denoise(self, image, strength=10):
        """
        Remove noise from image.
        
        Args:
            image: Input BGR image
            strength: Denoising strength (1-20)
        
        Returns:
            Denoised image
        """
        return cv2.fastNlMeansDenoisingColored(image, None, strength, strength, 7, 21)
    
    def sharpen(self, image, amount=1.0):
        """
        Sharpen the image.
        
        Args:
            image: Input BGR image
            amount: Sharpening amount (0.5-2.0)
        
        Returns:
            Sharpened image
        """
        kernel = np.array([[-1, -1, -1],
                          [-1, 9 + amount, -1],
                          [-1, -1, -1]]) / (1 + amount)
        return cv2.filter2D(image, -1, kernel)
    
    def adjust_brightness_contrast(self, image, brightness=0, contrast=1.0):
        """
        Adjust brightness and contrast.
        
        Args:
            image: Input BGR image
            brightness: Brightness adjustment (-100 to 100)
            contrast: Contrast multiplier (0.5 to 2.0)
        
        Returns:
            Adjusted image
        """
        return cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    
    def white_balance(self, image):
        """
        Apply automatic white balance.
        
        Args:
            image: Input BGR image
        
        Returns:
            White balanced image
        """
        result = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        avg_a = np.average(result[:, :, 1])
        avg_b = np.average(result[:, :, 2])
        
        result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
        result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
        
        result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
        return result
    
    def enhance_full(self, image):
        """
        Apply full enhancement pipeline.
        
        Args:
            image: Input BGR image
        
        Returns:
            Fully enhanced image
        """
        # Step 1: Denoise
        result = self.denoise(image, strength=5)
        
        # Step 2: White balance
        result = self.white_balance(result)
        
        # Step 3: Auto enhance (CLAHE)
        result = self.auto_enhance(result)
        
        # Step 4: Slight sharpening
        result = self.sharpen(result, amount=0.5)
        
        return result
    
    def create_before_after(self, original, enhanced):
        """
        Create a before/after comparison image.
        
        Args:
            original: Original image
            enhanced: Enhanced image
        
        Returns:
            Side-by-side comparison
        """
        # Resize both to same height
        h = min(original.shape[0], enhanced.shape[0])
        w_orig = int(original.shape[1] * h / original.shape[0])
        w_enh = int(enhanced.shape[1] * h / enhanced.shape[0])
        
        orig_resized = cv2.resize(original, (w_orig, h))
        enh_resized = cv2.resize(enhanced, (w_enh, h))
        
        # Add labels
        cv2.putText(orig_resized, "Original", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(enh_resized, "Enhanced", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Combine
        divider = np.ones((h, 5, 3), dtype=np.uint8) * 128
        comparison = np.hstack([orig_resized, divider, enh_resized])
        
        return comparison


# Demo
if __name__ == "__main__":
    print("=" * 60)
    print("PHOTO ENHANCER DEMO")
    print("=" * 60)
    
    # Create a sample "low quality" image
    np.random.seed(42)
    sample = np.random.randint(50, 150, (300, 400, 3), dtype=np.uint8)
    # Add some structure
    cv2.rectangle(sample, (100, 80), (300, 220), (180, 150, 120), -1)
    cv2.putText(sample, 'TEST', (130, 165), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (50, 50, 80), 3)
    
    # Initialize enhancer
    enhancer = PhotoEnhancer()
    
    # Apply enhancements
    enhanced = enhancer.enhance_full(sample)
    
    # Create comparison
    comparison = enhancer.create_before_after(sample, enhanced)
    
    # Save results
    cv2.imwrite('/tmp/photo_original.jpg', sample)
    cv2.imwrite('/tmp/photo_enhanced.jpg', enhanced)
    cv2.imwrite('/tmp/photo_comparison.jpg', comparison)
    
    print("\nOutput files:")
    print("  - /tmp/photo_original.jpg")
    print("  - /tmp/photo_enhanced.jpg")
    print("  - /tmp/photo_comparison.jpg")
    print("\n✓ Photo Enhancer demo complete!")
