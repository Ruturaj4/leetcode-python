#You are given a string s containing lowercase English letters, and a matrix shift,
#where shift[i] = [direction, amount]:

#direction can be 0 (for left shift) or 1 (for right shift).
#amount is the amount by which string s is to be shifted.
#A left shift by 1 means remove the first character of s and append it to the end.
#Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
#Return the final string after all operations.

# my initial attempt
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in shift:
            if i[0] == 1:
                for j in range(i[1]):
                    last = s[-1]
                    s = s[:-1]
                    s = last + s
            else:
                for j in range(i[1]):
                    first = s[0]
                    s = s[1:]
                    s = s+first
        return s

# another solution
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amt in shift:
            amt %= len(s)
            if not direction:
                s = s[amt:] + s[:amt]
            else: s = s[-amt:] + s[:-amt]
        return s

# another solution
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0
        for i,j in shift:
            if i: move += j
            else: move -= j
        move %= len(s)
        return s[-move:] + s[:-move]
