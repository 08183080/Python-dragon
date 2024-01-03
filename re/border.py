import re

"""
^ matches the beginning.
$ matches the ending.
"""

text1 = r'How, China Country.'
text2 = r'The World is on your side.'
text3 = r'vwcdvchjd vddcshds \
cshjhbsdjbjds'

pattern1 = r'^How.*Country\.$'
pattern2 = r'\bThe\b'  # \b is the border of a word
pattern3 = r'^(.*)$'

match1 = re.search(pattern1, text1)
if match1:
    print(match1.group())

match2 = re.search(pattern2, text2)
if match2:
    print(match2.group())

match3 = re.search(pattern3, text3)
if match3:
    print(match3.group())