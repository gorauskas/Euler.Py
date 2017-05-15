# -*- coding: utf-8 -*-

import argparse
import math
from euler import __version__


def parse_options(args):
    parser = argparse.ArgumentParser(
        description='Solutions to Project Euler problems written in Python 3',
        epilog='written by Jonas Gorauskas')

    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s {vrs} '.format(vrs=__version__) +
                        '- written by Jonas Gorauskas')

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Prints the problem statement and the solution')

    parser.add_argument('-p', '--problem',
                        help='The problem/solution number you want to run')

    return parser.parse_args()


def is_prime(n):
    '''
    Check if n is a prime number
    '''
    n = abs(int(n))
    if n < 2:
        return False

    if n == 2:
        return True

    if not n & 1:
        return False

    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def is_multiple_of(num, multiple):
    if num == 0:
        return False

    return num % multiple == 0


def number_of_divisors(n):
    if n == 1:
        return 1

    return len([x for x in range(1, int(math.sqrt(n)))
                if is_multiple_of(n, x)]) * 2


def sum_of_divisors(n):
    c = 1
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            c += x
            if x != n / x:
                c += n / x
    return c


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def is_pandigital(n, l=9):
    return len([i for j, i in enumerate([int(x) for x
                                         in list('1234567890')[:l]])
                if j not in [int(y) - 1 for y in str(n)]]) == 0
