#Problem Statement
# Write a function that takes two numbers and finds the average between the two.

def average(num1: float, num2: float) -> float:
    """Returns the average of two numbers."""
    return (num1 + num2) / 2

def main() -> None:
    """Calculates and prints the averages of given numbers."""
    avg1 = average(2, 4)
    avg2 = average(10, 20)
    final_avg = average(avg1, avg2)

    print(f"Average 1: {avg1:.2f}")
    print(f"Average 2: {avg2:.2f}")
    print(f"Final Average: {final_avg:.2f}")

if __name__ == "__main__":
    main()