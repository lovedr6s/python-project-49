import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def play():
    num_one = 5#random.randint(1, 10)
    num_two = 10#random.randint(1, 10)
    
    correct = gcd(num_one, num_two)
    
    return f"{num_one} {num_two}", str(correct)
