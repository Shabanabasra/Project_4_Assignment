# Problem Statement
#Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!
#Here's a sample run (user input is in blue):Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12


def print_divisors(num: int) -> None:
    """Prints all divisors of a given number."""
    divisors = [str(n) for n in range(1, num + 1) if num % n == 0]
    print(f"Here are the divisors of {num}: " + " ".join(divisors))

def main() -> None:
    """Gets user input and prints the divisors of the given number."""
    while True:
        try:
            num = int(input("Enter a number: "))
            if num <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_divisors(num)

if __name__ == "__main__":
    main()
