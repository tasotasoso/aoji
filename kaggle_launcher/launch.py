# -*- coding: utf-8 -*-
"""
"""

import kaggle_launcher.KaggleApi_extended as kae
import kaggle_launcher.create_project as cp
import re


def authenticate():
    """Authenticate kaggle account.

    This function authenticate your kaggle account.
    Raises OSError when kaggle.json not found or no environment method.
    
    --------

    Args:
        None

    Return:
        api(KaggleApi_extended): authenticated kaggle API instance.
    """

    try:
        api = kae.KaggleApi_extended()
        api.authenticate()
    except OSError as e:
        print(e)
    return api

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

def choise_competition(competition_numbers):
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
    print("\nChoose competition you create project.")
    print("Input number. example: 1.")
    print("If you stop launch, please enter \"Exit\".")
    choice = input()

    m = re.fullmatch(r'[0-9]+', choice)
    if m is None:
        print("Please input number.")
        result = -1
        return result
    elif choice == "Exit":
        print("Stop launch.")
        result = -2
        return result
    elif int(choice) not in range(1, competition_numbers):
        print("Your entered number is out of range of competitions.")
        result = -3
        return result
    else:
        result = int(choice)
        return result

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
    competition_number = choise_competition(len(competitions))
    ref = getattr(competitions[competition_number], "ref")
    
    
    #cp.create_project(ref)
    for key, value in competitions[0].__dict__.items():
        if key == "tags":
            for tag in value:
                print(value, type(value))
                print(tag, type(tag))
                #for item in tag.__dict__.items():
                #    print(tag.__dict__.items(),":",tag, ':', type(tag))
    


if __name__ == "__main__":
    launch()
