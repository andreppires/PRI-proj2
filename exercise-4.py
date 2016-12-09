import xml.etree.ElementTree as ET
from dominate.tags import *

# return s1 appended with s2 with '\n' between them
def append_strings(s1, s2):
	if (s1 == None and s2 == None):
		return None

	if (s1 == None):
		return s2

	if (s2 == None):
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

# export results to html file
def export_html(file_name):
	_html = html()
	_head, _body = _html.add(head(title("PRI Project - Exercise 4")), body())

	# exercise 1 algorithm candidates
	_body.add(h1("Candidates for algorithm used in exercise 1:"))
	insert_candidates(_body, [1, 2, 3])

	# exercise 2 algorithm candidates
	_body.add(h1("Candidates for algorithm used in exercise 2:"))
	insert_candidates(_body, [1, 2, 3, 4])

	# exercise 3 algorithm candidates
	_body.add(h1("Candidates for algorithm used in exercise 3:"))
	insert_candidates(_body, [1, 2, 3, 4, 5])

	with open(file_name, "w") as f:
		f.write(_html.render(xhtml=True))

export_html();
#doc = convert_xml_to_string("nyt_rss.xml")
#print doc

