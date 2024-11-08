from brain_games.utils import get_random_number
from brain_games import const

DESCRIPTION = ("Answer \"yes\" if given number is prime. "
               "Otherwise answer \"no\".")


def play():
    number = get_random_number(2, 10)
    correct = const.CORRECT
    for char in range(2, number):
        if number % char == 0:
            correct = const.NOT_CORRECT
            break
    return number, correct
