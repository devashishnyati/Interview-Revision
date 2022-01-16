"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.__is_valid_horizontal_line(board) and self.__is_valid_verital_line(board) and self.__is_valid_square(board)
    
    def __is_valid_horizontal_line(self, board):
        for row in board:
            if not self.__is_no_repetition(row):
                return False
        return True 
    
    def __is_valid_verital_line(self, board):
        for i in range(len(board)):
            col = []
            for j in range(len(board[0])):
                col.append(board[j][i])
            if not self.__is_no_repetition(col):
                return False
        return True
    
    def __is_valid_square(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        square.append(board[x][y])
                if not self.__is_no_repetition(square):
                    return False
        return True
    
    def __is_no_repetition(self, check_list):
        check_set = set()
        for item in check_list:
            if item != ".":
                if item not in check_set:
                    check_set.add(item)
                else:
                    return False
        return True