max_hieght:int = 50
def main():
    while True:
        height = input("Enter Your Height (Press Enter to Stop):")

        if height == "":
            print("Exiting the program...")
            break
        try:
            height = int(height)
            if height >= max_hieght:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Invalid input! Please enter a number.")

main()