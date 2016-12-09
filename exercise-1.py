from stop_words import get_stop_words
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import operator

# return feature names from file using tf-idf algorithm
def get_feature_names(file_name):
	print "Getting feature names..."

	# get stop words
	stop_words = get_stop_words("en")

	# fetch test data
	train = fetch_20newsgroups(subset="train")

	# tri-gramas and no stop-words
	vectorizer = TfidfVectorizer(use_idf=False, ngram_range=(1, 3)
	, stop_words=stop_words)

	# learn idf
	trainvec = vectorizer.fit_transform(train.data)

	# input document as array
	input_document = []

	# read file
	with open(file_name, "r") as f:
		content = f.read()
		input_document.append(content)
		f.close()

	# apply tf
	testvec = vectorizer.transform(input_document)

	# get feature names
	feature_names = vectorizer.get_feature_names()

	return feature_names[:10]

# return page rank for each keyphrase
def get_page_rank(keyphrashes):
	print "Getting page ranks..."

	keywords=[]

	# clean unicode
	for key in keyphrashes:
		keywords.append(key.encode('utf-8'))

	# create PR structure
	PR={}
	for x in keywords:
		PR.setdefault(x, [])
		PR[x].append(1)

	# find links
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

	# run page rank
	N=len(keywords)
	d=0.15
	interation=1
	for i in xrange(interation):
		for key in PR:
		    PR[key].pop(0)
		    PRj=0
		    for yek in PR[key]:
		        PRj=PRj + PR[yek][0]
		    links=len(PR[key])
		    PR[key].insert(0, ((1-d)*(PRj/links)+d/N))

	return PR

# return top five element (highest page rank)
def get_top_five(PR):
	print "Getting top five..."

	top_five = []
	orderedPR = sorted(PR.items(), key=operator.itemgetter(1), reverse = True)
	for i in xrange(5):
		top_five.append(orderedPR[i][0])

	return top_five

fn = get_feature_names("test.txt")
pr = get_page_rank(fn)
tf = get_top_five(pr)
for w in tf:
	print w
