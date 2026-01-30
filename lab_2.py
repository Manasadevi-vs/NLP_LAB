import re

def clean_sentence(sentence: str) -> str:
    """
    Removes non-alphanumeric characters from the start and end of a sentence.
    Keeps the middle content intact.
    """
    pattern = r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'
    cleaned = re.sub(pattern, '', sentence)
    return cleaned

if __name__ == "__main__":
    # Take input from the user
    user_sentence = input("Enter a sentence: ")
    result = clean_sentence(user_sentence)
    print("Cleaned sentence:", result)