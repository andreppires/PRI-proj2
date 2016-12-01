from stop_words import get_stop_words
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

#part 1: criar os candidatos: tri-gramas e ignorar stop-words
# get stop words
stop_words = get_stop_words('en')
# fetch test data
test = fetch_20newsgroups(subset='test')
# tri-gramas and no stop-words
vectorizer = TfidfVectorizer(use_idf=False, ngram_range=(1, 3), stop_words=stop_words)
# apply tf
trainvec = vectorizer.fit_transform(test.data)
feature_names = vectorizer.get_feature_names()
print feature_names

#part 2: fazer o ranking de acordo com a formula. 50 iteracoes max
#part 3: escolher os 5 melhores
