from stop_words import get_stop_words
from nltk import ngrams
import operator
import string

# return new content witthout punctuation and stop_words
def clean_content(content):
	# get stop words
	stop_words = get_stop_words("en")

	# erase punctuation
	content = "".join(ch for ch in content if ch not in string.punctuation)

	# erase stop words
	content  = [word for word in content.split() if word.lower() not in stop_words]

	return " ".join(content)

# return candidates for file_name or file_content
def get_candidates(file_name, file_content, small_n_gram, high_n_gram):
	# content to work with
	new_content = ""

	# read file
	if (file_name is not None):
		with open(file_name, "r") as f:
			content = f.read()
			new_content = clean_content(content);
			f.close()
	else:
		new_content = clean_content(file_content)

	# candidates
	candidates = []

	# get candidates (n grams)
	for n in range(small_n_gram, high_n_gram + 1):
		n_grams = ngrams(new_content.split(), n)
		for grams in n_grams:
			candidate = " ".join(grams)
			candidates.append(candidate)

	return list(set(candidates))

# return page rank for each keyphrase
def get_page_rank(keyphrases):
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
	candidates = get_candidates(file_name, file_content, 1, 3)
	pr = get_page_rank(candidates)

	top_five = []
	orderedPR = sorted(pr.items(), key=operator.itemgetter(1), reverse = True)
	for i in xrange(5):
		top_five.append(orderedPR[i][0])

	return top_five

if __name__ == "__main__":
	tf = get_top_five("test.txt", None)
	for keyphrase in tf:
		print keyphrase

