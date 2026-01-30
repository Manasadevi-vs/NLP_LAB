from collections import Counter
import re

def process_document(text: str):
    """
    Removes repeated words and counts occurrences.
    
    Parameters:
        text (str): The input document or paragraph.
    
    Returns:
        tuple: (unique_words, word_counts)
            - unique_words: list of words without repetition (order preserved)
            - word_counts: dictionary with word frequencies
    """
    # Normalize text: lowercase and remove punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count occurrences
    word_counts = Counter(words)
    
    # Remove duplicates while preserving order
    unique_words = []
    seen = set()
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    return unique_words, word_counts


# Example usage
if __name__ == "__main__":
    document = input("Enter your document text: ")
    unique_words, word_counts = process_document(document)
    
    print("\nUnique Words (no repetition):")
    print(unique_words)
    
    print("\nWord Counts:")
    for word, count in word_counts.items():
        if count > 1:
            print(f"{word}: {count} times")