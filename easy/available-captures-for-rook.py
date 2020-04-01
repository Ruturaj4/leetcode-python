# Available Captures for Rook
# I saw this solution in the comments section

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Get the position of rook
        y,x = [(i, j) for j in range(8) for i in range(8) if board[i][j] == "R"][0]
        # Seach in the cardinal directions
        row = "".join(board[y][j] for j in range(8) if board[y][j] != ".")
        column = "".join(board[j][x] for j in range(8) if board[j][x] != ".")
        # If pawn is found, then capture
        return sum("Rp" in i for i in (row, column)) + sum("pR" in i for i in (row, column))
