# Function to repeatedly double a number until it reaches or exceeds 100
def double_until_100():
    """
    Asks the user for a number, then doubles it repeatedly until it reaches 100 or more.
    Prints the sequence in a single line.
    """
    while True:
        try:
            curr_value = int(input("Enter a number: "))  # Get user input
            if curr_value <= 0:  # Ensure the number is positive
                print("Please enter a positive number.")
                continue
            break  # Exit loop if valid input
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # List to store the sequence
    doubled_values = []

    # Continue doubling until curr_value reaches or exceeds 100
    while curr_value < 100:
        curr_value *= 2  # Double the number
        doubled_values.append(curr_value)  # Store in list

    # Print the sequence in a single line
    print(" ".join(map(str, doubled_values)))

# Run the function
if __name__ == "__main__":
    double_until_100()