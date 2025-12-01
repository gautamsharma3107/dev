"""
MINI PROJECT 3: Word Frequency Analyzer
========================================
Build a text analyzer that uses hash maps for fast lookups

Features:
1. Count word frequencies
2. Find most common words
3. Search for specific words
4. Compare two texts for similarity
5. Build word index (which lines contain which words)
"""

print("=" * 60)
print("MINI PROJECT: WORD FREQUENCY ANALYZER")
print("=" * 60)

from collections import Counter, defaultdict
import re

# ============================================================
# TEXT ANALYZER CLASS
# ============================================================

class TextAnalyzer:
    """
    Analyze text using hash maps for efficient operations
    """
    
    def __init__(self, text=""):
        """Initialize with optional text"""
        self.text = text
        self.words = []
        self.word_freq = {}
        self.word_index = defaultdict(list)  # word -> list of line numbers
        
        if text:
            self.analyze(text)
    
    def _tokenize(self, text):
        """
        Convert text to lowercase words
        Remove punctuation
        """
        # Convert to lowercase and extract words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return words
    
    def analyze(self, text):
        """
        Analyze text and build data structures
        - word list
        - frequency map
        - line index
        """
        self.text = text
        self.words = self._tokenize(text)
        
        # Build frequency map - O(n)
        self.word_freq = {}
        for word in self.words:
            self.word_freq[word] = self.word_freq.get(word, 0) + 1
        
        # Build line index - O(n)
        self.word_index = defaultdict(list)
        for line_num, line in enumerate(text.split('\n'), 1):
            line_words = self._tokenize(line)
            for word in set(line_words):  # Use set to avoid duplicates per line
                self.word_index[word].append(line_num)
    
    def get_frequency(self, word):
        """Get frequency of a specific word - O(1)"""
        return self.word_freq.get(word.lower(), 0)
    
    def get_top_words(self, n=10):
        """Get n most common words - O(n log n)"""
        sorted_words = sorted(
            self.word_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_words[:n]
    
    def search_word(self, word):
        """
        Search for word and return:
        - frequency
        - line numbers where it appears
        O(1) for lookup!
        """
        word = word.lower()
        return {
            'word': word,
            'frequency': self.word_freq.get(word, 0),
            'lines': self.word_index.get(word, [])
        }
    
    def get_unique_words(self):
        """Get all unique words - O(1)"""
        return list(self.word_freq.keys())
    
    def get_word_count(self):
        """Get total word count - O(1)"""
        return len(self.words)
    
    def get_unique_count(self):
        """Get unique word count - O(1)"""
        return len(self.word_freq)
    
    def get_statistics(self):
        """Get text statistics"""
        return {
            'total_words': self.get_word_count(),
            'unique_words': self.get_unique_count(),
            'avg_word_length': sum(len(w) for w in self.words) / max(len(self.words), 1),
            'line_count': len(self.text.split('\n'))
        }


# ============================================================
# TEXT COMPARISON
# ============================================================

def compare_texts(text1, text2):
    """
    Compare two texts for similarity using hash sets
    
    Returns:
    - Common words
    - Words only in text1
    - Words only in text2
    - Jaccard similarity score
    """
    analyzer1 = TextAnalyzer(text1)
    analyzer2 = TextAnalyzer(text2)
    
    set1 = set(analyzer1.word_freq.keys())
    set2 = set(analyzer2.word_freq.keys())
    
    common = set1 & set2
    only_in_1 = set1 - set2
    only_in_2 = set2 - set1
    
    # Jaccard similarity: |A ∩ B| / |A ∪ B|
    union = set1 | set2
    similarity = len(common) / len(union) if union else 0
    
    return {
        'common_words': common,
        'only_in_text1': only_in_1,
        'only_in_text2': only_in_2,
        'similarity': similarity
    }


# ============================================================
# DEMO
# ============================================================

sample_text = """
Python is a programming language.
Python is easy to learn.
Python is used for web development.
Machine learning uses Python extensively.
Data science and Python go hand in hand.
Learning Python opens many opportunities.
"""

print("\n--- Analyzing Sample Text ---")
print(sample_text)

analyzer = TextAnalyzer(sample_text)

# Statistics
print("\n📊 Statistics:")
stats = analyzer.get_statistics()
for key, value in stats.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# Top words
print("\n📈 Top 5 Words:")
for word, freq in analyzer.get_top_words(5):
    print(f"  '{word}': {freq} times")

# Search specific word
print("\n🔍 Search Results for 'python':")
result = analyzer.search_word('python')
print(f"  Frequency: {result['frequency']}")
print(f"  Found on lines: {result['lines']}")

# Search another word
print("\n🔍 Search Results for 'learning':")
result = analyzer.search_word('learning')
print(f"  Frequency: {result['frequency']}")
print(f"  Found on lines: {result['lines']}")

# ============================================================
# COMPARE TWO TEXTS
# ============================================================

text_a = "Python is great for data science and machine learning"
text_b = "Java is popular for enterprise applications and Android"

print("\n" + "=" * 60)
print("TEXT COMPARISON")
print("=" * 60)
print(f"\nText A: '{text_a}'")
print(f"Text B: '{text_b}'")

comparison = compare_texts(text_a, text_b)
print(f"\n📊 Comparison Results:")
print(f"  Common words: {comparison['common_words']}")
print(f"  Only in Text A: {comparison['only_in_text1']}")
print(f"  Only in Text B: {comparison['only_in_text2']}")
print(f"  Similarity: {comparison['similarity']:.2%}")


# ============================================================
# YOUR CHALLENGES
# ============================================================

print("""

=== YOUR CHALLENGES ===

1. Add a method to find words that appear exactly N times

2. Add a method to find the longest/shortest words

3. Add support for stop words (common words like "the", "is", "a")
   - Filter them out from analysis
   
4. Add a method to find similar words (words that differ by 1 letter)

5. Build an inverted index:
   - For a collection of documents
   - Map: word -> list of document IDs
   - This is how search engines work!

6. Add TF-IDF scoring:
   - Term Frequency: How often a word appears in a document
   - Inverse Document Frequency: Rare words are more important
""")

# ============================================================
# INTERACTIVE MODE
# ============================================================

def run_analyzer():
    """Run interactive text analyzer"""
    print("\n" + "=" * 60)
    print("INTERACTIVE TEXT ANALYZER")
    print("Commands: analyze, search, top, stats, compare, quit")
    print("=" * 60)
    
    analyzer = None
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == 'quit':
            print("Goodbye!")
            break
        
        elif cmd == 'analyze':
            print("Enter text (end with empty line):")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            text = '\n'.join(lines)
            analyzer = TextAnalyzer(text)
            print(f"✅ Analyzed {analyzer.get_word_count()} words")
        
        elif cmd == 'search' and analyzer:
            word = input("Search word: ")
            result = analyzer.search_word(word)
            print(f"'{word}': {result['frequency']} times, lines: {result['lines']}")
        
        elif cmd == 'top' and analyzer:
            n = int(input("How many? "))
            for word, freq in analyzer.get_top_words(n):
                print(f"  {word}: {freq}")
        
        elif cmd == 'stats' and analyzer:
            for k, v in analyzer.get_statistics().items():
                print(f"  {k}: {v}")
        
        else:
            print("Unknown command or no text analyzed yet")


# Uncomment to run interactive mode:
# run_analyzer()

print("\n" + "=" * 60)
print("Mini Project Complete! Try the challenges above.")
print("=" * 60)
