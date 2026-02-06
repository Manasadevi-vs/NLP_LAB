from nltk import ngrams

sentence = "Generate n-grams in reverse order starting from the end"
words = sentence.lower().split()[::-1]  # reverse words

n = 2  # bigrams
rev_ngrams = list(ngrams(words, n))

for gram in rev_ngrams:
    print(gram)