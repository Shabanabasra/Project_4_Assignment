#Problem Statement In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Function to read phone numbers from the user and store them in a dictionary
def read_phone_numbers():
    phonebook = {}  # Dictionary to store phone numbers

    while True:
        name = input("Enter name (or press Enter to stop): ").strip().lower()  # Convert to lowercase
        if name == "":
            break
        phone = input("Enter phone number: ").strip()
        phonebook[name] = phone  # Store name (in lowercase) and phone number

    return phonebook

# Function to print all saved phone numbers
def print_phonebook(phonebook):
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("\n--- Phonebook Entries ---")
        for name, phone in phonebook.items():
            print(f"{name.capitalize()}: {phone}")  # Capitalize the first letter for display

# Function to look up numbers in the phonebook
def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup (or press Enter to stop): ").strip().lower()
        if name == "":
            break
        if name in phonebook:
            print(f"Phone number for {name.capitalize()}: {phonebook[name]}")
        else:
            print(f"{name.capitalize()} not found in phonebook.")

# Main function to run the phonebook program
def main():
    phonebook = read_phone_numbers()  # Get user input
    print_phonebook(phonebook)  # Display all saved contacts
    lookup_numbers(phonebook)  # Allow user to search for contacts

# Run the program
if __name__ == "__main__":
    main()