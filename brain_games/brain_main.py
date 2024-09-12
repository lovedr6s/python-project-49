from brain_games.scripts import brain_games


def main(module_game):
    name = brain_games.main()
    print(module_game.DESCRIPTION)
    won = True
    for _ in range(0, 3):
        question, correct = module_game.play()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == correct:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}')")
            print(f"Let's try again, {name}!")
            won = False
            break
    if won: print(f"Congradulations, {name}!")

if __name__ == "__main__":
    main()