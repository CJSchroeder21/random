# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)

mag="abgtfhfbbbba"
ran="fihjjjjei"
mag1="hjibagacbhadfaefdjaeaebgi"
y=[]
count=0
for x in mag1:
    if x in ran:
        y.append(x)
        print(y)
if len(y) < len(ran):
    print("false")
for x in ran:
    if x not in y:
        print("no")
        continue
    if x in y:
        print("yes")
        count+=1
if count==len(ran):
    print("True")
else:
    print("False")