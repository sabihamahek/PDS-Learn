import numpy as np
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
