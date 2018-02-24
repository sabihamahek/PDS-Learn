documents=["the goal of this lecture is to explain the basics of free text processing",
"the bag of words model is one such approach",
"text processing via bag of words"
]
document_word = [doc.split() for doc in documents]
vocab = sorted(set(sum(document_word,[])))
vocab_dict = {k:i for i,k in enumerate(vocab)}
print(vocab,"\n")
print(vocab_dict,"\n")

import numpy as np
X_tf = np.zeros((len(documents),len(vocab)),dtype=int)
for i,doc in enumerate(document_word):
    for word in doc:
        X_tf[i,vocab_dict[word]]+=1
print(X_tf)

idf = np.log(X_tf.shape[0]/X_tf.astype(bool).sum(axis=0))
print(idf)

X_tfidf = X_tf*idf
print(X_tfidf)
