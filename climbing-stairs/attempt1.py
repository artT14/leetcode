"""
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num1 = 1
        num2 = 1
        while n - 1:
            temp = num2
            num2 = num2 + num1
            num1 = temp
            n -= 1
        return num2