# -*- coding: utf-8 -*-

from euler.solutions.euler22 import Euler
import unittest


class TestEuler(unittest.TestCase):
    def setUp(self):
        self.fixture = Euler()

    def tearDown(self):
        del self.fixture

    def test_solve(self):
        self.assertEqual(self.fixture.solve(), 871198282)
