import collections

class Solution:
    def orangesRotting(self, grid):
        q = collections.deque() #initialize queue
        fresh = 0 #count fresh oranges
        time = 0 #minutes to rot all

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1		#count fresh ones
                if grid[r][c] == 2:
                    q.append((r, c)) #mark rotten ones to start bfs

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]	#UP DOWN LEFT RIGHT
        while fresh > 0 and q: # if any fresh ones available and queue has available nodes to explore
            length = len(q)
            for i in range(length): # explores the rotten ones in queue
                r, c = q.popleft()

                for dr, dc in directions: #UP DOWN LEFT RIGHT
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2 # convert to rotten
                        q.append((row, col)) # add this one to be explored in queue
                        fresh -= 1 # decrement fresh ones
            time += 1 # After all rotten ones infect neighbours, 1 minute has passed
        return time if fresh == 0 else -1 #if there are still fresh ones present, then there exists a fresh one that will never be infected
