# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)
target=20
nums=[10,2,8,10]
num=[]
z=-1
for x in nums:
    z+=1
    y=target-x
    if y in nums:
        print("here,maybe")
        in1=z
        print(in1)
        in2=nums.index(y)
        print(in2)
        if in1==in2:
            continue 
        else:
            num.append(in1)
            num.append(in2)
            num.sort()
            print(num)
            break
    
    else:
        continue 
