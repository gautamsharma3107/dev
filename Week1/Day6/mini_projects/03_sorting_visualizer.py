"""
Day 6 Mini Project 3: Sorting Visualizer
========================================
Visualize how merge sort and quick sort work
step by step.

Features:
- Step-by-step merge sort visualization
- Step-by-step quick sort visualization
- Compare both algorithms
- Performance analysis
"""

import time
import random

class SortingVisualizer:
    """
    Visualize sorting algorithms step by step.
    """
    
    def __init__(self, arr):
        """Initialize with array to sort."""
        self.original = arr.copy()
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    def reset(self):
        """Reset counters."""
        self.steps = []
        self.comparisons = 0
        self.swaps = 0
    
    @staticmethod
    def visualize_array(arr, highlight=None, pivot=None, left=None, right=None):
        """
        Create visual representation of array.
        """
        result = "["
        for i, val in enumerate(arr):
            if i == pivot:
                result += f" 🎯{val} "
            elif highlight and i in highlight:
                result += f" ⭐{val} "
            elif left is not None and right is not None and left <= i <= right:
                result += f" [{val}]"
            else:
                result += f" {val} "
        result += "]"
        return result
    
    # ===== MERGE SORT =====
    
    def merge_sort_visual(self, arr=None, depth=0, show_steps=True):
        """
        Visualize merge sort step by step.
        """
        if arr is None:
            arr = self.original.copy()
            self.reset()
        
        indent = "  " * depth
        
        if show_steps:
            print(f"{indent}📥 Input: {arr}")
        
        if len(arr) <= 1:
            if show_steps:
                print(f"{indent}📤 Return: {arr} (base case)")
            return arr
        
        mid = len(arr) // 2
        if show_steps:
            print(f"{indent}✂️  Split at index {mid}")
        
        left = self.merge_sort_visual(arr[:mid], depth + 1, show_steps)
        right = self.merge_sort_visual(arr[mid:], depth + 1, show_steps)
        
        merged = self._merge_visual(left, right, depth, show_steps)
        
        if show_steps:
            print(f"{indent}✅ Merged: {merged}")
        
        return merged
    
    def _merge_visual(self, left, right, depth=0, show_steps=True):
        """
        Merge two sorted arrays with visualization.
        """
        indent = "  " * depth
        result = []
        i = j = 0
        
        if show_steps:
            print(f"{indent}🔀 Merging: {left} + {right}")
        
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                if show_steps:
                    print(f"{indent}   Compare {left[i]} <= {right[j]}: take {left[i]}")
                i += 1
            else:
                result.append(right[j])
                if show_steps:
                    print(f"{indent}   Compare {left[i]} > {right[j]}: take {right[j]}")
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    # ===== QUICK SORT =====
    
    def quick_sort_visual(self, arr=None, depth=0, show_steps=True):
        """
        Visualize quick sort step by step.
        """
        if arr is None:
            arr = self.original.copy()
            self.reset()
        
        indent = "  " * depth
        
        if show_steps:
            print(f"{indent}📥 Input: {arr}")
        
        if len(arr) <= 1:
            if show_steps:
                print(f"{indent}📤 Return: {arr} (base case)")
            return arr
        
        # Choose pivot (middle element)
        pivot_idx = len(arr) // 2
        pivot = arr[pivot_idx]
        
        if show_steps:
            print(f"{indent}🎯 Pivot: {pivot} (index {pivot_idx})")
        
        # Partition
        left = []
        middle = []
        right = []
        
        for val in arr:
            # Count comparisons only for actual comparisons (excluding pivot itself)
            if val != pivot:
                self.comparisons += 1
            if val < pivot:
                left.append(val)
            elif val == pivot:
                middle.append(val)
            else:
                right.append(val)
        
        if show_steps:
            print(f"{indent}📊 Partition:")
            print(f"{indent}   Left (<{pivot}): {left}")
            print(f"{indent}   Middle (={pivot}): {middle}")
            print(f"{indent}   Right (>{pivot}): {right}")
        
        sorted_left = self.quick_sort_visual(left, depth + 1, show_steps) if left else []
        sorted_right = self.quick_sort_visual(right, depth + 1, show_steps) if right else []
        
        result = sorted_left + middle + sorted_right
        
        if show_steps:
            print(f"{indent}✅ Combined: {result}")
        
        return result
    
    def quick_sort_inplace_visual(self, arr=None, low=0, high=None, depth=0, show_steps=True):
        """
        Visualize in-place quick sort.
        """
        if arr is None:
            arr = self.original.copy()
            high = len(arr) - 1
            self.reset()
        
        indent = "  " * depth
        
        if low < high:
            if show_steps:
                print(f"\n{indent}📥 Sorting indices [{low}:{high}]")
                print(f"{indent}   Array: {self.visualize_array(arr, left=low, right=high)}")
            
            # Partition
            pivot_idx = self._partition_visual(arr, low, high, depth, show_steps)
            
            if show_steps:
                print(f"{indent}   After partition: {self.visualize_array(arr, pivot=pivot_idx)}")
            
            # Recursively sort
            self.quick_sort_inplace_visual(arr, low, pivot_idx - 1, depth + 1, show_steps)
            self.quick_sort_inplace_visual(arr, pivot_idx + 1, high, depth + 1, show_steps)
        
        return arr
    
    def _partition_visual(self, arr, low, high, depth=0, show_steps=True):
        """
        Partition with visualization.
        """
        indent = "  " * depth
        pivot = arr[high]
        
        if show_steps:
            print(f"{indent}🎯 Pivot: {pivot} (at index {high})")
        
        i = low - 1
        
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    # Save values before swap for correct message
                    val_i, val_j = arr[i], arr[j]
                    arr[i], arr[j] = arr[j], arr[i]
                    self.swaps += 1
                    if show_steps:
                        print(f"{indent}   Swap arr[{i}]={val_i} with arr[{j}]={val_j}")
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        
        if show_steps:
            print(f"{indent}   Place pivot at index {i + 1}")
        
        return i + 1
    
    # ===== COMPARISON =====
    
    def compare_algorithms(self, show_steps=False):
        """
        Compare merge sort and quick sort.
        """
        print("\n" + "=" * 60)
        print("📊 ALGORITHM COMPARISON")
        print("=" * 60)
        print(f"Array: {self.original}")
        print(f"Length: {len(self.original)}")
        print()
        
        # Merge Sort
        self.reset()
        start = time.time()
        result_merge = self.merge_sort_visual(show_steps=show_steps)
        merge_time = time.time() - start
        merge_comparisons = self.comparisons
        
        # Quick Sort
        self.reset()
        start = time.time()
        result_quick = self.quick_sort_visual(show_steps=show_steps)
        quick_time = time.time() - start
        quick_comparisons = self.comparisons
        
        print("\n" + "-" * 60)
        print("Results:")
        print("-" * 60)
        print(f"{'Metric':<20} {'Merge Sort':<20} {'Quick Sort':<20}")
        print("-" * 60)
        print(f"{'Time (ms)':<20} {merge_time*1000:.4f}{'':<13} {quick_time*1000:.4f}")
        print(f"{'Comparisons':<20} {merge_comparisons:<20} {quick_comparisons:<20}")
        print(f"{'Result':<20} {result_merge == result_quick}")
        print("-" * 60)
        
        return {
            'merge_sort': {
                'time': merge_time,
                'comparisons': merge_comparisons,
                'result': result_merge
            },
            'quick_sort': {
                'time': quick_time,
                'comparisons': quick_comparisons,
                'result': result_quick
            }
        }


def main():
    """Demo the sorting visualizer."""
    print("=" * 60)
    print("🔄 SORTING VISUALIZER")
    print("=" * 60)
    
    # Small array for detailed visualization
    small_arr = [38, 27, 43, 3, 9, 82, 10]
    
    print("\n" + "=" * 60)
    print("MERGE SORT VISUALIZATION")
    print("=" * 60)
    print(f"\nOriginal array: {small_arr}")
    print("-" * 60)
    
    visualizer = SortingVisualizer(small_arr)
    sorted_arr = visualizer.merge_sort_visual()
    
    print("-" * 60)
    print(f"Sorted array: {sorted_arr}")
    print(f"Comparisons: {visualizer.comparisons}")
    
    print("\n" + "=" * 60)
    print("QUICK SORT VISUALIZATION")
    print("=" * 60)
    print(f"\nOriginal array: {small_arr}")
    print("-" * 60)
    
    visualizer = SortingVisualizer(small_arr)
    sorted_arr = visualizer.quick_sort_visual()
    
    print("-" * 60)
    print(f"Sorted array: {sorted_arr}")
    print(f"Comparisons: {visualizer.comparisons}")
    
    # Performance comparison with larger array
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    test_sizes = [10, 50, 100]
    
    for size in test_sizes:
        random_arr = [random.randint(1, 1000) for _ in range(size)]
        visualizer = SortingVisualizer(random_arr)
        
        print(f"\n--- Array size: {size} ---")
        visualizer.compare_algorithms(show_steps=False)
    
    print("\n" + "=" * 60)
    print("✅ Sorting Visualizer Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
