"""
https://leetcode.com/problems/longest-increasing-subsequence/
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        for i in range(len(nums)-1):
            maxi = nums[i]
            local_longest = 1
            for num in nums[i+1:]:
                if num > maxi:
                    local_longest += 1
                    maxi = num
            longest = max(longest,local_longest)
        return longest
    
# WRONG SOLUTION