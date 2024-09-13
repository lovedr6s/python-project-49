import random

DESCRIPTION = ("Answer \"yes\" if given number is prime."
" Otherwise answer \"no\".")


def play():
    first_number = random.randint(2, 10)
    correct = "yes"
    for char in range(2, first_number):
        if first_number % char == 0:
            correct = "no"
    return first_number, correct
