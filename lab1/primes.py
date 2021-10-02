#!/usr/bin/env python3

import sys
from sympy import isprime
from main import convert


def print_primes():
    num_list = list()
    for e in  sys.argv[1:]:
        try:
            num_list.append(convert(e, int))
        except ValueError:
            pass

    for num in num_list:
        if isprime(int(num)):
            print(num)

if __name__ == "__main__":
    print_primes()
    


