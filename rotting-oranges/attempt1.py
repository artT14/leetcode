"""
https://leetcode.com/problems/rotting-oranges/
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        minutes = 0

        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            count = 0
            while q:
                row, col = q.popleft()
                print(row,col,count)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                new_rots = 0
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    
                    if (r in range(ROWS)    and
                        c in range(COLS)    and
                        grid[r][c] == 1      and
                        (r,c) not in visit
                    ):
                        q.append((r,c))
                        visit.add((r,c))
                        new_rots = max(1,new_rots)
                count += new_rots
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2 and (r,c) not in visit:
                    minutes = max(minutes,bfs(r,c))
        
        return minutes
        #WRONG ANSWER
