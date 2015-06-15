# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeRange
from euler.util import is_prime


class Euler(BaseEuler):
    def solve(self):
        pl = list(PrimeRange(10000))

        for ub in range(546, 0, -1):
            lb = 0
            s = sum(pl[lb:lb + ub])
            while s < 1000000:
                if is_prime(s):
                    return s
                lb += 1
                s = sum(pl[lb:lb+ub])

    @property
    def answer(self):
        return ('The prime below one-million that can be written as the sum ' +
                'of the most consecutive primes is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 50

    The prime 41, can be written as the sum of six consecutive primes:

        41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below
    one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
'''
