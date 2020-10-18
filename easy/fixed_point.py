# Given an array A of distinct integers sorted in ascending order, return
# the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i,v in enumerate(A):
            if i==v: return i
        return -1

# binary search
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l,r = 0,len(A)-1
        while l<r:
            mid = (l+r)//2
            if A[mid] < mid:
                l =mid+1
            else:
                r =mid
        if l == A[l]: return l
        return -1
