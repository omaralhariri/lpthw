from sys import exit
import random

print("Guess what number in my mind (0 - 10)")

guesses = []

def play():
    num = random.randint(0, 10)
    guess = int(input("Enter a nember > "))

    if guess <= 10:
        if guess == num:
            print("Your guess is right")
            guesses.append(guess)
            print("Your guesses:", guesses)
            exit(0)
        else:
            print("That's not it.")
            guesses.append(guess)
            print("Play again?")
            playAgain = input("Yes or No? ")
            playAgain = str.lower(playAgain)

            if playAgain == "yes" or playAgain == "y":
                play()
            else:
                die("Goodbye!")
                exit(0)
        
    else:
        die("Not a valid number!")
        play()

def die(msg):
    print(msg)

play()