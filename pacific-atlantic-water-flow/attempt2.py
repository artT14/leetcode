class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        #DIMENSIONS OF ISLAND
        ROWS, COLS = len(heights), len(heights[0])
        #SETS FOR STORING THE TILES VISITED FROM PACIFIC & ATLANTIC OCEANS
        #b.c. we are flipping the problem 
        pac,atl = set(), set()
        
        def dfs(r,c, visit, prevHeight):
            if((r,c) in visit                   #if already visited
                or  r < 0                       #if row out of range
                or  r == ROWS                   #if row out of range
                or  c < 0                       #if col out of range
                or  c == COLS                   #if col out of range
                or heights[r][c] < prevHeight   #if last cell has higher height
            ): return                           #EITHER water can't flow here OR already visited OR out of range
            visit.add((r,c)) # ADD to VISITED
            dfs(r+1,c,visit,heights[r][c]) #DFS to bottom tile
            dfs(r-1,c,visit,heights[r][c]) #DFS to above tile
            dfs(r,c+1,visit,heights[r][c]) #DFS to right tile
            dfs(r,c-1,visit,heights[r][c]) #DFS to left tile
        
        for c in range(COLS):
            dfs(0,c,pac, heights[0][c])         #START DFS from TOP for pacific
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])#START DFS from BOTTOM for atlantic
        
        for r in range(ROWS):
            dfs(r,0,pac, heights[r][0])         #START DFS from LEFT for pacific
            dfs(r,COLS-1,atl,heights[r][COLS-1])#START DFS from RIGHT for atlantic
        
        res = []    # return array
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c]) #IF both atlantic and pacific were able to visit the tile, then water will flow to both oceans
        return res
        #ACCEPTED