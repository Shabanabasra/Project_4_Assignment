def main():
    lst = [] 

    val = input("Enter a value: ") 
    while val: 
        lst.append(val) 
        val = input("Enter a value: ") 

    print("Here's the list:", lst)
main()