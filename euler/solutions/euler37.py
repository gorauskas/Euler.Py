# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import is_prime
import re


class Euler(BaseEuler):
    def solve(self):
        n, f = 11, 1
        L = []

        while len(L) < 11:
            n += 3 - f
            f = -f
            if not (n > 100 and re.search('[245680]', str(n))):
                if is_prime(n) and self._is_truncatable(n):
                    L.append(n)

        print('The sum of the only eleven primes that are both truncatable\n' +
              'left and right is %d' % sum(L))

    def _is_truncatable(self, n):
        for d in range(1, len(str(n))):
            if not is_prime(str(n)[d:]) or not is_prime(str(n)[:d]):
                return False
        return True

    @property
    def problem(self):
        return '''
Project Euler Problem 37:

    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
    left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
