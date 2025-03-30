#Problem Statement
#Fill out the function count_even(lst) which first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),
# and then prints the number of even numbers in the list. If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def count_even(lst: list[int]) -> int:
    """Returns the count of even numbers in the list."""
    return sum(1 for num in lst if num % 2 == 0)  # List comprehension for efficiency

def get_list_of_ints() -> list[int]:
    """Prompts user for integers until they press Enter, returning the list."""
    lst = []
    
    while True:
        user_input = input("Enter an integer or press Enter to stop: ").strip()

        if not user_input:  # Stop if the user presses Enter
            break

        try:
            lst.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return lst

def main() -> None:
    """Runs the program to collect numbers and count evens."""
    lst = get_list_of_ints()
    print(f"The number of even numbers in the list is: {count_even(lst)}")

if __name__ == "__main__":
    main()
