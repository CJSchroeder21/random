# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)
num = int(input("Input a number!"))
i=0
while True:
    if i<=num:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
            i+=1
        if i%3==0:
            print("Fizz")
            i+=1
        if i%5==0:
            print("Buzz")
            i+=1
        print (i)
        i+=1
    
    
    
    