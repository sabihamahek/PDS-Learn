import gensim as gs
import numpy as np

documents=[
"pittsburgh has some excellent new restaurants",
"boston is a city with great cuisine",
"postgresql is a relational database management system"


]
document_word = [doc.split() for doc in documents]
dictionary = gs.corpora.Dictionary(document_word)
corpus = [dictionary.doc2bow(doc) for doc in document_word]
tfidf = gs.models.TfidfModel(corpus)
X_tfidf = gs.matutils.corpus2csc(tfidf[corpus])
print(X_tfidf.todense().T)

M = gs.similarities.MatrixSimilarity(tfidf[corpus])
print(M.get_similarities(tfidf[corpus]))
