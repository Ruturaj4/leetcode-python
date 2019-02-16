class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        return (haystack.index(needle)) if (needle in haystack) else -1

# Another solution - return haystack.find(needle)
