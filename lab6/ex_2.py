from collections import Counter
import sys


print(dict(sorted(Counter([len(y.strip()) for x in [x.split() for x in sys.stdin.readlines()] for y in x]).items(), key=lambda x: x[0])))
