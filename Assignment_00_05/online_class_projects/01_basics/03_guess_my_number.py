#Problem Statement
#Guess My Number
#I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
#Enter a new number: 25 Your guess is too low
#Enter a new number: 40 Your guess is too low
#Enter a new number: 45 Your guess is too low
#Enter a new number: 48 Congrats! The number was: 48



import random

def guess_my_number():
    """A number guessing game where the user tries to guess a random number between 1 and 99."""
    
    secret_number = random.randint(1, 99)  # Generate a random number
    print("🎯 I'm thinking of a number between 1 and 99. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: ").strip())  # Strip spaces and ensure valid input
            
            if guess < 1 or guess > 99:
                print("⚠️ Please enter a number between 1 and 99.")
                continue
            
            if guess < secret_number:
                print("📉 Your guess is too low.")
            elif guess > secret_number:
                print("📈 Your guess is too high.")
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break  # Exit loop when the correct number is guessed
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    guess_my_number()
