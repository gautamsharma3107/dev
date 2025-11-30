"""
Day 4 - Text File Operations
============================
Learn: Advanced text file handling techniques

Key Concepts:
- Count lines, words, characters
- Search and replace
- Filter and process lines
- Handle large files efficiently
"""

import os

# ========== SETUP: CREATE SAMPLE FILE ==========
print("=" * 50)
print("SETUP: Creating Sample Files")
print("=" * 50)

poem = """The Road Not Taken
by Robert Frost

Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same."""

with open("poem.txt", "w") as file:
    file.write(poem)
print("✅ Created 'poem.txt'")

# ========== COUNTING STATS ==========
print("\n" + "=" * 50)
print("COUNTING LINES, WORDS, CHARACTERS")
print("=" * 50)

with open("poem.txt", "r") as file:
    content = file.read()
    
    lines = content.split('\n')
    words = content.split()
    chars = len(content)
    chars_no_space = len(content.replace(' ', '').replace('\n', ''))
    
print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
print(f"Characters (with spaces): {chars}")
print(f"Characters (no spaces): {chars_no_space}")

# ========== SEARCH IN FILE ==========
print("\n" + "=" * 50)
print("SEARCHING IN FILE")
print("=" * 50)

search_term = "road"
print(f"Lines containing '{search_term}':")

with open("poem.txt", "r") as file:
    for num, line in enumerate(file, 1):
        if search_term.lower() in line.lower():
            print(f"  Line {num}: {line.strip()}")

# ========== SEARCH AND REPLACE ==========
print("\n" + "=" * 50)
print("SEARCH AND REPLACE")
print("=" * 50)

# Read original
with open("poem.txt", "r") as file:
    content = file.read()

# Replace
new_content = content.replace("road", "path")

# Write to new file
with open("poem_modified.txt", "w") as file:
    file.write(new_content)

print("✅ Replaced 'road' with 'path'")
print("\nFirst lines comparison:")
print(f"  Original: {content.split(chr(10))[0]}")
print(f"  Modified: {new_content.split(chr(10))[0]}")

# ========== FILTER LINES ==========
print("\n" + "=" * 50)
print("FILTERING LINES")
print("=" * 50)

# Create data file
data = """John,25,Engineer
Jane,30,Doctor
Bob,22,Student
Alice,28,Designer
Charlie,35,Manager"""

with open("people.txt", "w") as file:
    file.write(data)

print("People over 25:")
with open("people.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        name, age, job = parts[0], int(parts[1]), parts[2]
        if age > 25:
            print(f"  {name} ({age}) - {job}")

# ========== MERGE FILES ==========
print("\n" + "=" * 50)
print("MERGING FILES")
print("=" * 50)

with open("file1.txt", "w") as f:
    f.write("Content from file 1\nLine 2 of file 1\n")

with open("file2.txt", "w") as f:
    f.write("Content from file 2\nLine 2 of file 2\n")

files_to_merge = ["file1.txt", "file2.txt"]

with open("merged.txt", "w") as outfile:
    for filename in files_to_merge:
        outfile.write(f"--- {filename} ---\n")
        with open(filename, "r") as infile:
            outfile.write(infile.read())
        outfile.write("\n")

print("✅ Created 'merged.txt'")
with open("merged.txt", "r") as f:
    print(f.read())

# ========== LARGE FILES ==========
print("=" * 50)
print("HANDLING LARGE FILES")
print("=" * 50)

# Create large file
with open("large.txt", "w") as f:
    for i in range(1000):
        f.write(f"Line number {i+1}\n")
print("✅ Created 'large.txt' with 1000 lines")

# Method 1: Line by line (memory efficient)
print("\nMethod 1: Line by line")
count = 0
with open("large.txt", "r") as file:
    for line in file:
        count += 1
print(f"  Counted {count} lines")

# Method 2: Read in chunks
print("\nMethod 2: Read in chunks")
chunk_size = 1024
chunks = 0
with open("large.txt", "r") as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        chunks += 1
print(f"  Read {chunks} chunks of {chunk_size} bytes")

# ========== SPECIFIC LINES ==========
print("\n" + "=" * 50)
print("READ SPECIFIC LINES")
print("=" * 50)

import linecache

line5 = linecache.getline("large.txt", 5)
line100 = linecache.getline("large.txt", 100)

print(f"Line 5: {line5.strip()}")
print(f"Line 100: {line100.strip()}")

linecache.clearcache()

# ========== FILE ENCODING ==========
print("\n" + "=" * 50)
print("FILE ENCODING")
print("=" * 50)

# Unicode text
unicode_text = "Hello! Bonjour! 你好! 🐍 Python"

with open("unicode.txt", "w", encoding="utf-8") as file:
    file.write(unicode_text)

with open("unicode.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"Unicode content: {content}")

# ========== PRACTICAL: TEXT ANALYZER ==========
print("\n" + "=" * 50)
print("PRACTICAL: Text Analyzer Function")
print("=" * 50)

def analyze_file(filename):
    """Analyze text file and return stats"""
    stats = {
        "lines": 0,
        "words": 0,
        "chars": 0,
        "empty_lines": 0,
        "word_freq": {}
    }
    
    with open(filename, "r") as file:
        for line in file:
            stats["lines"] += 1
            stats["chars"] += len(line)
            
            if line.strip() == "":
                stats["empty_lines"] += 1
                continue
            
            for word in line.split():
                word = word.lower().strip(".,!?;:")
                stats["words"] += 1
                stats["word_freq"][word] = stats["word_freq"].get(word, 0) + 1
    
    return stats

result = analyze_file("poem.txt")
print(f"File: poem.txt")
print(f"  Lines: {result['lines']}")
print(f"  Empty lines: {result['empty_lines']}")
print(f"  Words: {result['words']}")
print(f"  Characters: {result['chars']}")

# Top 5 words
top_words = sorted(result["word_freq"].items(), key=lambda x: x[1], reverse=True)[:5]
print(f"\n  Top 5 words:")
for word, count in top_words:
    print(f"    '{word}': {count}")

# Cleanup
for f in ["poem.txt", "poem_modified.txt", "people.txt", "file1.txt", 
          "file2.txt", "merged.txt", "large.txt", "unicode.txt"]:
    if os.path.exists(f):
        os.remove(f)
print("\n✅ Cleaned up files")

print("\n" + "=" * 50)
print("✅ Text Files - Complete!")
print("=" * 50)
