# Lab 10: Implement text classification using HMM
from hmmlearn import hmm
import numpy as np
docs = input().split(",")  # enter sentences separated by comma
X = np.array([[len(w)] for d in docs for w in d.split()])
model = hmm.GaussianHMM(n_components=2).fit(X)
print("Score:", model.score(X))


# Lab 10 (Additional 1): Cross-domain classification using HMM
from hmmlearn import hmm
import numpy as np
train = input().split()   # domain 1
test = input().split()    # domain 2
X = np.array([[len(w)] for w in train])
model = hmm.GaussianHMM(n_components=2).fit(X)
print("Test Score:", model.score(np.array([[len(w)] for w in test])))


# Lab 10 (Additional 2): Hybrid HMM + Naive Bayes classification
from hmmlearn import hmm
from sklearn.naive_bayes import GaussianNB
import numpy as np
text = input().split()
X = np.array([[len(w)] for w in text])
h = hmm.GaussianHMM(n_components=2).fit(X)
features = h.predict(X).reshape(-1,1)
print(GaussianNB().fit(features, [0]*len(features)).predict(features))
