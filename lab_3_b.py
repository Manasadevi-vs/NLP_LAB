def generate_prefixes_suffixes(word: str):
    """
    Generates all possible prefixes and suffixes of a given word.
    
    Parameters:
        word (str): The input word.
    
    Returns:
        tuple: Two lists - one containing prefixes and the other containing suffixes.
    """
    prefixes = []
    suffixes = []
    
    # Generate prefixes (from 1 to full length)
    for i in range(1, len(word) + 1):
        prefixes.append(word[:i])
    
    # Generate suffixes (from 1 to full length)
    for i in range(len(word)):
        suffixes.append(word[i:])
    
    return prefixes, suffixes


# Example usage
if __name__ == "__main__":
    input_word = input("Enter a word: ")
    prefixes, suffixes = generate_prefixes_suffixes(input_word)
    
    print(f"Original Word: {input_word}")
    print("Prefixes:")
    for p in prefixes:
        print(p)
    
    print("Suffixes:")
    for s in suffixes:
        print(s)