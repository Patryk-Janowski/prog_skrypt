#!/usr/bin/env python3


from fractions import Fraction
import cmath


def isdigit(x):
    try:
        float(x)
    except:
        return False
    else:
        return True
    

def convert(x, func):
    if type(x) == type(str()):
        if isdigit(x):
            return func(x)
        else:
            raise ValueError(f'str {x} can not be converted to {func}')
    else:
        return x



def sum(x, y):
    x, y = convert(x, float), convert(y, float)
    try:
        s = x + y
    except:
        raise TypeError(f'{type(x)} and {type(y)} does not support addition')
    else:
        return s



if __name__ == '__main__':
    sum(2, 5)