class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = CURR = nums[0]
        for i in range(1,len(nums)):
            CURR = max(CURR+nums[i],nums[i]) # KEEP ADDING OR FRESH START?
            MAX = max(CURR,MAX) # IS THE CURRENT SUM BEATING THE MAX?
        return MAX

"""
Success
Details 
Runtime: 696 ms, faster than 74.30% of Python online submissions for Maximum Subarray.
Memory Usage: 25.8 MB, less than 23.81% of Python online submissions for Maximum Subarray.
"""

"""
EXAMPLE RUN:
----------------------
0 nums[i]: -2
0 CURR: -2
0 MAX: -2

1 nums[i]:  1
1 CURR:  1
1 MAX:  1

2 nums[i]:  -3
2 CURR:  -2
2 MAX:  1

3 nums[i]:  4
3 CURR:  4
3 MAX:  4

4 nums[i]:  -1
4 CURR:  3
4 MAX:  4

5 nums[i]:  2
5 CURR:  5
5 MAX:  5

6 nums[i]:  1
6 CURR:  6
6 MAX:  6

7 nums[i]:  -5
7 CURR:  1
7 MAX:  6

8 nums[i]:  4
8 CURR:  5
8 MAX:  6
----------------------
"""