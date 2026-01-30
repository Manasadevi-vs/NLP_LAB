import re

def replace_non_alphanumeric(sentence: str, replacement: str) -> str:
    """
    Replaces all characters in the sentence that are not letters or numbers
    with the specified replacement character.
    """
    # Regex pattern: match any character that is NOT a-z, A-Z, or 0-9
    pattern = r'[^a-zA-Z0-9]'
    
    # Replace all matches with the replacement character
    replaced = re.sub(pattern, replacement, sentence)
    
    return replaced

if __name__ == "__main__":
    # Take input from the user
    user_sentence = input("Enter a sentence: ")
    replacement_char = input("Enter the replacement character: ")
    
    # Ensure only one character is used for replacement
    if len(replacement_char) != 1:
        print("Please enter exactly one character for replacement.")
    else:
        result = replace_non_alphanumeric(user_sentence, replacement_char)
        print("Modified sentence:", result)