# Given a string S of lowercase letters, a duplicate removal consists of choosing
# two adjacent and equal letters, and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have been made.
# It is guaranteed the answer is unique.

class Solution:
    def removeDuplicates(self, S: str) -> str:
        temp = []
        for c in S:
            if temp:
                if c != temp[-1]:
                    temp.append(c)
                else:
                    temp.pop()
            else:
                temp.append(c)
        return "".join(temp)
