#Problem Statement There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.
#W#rite a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
#Here is an example run of the program (user input is in bold italics):

#How many (apple) do you want?: 2
#How many (durian) do you want?: 0
#How many (jackfruit) do you want?: 1
#How many (kiwi) do you want?: 0
#How many (rambutan) do you want?: 1
#How many (mango) do you want?: 3
#Your total is $99.5


# Function that asks the user how many of each fruit they want to buy.
def fruit_shop():
    # Dictionary of fruits and their prices
    fruits = {
        "apple": 15,
        "banana": 8,
        "orange": 10,
        "grape": 4,
        "kiwi": 5,
        "mango": 10,
        "pear": 7,
        "payaya": 8,
        "rambutan": 5,
        "jackfruit": 50,
    }

    total_cost = 0  # Variable to store the total cost of the fruits bought
    purchase_summary = {}  # Dictionary to track fruit purchases

    # Loop through the fruits dictionary
    for fruit_name, price in fruits.items():
        while True:  # Loop until valid input is entered
            try:
                fruit_bought = int(input(f"How many {fruit_name} (${price} each) do you want to buy? "))
                if fruit_bought < 0:
                    print("Please enter a valid number (0 or more).")
                    continue
                break  # Exit loop if valid input
            except ValueError:
                print("Invalid input! Please enter a number.")

        if fruit_bought > 0:
            purchase_summary[fruit_name] = fruit_bought  # Store the number of fruits bought
        total_cost += price * fruit_bought  # Calculate total cost

    # Display a summary of the purchase
    print("\n--- Purchase Summary ---")
    if purchase_summary:
        for fruit, quantity in purchase_summary.items():
            print(f"{quantity} x {fruit.capitalize()} (${fruits[fruit]} each) = ${quantity * fruits[fruit]}")
    else:
        print("No fruits purchased.")

    # Print the total cost with 2 decimal places
    print(f"\nYour total cost is **${total_cost:.2f}**")


# Run the program
if __name__ == "__main__":
    fruit_shop()