from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
import operator
import os

# return feature names from file using tf-idf algorithm
def get_feature_names(file_name, file_content):
	print "Getting feature names..."

	# get stop words
	stop_words = get_stop_words("en")

	# fetch train data/collenction from disk
	# using wiki20 collection from https://github.com/zelandiya/keyword-extraction-datasets
	train = []
	for file in os.listdir("wiki20/documents"):
		if file.endswith(".txt"):
		    with open("wiki20/documents/" + file, 'r') as myfile:
		        train.append(myfile.read().replace('\n', ''))

	# tri-gramas and no stop-words
	vectorizer = TfidfVectorizer(use_idf=False, ngram_range=(1, 3)
	, stop_words=stop_words)

	# learn idf
	# carefull here. more document -> more precision -> more time to compute them all
	trainvec = vectorizer.fit_transform(train[:2])

	# input document as array
	input_document = []

	# read file
	if (file_name is not None):
		with open(file_name, "r") as f:
			content = f.read()
			input_document.append(content)
			f.close()
	else:
		input_document.append(file_content)

	# apply tf
	testvec = vectorizer.transform(input_document)

	# get feature names
	feature_names = vectorizer.get_feature_names()

	return feature_names

# return page rank for each keyphrase
def get_page_rank(keyphrases):
	print "Getting page ranks..."
	keywords = []

	# clean unicode
	for key in keyphrases:
		keywords.append(key.encode('utf-8'))

	# create PR structure
	PR = {}
	for x in keywords:
		PR.setdefault(x, [])
		PR[x].append(1)

	# find links
	x = []
	for u in keywords:
		x = u.split(" ")
		for v in keywords:
		    if u == v:
		        continue
		    for y in x:
		        if y in v:
		            PR[u].append(v)
		            break
		    continue

	# run page rank
	N = len(keywords)
	d = 0.15
	interation = 50
	for i in xrange(interation):
		for key in PR:
		    PR[key].pop(0)
		    PRj = 0
		    for yek in PR[key]:
		        PRj = PRj + PR[yek][0]
		    links = len(PR[key])
		    PR[key].insert(0, ((1-d)*(PRj/links)+d/N))

	return PR

# get top 5 keyphrases from file_name or file_content using PageRank algorithm
def get_top_five(file_name, file_content):
	fn = get_feature_names(file_name, file_content)
	pr = get_page_rank(fn)

	print "Getting top five..."
	top_five = []
	orderedPR = sorted(pr.items(), key=operator.itemgetter(1), reverse = True)
	for i in xrange(5):
		top_five.append(orderedPR[i][0])

	return top_five

if __name__ == "__main__":
	tf = get_top_five("test.txt", None)
	for keyphrase in tf:
		print keyphrase

