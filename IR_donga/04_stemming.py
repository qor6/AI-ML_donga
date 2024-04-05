from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
text =c
words = word_tokenize(text)
for w in words:
  print(w, " : ", ps.stem(w))
