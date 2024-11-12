from brain_games.utils import get_random_number
import math
from brain_games import engine

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return math.gcd(a, b)


def get_question_and_answer():
    num_one = get_random_number()
    num_two = get_random_number()
    correct = gcd(num_one, num_two)
    return f"{num_one} {num_two}", str(correct)

def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)