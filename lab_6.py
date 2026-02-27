import re

text = input("Enter text: ")
clean_text = re.sub(r"#\w+", "", text)
clean_text = re.sub(r"[^\w\s]", "", clean_text)
clean_text = re.sub(r"\s+", " ", clean_text).strip()
print(clean_text)