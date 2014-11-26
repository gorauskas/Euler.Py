# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler


def collatz_list(n):
    l = []

    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        l.append(n)

    return l


class Euler(BaseEuler):
    def solve(self):
        nums = list(range(2, 1000000))
        l, j, k = [], 0, 0

        for num in nums:
            if len(collatz_list(num)) > j:
                l = collatz_list(num)
                j = len(l)
                k = num

        print('Starting Number: %d; Chain Lenght: %d' % (k, j))

    @property
    def problem(self):
        return '''
Project Euler Problem 14:

    The following iterative sequence is defined for the n of positive
    integers:

    n -> n/2      (n is even)
    n -> 3n + 1   (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

    13  40  20  10  5  16  8  4  2  1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
'''
