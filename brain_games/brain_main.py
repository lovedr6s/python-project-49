import prompt


def main(module_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(module_game.DESCRIPTION)
    won = True
    for _ in range(0, 3):
        question, correct = module_game.play()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(."
                  "Correct answer was '{correct}')")
            print(f"Let's try again, {name}!")
            won = False
            break
    if won:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
