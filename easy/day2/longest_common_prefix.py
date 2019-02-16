#longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        temp = ""
        if strs != []:
            m = min(strs)
            for i in range(len(m)):
                for item in strs:
                    if not m[:i+1] == item[:i+1]:
                        return temp
                temp = m[:i+1]
        return temp
