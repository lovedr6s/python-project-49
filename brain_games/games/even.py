#!/usr/bin/env python3
import random


DESCRIPTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def play():
    number = random.randint(0, 100)
    correct_answer = ""
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return number, correct_answer
