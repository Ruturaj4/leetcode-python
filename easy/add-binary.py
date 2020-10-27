#Given two binary strings, return their sum (also a binary string).

#The input strings are both non-empty and contains only characters 1 or 0.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result,carry = [],0
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0:
            digit1 = a[i] if i>=0 else "0"
            digit2 = b[j] if j>=0 else "0"
            if digit1=="1" and digit2=="1":
                if carry == 1:
                    result.append("1")
                else:
                    result.append("0")
                carry =1
            elif digit1 =="0" and digit2=="0":
                if carry == 1:
                    result.append("1")
                else:
                    result.append("0")
                carry =0
            else:
                if carry ==1:
                    result.append("0")
                    carry =1
                else:
                    result.append("1")
                    carry =0
            i-=1
            j-=1
        return str(carry)+"".join(result[::-1]) if carry else "".join(result[::-1])

# very simple
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+int(b,2))

# classic algorithm
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a,b = a.zfill(n), b.zfill(n)
        carry, result = 0, []
        for i in range(n-1,-1,-1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry +=1
            if carry %2 == 1:
                result.append("1")
            else:
                result.append("0")
            carry //=2
        if carry:
            result.append("1")
        return "".join(result[::-1])
