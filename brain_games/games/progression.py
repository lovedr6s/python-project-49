from brain_games.utils import get_random_number
from brain_games import engine

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    first_number = get_random_number()
    progression_number = get_random_number()
    hidden_index = get_random_number(0, 9)
    progression = [first_number + i * progression_number for i in range(10)]
    correct_answer = progression[hidden_index]
    question = ' '.join(".." if i == hidden_index else str(num) for i,
                        num in enumerate(progression))

    return question, str(correct_answer)


def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)
