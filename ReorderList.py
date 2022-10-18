# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
digitlist=[]   
letlist=[]
for x in logs:
    y=x.split()[1]
    if y.isdigit():
        digitlist.append(x)
        
    if y.isalpha():
        letlist.append(x)
        

print(letlist + digitlist)
    


