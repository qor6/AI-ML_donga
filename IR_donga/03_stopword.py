import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "I loveinformation retrieval course at the University of Southern Maine!"
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
filtered_text = [w for w in word_tokens if not w.lower() in stop_words]
print(word_tokens)
print(filtered_text)
