from brain_games.utils import get_random_number
import math
from brain_games import engine

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1, number2 = get_random_number(), get_random_number()
    correct_answer = str(math.gcd(number1, number2))
    question = f"{number1} {number2}"
    return question, correct_answer


def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)
