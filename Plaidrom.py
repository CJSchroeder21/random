# This is a basic program on Python
#
# Try to modify and run it and check out
# the output in the terminal below
#
# Happy coding! :-)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        word=[]
        if x < 0:
            return False
        y=[int(i) for i in str(x)]
        
        if y[:] == y[::-1]:
            return True
        else:
            return False

