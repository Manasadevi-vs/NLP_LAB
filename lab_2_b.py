def count_non_alphanumeric(sentence: str) -> int:
    """
    Counts the number of characters in the sentence
    that are not letters (a-z, A-Z) or numbers (0-9).
    """
    count = 0
    for char in sentence:
        if not char.isalnum():  # isalnum() returns True if char is letter or number
            count += 1
    return count

if __name__ == "__main__":
    # Take input from the user
    user_sentence = input("Enter a sentence: ")
    result = count_non_alphanumeric(user_sentence)
    print("Number of non-alphanumeric characters:", result)