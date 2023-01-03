"""
https://leetcode.com/problems/max-area-of-island/
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
import collections

class Solution(object):
	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not grid:
			return 0
		rows,cols = len(grid), len(grid[0])
		visit = set()
		max_area = 0

		def bfs(r,c):
			q = collections.deque()
			visit.add((r,c))
			q.append((r,c))
			count = 1
			while q:
				row, col = q.popleft()
				directions = [[1,0],[-1,0],[0,1],[0,-1]]

				for dr, dc in directions:
					r,c = row+dr,col+dc
					if (r in range(rows) 
					and c in range(cols)
					and grid[r][c] == 1
					and (r,c) not in visit):
						q.append((r,c))
						visit.add((r,c))
						count += 1
			return count


		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 1 and (r,c) not in visit:
					max_area = max(max_area,bfs(r, c))
		return max_area
		#ACCEPTED

s = Solution()
print(
    s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
)