class Solution:
    def titleToNumber(self, s: 'str') -> 'int':
        import string
        letters = list(string.ascii_uppercase)
        dic = {y:x+1 for x,y in enumerate(letters)}
        temp = 0
        for index, letter in enumerate(s[::-1]):
            try:
                temp+=(dic[letter]*(26**index))
            except:
                pass
        return temp
# This can be optimized by using ord() instead of this approach