import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def play():
    one_numbers = []
    second_numbers = []
    num_one = random.randint(0, 100)
    num_two = random.randint(0, 100)

    for num in range(1, num_one + 1):
        if num_one % num == 0:
            one_numbers.append(num)


    for num_second in range(1, num_two + 1):
        if num_two % num_second == 0:
            second_numbers.append(num_second)


    for count in one_numbers:
        for count_second in second_numbers:
            if count == count_second:
                correct = count 


    return f"{num_one} {num_two}", str(correct)

    
