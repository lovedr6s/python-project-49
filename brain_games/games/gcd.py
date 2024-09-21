#!/usr/bin/env python3
from brain_games.utils import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    return math.gcd(a, b)


def play():
    num_one = random(1, 10)
    num_two = random(1, 10)
    correct = gcd(num_one, num_two)
    return f"{num_one} {num_two}", str(correct)
