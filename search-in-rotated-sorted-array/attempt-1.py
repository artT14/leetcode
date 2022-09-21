# LINK: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
DESCRIPTION:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # STEP 1: FIND PIVOT POINT
		# STEP 2: DO BINARY SEARCH USING PIVOT POINT
        length = len(nums)
        low = 0
        high = length - 1
        mid = (high+low)//2
        PIVOT = None
        while PIVOT is None:
            print(low,mid,high)
            if nums[low] < nums[high]:
                PIVOT = low
            elif (high - mid <= 1) and (mid - low <= 1):
                check_low = min(0, nums[mid] - nums[low])
                check_high = min(0, nums[mid] - nums[high])
                if check_low and check_high:
                    PIVOT = high
                if not check_low and not check_high:
                    PIVOT = mid
                if check_low and not check_high:
                    PIVOT = low
            if nums[low] > nums[mid] and nums[mid] < nums[high]:
                high = mid
                mid = (high+low)//2
            if nums[low] < nums[mid] and nums[mid] > nums[high]:
                low = mid
                mid = (high+low)//2
        return PIVOT

sol = Solution().search([4,5,6,7,0,1,2,3],0)
print(sol)

# OUT OF TIME
# CHECK SOLUTION https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/2595571/my-solution