def get_frist_element(lst):
    print(lst[0])

def main():
    lst = []
    
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst
lst = main()
get_frist_element(lst)