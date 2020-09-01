# -*- coding: utf-8 -*-
"""Functions for create project directory and files.
"""

import os

import pathlib
import git

def create_file(root_path, file_name):
    """Touch file of file_name at root_path.

    This function touch new empty file which name file_name at root_path.

    ----------

    Args:
        root_path(str): project rootpath.
        file_name(str): file name created under project root.

    Returns:
        result(boolean): flag for judge file created successfully.

    """
    file_path_str = root_path + "/" + file_name
    file_path = pathlib.Path(file_path_str)
    if file_path.exists():
        print("{} if already exists.".format(file_path_str))
        result = False
        return result
    else:
        file_path.touch()
        result = True
        return True

def git_init_project(root_path):
    """Git init at project root.

    This function execute git init at project root.

    ----------

    Args:
        root_path(str): project rootpath.

    Returns:
        None
    """
    _ = git.Repo.init(root_path)

def create_project(ref):
    """Create project.

    This function creates project directory and files.

    ---------

    Args:
        ref(str): competition name.

    Returns:
        None
    """
    root_path = "./" + ref
    os.mkdir(root_path)
    
    create_file(root_path, ".gitignore")
    create_file(root_path, "README.md")
    git_init_project(root_path)


    