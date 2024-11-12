from brain_games.utils import get_random_number, get_random_element
from brain_games import engine

DESCRIPTION = "What is the result of the expression?"


def get_random_operation():
    return get_random_element()


def get_question_and_answer():
    operation = get_random_operation()
    first_number = get_random_number()
    second_number = get_random_number()

    match operation:
        case "+":
            correct_answer = first_number + second_number
        case "-":
            correct_answer = first_number - second_number
        case "*":
            correct_answer = first_number * second_number

    return f"{first_number} {operation} {second_number}", str(correct_answer)


def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)