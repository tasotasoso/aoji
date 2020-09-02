import time
import pathlib
import os
import unittest

from utils import input as lc

class Testlaunch(unittest.TestCase):
    def test_choise_competition_normal_low(self):
        actual = lc.valid_choice("0", 10)
        self.assertEqual(actual, 0)

    def test_choise_competition_normal_up(self):
        actual = lc.valid_choice("9", 10)
        self.assertEqual(actual, 9)

    def test_choise_competition_entered_none(self):
        actual = lc.valid_choice("", 10)
        self.assertEqual(actual, -1)
        
    def test_choise_competition_entered_exit(self):
        actual = lc.valid_choice("Exit", 10)
        self.assertEqual(actual, -2)

    def test_choise_competition_out_of_range(self):
        actual = lc.valid_choice("11", 10)
        self.assertEqual(actual, -3)
