#Q7 Stemming & Lemmatization
from nltk.stem import PorterStemmer, WordNetLemmatizer
words = input().split()
print([PorterStemmer().stem(w) for w in words], [WordNetLemmatizer().lemmatize(w) for w in words])

#Q7a Custom Tokenizer
import re
text = input()
print(re.sub(r"(http\S+|@\w+|#\w+|[^\w\s])","",text).split())

#Q7b NER and Normalization
import nltk,re
text = input()
print(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))))
print(re.sub(r'\d+',"NUM",text))
