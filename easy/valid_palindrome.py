#Given a string, determine if it is a palindrome, considering only
#alphanumeric characters and ignoring cases.

# easy solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c.lower() for c in s if c.isalnum()]
        return a == a[::-1]

# another naive solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j, decision = 0, len(s)-1, True
        while i<j and s:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            decision = s[i].lower() == s[j].lower()
            if not decision:
                return False
            j-=1
            i +=1
        return decision
# a better solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i<j:
            while not s[i].isalnum() and i<j:
                i+=1
            while not s[j].isalnum() and i<j:
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            j-=1
            i +=1
        return True
