from brain_games.utils import get_random_number

DESCRIPTION = ("Answer \"yes\" if given number is prime. "
               "Otherwise answer \"no\".")


def play():
    number = get_random_number(2, 10)
    correct = "yes"
    for char in range(2, number):
        if number % char == 0:
            correct = "no"
            break
    return number, correct
