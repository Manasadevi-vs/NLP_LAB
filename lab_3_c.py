import random

def random_splits(word: str):
    """
    Splits a word into two parts at random positions and prints all splits.
    
    Parameters:
        word (str): The input word.
    """
    positions = list(range(1, len(word)))  # valid split positions
    random.shuffle(positions)  # shuffle to make splits random
    
    for pos in positions:
        left = word[:pos]
        right = word[pos:]
        print((left, right))


# Example usage
if __name__ == "__main__":
    input_word = input("Enter a word: ")
    print(f"Original Word: {input_word}")
    print("Random Splits:")
    random_splits(input_word)