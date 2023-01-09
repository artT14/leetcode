from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                tile = board[r][c]
                if tile == '.': continue
                if (tile in rows[r] or
                    tile in cols[c] or 
                    tile in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(tile)
                cols[c].add(tile)
                squares[(r // 3, c // 3)].add(tile)
        # print(rows)
        # print(cols)
        # print(squares)
        return True
        # ACCEPTED

# s = Solution()

# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# print(s.isValidSudoku(board))