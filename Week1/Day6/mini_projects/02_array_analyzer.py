"""
Day 6 Mini Project 2: Array Analyzer
====================================
Use two-pointer and sliding window techniques
to analyze arrays and find patterns.

Features:
- Find pairs summing to target
- Find max/min in windows
- Detect patterns
- Analyze subarrays
"""

class ArrayAnalyzer:
    """
    Analyze arrays using two-pointer and sliding window techniques.
    """
    
    def __init__(self, data):
        """Initialize with array data."""
        self.data = data
        self.sorted_data = sorted(data)
    
    def display(self):
        """Display the array."""
        print(f"Array: {self.data}")
        print(f"Length: {len(self.data)}")
        print(f"Sorted: {self.sorted_data}")
    
    # ===== TWO-POINTER METHODS =====
    
    def find_pair_sum(self, target):
        """
        Find all pairs that sum to target.
        Uses two-pointer on sorted array.
        """
        arr = self.sorted_data
        pairs = []
        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                pairs.append((arr[left], arr[right]))
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return pairs
    
    def find_triplet_sum(self, target):
        """
        Find all triplets that sum to target.
        Uses two-pointer after fixing first element.
        """
        arr = self.sorted_data
        triplets = []
        
        for i in range(len(arr) - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            
            left, right = i + 1, len(arr) - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == target:
                    triplets.append((arr[i], arr[left], arr[right]))
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return triplets
    
    def count_elements_less_than(self, threshold):
        """
        Count elements less than threshold using binary search concept.
        """
        count = 0
        for num in self.data:
            if num < threshold:
                count += 1
        return count
    
    # ===== SLIDING WINDOW METHODS =====
    
    def max_sum_window(self, k):
        """
        Find maximum sum of k consecutive elements.
        Fixed-size sliding window.
        """
        if len(self.data) < k:
            return None
        
        window_sum = sum(self.data[:k])
        max_sum = window_sum
        max_start = 0
        
        for i in range(k, len(self.data)):
            window_sum = window_sum - self.data[i - k] + self.data[i]
            if window_sum > max_sum:
                max_sum = window_sum
                max_start = i - k + 1
        
        return {
            'max_sum': max_sum,
            'start_index': max_start,
            'subarray': self.data[max_start:max_start + k]
        }
    
    def min_sum_window(self, k):
        """
        Find minimum sum of k consecutive elements.
        """
        if len(self.data) < k:
            return None
        
        window_sum = sum(self.data[:k])
        min_sum = window_sum
        min_start = 0
        
        for i in range(k, len(self.data)):
            window_sum = window_sum - self.data[i - k] + self.data[i]
            if window_sum < min_sum:
                min_sum = window_sum
                min_start = i - k + 1
        
        return {
            'min_sum': min_sum,
            'start_index': min_start,
            'subarray': self.data[min_start:min_start + k]
        }
    
    def average_window(self, k):
        """
        Calculate average for each window of size k.
        """
        if len(self.data) < k:
            return []
        
        averages = []
        window_sum = sum(self.data[:k])
        averages.append(window_sum / k)
        
        for i in range(k, len(self.data)):
            window_sum = window_sum - self.data[i - k] + self.data[i]
            averages.append(window_sum / k)
        
        return averages
    
    def smallest_subarray_with_sum(self, target):
        """
        Find smallest subarray with sum >= target.
        Variable-size sliding window.
        """
        min_length = float('inf')
        window_sum = 0
        left = 0
        result = None
        
        for right in range(len(self.data)):
            window_sum += self.data[right]
            
            while window_sum >= target:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = {
                        'length': min_length,
                        'start_index': left,
                        'subarray': self.data[left:right + 1],
                        'sum': sum(self.data[left:right + 1])
                    }
                window_sum -= self.data[left]
                left += 1
        
        return result if result else {'length': 0, 'message': 'No valid subarray'}
    
    def longest_subarray_with_max_sum(self, max_sum):
        """
        Find longest subarray with sum <= max_sum.
        Variable-size sliding window.
        """
        max_length = 0
        window_sum = 0
        left = 0
        result = None
        
        for right in range(len(self.data)):
            window_sum += self.data[right]
            
            while window_sum > max_sum and left <= right:
                window_sum -= self.data[left]
                left += 1
            
            if right - left + 1 > max_length:
                max_length = right - left + 1
                result = {
                    'length': max_length,
                    'start_index': left,
                    'subarray': self.data[left:right + 1],
                    'sum': sum(self.data[left:right + 1])
                }
        
        return result
    
    # ===== ANALYSIS METHODS =====
    
    def detect_increasing_sequence(self, min_length=3):
        """
        Find longest increasing consecutive sequence.
        """
        if len(self.data) < min_length:
            return None
        
        max_length = 1
        current_length = 1
        max_start = 0
        current_start = 0
        
        for i in range(1, len(self.data)):
            if self.data[i] > self.data[i - 1]:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
                current_length = 1
                current_start = i
        
        if current_length > max_length:
            max_length = current_length
            max_start = current_start
        
        if max_length >= min_length:
            return {
                'length': max_length,
                'start_index': max_start,
                'sequence': self.data[max_start:max_start + max_length]
            }
        return None
    
    def find_peaks(self):
        """
        Find all local maximum points.
        """
        peaks = []
        for i in range(1, len(self.data) - 1):
            if self.data[i] > self.data[i - 1] and \
               self.data[i] > self.data[i + 1]:
                peaks.append({
                    'index': i,
                    'value': self.data[i]
                })
        return peaks
    
    def find_valleys(self):
        """
        Find all local minimum points.
        """
        valleys = []
        for i in range(1, len(self.data) - 1):
            if self.data[i] < self.data[i - 1] and \
               self.data[i] < self.data[i + 1]:
                valleys.append({
                    'index': i,
                    'value': self.data[i]
                })
        return valleys
    
    def statistics(self):
        """
        Calculate basic statistics.
        """
        if not self.data:
            return {}
        
        return {
            'count': len(self.data),
            'sum': sum(self.data),
            'min': min(self.data),
            'max': max(self.data),
            'average': sum(self.data) / len(self.data),
            'range': max(self.data) - min(self.data)
        }


def main():
    """Demo the array analyzer."""
    print("=" * 50)
    print("📊 ARRAY ANALYZER")
    print("=" * 50)
    
    # Create analyzer
    data = [2, 1, 5, 1, 3, 2, 8, 4, 3, 7, 6, 9, 2, 5]
    analyzer = ArrayAnalyzer(data)
    
    # Display data
    print("\nData Overview:")
    analyzer.display()
    
    # Statistics
    print("\n" + "=" * 50)
    print("📈 STATISTICS")
    print("=" * 50)
    stats = analyzer.statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Two-pointer analysis
    print("\n" + "=" * 50)
    print("👉 TWO-POINTER ANALYSIS")
    print("=" * 50)
    
    target = 9
    pairs = analyzer.find_pair_sum(target)
    print(f"\nPairs summing to {target}: {pairs}")
    
    target = 12
    triplets = analyzer.find_triplet_sum(target)
    print(f"Triplets summing to {target}: {triplets}")
    
    # Sliding window analysis
    print("\n" + "=" * 50)
    print("🪟 SLIDING WINDOW ANALYSIS")
    print("=" * 50)
    
    k = 3
    result = analyzer.max_sum_window(k)
    print(f"\nMax sum window (k={k}):")
    print(f"  Sum: {result['max_sum']}")
    print(f"  Subarray: {result['subarray']}")
    
    result = analyzer.min_sum_window(k)
    print(f"\nMin sum window (k={k}):")
    print(f"  Sum: {result['min_sum']}")
    print(f"  Subarray: {result['subarray']}")
    
    averages = analyzer.average_window(k)
    print(f"\nAverages (k={k}): {[round(a, 2) for a in averages]}")
    
    target = 10
    result = analyzer.smallest_subarray_with_sum(target)
    print(f"\nSmallest subarray with sum >= {target}:")
    print(f"  Length: {result['length']}")
    print(f"  Subarray: {result['subarray']}")
    print(f"  Sum: {result['sum']}")
    
    # Pattern detection
    print("\n" + "=" * 50)
    print("🔍 PATTERN DETECTION")
    print("=" * 50)
    
    result = analyzer.detect_increasing_sequence()
    if result:
        print(f"\nLongest increasing sequence:")
        print(f"  Length: {result['length']}")
        print(f"  Sequence: {result['sequence']}")
    
    peaks = analyzer.find_peaks()
    print(f"\nPeaks: {[(p['index'], p['value']) for p in peaks]}")
    
    valleys = analyzer.find_valleys()
    print(f"Valleys: {[(v['index'], v['value']) for v in valleys]}")
    
    print("\n" + "=" * 50)
    print("✅ Array Analyzer Demo Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
