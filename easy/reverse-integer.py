#Given a 32-bit signed integer, reverse digits of an integer.

#Note:
#Assume we are dealing with an environment that could only store integers within
#the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
#assume that your function returns 0 when the reversed integer overflows.

# my initial attempt
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        reverse = 0
        while x >0:
            reverse = reverse*10+x%10
            x//=10
        if reverse>2**31:
            return 0
        return reverse*-1 if negative else reverse

# another easy solution in python
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = int("-"+s[1:][::-1]) if s[0]=="-" else int(s[::-1])
        return 0 if s>2**31 or s<-2**31 else s
