#Problem Statement
#Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements The first even number is 0:0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

# Function to print the first 20 even numbers
def even_numbers():
    """
    Prints the first 20 even numbers in a single line.
    """
    even_list = [n * 2 for n in range(20)]  # Generate even numbers using list comprehension
    print(" ".join(map(str, even_list)))  # Print all numbers in one line

# Run the function
if __name__ == "__main__":
    even_numbers()