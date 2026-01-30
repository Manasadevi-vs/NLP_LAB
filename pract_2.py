import re

def validate_password(password: str) -> bool:
    """
    Validates if the password is strong.
    Conditions:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    
    # Regex checks
    if not re.search(r'[A-Z]', password):  # Uppercase
        return False
    if not re.search(r'[a-z]', password):  # Lowercase
        return False
    if not re.search(r'[0-9]', password):  # Digit
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):  # Special character
        return False
    
    return True


# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password: ")
    if validate_password(user_password):
        print("✅ Strong password")
    else:
        print("❌ Weak password - must be at least 8 characters with uppercase, lowercase, digit, and special character.")