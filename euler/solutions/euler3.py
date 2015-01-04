# -*- coding: utf-8 -*-

from math import ceil, sqrt
from euler.baseeuler import BaseEuler


class Euler(BaseEuler):
    def prime_factors(self, n):
        if n <= 1:
            return []
        prime = next((x for x in range(2, ceil(sqrt(n)) + 1) if n % x == 0), n)
        return [prime] + self.prime_factors(n // prime)

    def solve(self):
        pf = self.prime_factors(600851475143)
        return max(pf)

    @property
    def answer(self):
        return ('The largest prime factor of the number 600851475143 is: %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 3:

   The prime factors of 13195 are 5, 7, 13 and 29.

   What is the largest prime factor of the number 600851475143 ?
'''
