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