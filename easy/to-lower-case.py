#Implement function ToLowerCase() that has a string parameter str,
#and returns the same string in lowercase.

class Solution:
    def toLowerCase(self, str: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        temp = dict(zip(upper, lower))
        return "".join([temp[x] if x in temp else x for x in str])
