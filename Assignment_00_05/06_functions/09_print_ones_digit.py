# Problem Statement
#Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!
#Here's a sample run (user input is in blue): Enter a number: 42 The ones digit is 2


def print_ones_digit(num: int) -> None:
    """Prints the ones digit of the given integer."""
    ones_digit = abs(num) % 10  # Use abs() to handle negative numbers correctly
    print(f"The ones digit of {num} is {ones_digit}.")

def main() -> None:
    """Gets user input and prints the ones digit of the number."""
    while True:
        try:
            num = int(input("Enter a number: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print_ones_digit(num)

if __name__ == "__main__":
    main()
