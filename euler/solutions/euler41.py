# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.util import is_pandigital, is_prime


class Euler(BaseEuler):
    def solve(self):
        '''
        Why is N equal to 7654321? So let’s eliminate some values of n by using
        the divisibility rule that any integer is divisible by 3 whose sum of
        digits is divisible by 3; therefore composite and not prime.

        9+8+7+6+5+4+3+2+1 = 45,
        8+7+6+5+4+3+2+1 = 36,
        6+5+4+3+2+1 = 21, and
        5+4+3+2+1 = 15,

        all of which are divisible by 3 and therefore could not yield a 1 to
        {5, 6, 8, 9} pandigital prime. So that leaves 4 and 7 digit prime
        numbers less than 4321 and 7654321 respectively. Since we want the
        largest pandigital prime we’ll check the 7 digit group first.
        '''
        n = 7654321
        while not (is_pandigital(n, 7) and is_prime(n)):
            n -= 2

        return n

    @property
    def answer(self):
        return ('The largest n-digit pandigital prime that exists is %d'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 41

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?
'''
