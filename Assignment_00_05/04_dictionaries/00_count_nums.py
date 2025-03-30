#Problem Statement This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.
#An example run of the program looks like this (user input is in blue):Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# Function to get user input and store numbers in a list
def get_user_numbers():
    user_numbers = []  # List to store user inputs
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":  # Stop when user presses Enter
            break
        try:
            number = int(user_input)  # Convert input to integer
            user_numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return user_numbers

# Function to count occurrences of numbers using a dictionary
def count_numbers(num_list):
    num_dict = {}  # Dictionary to store counts
    for num in num_list:
        num_dict[num] = num_dict.get(num, 0) + 1  # Increment count
    return num_dict

# Function to print the count of each number
def print_count(num_dict):
    for num in sorted(num_dict):  # Sorting for better readability
        print(f"{num} appears {num_dict[num]} times.")

# Main function to execute the program
def main():
    user_numbers = get_user_numbers()  # Get numbers from user
    num_dict = count_numbers(user_numbers)  # Count occurrences
    print_count(num_dict)  # Print results

# Run the program
if __name__ == "__main__":
    main()