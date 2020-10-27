#Given a square matrix mat, return the sum of the matrix diagonals.

#Only include the sum of all the elements on the primary diagonal and all the
#elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        temp =0
        n = len(mat)
        for i in range(n):
            temp += mat[i][i] + mat[i][n-1-i]
        return temp-mat[n//2][n//2] if n%2==1 else temp

# one liner!
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(sum(r[j] for j in {i, len(r)-i-1}) for i,r in enumerate(mat))
