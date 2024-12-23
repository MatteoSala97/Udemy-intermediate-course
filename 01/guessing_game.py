import random

def guessing_game():
    # Pick a random integer from 1 to 100
    number_to_guess = random.randint(1, 100)
    guesses_taken = 0
    max_guesses = 5

    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess it?")

    while guesses_taken < max_guesses:
        try:
            guess = int(input(f"Guess {guesses_taken + 1}: "))
            guesses_taken += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {guesses_taken} guesses.")
                return
        except ValueError:
            print("Please enter a valid integer.")

    print(f"Sorry, you've used all {max_guesses} guesses. The number was {number_to_guess}.")

# Run the guessing game
guessing_game()
