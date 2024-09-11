import random
from brain_games.scripts import brain_games

name = brain_games.main()

def main():
    print("What is the result of the expression?")

    count = 0
    while count < 3:
        number_one = random.randint(0, 100)
        number_two = random.randint(0, 100)
        middle_random = random.randint(0, 2)
        match middle_random:
            case 0:
                middle_show = "+"
                middle = number_one + number_two
            case 1:
                middle_show = "-"
                middle = number_one - number_two
            case 2:
                middle_show = "*"
                middle = number_one * number_two
        print(f"Question: {number_one} {middle_show} {number_two}")
        answer = input("Your answer: ")
        if int(answer) == middle:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{middle}'")
            print(f"Let's try again, {name}")
            break
    if count == 3: print(f"Congradulations, {name}!")


if __name__ == "__main__":
    main()
