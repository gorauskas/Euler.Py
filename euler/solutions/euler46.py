# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def solve(self):
        n = 5
        f = 1
        primes = set()

        while True:
            if all(n % p for p in primes):
                primes.add(n)
            else:
                if not any((n-2*i*i) in primes for i in range(1, n)):
                    break
            n += 3-f
            f = -f

        return n

    @property
    def answer(self):
        return ('The smallest odd composite that cannot be written as the ' +
                'sum of a prime and twice a square is %d.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 46

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

    9 = 7 + 2×12
    15 = 7 + 2×22
    21 = 3 + 2×32
    25 = 7 + 2×32
    27 = 19 + 2×22
    33 = 31 + 2×12

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?
'''
