#Given a string S, return the number of substrings that have only one
#distinct letter.

# naive solution
class Solution:
    def countLetters(self, S: str) -> int:
        count = 0
        for i in range(len(S)):
            for j in range(i, len(S)):
                if not S[i] == S[j]:
                    break
                count+=1
        return count

# another naive solution
class Solution:
    def countLetters(self, S: str) -> int:
        count = 0
        i = j = 0
        s = len(S)
        while i<s and j<s:
            if not S[i] == S[j]:
                i+=1
                j=i
            else:
                count+=1
                j+=1
                if j==s:
                    i+=1
                    j=i
        return count

# much better solution
class Solution:
    def countLetters(self, S: str) -> int:
        count, total = 1,1
        for i in range(1, len(S)):
            if S[i]!=S[i-1]:
                count =1
            else:
                count+=1
            total+=count
        return total

# another solution - using an intuition - n(n+1)/2
class Solution:
    def countLetters(self, S: str) -> int:
        s = len(S)
        final,i,j = 0,1,0
        while i<=s and j<s:
            if (i==s) or (S[i] != S[j]):
                final += (i-j+1)*(i-j)//2
                j = i
            i+=1
        return final
