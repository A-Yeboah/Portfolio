# This game allows users to guess a specific number.
# Users are allowed 5 attempts.

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game. Enjoy!!")
    print("I am thinking of a number from 1 to 10.")

    # generate random number from 1 to 10
    number_to_guess = random.randint(1, 10)

    attempts = 5
    while attempts >= 1: 
        try:
            guess = int(input("Enter the number: "))
            attempts -= 1
            attempts_left = attempts 
          

            if guess < number_to_guess:
                print(f"Too low! You have {attempts_left} attempts left. Try again.")
            elif guess > number_to_guess:
                print(f"Too high! You have {attempts_left} attempts left. Try again.")
            else:
                print(f"Congratulations! You guessed it in {5-attempts_left} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()
