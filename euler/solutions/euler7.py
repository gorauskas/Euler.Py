# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import is_prime


class Euler(BaseEuler):
    def solve(self):
        num, prms, res = 1, 1, 0  # all primes above 2 are odd
        while True:
            if is_prime(num):
                prms += 1

            if prms == 10001:     # stop at the number we want
                res = num
                break

            num += 2

        return res

    @property
    def answer(self):
        return ('The 10001st prime is %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 7:

   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
   we can see that the 6th prime is 13.

   What is the 10001st prime number?
'''
