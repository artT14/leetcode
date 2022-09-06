"""
PROMPT:
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = CURR_MAX = CURR_MIN = nums[0]
        for i in range(1,len(nums)):
            T1 = CURR_MAX*nums[i]
            T2 = CURR_MIN*nums[i]
            CURR_MAX = max(T1, T2, nums[i]) # KEEP MULTIPLYING OR FRESH START?
            CURR_MIN = min(T1, T2, nums[i]) # KEEP MULTIPLYING OR FRESH START?
            MAX = max(CURR_MAX,MAX) # IS THE CURRENT PRODUCT BEATING THE MAX?
        return MAX      

"""
Success
Details 
Runtime: 63 ms, faster than 88.27% of Python online submissions for Maximum Product Subarray.
Memory Usage: 14.1 MB, less than 31.90% of Python online submissions for Maximum Product Subarray.
"""

sol = Solution().maxProduct([-2,0,-1])

print(sol)