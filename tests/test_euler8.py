# -*- coding: utf-8 -*-

from euler.solutions.euler8 import Euler
import unittest


class TestEuler(unittest.TestCase):
    def setUp(self):
        self.fixture = Euler()

    def tearDown(self):
        del self.fixture

    def test_solve(self):
        self.assertEqual(self.fixture.solve(), 23514624000)
