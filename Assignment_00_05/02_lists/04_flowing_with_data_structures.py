def main(my_list,msg):
   for i in range(3):
      my_list.append(msg)
def man():
    msg = input("Enter a msg ")
    mylist = []
    print(f"Before my list {mylist}")
    main(mylist,msg)
    print(f"after my list {mylist}")
man()