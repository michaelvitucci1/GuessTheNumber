
def make_initial_guess():
    invalid_guess = True
    while invalid_guess:
        try:
            guess = int(input("What is your first guess?\n"))
            invalid_guess = False
            return guess
        except ValueError:
            print("Please enter a valid integer.")


def make_guess(guesses_remaining, high_low):
    invalid_guess = True
    while invalid_guess:
        try:
            guess = int(input("Your guess was too " + high_low + ". You have " + str(guesses_remaining) +
                              " guesses remaining.\nPlease make another guess: \n"))
            invalid_guess = False
            return guess
        except ValueError:
            print("Please enter a valid integer.")
