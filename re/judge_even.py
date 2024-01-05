import re
"""
test online: https://regexr.com/
find and match all even numbers in the text
"""
text = r'2 4 68 13 45 19 xhl dragon 100'
even_pattern = r'\b\d*[02468]\b'

match = re.findall(even_pattern, text)
if match:
    print(match)