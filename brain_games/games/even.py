from brain_games.utils import get_random_number
from brain_games import engine


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = get_random_number()
    answer = "yes" if is_even(number) else "no"
    return number, answer


def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)
