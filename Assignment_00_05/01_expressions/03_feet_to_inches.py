INCHES_IN_FOOT: int = 12

def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_IN_FOOT
    print("That is", inches, "inches!")

main()