"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
"""
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        out=[]
        for index,query in enumerate(queries):
            out.append(0)
            for num in nums:
                query -= num
                if query < 0:
                    break
                out[index] += 1
        return out