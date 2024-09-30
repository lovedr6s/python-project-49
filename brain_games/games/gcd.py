from brain_games.utils import get_random_number
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return math.gcd(a, b)


def play():
    num_one = get_random_number(1, 10)
    num_two = get_random_number(1, 10)
    correct = gcd(num_one, num_two)
    return f"{num_one} {num_two}", str(correct)
