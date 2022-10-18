# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#at
# Happy coding! :-)
import random

import string
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
password="".join(password)

txt=input("Enter something to be coded!\n")
txt=txt.lower()
code=txt
text=list(txt)
code_list={}
encript=["e","y","q","7","$"]
t=0
for i in text:
    e1=random.choice(encript)
    #text=text.replace(text[t],e1)
    code_list[text[t]+str(t)]=e1
    text[t]=e1
    t+=1
print("".join(text))
print(f"Your password for the encription is {password}")

def unencrpt_code():
    attempts=0
    while attempts != 3:
        pass_word=input("To unencript, enter the password")
        if pass_word == password:
            unencrypt=[]
            for key, value in code_list.items():
                unencrypt.append(key[0])
            print("".join(unencrypt))
            break
        else:
            print("You failed")
            attempts+=1
            print(f"{3-attempts} attempts left" )
            

unencrpt_code()


