"""
PROMPT:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        low = 0
        high = length - 1
        mid = (high+low)//2
        FOUND = None
        while FOUND is None:
            print(low,mid,high)
            if nums[low] < nums[high]:
                FOUND = nums[low]
            elif (high - mid <= 1) and (mid - low <= 1):
                FOUND = min(nums[low],nums[mid],nums[high])
            if nums[low] > nums[mid] and nums[mid] < nums[high]:
                high = mid
                mid = (high+low)//2
            if nums[low] < nums[mid] and nums[mid] > nums[high]:
                low = mid
                mid = (high+low)//2
        return FOUND 

sol = Solution().findMin([1,2])

print(sol)

"""
Success
Details 
Runtime: 34 ms, faster than 71.38% of Python online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.6 MB, less than 80.99% of Python online submissions for Find Minimum in Rotated Sorted Array.
"""