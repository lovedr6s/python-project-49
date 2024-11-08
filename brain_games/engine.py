import prompt
from brain_games import const


def main(module_game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}')
    print(module_game.DESCRIPTION)
    for _ in range(const.ROUNDS):
        question, correct = module_game.play()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct}')")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
