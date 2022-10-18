# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)
import string
import random
numbers=["0","1","2","3","4","5","6","7","8","9"]
norl=[]
password=[]
n=int(input("How many characters for the password\n"))
def random_pass():
    for _ in range(n):
        norl=[]
        y=random.choice(numbers)
        x=random.choice(string.ascii_letters)
        norl.append(y)
        norl.append(x)
        password.append(random.choice(norl))
        norl=[]
        
        
random_pass()
print("".join(password))