documents=["the goal of this lecture is to explain the basics of free text processing",
"the bag of words model is one such approach",
"text processing via bag of words"
]
document_word = [doc.split() for doc in documents]
vocab = sorted(set(sum(document_word,[])))
vocab_dict = {k:i for i,k in enumerate(vocab)}
print(vocab,"\n")
print(vocab_dict,"\n")
