#!/usr/bin/env python3


from fractions import Fraction
import cmath


def convert(x, func):
    if type(x) == type(str()):
        try:
            x = func(x)
        except:
            raise ValueError(f'str {x} can not be converted to {func}')
        else:
            return x
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