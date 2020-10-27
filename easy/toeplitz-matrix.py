#A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

#Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for r, row in enumerate(matrix):
            for c, column in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = column
                elif groups[r-c] !=column:
                    return False
        return True

# another solution
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r==0  or c==0 or matrix[r-1][c-1]==val for r,row in enumerate(matrix) for c,val in enumerate(row))
