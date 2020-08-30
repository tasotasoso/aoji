import re

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