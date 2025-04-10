import random

NUM_ROUNDS = 5  # Number of rounds to play

def get_user_guess():
    while True:
        try:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                return guess
            print("Invalid input! Please enter either 'higher' or 'lower'.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            exit()

def play_round(round_num):
    print(f"\n--- Round {round_num} ---")
    
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is {user_number}")

    guess = get_user_guess()

    if (guess == "higher" and user_number > computer_number) or \
       (guess == "lower" and user_number < computer_number):
        print("You were right!", end=" ")
        print(f"The computer's number was {computer_number}.")
        return 1
    else:
        print("Aww, that's incorrect.", end=" ")
        print(f"The computer's number was {computer_number}.")
        return 0

def main():
    print("Welcome to the High-Low Game!")
    print("-----------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        score += play_round(round_num)
        print(f"Your score is now {score}\n")

    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Good job, you played really well!")
    else:
        print("😢 Better luck next time!")

if __name__ == '__main__':
    main()
