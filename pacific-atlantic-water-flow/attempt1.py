class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights), len(heights[0])
        both_ways=[]
        
        def bfs(r,c):
            if (r < 0 or c < 0):
                return "p"
            if (r >= rows or c >= cols):
                return "a"
            if [r,c] in both_ways:
                return "ap"
            up = True if r-1 < 0 or (r-1 >= 0 and heights[r][c] >= heights[r-1][c]) else False
            down = True if r+1 >= rows or (r+1 < rows and heights[r][c] >= heights[r+1][c]) else False
            left = True if c-1 < 0 or (c-1 >= 0 and heights[r][c] >= heights[r][c-1]) else False
            right = True if c+1 >= cols or (c+1 < cols and heights[r][c] >= heights[r][c+1]) else False
            if "a" and "p" in (
                up * bfs(r-1,c) +
                down * bfs(r+1,c) +
                left * bfs(r,c-1) +
                right * bfs(r,c+1)
            ): both_ways.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if [r,c] not in both_ways:
                    bfs(r,c)
        return both_ways
        # MAX RECURSION DEPTH EXCEEDED