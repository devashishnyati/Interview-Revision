"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # -1 -> dead to alive
        # -2 -> alive to dead
        
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == 0:
                    board[m][n] = self.__dead_cell_rules(m, n, board)
                else:
                    board[m][n] = self.__alive_cell_rules(m, n, board)
                    
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == -1:
                    board[m][n] = 1
                elif board[m][n] == -2:
                    board[m][n] = 0
        # print(board)
    
    def __alive_cell_rules(self, m, n, board):
        alive_neighbors = self.__get_alive_neighbors(m, n, board)
        # case 1
        if alive_neighbors < 2:
            return -2
        # case 3
        elif alive_neighbors > 3:
            return -2
        # case 2
        else: return 1
        
    def __dead_cell_rules(self, m, n, board):
        alive_neighbors = self.__get_alive_neighbors(m, n, board)
        # case 4
        if alive_neighbors == 3:
            return -1
        else: return 0
        
            
    def __get_alive_neighbors(self, m, n, board):
        coordinates = [(-1,0),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]
        alive = 0
        for x, y in coordinates:
            nx = m+x
            ny = n+y
            if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]):
                if board[nx][ny] == 1 or board[nx][ny] == -2:
                    alive += 1
        return alive
                