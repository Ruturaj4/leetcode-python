# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

# my initial attempt
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in ops:
            if i == "C":
                del result[-1]
            elif i == "D":
                result.append(result[-1]*2)
            elif i == "+":
                result.append(result[-1]+result[-2])
            else:
                result.append(int(i))
        return sum(result)

# pop instead of delete makes it faster
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in ops:
            if i == "C":
                result.pop()
            elif i == "D":
                result.append(result[-1]*2)
            elif i == "+":
                result.append(result[-1]+result[-2])
            else:
                result.append(int(i))
        return sum(result)
