#!/usr/bin/env python3
from brain_games.utils import random

DESCRIPTION = ("Answer \"yes\" if given number is prime. "
               "Otherwise answer \"no\".")


def play():
    first_number = random(2, 10)
    correct = "yes"
    for char in range(2, first_number):
        if first_number % char == 0:
            correct = "no"
    return first_number, correct
