"""
https://leetcode.com/problems/combination-sum-iv/
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations
that sum up to target is less than 150 combinations for the given input.
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        
        def dfs(i,cur, total):
            if total == target: # success
                res.append(cur.copy()) # append succesfuls sum to results
                return # stop this branch
            if i >= len(candidates) or total > target: # if index out of bounds or exceed target
                return # stop this branch
            cur.append(candidates[i]) # add candidate @ i to current list
            dfs(i,cur, total+candidates[i]) # recurse dfs including i
            cur.pop() # take out candidate @ i from current list
            dfs(i+1,cur, total+candidates[i]) # recurse dfs not including i
        
        dfs(0,[],0) # start dfs at i=0
        return res # return the results