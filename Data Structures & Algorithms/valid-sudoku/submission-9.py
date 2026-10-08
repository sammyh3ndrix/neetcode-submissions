class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cells in row:
                if cells != "." and cells in seen:
                    return False
                if cells != ".":
                    seen.add(cells)
        for col in range(9):
            seen = set()
            for row in range(9):
                cells = board[row][col]
                if cells != "." and cells in seen:
                    return False
                if cells != ".":
                    seen.add(cells)
        box = {

        }
        for col in range(9):
            for row in range(9):
                boxes = (row // 3, col // 3)
                if boxes not in box:
                    box[boxes] = set()
                cell = board[row][col]
                if cell != "." and cell in box[boxes]:
                    return False
                if cell != ".":
                    box[boxes].add(cell)
        return True

        