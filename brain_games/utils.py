from random import randint, choice
from brain_games import const


def get_random_number(begin=const.DEFAULT_BEGIN, end=const.DEFAULT_END):
    return randint(begin, end)


def get_random_element(elements=const.DEFAULT_LIST):
    return choice(elements)
