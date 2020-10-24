# Given a string, determine if a permutation of the string could form a palindrome.

# my initial solution in one line
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return len([x for x in collections.Counter(s).values() if x%2!=0])<=1

# this will improve the runtime
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return len([x for x in collections.Counter(s).values() if x%2])<=1

# one more solution
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(x%2 for x in collections.Counter(s).values())<=1

# another solution
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = (s.count(k)%2 for k in set(s))
        return sum(temp)<=1

# slightly modifying the above solution
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(s.count(k)%2 for k in set(s))<=1
