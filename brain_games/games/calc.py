#!/usr/bin/env python3
from brain_games.utils import random

DESCRIPTION = "What is the result of the expression?"


def play():
    operations = ["+", "-", "*"]
    first_number = random(0, 10)
    second_number = random(0, 10)
    correct_operation = operations[random(0, 2)]
    match correct_operation:
        case "+":
            correct_answer = first_number + second_number
        case "-":
            correct_answer = first_number - second_number
        case "*":
            correct_answer = first_number * second_number

    return f"{first_number} {correct_operation} {second_number}", str(correct_answer)
