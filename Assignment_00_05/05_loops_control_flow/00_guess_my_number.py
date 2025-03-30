#Problem Statement Guess My Number I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low Enter a new number: 45 Your guess is too low Enter a new number: 48 Congrats! The number was: 48


import random

def guess_my_number():
    """
    A simple number guessing game where the player must guess a randomly generated number
    within a given range. Provides hints until the correct number is guessed.
    """
    # Define the range for the random number
    min_number = 1
    max_number = 99

    # Generate the secret number
    secret_number = random.randint(min_number, max_number)

    print(f"\n🎯 I'm thinking of a number between {min_number} and {max_number}. Try to guess it!")

    attempts = 0  # Count the number of guesses

    while True:
        try:
            # Get user input and ensure it's a valid integer
            guess = int(input("Enter your guess: "))
            
            # Validate guess is within range
            if guess < min_number or guess > max_number:
                print(f"⚠️ Please enter a number between {min_number} and {max_number}.")
                continue

            attempts += 1  # Increase attempt count
            
            # Check the guess
            if guess < secret_number:
                print("⬆️ Your guess is too low. Try again.")
            elif guess > secret_number:
                print("⬇️ Your guess is too high. Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} attempts. The number was {secret_number}.")
                break  # Exit the loop when the correct number is guessed

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_my_number()