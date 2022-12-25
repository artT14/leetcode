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
        """
        :type node: Node
        :rtype: Node
        """
        hm={}
        stack=[node]
        head = node.val
        while len(stack) > 0:
            curr = stack.pop(0)
            if curr.val in hm:
                continue
            hm[curr.val] = Node(val=curr.val)
            for neighbor in curr.neighbors:
                if neighbor.value in hm:
                    hm[neighbor.value].neighbors.append(hm[curr.val])
                else:
                    stack.append(neighbor)
        return hm[head]
        #WRONG ANSWER