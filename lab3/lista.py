#!/usr/bin/env python3
#-*-coding: utf-8-*-

from func_name import myself
import sys
from collections import Counter
import re

print(f'Ładowanie modułu "{__name__}"')

lista = list()


def zapisz():
    print(f'Wywołano funkcję "{myself()}" modułu "{__name__}"')

    try:
        assert len(sys.argv) > 1
    except AssertionError:
        print('Wprowadz odpowiednie dane')
        return
    else:
        args = ''.join(sys.argv[1:])
        nums = re.findall(r'\d{1}', args)
        if nums:
            nums = [int(n) for n in sorted(nums)]
            global lista
            for i in range(nums[-1]):
                lista.append(int(0))
            
            for n in nums:
                 lista[n-1] += 1
        else:
            print('podaj liczby')
            return
                

def wypisz():
    print(f'Wywołano funkcję "{myself()}" modułu "{__name__}"')

    if not lista:
        print('lista jest pusta')
    else:
        for i in range(len(lista)):
            if lista[i]:
                print(f'{i+1}:{lista[i]}', end=',')
        print()






print(f'Załadowano moduł "{__name__}"')

if __name__ == '__main__':
    zapisz()
    wypisz()