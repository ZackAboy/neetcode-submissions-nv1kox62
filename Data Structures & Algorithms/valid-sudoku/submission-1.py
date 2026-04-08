class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                b = (r//3, c//3)
                val = board[r][c]
                if val == ".":
                    continue
                if val in row[r] or val in col[c] or val in box[b]:
                    return False
                else:
                    row[r].add(val)
                    col[c].add(val)
                    box[b].add(val)
        return True