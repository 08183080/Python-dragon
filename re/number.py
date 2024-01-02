import re

"""
\d: 0-9, digital
\s: space
(): capture group
[]
{}: quanti
"""

def pattern_match(pattern, string):
    m = re.search(pattern, string)
    if m:
        print(m.group())

text = r'num1 = 34567.89 \r\n num2 = 12'
phone = r'778-213-4569' # american phone

integer_pattern = r'\d+'
float_pattern = r'\d+.\d+'
pattern = r'(\d{3})-?(\d{3})-?(\d{4})'

# pattern_match(float_pattern, text)
# pattern_match(integer_pattern, text)
pattern_match(pattern, phone)