import unittest
import time
import pathlib
import os

import kaggle_launcher as kl

class TestCreateProject(unittest.TestCase):
    def test_create_file(self):
        root_path = "./tests/work"
        file_path = "test_create_file.txt"

        kl.create_file(root_path, file_path)

        file_path_actual = pathlib.Path(root_path + "/" + file_path)
        self.assertTrue(file_path_actual.exists())

    #def test_create_project(self):
    #    root_path = "./tests/work/test_create_project"
    #    gitignore_path_str = root_path + "/" + ".gitignore"
    #    README_path_str = root_path + "/" + "README.md"

    #    kl.create_project(root_path)

    #    actual_gitignore = pathlib.Path(gitignore_path_str).exists()
    #    actual_README = pathlib.Path(README_path_str).exists()

    #    actual = actual_gitignore and actual_README
    #    self.assertTrue(actual)

    def test_create_file_false(self):
        """test create_file_false case when already file exists.
        """
        root_path = "./tests/work"
        file_path = "test_create_file.txt"

        actual = kl.create_file(root_path, file_path)

        self.assertFalse(actual)

