class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    b = (r//3, c//3)
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in box[b]:
                        return False
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[b].add(board[r][c])
        return True