import nltk
nltk.download('punkt')
text = "I love information retrieval course at the University of Southern Maine!"
tokens_words = nltk.word_tokenize(text)
print(tokens_words)
