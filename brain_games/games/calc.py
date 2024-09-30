from brain_games.utils import get_random_number
from brain_games.utils import get_random_element

DESCRIPTION = "What is the result of the expression?"


def play():
    operation = get_random_element(["+", "-", "*"])
    first_number = get_random_number(0, 10)
    second_number = get_random_number(0, 10)
    match operation:
        case "+":
            correct_answer = first_number + second_number
        case "-":
            correct_answer = first_number - second_number
        case "*":
            correct_answer = first_number * second_number

    return f"{first_number} {operation} {second_number}", str(correct_answer)
