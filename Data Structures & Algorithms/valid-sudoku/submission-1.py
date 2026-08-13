class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkBoxes(board)

    def checkRows(self, board):
        for row in range(0, 9):
            rowmap = {}
            for col in range(0,9):
                if board[row][col] != "." and board[row][col] in rowmap:
                    return False
                else:
                    rowmap[board[row][col]] = 1
        return True
    def checkCols(self, board):
        for col in range(0, 9):
            colmap = {}
            for row in range(0,9):
                if board[row][col] != "." and board[row][col] in colmap:
                    return False
                else:
                    colmap[board[row][col]] = 1
        return True
    def checkBoxes(self, board):
        for box in range(0,9):
            brow = (box // 3) * 3
            bcol = (box % 3) * 3
            bmap = {}
            for row in range(brow, brow+3):
                for col in range(bcol, bcol+3):
                    if board[row][col] != "." and board[row][col] in bmap:
                        return False
                    else:
                        bmap[board[row][col]] = 1
        return True