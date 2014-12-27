# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        LS = ''.join(list(str(n) for n in range(1000000)))
        ans = int(LS[1]) * int(LS[10]) * int(LS[100]) * int(LS[1000]) * \
            int(LS[10000]) * int(LS[100000]) * int(LS[1000000])
        print('The value is %d' % ans)

    @property
    def problem(self):
        return '''
Project Euler Problem 40:

    An irrational decimal fraction is created by concatenating the positive
    integers:

        0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of
    the following expression.

        d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
