from brain_games.utils import get_random_number


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def play():
    number = get_random_number(0, 100)
    return number, "yes" if number % 2 == 0 else "no"
