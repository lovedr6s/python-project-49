#!/usr/bin/env python3
from brain_games.utils import random


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def play():
    number = random(0, 100)
    return number, "yes" if number % 2 == 0 else "no"
