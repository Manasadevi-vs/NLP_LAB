# User input
sentence = input("Enter a sentence: ").lower().split()[::-1]  # reversed words
n = int(input("Enter n (e.g., 2 for bigram): "))

# Generate reverse n-grams
rev_ngrams = [tuple(sentence[i:i+n]) for i in range(len(sentence)-n+1)]

# Print results
for gram in rev_ngrams:
    print(gram)