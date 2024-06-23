import random

def guessGame(secretNum):
    guess = -1
    attemps = 0
    try:
        guess = int(input("Enter a num to guess "))
        attemps+=1
        while guess!=secretNum:
            if guess<secretNum:
                print("It's too low")
            elif guess>secretNum:
                print("It's too high")
            guess = int(input("Enter a num to guess "))
            attemps+=1
        print(f"You won! times of tries: {attemps} and the guess num was {guess}")
    except ValueError:
        print("You stupid its guess game its with numbers")
playAgain = "Y"
while playAgain=="Y":
    num = random.randint(0,100)
    guessGame(num)
    print("Do you want to play again?(Y/N) Y for yes N for no")
    playAgain = input()
    playAgain.upper()
    if(playAgain=="N"):
        print("Thanks for playing hope to see you later!")
        break

