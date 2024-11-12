from brain_games.utils import get_random_number
from brain_games import engine


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_question_and_answer():
    number = get_random_number()
    return number, "yes" if number % 2 == 0 else "no"


def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)