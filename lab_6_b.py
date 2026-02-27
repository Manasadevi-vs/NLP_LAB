import re

text = input("Enter text: ")
normalized = re.sub(r"\s+", " ", text).strip().lower()
print(normalized)