# -*- coding: utf-8 -*-

from euler.solutions.euler16 import Euler
import unittest


class TestEuler(unittest.TestCase):
    def setUp(self):
        self.fixture = Euler()

    def tearDown(self):
        del self.fixture

    def test_solve(self):
        self.assertEqual(self.fixture.solve(), 1366)
