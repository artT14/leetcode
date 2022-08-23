class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        for i in range(len_nums):
            second_target = target - nums[i]
            for j in range(i+1,len_nums):
                if nums[j] == second_target:
                    return [i,j]
"""
Runtime: 1577 ms, faster than 41.65% of Python online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 45.09% of Python online submissions for Two Sum.
"""