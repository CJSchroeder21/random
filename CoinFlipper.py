# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)

import random
import time

coin = ["Heads", "Tails"]
flipped= []
flipping_text=["Flipping", ".",".","."]

def intro():
    print("This is a coin flipper game!")

def flipping(text):
    for x in text:
        print(x, end="",flush=True)
        time.sleep(1)
    
def flip():
    while True:
        player_in=input("Would you like to play?\nYes. No . or S for past flips\n")
        player_in = player_in.lower()  
        if player_in == "yes":
            flipping(flipping_text)
            result=random.choice(coin)
            print(f"The result was {result}!")
            flipped.append(result)
            time.sleep(2)
            player_in == 0
            flip()
    
        elif player_in == "no":
            print("See you again!")
            player_in == 0
            break
            
        elif player_in == "s":
            print(", ".join(flipped))
            time.sleep(2)
            player_in==0
            flip()
                
        elif player_in != "s" or "no" or "yes":
            print("not vaild")
            player_in==0
            flip()
        break
          
        
intro()
flip()