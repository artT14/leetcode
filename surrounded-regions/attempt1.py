"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        dont_remove = set()
        
        def dfs(r,c):
            if (r < 0       or
                c < 0       or
                r >= ROWS   or
                c >= COLS   or
                (r,c) in dont_remove or
                board[r][c] == "X"
            ): return
            dont_remove.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] != "X" and (r,c) not in dont_remove):
                    board[r][c] = "X"
        return board
    #ACCEPTED