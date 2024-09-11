import random

DESCRIPTION = "What is the result of the expression?"

def play():
    operation = ["+", "-", "*"]
    one = random.randint(0, 10)
    two = random.randint(0, 10)
    correct_operation = operation[random.randint(0,2)]
    if correct_operation == "+":
        correct = one + two
    elif correct_operation == "-":
        correct = one - two
    elif correct_operation == "*":
        correct = one * two
    return f"{one} {correct_operation} {two}", str(correct)

