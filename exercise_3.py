from exercise_1 import get_candidates, get_page_rank
import operator

def get_top_five(file_name, file_content):
	# top 5 candidates
	top_five = []

	# candidates from exercise 1
	candidates_ex1 = get_candidates(file_name, file_content, 1, 3)
	pr = get_page_rank(candidates_ex1)

	# weight from exercise 1
	weight_ex1 = 1.2

	# candidates and weight from exercise 1
	weight_candidates_ex1 = {}
	for key in pr:
		weight_candidates_ex1[key] = pr[key][0]*weight_ex1

	# ordered candidates
	ordered_candidates = sorted(weight_candidates_ex1.items(), key=operator.itemgetter(1), reverse = True)

	# get top five
	for i in xrange(5):
		top_five.append(ordered_candidates[i][0])
	
	return top_five

if __name__ == "__main__":
	tf = get_top_five("test.txt", None)
	for keyphrase in tf:
		print keyphrase

