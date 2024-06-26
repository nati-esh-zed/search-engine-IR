
# from libs.porter_stemmer import PorterStemmer
from nltk.stem import PorterStemmer

irrelevant_symbols = set('\r \n \t . ? ! : ;'.split(' '))
stop_list = set('for a of the and to in'.split(' '))
rawText = 'A beautifully made tokenizer. Artificial intelligence. Apply cream while sitting.'


ps = PorterStemmer()
# filter out punctuation marks and other irrelevant symbols
words = ''.join([letter for letter in rawText if letter not in irrelevant_symbols])
# lower case, stem, and tokenize words
tokens = [word for word in ps.stem(words).split(' ') if word not in stop_list]

print(rawText)
print(words)
print(tokens)

