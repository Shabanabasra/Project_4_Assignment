def main():
    # Step 1: Create a list with given fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Step 2: Print the original list and its length
    print("Original fruit list:", fruit_list)
    print("Length of fruit list:", len(fruit_list))
    
    # Step 3: Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Step 4: Print the updated list
    print("Updated fruit list after adding 'mango':", fruit_list)

    # Optional Bonus: Show index of a fruit (e.g., 'orange')
    if 'orange' in fruit_list:
        print("Index of 'orange':", fruit_list.index('orange'))

if __name__ == "__main__":
    main()
