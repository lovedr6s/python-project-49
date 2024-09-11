import random

def main():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    count = 0
    won = True
    while count < 3:
        rand = random.randint(0, 100)
        print(f"Question: {rand}")
        inp = input("Your answer: ")
        if rand % 2 == 0 and inp == "yes":
            print('Correct!')
            count += 1
        elif rand % 2 != 0 and inp == "no":
            print("Correct!")
            count += 1
        else:
            if inp == "yes":
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                won = False
                break
                
            elif inp == "no":
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                won = False
                break
    if won: print("Congratulations, Bill!") #Поменяй расположениею Должно выводить только при правильном ответе а не при плохой тоже


if __name__ == "__main__":
    main()
    