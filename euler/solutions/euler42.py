# -*- coding: utf-8 -*-

from euler.baseeuler import BaseEuler

from math import sqrt
from os import path, getcwd


class Euler(BaseEuler):
    def solve(self):
        fp = path.join(getcwd(), 'euler/resources/words.txt')
        with open(fp, 'r') as f:
            words = [x[1:-1] for x in f.read().split(',')]

            def is_triangle_number(n):
                return not bool(((sqrt(1 + 8 * n) - 1) / 2) % 1)

            def word_score(word):
                return sum(abs(64 - ord(letter)) for letter in word)

            return sum(is_triangle_number(word_score(word))
                       for word in words)

    @property
    def answer(self):
        return ('There are %d triangle words in the file.'
                % self.solve())

    @property
    def problem(self):
        return '''
Project Euler Problem 42

    The nth term of the sequence of triangle numbers is given by,
    tn = ½n(n+1); so the first ten triangle numbers are:

      1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text
    file containing nearly two-thousand common English words, how many are
    triangle words?
'''
