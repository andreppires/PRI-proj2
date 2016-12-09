import xml.etree.ElementTree as ET
from dominate.tags import *
from exercise_1 import get_top_five as gtf_ex1
from exercise_3 import get_top_five as gtf_ex3

# return s1 appended with s2 with '\n' between them
def append_strings(s1, s2):
	if (s1 is None and s2 is None):
		return None

	if (s1 is None):
		return s2

	if (s2 is None):
		return s1

	if (s1 != ""):
		s1 = s1 + "\n"

	s1 = s1 + s2

	return s1

# return plain string with titles and descriptions from NYT XML/RSS feed document
# elements are split by '\n'
def convert_xml_to_string(file_name):
	doc = "";		# empty document

	root = ET.parse(file_name)
	for channel in root.findall("channel"):
		# loop each item (news)
		for item in channel.findall("item"):
			# title
			title = item.find("title").text
			doc = append_strings(doc, title)
			# description
			description = item.find("description").text
			doc = append_strings(doc, description)

	return doc

# insert candidates in html element
def insert_candidates(element, candidates):
	_div = element.add(div())
	_ul = _div.add(ul())
	for candidate in candidates:
		_ul.add(li(candidate))

# export results taken from previous exercises applied on xml_file_name to html_file_name
def export_to_html(xml_file_name, html_file_name):
	# content to work with
	content = convert_xml_to_string(xml_file_name)

	# create html object
	_html = html()
	_head, _body = _html.add(head(title("PRI Project - Exercise 4")), body())

	# exercise 1 algorithm candidates
	_body.add(h1("Top 5 candidates for algorithm used in exercise 1:"))
	candidates1 = gtf_ex1(None, content)
	insert_candidates(_body, candidates1)

	# exercise 2 algorithm candidates
	_body.add(h1("Top 5 candidates for algorithm used in exercise 2:"))
	insert_candidates(_body, [1, 2, 3, 4])

	# exercise 3 algorithm candidates
	_body.add(h1("Top 5 candidates for algorithm used in exercise 3:"))
	candidates3 = gtf_ex3(None, content)
	insert_candidates(_body, candidates3)

	with open(html_file_name, "w") as f:
		f.write(_html.render(xhtml=True))

if __name__ == "__main__":
	export_to_html("nyt_rss.xml", "exercise_4.html");

