class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num != "." and num in seen:
                    return False
                if num != ".":
                    seen.add(num)
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != "." and cell in seen:
                    return False
                if cell != ".":
                    seen.add(cell)

        boxes = {}
        for row in range(9):
            for col in range(9):
                box = (row // 3, col // 3) 
                if box not in boxes:
                    boxes[box] = set()
                cell = board[row][col]
                if cell in boxes[box] and cell != ".":
                    return False
                if cell != ".":
                    boxes[box].add(cell)
        return True
               

                


        