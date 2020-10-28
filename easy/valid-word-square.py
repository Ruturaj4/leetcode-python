#Given a sequence of words, check whether it forms a valid word square.

# A sequence of words forms a valid word square if the kth row
# and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
# Note:
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j>=len(words) or i>=len(words[j]) or words[i][j]!=words[j][i]:
                    return False
        return True

# another solution
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row, i in enumerate(words):
            col = ""
            for s in words:
                if row < len(s):
                    col += s[row]
            print(col,i)
            if i!=col: return False

# another solution
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row, i in enumerate(words):
            col = ""
            for s in words:
                try:
                    col += s[row]
                except:
                    break
            print(col,i)
            if i!=col: return False
        return True
