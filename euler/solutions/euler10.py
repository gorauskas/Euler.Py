# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import PrimeGenerator


class Euler(BaseEuler):
    def solve(self):
        l = []
        for x in PrimeGenerator():
            if x >= 2000000:
                break
            l.append(x)

        print("The sum of all primes below 2 million is: %d" % sum(l))

    @property
    def problem(self):
        return '''
Project Euler Problem 10:

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
'''
