#Given an array A of integers and integer K, return the maximum S such that
#there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying
#this equation, return -1.

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        result = -1
        for i in range(len(A)):
            for j in range(len(A)):
                if i !=j:
                    temp = A[i]+A[j]
                    if temp < K:
                        result = max(result, temp)
        return result

# much better solution using two pointers
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        result = -1
        A = sorted(A)
        i,j = 0,len(A)-1
        while i<j:
            temp = A[i]+A[j]
            if temp < K:
                result = max(result, temp)
                i +=1
            else:
                j-=1
        return result
