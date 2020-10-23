# Given a non-empty string s, you may delete at most one character.
#Judge whether you can make it a palindrome.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def Palindrome(s, i,j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return Palindrome(s, i+1, j) or Palindrome(s, i, j-1)
            i +=1
            j-=1
        return True

# Another very good solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0,len(s) -1
        while i<j:
            if s[i] != s[j]:
                one, two = s[i:j], s[i+1:j+1]
                return one == one[::-1] or two == two[::-1]
            i,j = i+1, j-1
        return True
