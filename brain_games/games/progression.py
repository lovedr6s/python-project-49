import random

DESCRIPTION = "What number is missing in the progression?"


def play():
    first_number = random.randint(0, 10)
    working_number = random.randint(0, 10)
    result = []
    choosen_number = random.randint(0, 9)
    for _ in range(0, 10):
        result.append(first_number)
        first_number += working_number
    correct = result[choosen_number]
    result[choosen_number] = ".."
    return ' '.join(str(el) for el in result), str(correct)
