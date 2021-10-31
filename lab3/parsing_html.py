from functools import partial
import re

sentence = '''janusz pawlacz 
drugi'''

pattern = re.compile(r'[\n]')

match = pattern.finditer(sentence)

for m in match:
    print(m)


print(sentence)