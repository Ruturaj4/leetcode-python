#Given two non-negative integers num1 and num2 represented as string,
#return the sum of num1 and num2.

# initial attempt
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result1 = 0
        for i in num1:
            result1= 10*result1+dic[i]
        result2 = 0
        for i in num2:
            result2= 10*result2+dic[i]
        return str(result1 + result2)

# another attempt:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result,carry = [],0
        i,j = len(num1)-1,len(num2)-1
        while i>=0 or j>=0:
            n1 = dic[num1[i]] if i>=0 else 0
            n2 = dic[num2[j]] if j>=0 else 0
            temp = n1+n2+carry
            result.append(temp%10)
            carry = temp//10
            i -= 1
            j-=1
        if carry:
            result.append(carry)
        return "".join([str(i) for i in result])[::-1]
#another solution using lists
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result,carry = [],0
        i,j = list(num1),list(num2)
        while len(i)>0 or len(j)>0:
            n1 = dic[i.pop()] if len(i)>0 else 0
            n2 = dic[j.pop()] if len(j)>0 else 0
            temp = n1+n2+carry
            result.append(temp%10)
            carry = temp//10
        if carry:
            result.append(carry)
        return "".join([str(i) for i in result])[::-1]

# another solution using ord
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result,carry = [],0
        i,j = list(num1),list(num2)
        while len(i)>0 or len(j)>0:
            n1 = ord(i.pop())-ord("0") if len(i)>0 else 0
            n2 = ord(j.pop())-ord("0") if len(j)>0 else 0
            temp = n1+n2+carry
            result.append(temp%10)
            carry = temp//10
        if carry:result.append(carry)
        return "".join([str(i) for i in result])[::-1]
