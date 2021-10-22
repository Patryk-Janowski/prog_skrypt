#!/usr/bin/env python3
#-*-coding: utf-8-*-

import re

def main():
    while True:
        try:
            input_data = input('> ')
            if not input_data:
                break
            else:
                input_data = input_data.split(' ')
                assert len(input_data) == 1 
        except EOFError:
            print('\n- exiting')
            break
        except Exception:
            print('- enter correct data')
        else:
            word = input_data[0]
            words = re.findall(r'[^\W|^\d]{2,}', word)
            nums = re.findall(r'\d+',word)
            if words:
                print('Words:')
                for w in words: 
                    print('\t' + w)
            if nums:
                print('Numbers:')
                for n in nums:
                    print('\t' + n)


if __name__ == '__main__':
    main()
            


