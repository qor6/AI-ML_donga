import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()
text = "I loveinformation retrieval course at the University of Southern Maine!"
words = word_tokenize(text)
for w in words:
  print(w, " : ", lemmatizer.lemmatize(w))
