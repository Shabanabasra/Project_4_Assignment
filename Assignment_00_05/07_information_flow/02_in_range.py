#Problem Statement
#Implement the following function which takes in 3 integers as parameters:
#def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n: int, low: int, high: int) -> str:
    """Returns a message indicating whether n is in the inclusive range [low, high]."""
    return f"✅ {n} is in the range of {low} and {high}." if low <= n <= high else f"❌ {n} is NOT in the range of {low} and {high}."

def main():
    try:
        # Get user input safely
        n = int(input("Enter a number (n): ").strip())
        low = int(input("Enter the lower bound (low): ").strip())
        high = int(input("Enter the upper bound (high): ").strip())

        # Print result
        print(in_range(n, low, high))

    except ValueError:
        print("❌ Invalid input! Please enter valid integers.")

if __name__ == "__main__":
    main()