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
        counter = 10
        while counter:
            lower = nums[mid] > nums[low]  # mid > low 
            midder = nums[high] > nums[mid] # high > mid
            upper = nums[high] > nums[low] # high > low
            print(low,mid,high)
            if lower and midder and upper:
                FOUND = nums[low]
            if not lower and midder:
                # low stays same
                high = mid # high becomes mid
                mid = (high+low)//2
            if lower and not midder:
                # high stays same
                low = mid # low becomes mid
                mid = (high+low)//2
            counter -= 1
        return FOUND 

sol = Solution().findMin([5,6,4,3])

print(sol)

# RESULTS: time limit exceeded