"""
https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = set() # keep track of visited nodes
        hm = {i:[] for i in range(numCourses)} # initialize hashmap for storing prerequisites
        for crs,pre in prerequisites: 
            hm[crs].append(pre) # add prereqs for each class to hashmap
        def dfs(course):
            if course in visit: # if course already visited, there is a loop, return False
                return False
            if hm[course] == []: # if no prereqs left to consider, return True
                return True
            visit.add(course) # otherwise add course to visit set
            for pre in hm[course]: # recurse dfs on prereqs
                if not dfs(pre): return False # if one returns False, return False
            visit.remove(course) # if none of the prereqs returned false, then no need to keep in visit node, this course is cleared
            hm[course] = [] # remove prereqs from list in map, since prereq are cleared and no need to check
            return True # return True since valid
        
        for course in range(numCourses): # potentially need to run dfs on all courses since they might not have prereqs
            if not dfs(course):
                return False
        return True
