#!/usr/bin/env python3

from func_name import myself
import sys
from collections import Counter
import re


print(f'Ładowanie modułu "{__name__}"')

slownik = dict()

def zapisz():
    print(f'Wywołano funkcję "{myself()}" modułu "{__name__}"')

    try:
        assert len(sys.argv) > 1
    except AssertionError:
        print('Wprowadz odpowiednie dane')
        return
    else:
        args = ''.join(sys.argv[1:])
        nums = nums = [int(n) for n in re.findall(r'\d{1}', args)]
        if nums:
            global slownik
            slownik = dict(sorted(Counter(nums).items(), key=lambda x : x[0]))
        else:
            print('podaj liczby')
            return


def wypisz():
    print(f'Wywołano funkcję "{myself()}" modułu "{__name__}"')

    if not slownik:
        print('slownik jest pusty')
    else:
        for k, v in slownik.items():
            print(f'{k}:{v}', end=',')
        print()


print(f'Załadowano moduł "{__name__}"')

if __name__ == '__main__':
    zapisz()
    wypisz()