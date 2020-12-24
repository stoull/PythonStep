import re

pattern = re.compile('Search this inside')

a_string = 'Search this inside of this text please!'



a = pattern.search(a_string)
b = pattern.findall(a_string)
c = pattern.fullmatch(a_string)
d = pattern.match(a_string)

# print(a)
# print(b)
# print(c)
# print(d)


pattern_r = re.compile(r'(\w+ (\d+))')
txt_to_search = "Jan 1987\nMay 1969\nAug 2011"
matches = pattern_r.finditer(txt_to_search)
for match in matches:
	print(match[0])

bb = pattern_r.search(txt_to_search)
print(f"Group0: {bb.group(0)}")
print(f"Group1: {bb.group(1)}")
print(f"Group2: {bb.group(2)}")



email_check_pattern = re.compile(r"[0-9a-zA-Z_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+")
emails = "your email is : 23253332@qq.com Jack: jack_home@gamil.com, kevine-23i@vip.com"
get_matches = email_check_pattern.finditer(emails)
print(get_matches)
for ma in get_matches:
	print(ma)

