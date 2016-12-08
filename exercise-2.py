from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
import os

# fetching train data/collenction from disk
# using wiki20 collection from https://github.com/zelandiya/keyword-extraction-datasets
train = []
for file in os.listdir("wiki20/documents"):
    if file.endswith(".txt"):
        with open("wiki20/documents/" + file, 'r') as myfile:
            train.append(myfile.read().replace('\n', ''))
            
# get stop words
stop_words = get_stop_words('en')

# fetch words
vectorizer = TfidfVectorizer(use_idf=False, ngram_range=(1, 3), stop_words=stop_words)

# learn idf
trainvec = vectorizer.fit_transform(train)