import time
import pathlib
import os
import unittest

import kaggle_launcher as kl

class Testlaunch(unittest.TestCase):
    def test_choise_competition_normal(self):
        actual = kl.valid_choice("3", 10)
        self.assertEqual(actual, 3)

    def test_choise_competition_entered_none(self):
        actual = kl.valid_choice("", 10)
        self.assertEqual(actual, -1)
        
    def test_choise_competition_entered_exit(self):
        actual = kl.valid_choice("Exit", 10)
        self.assertEqual(actual, -2)

    def test_choise_competition_out_of_range(self):
        actual = kl.valid_choice("11", 10)
        self.assertEqual(actual, -3)
