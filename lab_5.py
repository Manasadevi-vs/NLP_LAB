import re

def greedy_tokenizer_remove_digits(sentence):
    tokens = sentence.split()
    tokens = [t for t in tokens if not re.search(r'\d', t)]
    return ' '.join(tokens)

s = input("Enter a sentence: ")
print("Original:", s)
print("Without digits:", greedy_tokenizer_remove_digits(s))