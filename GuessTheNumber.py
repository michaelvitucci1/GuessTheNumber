import random
from MakeGuess import *

new_game = True
high = "high"
low = "low"
name = input("What is your name? ").title()
print("Hello " + name + "! I am thinking of a number 1 - 20. You will have 3 guess to determine my number. ")
while new_game:
    guesses_remaining = 2
    game_start = True
    number = int(random.randint(1, 20))

    guess = int(make_initial_guess())

    while game_start:

        if guess == number:
            game_start = False
            print("The number was " + str(number) + ". Congratulations you win!")
            play_again = str(input("Would you like to play again, Yes or No:\n")).upper()
            if play_again == "YES":
                break

            else:
                new_game = False
                break

        if guess < number and guesses_remaining >= 1:
            guess = make_guess(guesses_remaining, low)
            guesses_remaining -= 1

        if guess > number and guesses_remaining >= 1:
            guess = make_guess(guesses_remaining, high)
            guesses_remaining -= 1

        if guess != number and guesses_remaining == 0:
            game_start = False
            print("Sorry, you are out of guesses. The number was " + str(number) + ".")
            play_again = str(input("Would you like to play again, Yes or No:\n")).upper()
            if play_again == "YES":
                break

            else:
                new_game = False
                break
print("Thanks for playing!")
