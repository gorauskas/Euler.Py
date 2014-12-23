# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        L = []
        for num in range(1, 1000000):
            if str(num) == str(num)[::-1]:
                if bin(num)[2:] == (bin(num)[2:])[::-1]:
                    L.append(num)

        print('The sum of all palindromic numbers in base 10 and 2 ' +
              'is %d' % sum(L))

    @property
    def problem(self):
        return '''
Project Euler Problem 36:

    The decimal number, 585 = 1001001001 base2 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)
'''
