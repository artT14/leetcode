class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        product = 1
        for num in nums:
            ans.append(product)
            product *= num
            
        product = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= product
            product *= nums[i]
            
        return ans

"""
Success
Details 
Runtime: 280 ms, faster than 60.26% of Python online submissions for Product of Array Except Self.
Memory Usage: 21 MB, less than 46.57% of Python online submissions for Product of Array Except Self.
"""