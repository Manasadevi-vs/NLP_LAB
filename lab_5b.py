import re

def extract_digits(sentence):
    digits = re.findall(r'\d', sentence)  # find all digits
    return digits

# User input
input_sentence = input("Enter a sentence: ")
print("Digits found:", extract_digits(input_sentence))