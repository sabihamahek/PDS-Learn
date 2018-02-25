import gensim as gs
import numpy as np

model = gs.models.KeyedVectors.load_word2vec_format('deps.words.bin',binary=True)


# x = model.wv["pittsburgh"][:10]
# print(x)
# import numpy as np
documents=[
"pittsburgh has some excellent new restaurants",
"boston is a city with great cuisine",
"postgresql is a relational database management system"


]
document_word = [doc.split() for doc in documents]
vocab = sorted(set(sum(document_word,[])))
vocab_dict = {k:i for i,k in enumerate(vocab)}
print(vocab_dict,"\n")

e_pittsburgh = np.zeros(len(vocab))
e_pittsburgh[vocab_dict["pittsburgh"]] = 1.0
print(e_pittsburgh)
x_w2v = np.array([sum(model.wv[w.lower()] for w in doc )for doc in document_word])
x_w2v = x_w2v/np.linalg.norm(x_w2v,axis=1)[:,None]
M = x_w2v @ x_w2v.T
print(M)
