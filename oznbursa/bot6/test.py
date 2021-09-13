import re

string = 'the apple is red'

print(re.search(r'^the (apple|orange|grape) is (red|orange|violet)', string))