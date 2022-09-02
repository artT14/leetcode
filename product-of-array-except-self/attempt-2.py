class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newarr = [1]*len(nums)
        
        prefix, postfix = 1, 1
        
        for i in range(len(nums)):
            newarr[i] = prefix
            prefix *= nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            newarr[i] *= postfix
            postfix *= nums[i]
            
        return newarr
"""
Success
Details 
Runtime: 315 ms, faster than 44.16% of Python online submissions for Product of Array Except Self.
Memory Usage: 21.1 MB, less than 46.57% of Python online submissions for Product of Array Except Self.
"""