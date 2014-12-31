# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import FibonacciSequence


class Euler(BaseEuler):
    def solve(self):
        res = [x for x in FibonacciSequence(4000000)
               if x % 2 == 0]
        return sum(res)

    @property
    def answer(self):
        return ('The sum of the even-valued terms in a Fibonacci sequence\n' +
                'not exceeding 4 million is: %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 2:

   Each new term in the Fibonacci sequence is generated by adding the
   previous two terms. By starting with 1 and 2, the first 10 terms
   will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

   By considering the terms in the Fibonacci sequence whose values do
   not exceed four million, find the sum of the even-valued terms.
'''
