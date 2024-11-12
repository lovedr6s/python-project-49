from brain_games.utils import get_random_number
from brain_games import const
from brain_games import engine

DESCRIPTION = ("Answer \"yes\" if given number is prime. "
               "Otherwise answer \"no\".")


def get_question_and_answer():
    number = get_random_number()
    correct = const.CORRECT
    for char in range(2, number):
        if number % char == 0:
            correct = const.NOT_CORRECT
            break
    return number, correct


def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)