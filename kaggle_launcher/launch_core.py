# -*- coding: utf-8 -*-
"""Core functions.
"""

from .KaggleApi_extended import KaggleApi_extended  # as kae
from .auth import *
from .create_project import *
from .input import *


def show_and_get_competitions_list(api):
    """Show and return kaggle competitions.

    This function show kaggle competitions which can get kaggle API and returns the list.

    ----------

    Args: 
        api(KaggleApi_extended): authenticated kaggle API instance.

    Return:
        competitions(List(kaggle_models_extended.Competition)): list of kaggle competitions.

    """
    competitions = api.competitions_list_cli()
    return competitions


def launch():
    """launch your project.

    This function execute flow to launch project.

    --------

    Args: 
         None

    Returns:
         None

    """
    api = authenticate()
    competitions = show_and_get_competitions_list(api)
    choice = input_competition_number()
    competition_number = valid_choice(choice, len(competitions))
    ref = getattr(competitions[competition_number], "ref")

    create_project(ref)


if __name__ == "__main__":
    launch()
