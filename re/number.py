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
phone1 = r'778-213-4569' # american phone
phone2 = r'778.234.4578'
phone3 = r'(789)-214-6723'

integer_pattern = r'\d+'
float_pattern = r'\d+.\d+'
pattern_1 = r'(\d{3})-?(\d{3})-?(\d{4})'
pattern_2 = r'(\d{3}[-.]?){2}\d{4}'
pattern_3 = r'^((\(\d{3}\)|\d{3})[-.]?)\d{3}[-.]?\d{4}$'

# pattern_match(float_pattern, text)
# pattern_match(integer_pattern, text)
pattern_match(pattern_3, phone1)
pattern_match(pattern_3, phone2)
pattern_match(pattern_3, phone3)