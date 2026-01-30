import re

def remove_html_tags(text: str) -> str:
    """
    Removes HTML tags from the given text using regex.
    
    Parameters:
        text (str): The input text containing HTML tags.
    
    Returns:
        str: Cleaned text without HTML tags.
    """
    # Regex pattern to match HTML tags
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text


# Example usage
if __name__ == "__main__":
    html_text = input("Enter text with HTML tags: ")
    result = remove_html_tags(html_text)
    print("Cleaned Text:", result)