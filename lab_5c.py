import re

def greedy_tokenizer(sentence):
    # Patterns for email and date
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    date_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'
    
    # Split sentence into tokens while keeping emails and dates intact
    tokens = []
    pos = 0
    while pos < len(sentence):
        email_match = re.match(email_pattern, sentence[pos:])
        date_match = re.match(date_pattern, sentence[pos:])
        
        if email_match:
            tokens.append(email_match.group())
            pos += len(email_match.group())
        elif date_match:
            tokens.append(date_match.group())
            pos += len(date_match.group())
        else:
            tokens.append(sentence[pos])
            pos += 1
    
    return tokens

# User input
input_sentence = input("Enter a sentence: ")
print("Tokens:", greedy_tokenizer(input_sentence))