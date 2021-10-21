#!/usr/bin/env python3
#-*-coding: utf-8-*-

import lista
import slownik
import sys

try:
    assert len(sys.argv) > 1
except AssertionError:
    print('Wprowadz odpowiednie dane')
else:
    if sys.argv[1] == '--lista':
        lista.zapisz()
        lista.wypisz()
    elif sys.argv[1] == '--slownik':
        slownik.zapisz()
        slownik.wypisz()
    else:
        print('obslugiwane opcje: [--lista] [--slownik]')