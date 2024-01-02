import re

def pattern_match(pattern, string):
    m = re.search(pattern, string)
    if m:
        print(m.group())

text = r'num1 = 34567.89 \r\n num2 = 12'

integer_pattern = r'\d+'
float_pattern = r'\d+.\d+'

pattern_match(float_pattern, text)
pattern_match(integer_pattern, text)