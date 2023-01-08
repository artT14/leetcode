"""
https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0,0 
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        # EXAMPLE RUN:
        """
        [2,7,9,3,1]
        0,0
        temp = max(0+2,0) = 2
        0,2
        temp = max(0+7,2) = 7
        2,7
        temp = max(2+9,7) = 11
        7,11
        temp = max(7+3,11) = 11
        11,11
        temp = max(11+1,11) = 12
        11,12
        return 12
        """
        # EXAMPLE RUN 2:
        """
            [   101,    3,  4,  105,    1,  2]
        max   101    101  105   206   206  208
        """