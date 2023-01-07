"""
https://leetcode.com/problems/course-schedule-ii/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

> For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = {crs: [] for crs in range(numCourses)}
        for crs,pre in prerequisites:
            adj_list[crs].append(pre) # inititate adjacency list
        visit, cycle = set(), set() # keep track of visited and cycles
        order = [] # the output list
        
        
        def dfs(course): # search func
            if course in cycle: #detect cycle
                return False # return False to stop algo
            if course in visit: # visited, no need to check it again, 
                return True # return True to stop recursion of this branch
            cycle.add(course) # add in to cycle set for later reference
            for prereq in adj_list[course]: 
                if not dfs(prereq):
                    return False # if cycle is detected, return False to stop algo
            cycle.remove(course) # if the top for loop terminates then, no cycles are detected, can safely remove
            visit.add(course) # add to visit set so that this node is not explored anymore
            order.append(course) # add to the output
            return True # done with this node, return True to stop recursion of this branch

        for course in range(numCourses): # potentially have to check for all 
            if not dfs(course): return [] # if at any moment False is returned, there is a cycle, return empty []
                
        return order # if no cycles, return the ordering
        # ACCEPTED