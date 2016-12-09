import xml.etree.ElementTree as ET

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
def convert_xml_to_string(filename):
	namespaces = {"dc" : "http://purl.org/dc/elements/1.1/",
				"media" : "http://search.yahoo.com/mrss/"}

	doc = "";		# empty document

	root = ET.parse(filename)
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

doc = convert_xml_to_string("nyt_rss.xml")
print doc

