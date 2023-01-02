"""
https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

"""
# Definition for a Node.
# """
class Node(object):
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
	def cloneGraph(self, node):
		oldToNew={} #hashmap for keeping track of cloned nodes
		
		def dfs(node):
			if node in oldToNew: #if already visited, return clone from HM
				return oldToNew[node] 
			
			copy = Node(node.val) #o.w. create a clone with value of original
			oldToNew[node] = copy #store in HM to keep track
			for nei in node.neighbors: #for all neighbors in original
				copy.neighbors.append(dfs(nei)) #recursively append a new clone or from HM
			return copy #return copy of the node
		
		return dfs(node) if node else None #Edge case, given node may be NONE