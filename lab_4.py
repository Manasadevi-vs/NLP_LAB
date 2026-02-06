from collections import Counter
from nltk import ngrams

# Input sentence
sentence = "Write a program to find out the frequencies of distinct words given a sentence using n-grams"

# Tokenize
words = sentence.lower().split()

# Choose n (e.g., 2 for bigrams, 3 for trigrams)
n = 2
ngram_list = list(ngrams(words, n))

# Count frequencies
freq = Counter(ngram_list)

# Print results
for gram, count in freq.items():
    print(gram, ":", count)