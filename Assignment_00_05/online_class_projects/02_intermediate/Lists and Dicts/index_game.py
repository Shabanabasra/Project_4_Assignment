# 🎮 Index Game
# A fun way to practice list indexing, slicing, and modification in Python!

def access_element(my_list, index):
    """Returns the element at the given index or an error message."""
    if 0 <= index < len(my_list):
        return f"✅ Element at index {index}: {my_list[index]}"
    return "❌ Index out of range!"

def modify_element(my_list, index, new_value):
    """Replaces the element at the given index with a new value."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"✅ Replaced '{old_value}' with '{new_value}'.\nUpdated list: {my_list}"
    return "❌ Index out of range!"

def slice_list(my_list, start, end):
    """Returns a sublist using slicing, with error handling."""
    if 0 <= start <= end <= len(my_list):
        return f"✅ Sliced list [{start}:{end}]: {my_list[start:end]}"
    return "❌ Invalid slice range!"

def show_list(my_list):
    """Displays the list with indices for better visualization."""
    print("\n📜 Current List:")
    for i, item in enumerate(my_list):
        print(f"  [{i}] {item}")

def main():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("🍓 Welcome to the Index Game!")
    print("Practice list access, modification, and slicing!\n")

    while True:
        show_list(my_list)

        print("\n🔧 Operations:\n  1. Access Element\n  2. Modify Element\n  3. Slice List\n  4. Exit")
        choice = input("👉 Choose an operation (1/2/3/4): ").strip()

        if choice == "1":
            try:
                index = int(input("Enter index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(my_list, start, end))
            except ValueError:
                print("❌ Please enter valid numbers.")

        elif choice == "4":
            print("👋 Exiting the game. Thanks for playing!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
