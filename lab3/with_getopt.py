#!/usr/bin/env python3
#-*-coding: utf-8-*-

import lista
import slownik
import sys
import getopt

try:
    opts, arg = getopt.getopt(sys.argv[1:], '', ['module='])
except getopt.GetoptError as err:
    print(err)
else:
    if opts[0][1] == 'slownik':
        slownik.zapisz()
        slownik.wypisz()
    elif opts[0][1] == 'lista':
        lista.zapisz()
        lista.wypisz()
    else:
        print(f'{sys.argv[0]} --module [lista] [slownik]')