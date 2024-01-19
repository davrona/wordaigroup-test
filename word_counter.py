import re
from collections import Counter

def word_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove non-alphanumeric characters and split into words
    words = re.findall(r'\b\w+\b', content.lower())

    # Calculate total number of words
    total_words = len(words)

    # Calculate the ten most common words
    common_words = Counter(words).most_common(10)

    return total_words, common_words

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    total_words, common_words = word_counter(file_path)

    print(f"Total number of words: {total_words}")
    print("Ten most common words and occurrences:")
    for word, count in common_words:
        print(f"{word}: {count}")