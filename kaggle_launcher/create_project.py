# -*- coding: utf-8 -*-
"""
"""

import pathlib
import os

def create_file(root_path, file_name):
    file_path_str = root_path + "/" + file_name
    file_path = pathlib.Path(file_path_str)
    if file_path.exists():
        print("{} if already exists.".format(file_path_str))
        return False
    else:
        file_path.touch()
        return True

def create_project(ref):
    root_path = "./" + ref
    os.mkdir(root_path)
    
    create_file(root_path, ".gitignore")
    create_file(root_path, "README.md")


    