#!/usr/bin/env python3
from brain_games.utils import random

DESCRIPTION = "What number is missing in the progression?"


def play():
    first_number = random(0, 10)
    progression_number = random(0, 10)
    choosen_number = random(0, 9)
    result = [first_number + i * progression_number for i in range(10)]
    correct = result[choosen_number]
    result[choosen_number] = ".."
    return ' '.join(map(str, result)), str(correct)
