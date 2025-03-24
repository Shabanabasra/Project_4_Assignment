import random
one_side = 6
def roll_dice():
    die1 = random.randint(1,one_side)
    die2 = random.randint(1,one_side)
    total = die1 + die2
    print(f"Total of The Two dice {total}")

def main():
    die1 = 10
    print("die1 in main() starts as :" + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() starts as :" + str(die1))

main()