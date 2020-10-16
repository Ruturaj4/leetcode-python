# Given a string s, find the length of the longest
# substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j, i, maximum, temp = 0, 0, 0, set()
        if s:
            while j<len(s):
                if s[j] not in temp:
                    temp.add(s[j])
                    maximum = max(len(temp), maximum)
                    j+=1
                else:
                    temp.remove(s[i])
                    i+=1
        return maximum
