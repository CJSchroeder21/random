# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
import random# Happy coding! :-)
user = 0
com=0
ran_list=["1","2","3"]
x=0
print("This is a Rock, Paper, Scissors game!")#print this is a RPS game (title)
print("Enter 'e' to Exit.")
print("(1)Rock")
print("(2)Paper")
print("(3)Scissors")
user=(str(input("Enter a Number. ")))

while user != "e":
    if user =="1":
        print("You picked Rock.")
        com=(random.choice(ran_list))
        if com == "1":
            print("Computer picked Rock.")
            print("Its a draw. Try again!")
            user=0
        elif com == "2":
            print("Computer picked Paper.")
            print("You lost. Try again.")
            user=0
        elif com == "3":
            print("Compter picked Scissors.")
            print("You Won!")
            user=0
    if user == "2":
        print("You picked Paper.")
        com=(random.choice(ran_list))
        if com == "2":
            print("Computer picked Paper.")
            print("Its a draw. Try again!")
            user=0
        elif com == "1":
            print("Computer picked Rock.")
            print("You Won!")
            user=0
        elif com == "3":
            print("Computer picked Scissors.")
            print("You lost. Try again.")
            user=0
    if user == "3":
        print("You picked Scissors.")
        com=(random.choice(ran_list))
        if com == "2":
            print("Computer picked Paper.")
            print("You Win!")
            user=0
        elif com == "1":
            print("Computer picked Rock.")
            print("You lost. Try again")
            user=0
        elif com == "3":
            print("Computer picked Scissors.")
            print("Its a draw. Try again.")
            user=0
    
    if user==0:
        x=input("Enter a key to continue. ")
        print("Enter 'e' to exit.")
        print("This is a Rock, Paper, Scissors game!")#print this is a RPS game (title)
        print("(1)Rock")
        print("(2)Paper")
        print("(3)Scissors")
        user=(str(input("Enter a Number. ")))
    else:
        print("Invalid input. Try again")
        user=0

        
else:
   print("Good Bye")
#output pick rock, paper, or scissors 
#input for user = 1,2,3
#if 1, they picked rock
#if 2 they picked paper
#if 3 they picked scissors 
#if input is not 1,2,3, error and pick again 
#after input is good make computer pick 
#random number between 1-3 picks computers choice 
#output results of game (user input vs computer random number
#restat game 
#if user wants to end program they input exit. 


