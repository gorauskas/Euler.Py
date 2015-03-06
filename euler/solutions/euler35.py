# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import is_prime


class Euler(BaseEuler):
    def solve(self):
        # all primes less than 1M
        primes = [p for p in range(1, 1000000) if is_prime(p)]
        res = []

        for prime in primes:
            if self._check_rotations([int(d) for d in str(prime)], prime):
                res.append(prime)

        return len(res)

    def _check_rotations(self, l, n):
        '''
        Checks the circular rotations of each prime number for primes
        Returns True if all rotations are also prime, false otherwise

        l - a list of digits that makes up the prime nunber n
        n - The prime number to check
        '''
        k = 0
        while n != k:
            cdr = l[1:]
            car = l[0]
            cdr.append(car)
            k = int(''.join([str(s) for s in cdr]))
            if not is_prime(k):
                return False
            l = cdr
        return True

    @property
    def answer(self):
        return ('There are %d circular primes below 1 million.' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 35:

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
'''
