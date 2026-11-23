class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell != "." and cell in seen:
                    return False
                if cell != ".":
                    seen.add(cell)
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != "." and cell in seen:
                    return False
                if cell != ".":
                    seen.add(cell)
        box = {}
        for row in range(9):
            for col in range(9):
                boxes = (row//3, col //3)
                if boxes not in box:
                    box[boxes] = set()
                cell = board[row][col]
                if cell != "." and cell in box[boxes]:
                    return False
                if cell != ".":
                    box[boxes].add(cell)
        return True
                
        