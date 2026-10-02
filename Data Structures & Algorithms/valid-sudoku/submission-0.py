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
            sawn = set()
            for i in range(9):
                if board[i][col] != "." and board[i][col] in sawn:
                    return False
                if board[i][col] != ".":
                    sawn.add(board[i][col])
        boxes = {}
        for row in range(9):
            for col in range(9):
                box = (row // 3, col // 3)
                if box not in boxes:
                    boxes[box] = set()
                if board[row][col] != "." and board[row][col] in boxes[box]:
                    return False
                if board[row][col] != ".":
                    boxes[box].add(board[row][col])
        return True


             

        


        