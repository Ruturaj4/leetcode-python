# Given an array of integers A, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A = sorted([(x,A.count(x)) for x in set(A)], key=itemgetter(0), reverse=True)
        for i in A:
            if i[1] == 1:
                return i[0]
        return -1

# simpler
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A = {x for x in set(A) if A.count(x) == 1}
        if A:
            return max(A)
        else:
            return -1

# much simpler
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A = {k for k,v in collections.Counter(A).items() if v== 1}
        return max(A) if A else -1

# one liner
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        return max([k for k,v in collections.Counter(A).items() if v== 1]+[-1])
