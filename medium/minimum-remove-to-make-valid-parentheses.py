# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')',
# in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        open = 0
        for c in s:
            if c == "(":
                open +=1
            elif c == ")":
                if open == 0: continue
                open -=1
            temp.append(c)
        result = []
        for c in temp[::-1]:
            if c == "(" and open>0:
                open -=1
                continue
            result.append(c)
        return result[::-1]

# another approch
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        temp = []
        for i,c in enumerate(s):
            if c == "(":
                temp.append(i)
            elif c == ")":
                if temp: temp.pop()
                else: s[i]=""
        for i in temp:
            s[i]=""
        return "".join(s)
