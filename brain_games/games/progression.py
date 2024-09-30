from brain_games.utils import get_random_number

DESCRIPTION = "What number is missing in the progression?"


def play():
    first_number = get_random_number(0, 10)
    progression_number = get_random_number(0, 10)
    choosen_number = get_random_number(0, 9)
    result = [first_number + i * progression_number for i in range(10)]
    correct = result[choosen_number]
    result[choosen_number] = ".."
    return ' '.join(map(str, result)), str(correct)
