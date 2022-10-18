# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)

import random
import time

DICE = [1,2,3,4,5,6]
dice_rolled = []
roll_text=["Rolling",".",".","."]

def intro():
    print("This is a dice roller.")
    time.sleep(1)

def rolling(text):
    for x in text:
        print(x, end="", flush=True)
        time.sleep(0.75)
    


def roll():
    while True:
        user_in = input("Would you like to roll? (Y/N)\nEnter S if you want to see past results.\n")
        user_in = user_in.lower()
        if user_in == "y":
            result = random.choice(DICE)
            dice_rolled.append(result)
            rolling(roll_text)
            print(f"The result is {result}!")
            time.sleep(1)
            roll()
        elif user_in == "n":
            print("Bye")
            break
        elif user_in == "s":
            print(*dice_rolled, sep=", ")
            time.sleep(1)
            roll()
        else:
            print("Invaild enter.")
            roll()
        break

intro()
roll()