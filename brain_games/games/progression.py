from brain_games.utils import get_random_number
from brain_games import engine

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    first_number = get_random_number()
    progression_number = get_random_number()
    choosen_number = get_random_number()
    result = [first_number + i * progression_number for i in range(10)]
    correct = result[choosen_number]
    result[choosen_number] = ".."
    return ' '.join(map(str, result)), str(correct)

def start_game():
    engine.run_game(DESCRIPTION, get_question_and_answer)
