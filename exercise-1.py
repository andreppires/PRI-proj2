from stop_words import get_stop_words
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import operator

#part 1: criar os candidatos: tri-gramas e ignorar stop-words
# get stop words
stop_words = get_stop_words('en')
# fetch test data
test = fetch_20newsgroups(subset='test')
# tri-gramas and no stop-words
vectorizer = TfidfVectorizer(use_idf=False, ngram_range=(1, 3)
, stop_words=stop_words)
# apply tf
trainvec = vectorizer.fit_transform(test.data[:20])
feature_names = vectorizer.get_feature_names()
#print feature_names
keywords=[]

#clean unicode
for i in feature_names:
    keywords.append(i.encode('utf-8'))

#create PR structure
PR={}
for x in keywords:
    PR.setdefault(x, [])
    PR[x].append(1)


#found links
x=[]
for u in keywords:
    x=u.split(" ")
    for v in keywords:
        if u == v:
            continue
        for y in x:
            if y in v:
                PR[u].append(v)
                break
        continue


#part 2: fazer o ranking de acordo com a formula. 50 iteracoes max
N=len(keywords)
d=0.15
interation=50
for i in xrange(interation):
    for key in PR:
        PR[key].pop(0)
        PRj=0
        for yek in PR[key]:
            PRj=PRj + PR[yek][0]
        links=len(PR[key])
        PR[key].insert(0, ((1-d)*(PRj/links)+d/N))

#part 3: escolher os 5 melhores

orderedPR= sorted(PR.items(), key=operator.itemgetter(1)) #reverse ordered
print "TOP-5 keywords:"
for i in xrange(5):
    print orderedPR[N-1-i][0]
