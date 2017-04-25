# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeRange
from euler.util import is_prime

'''
1. We need look at only those primes that have exactly 3 repeating digits.

2. The last (least significant) digit can’t be the repeating digit, because
replacing it would allow composite numbers

3. Since we are checking for an eight prime value family, we need only
those primes that have their repeating digit 0, 1 or 2;

this reduced the set to only 1,305 primes.
'''


class Euler(BaseEuler):
    def solve(self):
        for prime in list(PrimeRange(100000, 1000000)):
            s = str(prime)
            ld = s[5:6]
            if (s.count('0') == 3 and self._epf(s, '0')
                    or s.count('1') == 3 and ld != '1' and self._epf(s, '1')
                    or s.count('2') == 3 and self._epf(s, '2')):
                return int(s)

    def _epf(self, prime, rd):
        c = 0

        for d in '0123456789':
            n = int(prime.replace(rd, d))
            if (n > 100000 and is_prime(n)):
                c = c + 1

        return c == 8

    @property
    def answer(self):
        return ('The smallest prime which is part of an eight prime value ' +
                'family is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 51

    By replacing the 1st digit of the 2-digit number *3, it turns out that six
    of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
    56773, and 56993. Consequently 56003, being the first member of this
    family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight prime
    value family.
'''
