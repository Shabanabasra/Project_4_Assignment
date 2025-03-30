#Problem Statement
#Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


def subtract_seven(num: int) -> int:
    """Subtracts 7 from the given number and returns the result."""
    return num - 7

def main():
    """Gets user input, subtracts 7, and prints the result."""
    try:
        num = int(input("Enter a number: ").strip())  # Strip extra spaces & validate input
        print(f"The result after subtracting 7 is: {subtract_seven(num)}")
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
