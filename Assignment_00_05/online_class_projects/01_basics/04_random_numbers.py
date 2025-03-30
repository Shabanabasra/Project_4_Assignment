#Problem Statement
#Print 10 random numbers in the range 1 to 100.
#Here is an example run:
#45 79 61 47 52 10 16 83 19 12
#Each time you run your program you should get different numbers
#81 76 70 1 27 63 96 100 32 92
#Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:
#value = random.randint(1, 6)



import random

def generate_random_numbers(count=10, min_value=1, max_value=100):
    """Generates and prints 'count' random numbers in the range 'min_value' to 'max_value'."""
    
    random_numbers = [random.randint(min_value, max_value) for _ in range(count)]  # Generate numbers
    print(*random_numbers)  # Print numbers in a single line, space-separated

if __name__ == "__main__":
    generate_random_numbers()
