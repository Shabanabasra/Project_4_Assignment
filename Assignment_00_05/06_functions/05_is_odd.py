# Problem Statement
#10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd



def is_odd(value: int) -> bool:
    """Returns True if the number is odd, otherwise False."""
    return value % 2 == 1

def is_even(value: int) -> bool:
    """Returns True if the number is even, otherwise False."""
    return value % 2 == 0

def main() -> None:
    """Prints whether numbers from 10 to 19 are even or odd."""
    for num in range(10, 20):  # Fixes the range
        if is_odd(num):
            print(f"{num} odd")
        else:
            print(f"{num} even")

if __name__ == "__main__":
    main()