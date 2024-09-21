#!/usr/bin/env python3
from brain_games.utils import random

DESCRIPTION = "What is the result of the expression?"


def play():
    operation = ["+", "-", "*"]
    one = random(0, 10)
    two = random(0, 10)
    correct_operation = operation[random(0, 2)]
    match correct_operation:
        case "+":
            correct = one + two
        case "-":
            correct = one - two
        case "*":
            correct = one * two

    return f"{one} {correct_operation} {two}", str(correct)
