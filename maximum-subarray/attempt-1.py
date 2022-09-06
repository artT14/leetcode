""""
PROMPT:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""
import functools

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = functools.reduce(lambda a, b: a+b, nums)
        while len(nums) != 0:
            new_sum = 0
            for num in nums:
                new_sum += num
                if new_sum > sum:
                    sum = new_sum
            nums = nums[1:]
        return sum

"""
RESULTS:
Time Limit Exceeded
"""