"""
https://leetcode.com/problems/redundant-connection/
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.
"""
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        hm = {v:[] for v in range(1,len(edges)+1)}
        def dfs(start,end,referrer=None):
            if start == end:
                return True
            for neighbour in hm[start]:
                if neighbour != referrer:
                    if dfs(neighbour,end,start): return True
            return False
        for v1,v2 in edges:
            if dfs(v1,v2): return [v1,v2]
            hm[v1].append(v2)
            hm[v2].append(v1)
        #ACCEPTED