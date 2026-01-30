def split_word_into_pairs(word: str):
    """
    Splits a word into all possible pairs at every position.
    
    Parameters:
        word (str): The input word.
    
    Returns:
        list: A list of tuples where each tuple contains two parts of the split word.
    """
    pairs = []
    # Loop through positions from 1 to len(word)-1
    for i in range(1, len(word)):
        pairs.append((word[:i], word[i:]))
    return pairs


# Example usage
if __name__ == "__main__":
    input_word = input("Enter a word: ")
    result = split_word_into_pairs(input_word)
    
    print(f"Original Word: {input_word}")
    print("Pairs:")
    for pair in result:
        print(pair)