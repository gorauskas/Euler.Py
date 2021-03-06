# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler
from euler.sequences import FibonacciDigitLengthSequence


class Euler(BaseEuler):
    def solve(self):
        for i, l in FibonacciDigitLengthSequence():
            if l == 1000:
                break

        return i

    @property
    def answer(self):
        return ('The first number in the Fibonacci sequence to contain 1000 ' +
                'digits is: %d' % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 25:

    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?
'''
