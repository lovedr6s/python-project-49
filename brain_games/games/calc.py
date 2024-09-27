#!/usr/bin/env python3
from brain_games.utils import random
from brain_games.const import OPERATIONS

DESCRIPTION = "What is the result of the expression?"


def play():
    operations = OPERATIONS
    first_number = random(0, 10)
    second_number = random(0, 10)
    operation = operations[random(0, 2)]
    match operation:
        case "+":
            correct_answer = first_number + second_number
        case "-":
            correct_answer = first_number - second_number
        case "*":
            correct_answer = first_number * second_number

    return f"{first_number} {operation} {second_number}", str(correct_answer)
