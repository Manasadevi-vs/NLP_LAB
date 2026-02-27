import re

text = input("Enter text: ")

date_patterns = [
    r"\b\d{2}/\d{2}/\d{4}\b",          # DD/MM/YYYY
    r"\b\d{2}-\d{2}-\d{4}\b",          # MM-DD-YYYY
    r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b"  # Month Day, Year
]

dates = []
for pattern in date_patterns:
    dates.extend(re.findall(pattern, text))

print(dates)