# -*- coding: utf-8 -*-
"""Core functions.
"""

from .KaggleApi_extended import KaggleApi_extended  # as kae
from .auth import *
from .create_project import *
import re


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


def valid_choice(choice, competition_numbers):
    """Choise competition number.

    This function ask you to choose competition number your want to launch project.

    -------

    Args:
        competition_numbers(int): number of competitions you got by kaggle api.

    Returns:
        result(int): number replesents competition you choose or error.
        number is following:
            1 - competition_numbers: competition you choose
            -1 : entered none.
            -2 : entered "Exit"
            -3 : entered number out of range of competitions.

    """
    m = re.fullmatch(r'[0-9]+', choice)
    if choice == "Exit":
        print("Stop launch.")
        result = -2
        return result
    elif m is None:
        print("Please input number.")
        result = -1
        return result
    elif int(choice) not in range(0, competition_numbers):
        print("Your entered number is out of range of competitions.")
        result = -3
        return result
    else:
        result = int(choice)
        return result


def input_competition_number():
    """Receive standard input for competition choice.

    This function receives standard input for competition choice.

    ---------

    Args:
        None

    Returns:
        choice(String): competition number for input.
    """
    print("\nChoose competition you create project.")
    print("Input number. example: 1.")
    print("If you stop launch, please enter \"Exit\".")
    choice = input()
    return choice


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
