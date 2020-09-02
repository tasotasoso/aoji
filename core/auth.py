from .KaggleApi_extended import KaggleApi_extended 

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
        api = KaggleApi_extended()
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