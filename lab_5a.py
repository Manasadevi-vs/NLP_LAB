import re

def count_digits(sentence):
    digits = re.findall(r'\d', sentence)  # find all digits
    return len(digits)

# User input
input_sentence = input("Enter a sentence: ")
print("Number of digits:", count_digits(input_sentence))
