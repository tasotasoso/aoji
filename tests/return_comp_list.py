import datetime

from kaggle.kaggle_models_extended import Competition
from kaggle.kaggle_models_extended import Tag


def return_comp_list():
    """Returns competition list for test.

    This function returns competition list for test.

    --------
    Args:
        None

    Returns:
        competitions(List(kaggle_models_extended.Competition)): list of competition instance.
    """

    tag_set = {
        'ref': 'text data',
        'competitionCount': 34,
        'datasetCount': 466,
        'description': None,
        'fullPath': 'data type > text data',
        'isAutomatic': False,
        'name': 'text data',
        'scriptCount': 707,
        'totalCount': 1207
    }

    deadline_datetime = datetime.datetime.strptime(
        "2030-07-01 23:59:00", '%Y-%m-%d %H:%M:%S')
    enabledDate_datetime = datetime.datetime.strptime(
        "2020-07-30 21:03:15", '%Y-%m-%d %H:%M:%S')

    comp_set = {
        'ref': 'contradictory-my-dear-watson',
        'tags': [tag_set],
        'description': 'Detecting contradiction and entailment in multilingual text using TPUs',
        'id': 21733,
        'title': 'Contradictory, My Dear Watson',
        'url': 'https://www.kaggle.com/c/contradictory-my-dear-watson',
        'deadline': deadline_datetime,
        'category': 'Getting Started',
        'reward': 'Prizes',
        'organizationName': 'Kaggle',
        'organizationRef': 'Kaggle',
        'kernelCount': 0,
        'kernelCount': 185,
        'userHasEntered': False,
        'userRank': None,
        'mergerDeadline': None,
        'newEntrantDeadline': None,
        'enabledDate': enabledDate_datetime,
        'enabledDate_datetime': 5,
        'maxTeamSize': 5,
        'evaluationMetric': 'Categorization Accuracy',
        'Categorization Accuracy': False,
        'isKernelsSubmissionsOnly': True,
        'submissionsDisabled': False
    }

    text_data_comp = Competition(init_dict=comp_set)
    competitions = [text_data_comp]
    return competitions