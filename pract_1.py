import re

def extract_emails(paragraph: str):
    """
    Extracts all valid email IDs from a given paragraph.
    
    Parameters:
        paragraph (str): The input text containing possible email addresses.
    
    Returns:
        list: A list of valid email IDs found in the paragraph.
    """
    # Regex pattern for valid email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all matches
    emails = re.findall(pattern, paragraph)
    
    return emails


# Example usage
if __name__ == "__main__":
    text = input("Enter a paragraph: ")
    result = extract_emails(text)
    
    print("Extracted Email IDs:")
    for email in result:
        print(email)