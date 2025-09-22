
#Create a Number Guessing Game
#Solution:
import random   # to generate random numbers
def play_game():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0  # counter for number of guesses

    print(" Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    # Step 2: Repeat until user guesses correctly
    while True:
        guess = input("Enter your guess: ")

        # Step 3: Validate input
        if not guess.isdigit():
            print("X Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Step 4: Compare guess with secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f" Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    play_game()
#Output :
 #Welcome to the Number Guessing Game!
#I have chosen a number between 1 and 100. Can you guess it?
#Enter your guess: 10
#Too low! Try again.
#Enter your guess: 20 30 
#X Please enter a valid number.
#Enter your guess:

