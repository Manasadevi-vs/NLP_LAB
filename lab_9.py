# Lab 9: Perform POS tagging using NLTK
import nltk
t = input()
print(nltk.pos_tag(nltk.word_tokenize(t)))


# Lab 9 (Additional 1): POS + NP extraction + NER
import nltk
t = input()
tok = nltk.word_tokenize(t); pos = nltk.pos_tag(tok)
print("POS:", pos)
print("NP:", nltk.RegexpParser("NP: {<DT>?<JJ>*<NN>}").parse(pos))
print("NER:", nltk.ne_chunk(pos))


# Lab 9 (Additional 2): Improved noun phrase extraction using chunking
import nltk
t = input()
pos = nltk.pos_tag(nltk.word_tokenize(t))
print(nltk.RegexpParser("NP: {<DT>?<JJ>*<NN.*>}").parse(pos))


# Lab 9 (Additional 3): Multilingual POS tagging using spaCy
import spacy
t = input()
nlp = spacy.load("xx_ent_wiki_sm")
doc = nlp(t)
print([(w.text,w.pos_) for w in doc])
