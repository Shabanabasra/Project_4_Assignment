#Problem Statement
#Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.
#Here's a sample run of the program (user input is in blue):Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!


def print_multiple(message: str, repeats: int) -> None:
    """Prints a message multiple times."""
    print("\n".join([message] * repeats))  # Efficient way to print multiple times

def main() -> None:
    """Gets user input and prints the message the specified number of times."""
    message = input("Please type a message: ")

    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: "))
            if repeats < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_multiple(message, repeats)

if __name__ == "__main__":
    main()
