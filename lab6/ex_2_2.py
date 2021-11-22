#!/usr/bin/env python3

import sys

def get_lines():
    lines = []
    for x in range(1, len(sys.argv)):
        with open(sys.argv[x], 'r+') as f:
            lines += f.readlines()
    return lines


def get_numbers(lines):
    nums = [int(y.strip()) for x in [x.split() for x in lines] for y in x]
    return nums


nums = get_numbers(get_lines())
x = list(filter(lambda x: x % 2 == 0, get_numbers(get_lines())))
# y = [x for x in nums if x % 2 == 0]

print(x)
print(len(x))



